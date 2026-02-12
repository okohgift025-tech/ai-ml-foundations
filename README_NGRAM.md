# N-gram Text Analysis Application

A modular Python application for scalable N-gram text analysis with preprocessing, frequency distribution, and indexed noun lookup capabilities.

## Features

- **Text Preprocessing**: Tokenization, normalization, and punctuation handling
- **N-gram Generation**: Generate unigrams, bigrams, and trigrams
- **Frequency Analysis**: Compute and display frequency distributions
- **Indexed Noun Lookup**: Identify and analyze nouns using a customizable index
- **Multi-file Processing**: Analyze multiple text files simultaneously
- **Clean Architecture**: Modular design with reusable components
- **Error Handling**: Robust error handling and validation
- **Formatted Output**: Professional formatted output with customizable options

## Installation

No additional dependencies required - uses only Python standard library.

### Requirements

- Python 3.6 or higher

## Project Structure

```
ai-ml-foundations/
├── ngram_analyzer/          # Main application package
│   ├── __init__.py         # Package initialization
│   ├── analyzer.py         # Main orchestrator
│   ├── preprocessor.py     # Text preprocessing
│   ├── ngram_generator.py  # N-gram generation
│   ├── frequency.py        # Frequency distribution
│   ├── file_reader.py      # File ingestion
│   └── noun_index.py       # Noun indexing system
├── data/
│   ├── input/              # Input text files
│   ├── output/             # Analysis results
│   └── nouns.json          # Noun index file
├── main.py                 # Entry point script
└── README.md              # This file
```

## Usage

### Basic Usage

Analyze a single file:
```bash
python3 main.py data/input/sample1.txt
```

Analyze multiple files:
```bash
python3 main.py data/input/sample1.txt data/input/sample2.txt data/input/sample3.txt
```

### Advanced Usage

Analyze all files in a directory:
```bash
python3 main.py --directory data/input
```

Use noun indexing:
```bash
python3 main.py data/input/sample1.txt --noun-index data/nouns.json
```

Customize number of top results:
```bash
python3 main.py data/input/sample1.txt --top 15
```

Save results to a file:
```bash
python3 main.py --directory data/input --output results.txt
```

### Command-line Options

```
usage: main.py [-h] [-d DIRECTORY] [-n TOP] [-i NOUN_INDEX] [-o OUTPUT] 
               [-p PATTERN] [files ...]

positional arguments:
  files                 Input text files to analyze

optional arguments:
  -h, --help            Show this help message and exit
  -d, --directory       Directory containing text files to analyze
  -n, --top            Number of top N-grams to display (default: 10)
  -i, --noun-index     Path to noun index JSON file
  -o, --output         Output file for results (default: stdout)
  -p, --pattern        File pattern for directory mode (default: *.txt)
```

## Examples

### Example 1: Quick Analysis

```bash
python3 main.py data/input/sample1.txt --top 5
```

Output:
```
======================================================================
N-GRAM TEXT ANALYSIS RESULTS
======================================================================

SUMMARY STATISTICS
----------------------------------------------------------------------
Files Analyzed: 1
Total Tokens: 119
Unique Tokens: 79

TOP UNIGRAMS (Single Words)
============================
1. and: 6
2. language: 5
3. python: 4
4. is: 4
5. text: 4
...
```

### Example 2: Complete Analysis with Noun Indexing

```bash
python3 main.py --directory data/input --noun-index data/nouns.json --top 10 --output analysis.txt
```

This will:
1. Read all .txt files from data/input/
2. Apply preprocessing (tokenization, normalization)
3. Generate unigrams, bigrams, and trigrams
4. Compute frequency distributions
5. Identify indexed nouns
6. Save formatted results to analysis.txt

## Noun Index Format

The noun index is a JSON file that can be in two formats:

### Simple List Format
```json
["python", "data", "analysis", "language", "model"]
```

### Metadata Format
```json
{
  "python": {
    "type": "programming language",
    "category": "technology"
  },
  "data": {
    "type": "information",
    "category": "general"
  }
}
```

## Module Documentation

### preprocessor.py
Handles text preprocessing including:
- `tokenize(text)`: Tokenize text into words
- `normalize_text(text)`: Normalize text (lowercase, whitespace)
- `remove_punctuation(text)`: Remove punctuation
- `preprocess(text)`: Complete preprocessing pipeline

### ngram_generator.py
Generates N-grams from tokenized text:
- `generate_unigrams(tokens)`: Generate unigrams
- `generate_bigrams(tokens)`: Generate bigrams
- `generate_trigrams(tokens)`: Generate trigrams
- `generate_ngrams(tokens, n)`: Generate n-grams of any size

### frequency.py
Manages frequency distributions:
- `compute_frequency(items)`: Compute frequency distribution
- `sort_by_frequency(freq_dict)`: Sort by frequency
- `get_top_n(freq_dict, n)`: Get top N items
- `format_frequency_distribution(freq_list)`: Format for display

### file_reader.py
Handles file operations:
- `read_file(file_path)`: Read a single file
- `read_multiple_files(file_paths)`: Read multiple files
- `read_directory(directory_path)`: Read all files in directory
- `combine_file_contents(contents)`: Combine multiple files

### noun_index.py
Manages indexed noun lookup:
- `NounIndex`: Class for noun indexing
- `load_index(index_file)`: Load noun index from file
- `is_noun(word)`: Check if word is a noun
- `filter_nouns(tokens)`: Filter tokens to only nouns
- `create_sample_noun_index(output_file)`: Create sample index

### analyzer.py
Main orchestrator:
- `NgramAnalyzer`: Main analysis class
- `analyze_text(text)`: Analyze text
- `analyze_files(file_paths)`: Analyze multiple files
- `format_results(results)`: Format results for display

## Error Handling

The application includes comprehensive error handling:
- File not found errors
- Permission denied errors
- Encoding errors
- Invalid JSON in noun index
- Empty input validation

## Architecture

The application follows clean architecture principles:

1. **Separation of Concerns**: Each module has a single, well-defined responsibility
2. **Modularity**: Components are loosely coupled and highly cohesive
3. **Reusability**: Functions can be used independently or combined
4. **Extensibility**: Easy to add new features or modify existing ones
5. **Error Handling**: Graceful error handling throughout

## Contributing

To extend the application:

1. **Add new N-gram types**: Extend `ngram_generator.py`
2. **Add new preprocessing steps**: Extend `preprocessor.py`
3. **Add new output formats**: Extend `analyzer.py`
4. **Add new analysis features**: Create new modules

## License

This is a demonstration project for educational purposes.

## Author

Created as part of AI & ML Foundations project portfolio.
