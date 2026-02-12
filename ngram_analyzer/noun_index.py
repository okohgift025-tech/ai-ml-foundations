"""Indexed noun lookup module.

This module provides indexed lookup functionality for nouns in the text.
"""

import json
from typing import Dict, List, Set
from pathlib import Path


class NounIndex:
    """Indexed noun lookup system."""
    
    def __init__(self, index_file: str = None):
        """Initialize the noun index.
        
        Args:
            index_file: Path to JSON file containing noun index
        """
        self.noun_set: Set[str] = set()
        self.noun_metadata: Dict[str, Dict] = {}
        
        if index_file:
            self.load_index(index_file)
    
    def load_index(self, index_file: str):
        """Load noun index from a JSON file.
        
        Args:
            index_file: Path to JSON file
            
        Raises:
            ValueError: If file format is invalid
        """
        try:
            with open(index_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if isinstance(data, list):
                # Simple list of nouns
                self.noun_set = set(noun.lower() for noun in data)
            elif isinstance(data, dict):
                # Dictionary with metadata
                self.noun_metadata = {k.lower(): v for k, v in data.items()}
                self.noun_set = set(self.noun_metadata.keys())
            else:
                raise ValueError("Index file must contain a list or dictionary")
                
        except FileNotFoundError:
            raise ValueError(f"Index file not found: {index_file}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in index file: {index_file}")
    
    def is_noun(self, word: str) -> bool:
        """Check if a word is in the noun index.
        
        Args:
            word: Word to check
            
        Returns:
            True if word is indexed as a noun
        """
        return word.lower() in self.noun_set
    
    def get_metadata(self, word: str) -> Dict:
        """Get metadata for a noun.
        
        Args:
            word: Noun to look up
            
        Returns:
            Dictionary of metadata, or empty dict if not found
        """
        return self.noun_metadata.get(word.lower(), {})
    
    def filter_nouns(self, tokens: List[str]) -> List[str]:
        """Filter a list of tokens to only include nouns.
        
        Args:
            tokens: List of word tokens
            
        Returns:
            List of tokens that are nouns
        """
        return [token for token in tokens if self.is_noun(token)]
    
    def count_nouns(self, tokens: List[str]) -> int:
        """Count the number of nouns in a list of tokens.
        
        Args:
            tokens: List of word tokens
            
        Returns:
            Count of nouns
        """
        return sum(1 for token in tokens if self.is_noun(token))
    
    def add_noun(self, word: str, metadata: Dict = None):
        """Add a noun to the index.
        
        Args:
            word: Noun to add
            metadata: Optional metadata dictionary
        """
        word_lower = word.lower()
        self.noun_set.add(word_lower)
        if metadata:
            self.noun_metadata[word_lower] = metadata
    
    def save_index(self, output_file: str):
        """Save the noun index to a JSON file.
        
        Args:
            output_file: Path to output file
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            if self.noun_metadata:
                json.dump(self.noun_metadata, f, indent=2)
            else:
                json.dump(list(self.noun_set), f, indent=2)


def create_sample_noun_index(output_file: str):
    """Create a sample noun index file.
    
    Args:
        output_file: Path to output file
    """
    sample_nouns = {
        "python": {"type": "programming language", "category": "technology"},
        "data": {"type": "information", "category": "general"},
        "analysis": {"type": "process", "category": "general"},
        "text": {"type": "content", "category": "general"},
        "language": {"type": "communication", "category": "general"},
        "model": {"type": "representation", "category": "general"},
        "system": {"type": "structure", "category": "general"},
        "application": {"type": "software", "category": "technology"},
        "code": {"type": "instructions", "category": "technology"},
        "algorithm": {"type": "procedure", "category": "technology"},
        "function": {"type": "operation", "category": "programming"},
        "module": {"type": "component", "category": "programming"},
        "file": {"type": "document", "category": "general"},
        "word": {"type": "token", "category": "linguistics"},
        "token": {"type": "unit", "category": "linguistics"},
        "frequency": {"type": "occurrence", "category": "statistics"},
        "distribution": {"type": "pattern", "category": "statistics"},
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sample_nouns, f, indent=2)
