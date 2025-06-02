import streamlit as st
from scraper import scrape_mercadolibre

st.title("🔍 Comparador de Precios - MercadoLibre")

query = st.text_input("Buscar producto:")
if st.button("Buscar"):
    if query:
        with st.spinner("Buscando..."):
            results = scrape_mercadolibre(query)
        if results:
            for r in results:
                st.markdown(f"### {r['title']}")
                st.markdown(f"💲Precio: ${r['price']}")
                st.markdown(f"[Ver en MercadoLibre]({r['url']})")
                st.markdown("---")
        else:
            st.error("No se encontraron resultados o hubo un error.")
    else:
        st.warning("Por favor escribí un producto.")

