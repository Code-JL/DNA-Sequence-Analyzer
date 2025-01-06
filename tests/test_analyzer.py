import pytest
from src.sequence_analyzer import DNASequence

def test_gc_content():
    dna = DNASequence("GCGC")
    assert dna.gc_content() == 100.0
    
    dna = DNASequence("ATAT")
    assert dna.gc_content() == 0.0
    
    dna = DNASequence("ATGC")
    assert dna.gc_content() == 50.0

def test_invalid_sequence():
    with pytest.raises(ValueError):
        DNASequence("ATXG")

def test_complement():
    dna = DNASequence("ATGC")
    assert dna.complement() == "TACG"

def test_reverse_complement():
    dna = DNASequence("ATGC")
    assert dna.reverse_complement() == "GCAT"

def test_find_motif():
    dna = DNASequence("ATAGTAGTAG")
    assert dna.find_motif("TAG") == [3, 6, 9]
