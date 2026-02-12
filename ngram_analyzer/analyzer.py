"""Main N-gram text analysis application.

This module orchestrates the entire N-gram analysis pipeline.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Dict

from . import preprocessor
from . import ngram_generator
from . import frequency
from . import file_reader
from . import noun_index


class NgramAnalyzer:
    """Main N-gram analyzer class."""
    
    def __init__(self, noun_index_file: str = None):
        """Initialize the analyzer.
        
        Args:
            noun_index_file: Optional path to noun index file
        """
        self.noun_index = None
        if noun_index_file:
            self.noun_index = noun_index.NounIndex(noun_index_file)
    
    def analyze_text(self, text: str, top_n: int = 10) -> Dict:
        """Analyze text and generate N-gram statistics.
        
        Args:
            text: Input text to analyze
            top_n: Number of top items to return for each category
            
        Returns:
            Dictionary containing analysis results
        """
        # Preprocess text
        tokens = preprocessor.preprocess(text)
        
        if not tokens:
            return {
                'token_count': 0,
                'unigrams': [],
                'bigrams': [],
                'trigrams': [],
                'nouns': []
            }
        
        # Generate N-grams
        unigrams = ngram_generator.generate_unigrams(tokens)
        bigrams = ngram_generator.generate_bigrams(tokens)
        trigrams = ngram_generator.generate_trigrams(tokens)
        
        # Compute frequencies
        unigram_freq = frequency.compute_frequency(unigrams)
        bigram_freq = frequency.compute_frequency(bigrams)
        trigram_freq = frequency.compute_frequency(trigrams)
        
        # Get top N for each
        top_unigrams = frequency.get_top_n(unigram_freq, top_n)
        top_bigrams = frequency.get_top_n(bigram_freq, top_n)
        top_trigrams = frequency.get_top_n(trigram_freq, top_n)
        
        # Noun analysis if index is available
        top_nouns = []
        if self.noun_index:
            nouns = self.noun_index.filter_nouns(tokens)
            noun_freq = frequency.compute_frequency(nouns)
            top_nouns = frequency.get_top_n(noun_freq, top_n)
        
        return {
            'token_count': len(tokens),
            'unique_tokens': len(unigram_freq),
            'unigrams': top_unigrams,
            'bigrams': top_bigrams,
            'trigrams': top_trigrams,
            'nouns': top_nouns,
            'noun_count': len([t for t in tokens if self.noun_index and self.noun_index.is_noun(t)]) if self.noun_index else 0
        }
    
    def analyze_files(self, file_paths: List[str], top_n: int = 10) -> Dict:
        """Analyze multiple files.
        
        Args:
            file_paths: List of file paths to analyze
            top_n: Number of top items to return
            
        Returns:
            Dictionary containing analysis results
        """
        # Read files
        contents = file_reader.read_multiple_files(file_paths)
        
        if not contents:
            print("Error: No files could be read.")
            return None
        
        # Combine contents
        combined_text = file_reader.combine_file_contents(contents)
        
        # Analyze
        results = self.analyze_text(combined_text, top_n)
        results['file_count'] = len(contents)
        results['files_analyzed'] = list(contents.keys())
        
        return results
    
    def format_results(self, results: Dict) -> str:
        """Format analysis results for display.
        
        Args:
            results: Analysis results dictionary
            
        Returns:
            Formatted string output
        """
        if not results:
            return "No results to display."
        
        lines = []
        lines.append("\n" + "=" * 70)
        lines.append("N-GRAM TEXT ANALYSIS RESULTS")
        lines.append("=" * 70)
        
        # Summary statistics
        lines.append("\nSUMMARY STATISTICS")
        lines.append("-" * 70)
        if 'file_count' in results:
            lines.append(f"Files Analyzed: {results['file_count']}")
        lines.append(f"Total Tokens: {results['token_count']}")
        lines.append(f"Unique Tokens: {results['unique_tokens']}")
        if results.get('noun_count', 0) > 0:
            lines.append(f"Indexed Nouns Found: {results['noun_count']}")
        
        # Unigrams
        if results['unigrams']:
            lines.append(frequency.format_frequency_distribution(
                results['unigrams'], 
                title="\nTOP UNIGRAMS (Single Words)",
                show_index=True
            ))
        
        # Bigrams
        if results['bigrams']:
            lines.append(frequency.format_frequency_distribution(
                results['bigrams'], 
                title="\nTOP BIGRAMS (Two-Word Sequences)",
                show_index=True
            ))
        
        # Trigrams
        if results['trigrams']:
            lines.append(frequency.format_frequency_distribution(
                results['trigrams'], 
                title="\nTOP TRIGRAMS (Three-Word Sequences)",
                show_index=True
            ))
        
        # Nouns
        if results['nouns']:
            lines.append(frequency.format_frequency_distribution(
                results['nouns'], 
                title="\nTOP INDEXED NOUNS",
                show_index=True
            ))
        
        lines.append("\n" + "=" * 70 + "\n")
        
        return '\n'.join(lines)


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description='N-gram Text Analysis Application',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s file1.txt file2.txt
  %(prog)s data/input/*.txt --top 15
  %(prog)s file.txt --noun-index data/nouns.json
  %(prog)s --directory data/input --output results.txt
        """
    )
    
    parser.add_argument(
        'files',
        nargs='*',
        help='Input text files to analyze'
    )
    
    parser.add_argument(
        '-d', '--directory',
        help='Directory containing text files to analyze'
    )
    
    parser.add_argument(
        '-n', '--top',
        type=int,
        default=10,
        help='Number of top N-grams to display (default: 10)'
    )
    
    parser.add_argument(
        '-i', '--noun-index',
        help='Path to noun index JSON file'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Output file for results (default: stdout)'
    )
    
    parser.add_argument(
        '-p', '--pattern',
        default='*.txt',
        help='File pattern for directory mode (default: *.txt)'
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if not args.files and not args.directory:
        parser.error("Please provide either input files or a directory")
    
    try:
        # Initialize analyzer
        analyzer = NgramAnalyzer(args.noun_index)
        
        # Get file paths
        if args.directory:
            contents = file_reader.read_directory(args.directory, args.pattern)
            file_paths = list(contents.keys())
        else:
            file_paths = args.files
        
        if not file_paths:
            print("Error: No files to analyze", file=sys.stderr)
            return 1
        
        # Analyze files
        print(f"Analyzing {len(file_paths)} file(s)...", file=sys.stderr)
        results = analyzer.analyze_files(file_paths, args.top)
        
        if not results:
            return 1
        
        # Format and output results
        output_text = analyzer.format_results(results)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(output_text)
            print(f"Results written to {args.output}", file=sys.stderr)
        else:
            print(output_text)
        
        return 0
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
