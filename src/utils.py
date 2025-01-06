def read_fasta(file_path: str) -> dict:
    """Read FASTA file and return dictionary of sequences."""
    sequences = {}
    current_id = None
    current_seq = []
    
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_id:
                    sequences[current_id] = ''.join(current_seq)
                current_id = line[1:]
                current_seq = []
            else:
                current_seq.append(line)
    
    if current_id:
        sequences[current_id] = ''.join(current_seq)
    
    return sequences

def write_fasta(sequences: dict, file_path: str):
    """Write sequences to FASTA file."""
    with open(file_path, 'w') as f:
        for seq_id, sequence in sequences.items():
            f.write(f'>{seq_id}\n')
            # Write sequence in lines of 60 characters
            for i in range(0, len(sequence), 60):
                f.write(f'{sequence[i:i+60]}\n')
