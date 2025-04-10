
import streamlit as st

def run():
    st.title("📐 Marja de contribuție")
    st.markdown(
        "Află cât contribuie fiecare unitate vândută la acoperirea costurilor fixe și la profit. "
        "Un instrument util pentru decizii legate de preț, volum și eficiență."
    )

    pret_unitar = st.number_input("Preț de vânzare per unitate (RON)", min_value=0.0, step=1.0)
    cost_variabil_unitar = st.number_input("Cost variabil per unitate (RON)", min_value=0.0, step=1.0)

    if pret_unitar > 0 and cost_variabil_unitar >= 0:
        marja = pret_unitar - cost_variabil_unitar
        procent = (marja / pret_unitar) * 100 if pret_unitar > 0 else 0
        st.metric("💰 Marja de contribuție", f"{marja:.2f} RON / unitate")
        st.metric("📊 Marja procentuală", f"{procent:.1f}%")

        if procent < 20:
            st.warning("⚠️ Marjă redusă — spațiu limitat pentru acoperirea costurilor fixe.")
        elif procent < 40:
            st.info("ℹ️ Marjă moderată.")
        else:
            st.success("✅ Marjă bună — produsul contribuie semnificativ la profit.")
