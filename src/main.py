from sequence_analyzer import DNASequence
from utils import read_fasta, write_fasta
import argparse

def main():
    parser = argparse.ArgumentParser(description='DNA Sequence Analyzer')
    parser.add_argument('--input', '-i', help='Input FASTA file')
    parser.add_argument('--output', '-o', help='Output file for results')
    parser.add_argument('--analyze', '-a', action='store_true', help='Perform full sequence analysis')
    parser.add_argument('--find-motif', '-m', help='Find specific motif in sequence')
    
    args = parser.parse_args()
    
    if args.input:
        sequences = read_fasta(args.input)
    else:
        # Demo sequence
        sequences = {'demo': 'ATGCGATCGATCGATCGTAGCTAGCTGATCG'}
    
    results = []
    for seq_id, sequence in sequences.items():
        dna = DNASequence(sequence)
        
        if args.analyze:
            results.append(f"Analysis for sequence: {seq_id}")
            results.append(f"Length: {len(sequence)}")
            results.append(f"GC Content: {dna.gc_content():.2f}%")
            results.append(f"Nucleotide Frequency: {dna.nucleotide_frequency()}")
            results.append(f"Potential Genes: {len(dna.find_potential_genes())}")
            results.append("-" * 50)
        
        if args.find_motif:
            positions = dna.find_motif(args.find_motif)
            results.append(f"Motif '{args.find_motif}' found at positions: {positions}")
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write('\n'.join(results))
    else:
        print('\n'.join(results))

if __name__ == "__main__":
    main()
