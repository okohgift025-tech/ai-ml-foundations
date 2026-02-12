# AI & ML Foundations

Structured AI & Machine Learning projects demonstrating Python, data processing, and model development.

## Projects

### N-gram Text Analysis Application

A modular Python application for scalable N-gram text analysis with preprocessing, frequency distribution, and indexed noun lookup capabilities.

**Features:**
- Text preprocessing (tokenization, normalization, punctuation handling)
- N-gram generation (unigrams, bigrams, trigrams)
- Frequency distribution analysis
- Indexed noun lookup system
- Multi-file processing
- Clean architecture with reusable components

**Quick Start:**
```bash
python3 main.py data/input/sample1.txt --noun-index data/nouns.json --top 10
```

See [README_NGRAM.md](README_NGRAM.md) for detailed documentation.

## Repository Structure

```
ai-ml-foundations/
├── ngram_analyzer/          # N-gram text analysis package
│   ├── analyzer.py         # Main orchestrator
│   ├── preprocessor.py     # Text preprocessing
│   ├── ngram_generator.py  # N-gram generation
│   ├── frequency.py        # Frequency distribution
│   ├── file_reader.py      # File ingestion
│   └── noun_index.py       # Noun indexing system
├── data/
│   ├── input/              # Sample input files
│   ├── output/             # Analysis results
│   └── nouns.json          # Noun index data
├── main.py                 # Entry point
└── README_NGRAM.md        # Detailed documentation
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## License

Educational demonstration project.
