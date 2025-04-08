
import streamlit as st

def run():
    st.header("🧯 Buffer operațional")
    st.markdown("""
Află câte luni poate funcționa afacerea ta doar din rezervele de cash.

**Formula:** `Rezerve cash / Cheltuieli lunare`
    """)

    rezerve = st.number_input("Rezerve de cash disponibile (RON)", min_value=0.0, value=30000.0, step=1000.0)
    cheltuieli = st.number_input("Cheltuieli lunare medii (RON)", min_value=1.0, value=10000.0, step=500.0)

    buffer_luni = rezerve / cheltuieli
    st.markdown(f"- Poți funcționa aproximativ: **{buffer_luni:.1f} luni** fără venituri.")

    if buffer_luni < 1:
        st.error("⚠️ Bufferul este sub 1 lună. Risc financiar ridicat.")
    elif buffer_luni < 3:
        st.warning("⚠️ Buffer mic. Ar fi bine să crești rezervele de siguranță.")
    else:
        st.success("✅ Buffer solid. Ai o plasă de siguranță rezonabilă.")
