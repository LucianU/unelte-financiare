import streamlit as st

def run():
    st.title("📊 Cashflow lunar")
    st.markdown(
        "Află rapid dacă afacerea ta generează sau consumă bani în fiecare lună."
        "Aceasta este una dintre cele mai importante măsuri ale sănătății financiare."
    )

    incasari = st.number_input("Încasări lunare (RON)", min_value=0.0, step=500.0)
    cheltuieli_fixe = st.number_input("Cheltuieli fixe lunare (chirii, salarii etc.)", min_value=0.0, step=100.0)
    cheltuieli_variabile = st.number_input("Cheltuieli variabile lunare (materie primă, transport etc.)", min_value=0.0, step=100.0)
    alte_cheltuieli = st.number_input("Alte cheltuieli (dobânzi, comisioane etc.)", min_value=0.0, step=50.0)

    total_cheltuieli = cheltuieli_fixe + cheltuieli_variabile + alte_cheltuieli
    cashflow = incasari - total_cheltuieli

    st.markdown("---")
    st.metric("💵 Cashflow lunar", f"{cashflow:.2f} RON")

    if cashflow > 0:
        st.success("🟢 Ai un cashflow pozitiv: poți respira ușurat.")
    elif cashflow < 0:
        st.error("🔴 Cashflow negativ: acest ritm nu e sustenabil fără ajustări.")
    else:
        st.info("🟡 Cashflow neutru: veniturile acoperă fix cheltuielile.")

