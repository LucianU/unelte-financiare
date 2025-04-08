
import streamlit as st

def run():
    st.header("💸 Raport venituri / cheltuieli")
    st.markdown("""
Evaluează dacă veniturile lunare sunt suficiente pentru a acoperi cheltuielile recurente.

**Formula:** `Venituri lunare / Cheltuieli lunare`
    """)

    venituri = st.number_input("Venituri recurente lunare (RON)", min_value=0.0, value=15000.0, step=500.0)
    chelt_recurente = st.number_input("Cheltuieli recurente lunare (RON)", min_value=1.0, value=12000.0, step=500.0)

    raport = venituri / chelt_recurente
    st.markdown(f"- Raport venituri / cheltuieli: **{raport:.2f}**")

    if raport < 1:
        st.error("❌ Cheltuielile depășesc veniturile. Afacerea consumă din rezerve.")
    elif raport < 1.2:
        st.warning("⚠️ Veniturile sunt apropiate de cheltuieli. Atenție la orice fluctuație.")
    else:
        st.success("✅ Veniturile sunt semnificativ peste cheltuieli. Sustenabilitate bună.")
