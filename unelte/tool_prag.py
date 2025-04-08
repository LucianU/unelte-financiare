
import streamlit as st

def run():
    st.header("📉 Pragul de rentabilitate")
    st.markdown("""
Această unealtă te ajută să afli cât trebuie să vinzi pentru ca afacerea ta să nu fie pe pierdere.

**Formula:** `Costuri fixe / (Preț - Cost variabil)`
    """)

    pret = st.number_input("Preț mediu per unitate (RON)", min_value=0.0, value=100.0, step=10.0)
    cost_variable = st.number_input("Cost variabil per unitate (RON)", min_value=0.0, value=50.0, step=5.0)
    cost_fixe = st.number_input("Costuri fixe lunare (RON)", min_value=0.0, value=10000.0, step=500.0)

    if pret <= cost_variable:
        st.error("⚠️ Prețul trebuie să fie mai mare decât costul variabil pentru a exista marjă.")
    else:
        marja_unitara = pret - cost_variable
        prag_unitati = cost_fixe / marja_unitara
        venit_prag = prag_unitati * pret
        st.markdown(f"- Trebuie să vinzi aproximativ: **{prag_unitati:.0f} unități**")
        st.markdown(f"- Venit minim necesar: **{venit_prag:,.2f} RON**")
        st.info("💡 Tot ce vinzi peste acest prag reprezintă profit brut (neimpozitat).")
