import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from src.bio.dna_search import DNA_ENCODING

def run_bio_page():
    st.set_page_config(page_title="Quantum Bio-Origami", page_icon="🧬", layout="wide")
    
    st.title("🧬 Quantum Bio-Origami Explorer")
    st.markdown("""
    This module bridges **Quantum Computing** and **Structural Biology**. 
    Explore how quantum algorithms can revolutionize DNA search and Protein Folding (Bio-Origami).
    """)

    tab1, tab2 = st.tabs(["🔍 Quantum DNA Search", "🧩 Protein Origami (Lattice Folding)"])

    with tab1:
        st.header("Quantum DNA Search (Grover's Algorithm)")
        st.write("Traditional sequence alignment is O(N). Grover's algorithm provides an O(√N) speedup.")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            target_seq = st.text_input("Enter DNA Target (2 bases, e.g., 'AT', 'CG')", value="AT", max_chars=2).upper()
            if st.button("Run Quantum Search"):
                if all(base in "ACGT" for base in target_seq) and len(target_seq) == 2:
                    st.success(f"Encoding '{target_seq}' into Qubits...")
                    binary = DNA_ENCODING[target_seq[0]] + DNA_ENCODING[target_seq[1]]
                    st.code(f"Target: {target_seq}\nQubit Binary: |{binary}>")
                else:
                    st.error("Please enter a valid 2-base sequence using A, C, G, or T.")

        with col2:
            st.info("Quantum State Visualization")
            # Mock data for Grover's distribution
            bases = ["AA", "AC", "AG", "AT", "CA", "CC", "CG", "CT", "GA", "GC", "GG", "GT", "TA", "TC", "TG", "TT"]
            probs = [0.03] * 16
            if target_seq in bases:
                idx = bases.index(target_seq)
                probs[idx] = 0.6 # Amplified state
            
            fig = go.Figure(data=[go.Bar(x=bases, y=probs, marker_color='teal')])
            fig.update_layout(title="Probability Amplitude (After Grover Iteration)", xaxis_title="DNA Sequence", yaxis_title="Probability")
            st.plotly_chart(fig, use_container_view=True)

    with tab2:
        st.header("Protein Origami: HP Lattice Model")
        st.write("Simulating how proteins fold into their minimal energy geometric state using Quantum VQE.")
        
        protein_seq = st.text_input("Amino Acid Sequence (H=Hydrophobic, P=Polar)", value="HPHPPHH").upper()
        
        if st.button("Fold Protein"):
            if all(char in "HP" for char in protein_seq):
                st.write(f"Finding minimal energy conformation for: `{protein_seq}`")
                
                # Mock 2D Lattice Folding Visualization
                # In a real app, this would come from the VQE output in src/bio/protein_origami.py
                x = [0, 1, 1, 0, -1, -1, 0]
                y = [0, 0, 1, 1, 1, 0, -1]
                colors = ['red' if s == 'H' else 'blue' for s in protein_seq]
                
                fig_fold = go.Figure()
                # Draw connections
                fig_fold.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', 
                                             marker=dict(size=20, color=colors),
                                             line=dict(width=4, color='white'),
                                             text=list(protein_seq),
                                             hoverinfo='text'))
                
                fig_fold.update_layout(title="Predicted 2D Lattice Conformation", 
                                      showlegend=False,
                                      xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                      yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                      plot_bgcolor='rgba(0,0,0,0)',
                                      paper_bgcolor='rgba(0,0,0,0)')
                
                st.plotly_chart(fig_fold, use_container_view=True)
                st.success("Minimal Energy State Found (Conceptual VQE Result)")
            else:
                st.error("Sequence must only contain 'H' and 'P'.")

if __name__ == "__main__":
    run_bio_page()
