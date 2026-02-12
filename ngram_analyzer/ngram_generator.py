"""N-gram generation module.

This module generates unigrams, bigrams, and trigrams from tokenized text.
"""

from typing import List, Tuple


def generate_unigrams(tokens: List[str]) -> List[str]:
    """Generate unigrams from a list of tokens.
    
    Args:
        tokens: List of word tokens
        
    Returns:
        List of unigrams (same as input tokens)
    """
    return tokens


def generate_bigrams(tokens: List[str]) -> List[Tuple[str, str]]:
    """Generate bigrams from a list of tokens.
    
    Args:
        tokens: List of word tokens
        
    Returns:
        List of bigrams as tuples
    """
    if len(tokens) < 2:
        return []
    
    bigrams = []
    for i in range(len(tokens) - 1):
        bigrams.append((tokens[i], tokens[i + 1]))
    
    return bigrams


def generate_trigrams(tokens: List[str]) -> List[Tuple[str, str, str]]:
    """Generate trigrams from a list of tokens.
    
    Args:
        tokens: List of word tokens
        
    Returns:
        List of trigrams as tuples
    """
    if len(tokens) < 3:
        return []
    
    trigrams = []
    for i in range(len(tokens) - 2):
        trigrams.append((tokens[i], tokens[i + 1], tokens[i + 2]))
    
    return trigrams


def generate_ngrams(tokens: List[str], n: int) -> List[Tuple]:
    """Generate n-grams of any size from a list of tokens.
    
    Args:
        tokens: List of word tokens
        n: Size of n-grams to generate
        
    Returns:
        List of n-grams as tuples
        
    Raises:
        ValueError: If n is less than 1
    """
    if n < 1:
        raise ValueError("n must be at least 1")
    
    if len(tokens) < n:
        return []
    
    if n == 1:
        return [(token,) for token in tokens]
    
    ngrams = []
    for i in range(len(tokens) - n + 1):
        ngrams.append(tuple(tokens[i:i + n]))
    
    return ngrams
