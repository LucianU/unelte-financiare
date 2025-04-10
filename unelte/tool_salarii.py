
import streamlit as st

def run():
    st.title("🧮 Rata de acoperire a salariilor")
    st.markdown(
        "Vezi cât de bine sunt acoperite salariile lunare din veniturile curente. "
        "Un indicator simplu, dar esențial pentru sănătatea operațională."
    )

    venit_lunar = st.number_input("Venit lunar total (RON)", min_value=0.0, step=500.0)
    total_salarii = st.number_input("Total salarii lunare (RON)", min_value=0.0, step=100.0)

    if total_salarii > 0:
        rata = venit_lunar / total_salarii
        st.metric("📐 Rată de acoperire", f"{rata:.2f}x")
        if rata < 1:
            st.error("🔴 Veniturile nu acoperă salariile. Situație nesustenabilă.")
        elif rata < 1.5:
            st.warning("🟠 Situație fragilă. Spațiu redus de manevră.")
        else:
            st.success("🟢 Salariile sunt bine acoperite. Situație sustenabilă.")
    else:
        st.info("Introdu un total al salariilor pentru a calcula rata de acoperire.")
