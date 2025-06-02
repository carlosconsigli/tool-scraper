import streamlit as st
from scraper import scrape_page

st.title("🌐 Scraper Universal de Productos")

url = st.text_input("🔗 Ingresá la URL del producto o página de tienda")
query = st.text_input("🛒 ¿Qué producto estás buscando? (opcional)")

if st.button("Buscar producto"):
    if not url:
        st.warning("Por favor ingresá una URL válida.")
    else:
        with st.spinner("Analizando la página..."):
            result = scrape_page(url)
        
        if result["success"]:
            st.subheader("📄 Título de la página")
            st.write(result["title"])

            st.subheader("💵 Posibles precios encontrados")
            if result["prices"]:
                for p in result["prices"]:
                    st.write(f"• {p}")
            else:
                st.warning("No se encontraron precios en el contenido.")
        else:
            st.error(f"Error al analizar la página: {result['error']}")
