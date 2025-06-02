import streamlit as st
from scraper import scrape_mercadolibre

st.set_page_config(page_title="Comparador de precios ML", layout="centered")
st.title("🛒 Comparador de Precios - MercadoLibre 🇦🇷")

query = st.text_input("¿Qué producto querés buscar?", "")

if st.button("Buscar"):
    if query.strip() == "":
        st.warning("Por favor, escribí un producto.")
    else:
        with st.spinner("Buscando productos en MercadoLibre..."):
            resultados = scrape_mercadolibre(query)
        if resultados:
            for r in resultados:
                st.subheader(r["title"])
                st.write(f"💵 Precio: ${r['price']}")
                st.markdown(f"[🔗 Ver producto]({r['url']})")
                st.markdown("---")
        else:
            st.error("No se encontraron resultados. Verificá el término de búsqueda o probá más tarde.")


