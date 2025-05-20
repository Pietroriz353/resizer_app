
import streamlit as st

st.set_page_config(page_title="Ridimensionatore 3D", layout="centered")

st.title("Ridimensionatore 3D Proporzionale")

# Misure originali
originale = {"Lunghezza": 1000.0, "Larghezza": 1298.0, "Altezza": 1014.0}
rapporti = {
    "Lunghezza": 1.0,
    "Larghezza": originale["Larghezza"] / originale["Lunghezza"],
    "Altezza": originale["Altezza"] / originale["Lunghezza"],
}

# Selezione asse da modificare
asse_modificato = st.selectbox("Scegli l'asse da modificare:", list(originale.keys()))

# Input dell'asse scelto
valore_nuovo = st.number_input(
    f"Inserisci nuova {asse_modificato.lower()} (mm):",
    min_value=0.0,
    value=originale[asse_modificato],
    step=1.0,
    format="%.2f"
)

# Calcolo nuove dimensioni
scala = valore_nuovo / originale[asse_modificato]
nuove_misure = {asse: round(originale[asse] * scala, 2) for asse in originale}

# Output
st.markdown("### Nuove dimensioni proporzionali:")
for asse, valore in nuove_misure.items():
    st.write(f"**{asse}**: {valore} mm")

st.markdown("---")
st.caption("App creata da Pietro Rizzoni per ridimensionare in scala oggetti 3D")
