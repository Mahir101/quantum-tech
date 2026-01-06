# src/bio/dna_search.py

"""
Quantum DNA Searcher
Uses Grover's algorithm to search for a specific target sequence in a DNA dataset.
This is a conceptual implementation using Qiskit.
"""

from qiskit import QuantumCircuit
from qiskit.circuit.library import GroverOperator
from qiskit.visualization import plot_histogram

# Simple encoding: A=00, C=01, G=10, T=11
DNA_ENCODING = {
    'A': '00',
    'C': '01',
    'G': '10',
    'T': '11'
}

def create_dna_oracle(target_sequence):
    """
    Creates a quantum oracle that flips the phase of the target DNA sequence.
    For simplicity, we assume we are searching for a 2-base sequence (4 qubits).
    """
    if len(target_sequence) != 2:
        raise ValueError("This basic demo only supports 2-base (4-qubit) sequences.")
    
    binary_target = DNA_ENCODING[target_sequence[0]] + DNA_ENCODING[target_sequence[1]]
    
    # 4 qubits for 2 bases
    num_qubits = 4
    oracle = QuantumCircuit(num_qubits)
    
    # Flip the phase of the '|binary_target>' state
    # This is a bit-flip based oracle for demonstration
    for i, bit in enumerate(binary_target):
        if bit == '0':
            oracle.x(i)
            
    # Multi-controlled Z gate to target binary_target
    oracle.h(num_qubits - 1)
    oracle.mcx(list(range(num_qubits - 1)), num_qubits - 1)
    oracle.h(num_qubits - 1)
    
    for i, bit in enumerate(binary_target):
        if bit == '0':
            oracle.x(i)
            
    return oracle

def search_dna(target_sequence):
    """
    Performs the Grover search for the target DNA sequence.
    """
    print(f"🧬 Initializing Quantum Search for DNA sequence: {target_sequence}")
    
    num_qubits = 4
    oracle = create_dna_oracle(target_sequence)
    grover_op = GroverOperator(oracle)
    
    # Build full circuit
    qc = QuantumCircuit(num_qubits)
    qc.h(range(num_qubits)) # Superposition
    qc.append(grover_op, range(num_qubits))
    qc.measure_all()
    
    return qc

if __name__ == "__main__":
    # Example: Search for 'AT' (00 11)
    target = "AT"
    circuit = search_dna(target)
    print("✅ Quantum Circuit for DNA Pattern Matching generated.")
    print(circuit.draw())
