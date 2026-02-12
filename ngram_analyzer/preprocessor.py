"""Text preprocessing module for N-gram analysis.

This module handles tokenization, normalization, and punctuation handling.
"""

import re
from typing import List


def tokenize(text: str) -> List[str]:
    """Tokenize text into words.
    
    Args:
        text: Input text string
        
    Returns:
        List of tokens (words)
    """
    if not text:
        return []
    
    # Split on whitespace and common delimiters
    tokens = re.findall(r'\b\w+\b', text)
    return tokens


def normalize_text(text: str) -> str:
    """Normalize text by converting to lowercase and handling whitespace.
    
    Args:
        text: Input text string
        
    Returns:
        Normalized text string
    """
    if not text:
        return ""
    
    # Convert to lowercase
    normalized = text.lower()
    
    # Normalize whitespace
    normalized = ' '.join(normalized.split())
    
    return normalized


def remove_punctuation(text: str, keep_apostrophes: bool = True) -> str:
    """Remove punctuation from text.
    
    Args:
        text: Input text string
        keep_apostrophes: If True, keeps apostrophes in contractions
        
    Returns:
        Text with punctuation removed
    """
    if not text:
        return ""
    
    if keep_apostrophes:
        # Remove all punctuation except apostrophes
        text = re.sub(r"[^\w\s']", ' ', text)
    else:
        # Remove all punctuation
        text = re.sub(r'[^\w\s]', ' ', text)
    
    return text


def preprocess(text: str, lowercase: bool = True, 
               remove_punct: bool = True, 
               keep_apostrophes: bool = True) -> List[str]:
    """Complete preprocessing pipeline.
    
    Args:
        text: Input text string
        lowercase: Whether to convert to lowercase
        remove_punct: Whether to remove punctuation
        keep_apostrophes: Whether to keep apostrophes in contractions
        
    Returns:
        List of preprocessed tokens
    """
    if not text:
        return []
    
    # Remove punctuation if requested
    if remove_punct:
        text = remove_punctuation(text, keep_apostrophes)
    
    # Normalize (includes lowercasing)
    if lowercase:
        text = normalize_text(text)
    
    # Tokenize
    tokens = tokenize(text)
    
    return tokens
