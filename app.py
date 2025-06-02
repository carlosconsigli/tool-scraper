import streamlit as st
from scraper import scrape_mercadolibre

st.title("🔎 Comparador de Precios - MercadoLibre")

query = st.text_input("Buscar producto en MercadoLibre Argentina")

if query:
    st.write("Buscando productos...")
    results = scrape_mercadolibre(query)

    if results and "error" not in results[0]:
        for product in results:
            st.subheader(product["title"])
            st.write(f"💲 Precio: {product['price']}")
            st.markdown(f"[Ver en MercadoLibre]({product['url']})")
    else:
        st.warning(results[0]["error"])
