import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
from src.bio.chrono_necro_origami import ChronoNecroEngine

def run_chrono_page():
    st.set_page_config(page_title="Chrono-Necro-Origami", page_icon="🧘", layout="wide")
    
    st.title("🕳️ The Chrono-Necro-Origami Dimension")
    st.markdown("""
    ### *Where Time, Paleontology, and Quantum Physics Bleed Together*
    
    In this unprecedented space, we use **Quantum Bio-Resurrection** to simulate how the proteins of extinct species 
    (Mammoths, Trilobites, Dinosaurs) would fold under the crushing gravity of a **Kerr Black Hole**.
    
    **This allows us to hear the 'Gene-Song' of the past through the distortion of the future.**
    """)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.header("🏺 Resurrection Chamber")
        species = st.selectbox("Select Ancestral Genome", 
                              ["Woolly Mammoth", "Steller's Sea Cow", "Dodo Bird", "Utahraptor", "Ancient Leviathan"])
        
        dna_input = st.text_area("Ancient DNA Fragment (extracted from digital fossil)", 
                                 value="ATGCCGTAGCTAA", height=100).upper()
        
        gravity = st.slider("Relativistic Gravity Intensity (G-Force)", 0.0, 20.0, 1.0)
        
        if st.button("Initiate Dimensional Folding"):
            with st.spinner("Piercing the Chrono-Barrier..."):
                time.sleep(2)
                engine = ChronoNecroEngine(species, dna_input)
                results = engine.simulate_relativistic_folding(gravity)
                
                st.metric("Quantum Knot Density", f"{results['quantum_knots']} Knots")
                st.metric("Resonant Frequency", f"{results['chrono_frequency']:.2f} Hz")
                
                if gravity > 15:
                    st.warning("⚠️ CRITICAL: Dimensional instability detected. Protein is folding into 4-dimensional space.")
                else:
                    st.success(f"Status: {results['status']}")
                
                # Show species song
                song = engine.generate_spectral_biography()
                st.write("**Gene-Song (Spectral Mapping):**")
                st.info(" ➔ ".join(song))

    with col2:
        st.header("🌌 Event Horizon Visualization")
        
        # Create a visually "trippy" plot representing relativistic folding
        # We'll use a spiral that distorts with gravity
        t = np.linspace(0, 10, 500)
        z = np.linspace(0, 5, 500)
        r = t * (1 + 0.1 * gravity)
        
        # Distort the spiral based on "DNA sequence"
        noise = np.sin(t * 5) * (gravity / 5)
        x = (r + noise) * np.cos(t)
        y = (r + noise) * np.sin(t)
        
        fig = go.Figure(data=[go.Scatter3d(
            x=x, y=y, z=z,
            mode='lines',
            line=dict(
                width=8,
                color=z, # Color by time/depth
                colorscale='Viridis'
            )
        )])
        
        fig.update_layout(
            title=f"Folded Conformation of {species} at {gravity}G",
            scene=dict(
                xaxis=dict(visible=False),
                yaxis=dict(visible=False),
                zaxis=dict(visible=False),
                bgcolor='black'
            ),
            paper_bgcolor='black',
            font=dict(color='white'),
             margin=dict(l=0, r=0, b=0, t=40)
        )
        
        st.plotly_chart(fig, use_container_view=True)
        
        st.markdown("""
        **Scientific Interpretation:**
        The visualization above represents a 'Quantum Knot' trajectory. The distortions in the 
        geometric spiral are caused by the interaction between the **ancient hydrophobic residues** 
        and the **time-dilated metric tensor**. 
        """)

if __name__ == "__main__":
    run_chrono_page()
