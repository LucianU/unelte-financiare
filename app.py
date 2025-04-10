import streamlit as st
import importlib

TOOLS = {
    "prag": {
        "title": "📉 Pragul de rentabilitate",
        "module": "unelte.tool_prag",
        "description": "Află câte unități trebuie să vinzi pentru a acoperi costurile fixe și a intra pe profit."
    },
    "buffer": {
        "title": "🧯 Buffer operațional",
        "module": "unelte.tool_buffer",
        "description": "Estimează câte luni poți funcționa fără venituri, doar din rezervele financiare."
    },
    "raport": {
        "title": "💸 Raport venituri / cheltuieli",
        "module": "unelte.tool_raport",
        "description": "Verifică dacă veniturile lunare acoperă cheltuielile recurente."
    },
    "marja": {
        "title": "📐 Marja de contribuție",
        "module": "unelte.tool_marja",
        "description": "Vezi cât contribuie fiecare unitate vândută la acoperirea costurilor și profit.",
    },
    "venit": {
        "title": "💼 Venit necesar per angajat",
        "module": "unelte.tool_venit",
        "description": "Calculează venitul minim necesar pentru ca un angajat să fie sustenabil.",
    },
    "cash_flow": {
        "title": "📊 Cashflow lunar",
        "module": "unelte.tool_cashflow",
        "description": "Află dacă afacerea ta generează sau consumă bani în fiecare lună.",
    },
    "salarii": {
        "title": "🧮 Rata de acoperire a salariilor",
        "module": "unelte.tool_salarii",
        "description": "Verifică dacă veniturile lunare acoperă salariile angajaților.",
    },
    "breakeven_total": {
        "title": "💸 Break-even total",
        "module": "unelte.tool_break_even_total",
        "description": "Află în câte luni îți recuperezi investiția inițială.",
    }
}

st.set_page_config(page_title="Unelte financiare", layout="centered")

selected_tool = st.query_params.get("tool")

if selected_tool in TOOLS:
    if st.button("⬅️ Înapoi la unelte principale"):
        st.query_params.clear()
        st.rerun()

    module = importlib.import_module(TOOLS[selected_tool]["module"])
    module.run()
else:
    st.title("📊 Unelte financiare pentru afaceri mici și mijlocii")
    st.markdown("Selectează una dintre uneltele de mai jos:")

    cols = st.columns(3)
    for i, key in enumerate(TOOLS):
        with cols[i % 3]:
            st.markdown(f"### {TOOLS[key]['title']}")
            st.markdown(TOOLS[key]['description'])
            if st.button("➡️ Deschide", key=f"btn_{key}"):
                st.query_params["tool"] = key
                st.rerun()
