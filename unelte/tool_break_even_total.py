
import streamlit as st

def run():
    st.title("💸 Break-even total (recuperarea investiției)")
    st.markdown(
        "Află în câte luni îți recuperezi investiția inițială pe baza profitului net lunar estimat. "
        "Un indicator util pentru a ști când „ești pe plus cu totul”."
    )

    investitie_initiala = st.number_input("Investiție inițială (RON)", min_value=0.0, step=1000.0)
    profit_lunar = st.number_input("Profit net lunar estimat (RON)", step=100.0)

    if profit_lunar > 0:
        luni_recuperare = investitie_initiala / profit_lunar
        st.metric("⏳ Timp estimat de recuperare", f"{luni_recuperare:.1f} luni")
        if luni_recuperare > 36:
            st.warning("⏱ Peste 3 ani de recuperare — poate fi o investiție riscantă.")
        elif luni_recuperare > 12:
            st.info("📅 Recuperare moderată — între 1 și 3 ani.")
        else:
            st.success("⚡️ Recuperare rapidă — sub un an.")
    elif profit_lunar == 0:
        st.info("ℹ️ Profitul lunar este 0 — investiția nu poate fi recuperată.")
    else:
        st.error("❌ Profitul lunar este negativ — investiția nu este recuperabilă în acest ritm.")
