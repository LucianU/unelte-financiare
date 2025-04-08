
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
        with cols[i]:
            st.markdown(f"### {TOOLS[key]['title']}")
            st.markdown(TOOLS[key]['description'])
            if st.button("➡️ Deschide", key=f"btn_{key}"):
                st.query_params["tool"] = key
                st.rerun()
