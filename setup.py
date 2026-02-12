"""Setup configuration for N-gram Text Analysis Application."""

from setuptools import setup, find_packages

with open("README_NGRAM.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ngram-analyzer",
    version="1.0.0",
    author="AI & ML Foundations",
    description="A modular Python application for scalable N-gram text analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ngram-analyzer=ngram_analyzer.analyzer:main",
        ],
    },
)
