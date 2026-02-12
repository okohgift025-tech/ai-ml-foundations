#!/usr/bin/env python3
"""Demonstration script showcasing the N-gram text analysis application."""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ngram_analyzer import analyzer, preprocessor, ngram_generator, frequency, noun_index


def demo_preprocessing():
    """Demonstrate text preprocessing."""
    print("\n" + "="*70)
    print("DEMO 1: Text Preprocessing")
    print("="*70)
    
    text = "Hello, World! Python is GREAT!!! Don't you think?"
    print(f"\nOriginal text: {text}")
    
    tokens = preprocessor.preprocess(text)
    print(f"Preprocessed tokens: {tokens}")
    print(f"Token count: {len(tokens)}")


def demo_ngram_generation():
    """Demonstrate N-gram generation."""
    print("\n" + "="*70)
    print("DEMO 2: N-gram Generation")
    print("="*70)
    
    text = "The quick brown fox jumps over the lazy dog"
    tokens = preprocessor.preprocess(text)
    print(f"\nTokens: {tokens}")
    
    bigrams = ngram_generator.generate_bigrams(tokens)
    print(f"\nBigrams ({len(bigrams)}):")
    for bg in bigrams[:5]:
        print(f"  - {' '.join(bg)}")
    
    trigrams = ngram_generator.generate_trigrams(tokens)
    print(f"\nTrigrams ({len(trigrams)}):")
    for tg in trigrams[:5]:
        print(f"  - {' '.join(tg)}")


def demo_frequency_analysis():
    """Demonstrate frequency analysis."""
    print("\n" + "="*70)
    print("DEMO 3: Frequency Analysis")
    print("="*70)
    
    text = "the cat sat on the mat and the cat was fat"
    tokens = preprocessor.preprocess(text)
    
    freq = frequency.compute_frequency(tokens)
    top = frequency.get_top_n(freq, 5)
    
    print(f"\nText: {text}")
    print(f"\nTop 5 words:")
    for word, count in top:
        print(f"  {word}: {count}")


def demo_noun_indexing():
    """Demonstrate noun indexing."""
    print("\n" + "="*70)
    print("DEMO 4: Indexed Noun Lookup")
    print("="*70)
    
    # Create a simple noun index
    index = noun_index.NounIndex()
    index.add_noun("python", {"type": "programming language"})
    index.add_noun("data", {"type": "information"})
    index.add_noun("analysis", {"type": "process"})
    
    text = "Python is used for data analysis and machine learning"
    tokens = preprocessor.preprocess(text)
    
    print(f"\nText: {text}")
    print(f"All tokens: {tokens}")
    
    nouns = index.filter_nouns(tokens)
    print(f"\nIndexed nouns found: {nouns}")
    print(f"Noun count: {len(nouns)}")


def demo_complete_analysis():
    """Demonstrate complete analysis."""
    print("\n" + "="*70)
    print("DEMO 5: Complete Analysis Pipeline")
    print("="*70)
    
    # Initialize analyzer
    ngram_analyzer = analyzer.NgramAnalyzer('data/nouns.json')
    
    text = """
    Python is a powerful programming language. Python is used for data analysis.
    Data science requires Python skills. Machine learning uses Python extensively.
    """
    
    results = ngram_analyzer.analyze_text(text, top_n=5)
    
    print(f"\nAnalysis Results:")
    print(f"  Total tokens: {results['token_count']}")
    print(f"  Unique tokens: {results['unique_tokens']}")
    print(f"  Indexed nouns: {results['noun_count']}")
    
    print(f"\n  Top 5 unigrams:")
    for word, count in results['unigrams']:
        print(f"    - {word}: {count}")
    
    print(f"\n  Top 5 bigrams:")
    for bigram, count in results['bigrams']:
        print(f"    - {' '.join(bigram)}: {count}")


def main():
    """Run all demonstrations."""
    print("\n" + "="*70)
    print("N-GRAM TEXT ANALYSIS APPLICATION - FEATURE DEMONSTRATIONS")
    print("="*70)
    
    try:
        demo_preprocessing()
        demo_ngram_generation()
        demo_frequency_analysis()
        demo_noun_indexing()
        demo_complete_analysis()
        
        print("\n" + "="*70)
        print("All demonstrations completed successfully!")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\nError during demonstration: {e}", file=sys.stderr)
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
