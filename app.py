import streamlit as st
from scraper import scrape_mercadolibre

st.title("🔍 Comparador de Precios - MercadoLibre")

query = st.text_input("¿Qué producto querés buscar?", "")

if query:
    with st.spinner("Buscando productos..."):
        resultados = scrape_mercadolibre(query)
    
    if resultados:
        st.success(f"{len(resultados)} resultados encontrados")
        for r in resultados:
            st.write(f"### [{r['titulo']}]({r['url']})")
            st.write(f"💲 Precio: {r['precio']}")
            st.markdown("---")
    else:
        st.warning("No se encontraron resultados o hubo un error.")
