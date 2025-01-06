from typing import Dict, Tuple
import re

class DNASequence:
    def __init__(self, sequence: str):
        self.sequence = self._validate_sequence(sequence.upper())
        
    def _validate_sequence(self, sequence: str) -> str:
        """Validate DNA sequence contains only valid nucleotides."""
        if not re.match(r'^[ATCG]+$', sequence):
            raise ValueError("Invalid DNA sequence. Must contain only A, T, C, G.")
        return sequence
    
    def gc_content(self) -> float:
        """Calculate GC content percentage."""
        if not self.sequence:
            return 0.0
        gc_count = self.sequence.count('G') + self.sequence.count('C')
        return (gc_count / len(self.sequence)) * 100
    
    def nucleotide_frequency(self) -> Dict[str, int]:
        """Calculate frequency of each nucleotide."""
        return {
            'A': self.sequence.count('A'),
            'T': self.sequence.count('T'),
            'G': self.sequence.count('G'),
            'C': self.sequence.count('C')
        }
    
    def find_motif(self, motif: str) -> list:
        """Find all positions of a given motif."""
        positions = []
        for i in range(len(self.sequence) - len(motif) + 1):
            if self.sequence[i:i+len(motif)] == motif.upper():
                positions.append(i + 1)  # 1-based positioning
        return positions
    
    def complement(self) -> str:
        """Generate complement sequence."""
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complement_dict[base] for base in self.sequence)
    
    def reverse_complement(self) -> str:
        """Generate reverse complement sequence."""
        return self.complement()[::-1]
    
    def find_potential_genes(self) -> list:
        """Find potential genes (sequences between START and STOP codons)."""
        start_codon = 'ATG'
        stop_codons = ['TAA', 'TAG', 'TGA']
        genes = []
        
        for i in range(0, len(self.sequence) - 2, 3):
            if self.sequence[i:i+3] == start_codon:
                for j in range(i + 3, len(self.sequence) - 2, 3):
                    if self.sequence[j:j+3] in stop_codons:
                        genes.append(self.sequence[i:j+3])
                        break
        return genes
