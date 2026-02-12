"""Frequency distribution module.

This module computes and manages frequency distributions for n-grams.
"""

from typing import List, Tuple, Dict, Any
from collections import Counter


def compute_frequency(items: List[Any]) -> Dict[Any, int]:
    """Compute frequency distribution for a list of items.
    
    Args:
        items: List of items (can be strings, tuples, etc.)
        
    Returns:
        Dictionary mapping items to their frequencies
    """
    return dict(Counter(items))


def sort_by_frequency(freq_dict: Dict[Any, int], reverse: bool = True) -> List[Tuple[Any, int]]:
    """Sort frequency distribution by frequency count.
    
    Args:
        freq_dict: Dictionary mapping items to frequencies
        reverse: If True, sort in descending order
        
    Returns:
        List of tuples (item, frequency) sorted by frequency
    """
    return sorted(freq_dict.items(), key=lambda x: x[1], reverse=reverse)


def get_top_n(freq_dict: Dict[Any, int], n: int = 10) -> List[Tuple[Any, int]]:
    """Get top N most frequent items.
    
    Args:
        freq_dict: Dictionary mapping items to frequencies
        n: Number of top items to return
        
    Returns:
        List of tuples (item, frequency) for top N items
    """
    sorted_items = sort_by_frequency(freq_dict, reverse=True)
    return sorted_items[:n]


def format_ngram(ngram: Any) -> str:
    """Format an n-gram for display.
    
    Args:
        ngram: N-gram (string or tuple)
        
    Returns:
        Formatted string representation
    """
    if isinstance(ngram, tuple):
        return ' '.join(ngram)
    return str(ngram)


def format_frequency_distribution(freq_list: List[Tuple[Any, int]], 
                                  title: str = None,
                                  show_index: bool = True) -> str:
    """Format frequency distribution for display.
    
    Args:
        freq_list: List of tuples (item, frequency)
        title: Optional title for the output
        show_index: Whether to show index numbers
        
    Returns:
        Formatted string output
    """
    lines = []
    
    if title:
        lines.append(f"\n{title}")
        lines.append("=" * len(title))
    
    for idx, (item, freq) in enumerate(freq_list, 1):
        formatted_item = format_ngram(item)
        if show_index:
            lines.append(f"{idx}. {formatted_item}: {freq}")
        else:
            lines.append(f"{formatted_item}: {freq}")
    
    return '\n'.join(lines)
