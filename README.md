# DNA-Sequence-Analyzer

A robust Python-based bioinformatics tool for comprehensive DNA sequence analysis and manipulation.

## Features

- **GC Content Analysis**: Precise calculation of GC content percentage
- **Nucleotide Frequency**: Detailed nucleotide distribution analysis
- **Motif Finding**: Advanced pattern recognition and position reporting
- **Sequence Manipulation**: Generate complement and reverse complement sequences
- **Gene Detection**: Identification of potential coding regions using start/stop codons
- **FASTA Support**: Full support for standard FASTA file format

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dna_analyzer.git
cd dna_analyzer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

## Basic Analysis

```bash
python src/main.py -i data/example1.fasta -o results.txt -a
```

## Motif Search

```bash
python src/main.py -i data/example2.fasta -m ATCG -o motif_results.txt
```

## Command Line Arguments

- `-i, --input`: Input FASTA file path
- `-o, --output`: Output file path for results
- `-a, --analyze`: Perform complete sequence analysis
- `-m, --find-motif`: Search for specific DNA motif

## Example Data

The repository includes two example FASTA files in the 'data/' directory:

- `example1.fasta`: Contains human and mouse gene sequences
- `example2.fasta`: Contains COVID-19 spike protein and insulin gene fragments

## Testing

Run the test suite:

```bash
pytest tests/
```

## Project Structure

```bash
dna_analyzer/
├── src/
│   ├── sequence_analyzer.py
│   ├── utils.py
│   └── main.py
├── tests/
│   └── test_analyzer.py
├── data/
│   ├── example1.fasta
│   └── example2.fasta
└── docs/
```

## Technical Details

- Python 3.8+
- Modular architecture for easy extension
- Comprehensive test coverage
- Efficient sequence processing algorithms

## Contributing

- Fork the repository
- Create your feature branch (`git checkout -b feature/AmazingFeature`)
- Commit your changes (`git commit -m 'Add some AmazingFeature'`)
- Push to the branch (`git push origin feature/AmazingFeature`)
- Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

