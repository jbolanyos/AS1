import streamlit as st
from textblob import TextBlob

# Instalación necesaria
# pip install streamlit textblob

# Configuración de la página
st.set_page_config(page_title="Analizador de Sentimientos", page_icon="🧠")

st.title("🧠 Analizador de Sentimientos Sencillo")
st.write("Escribe una frase o un comentario abajo para evaluar si su tono es positivo, negativo o neutro.")

# --- Entrada de texto ---
# Dejamos un texto por defecto para que el usuario vea cómo funciona de inmediato
texto_usuario = st.text_area(
    "Introduce el texto a analizar:",
    value="I love this app! It's so easy to use and the design is fantastic."
)

if st.button("Analizar Sentimiento"):
    if not texto_usuario.strip():
        st.warning("Por favor, escribe algo para poder analizarlo.")
    else:
        try:
            # 1. Crear el objeto TextBlob con el texto del usuario
            blob = TextBlob(texto_usuario)
            
            # 2. Obtener la polaridad (-1 a 1) y la subjetividad (0 a 1)
            polaridad = blob.sentiment.polarity
            subjetividad = blob.sentiment.subjectivity
            
            st.subheader("Resultados del Análisis:")
            
            # --- Mostrar el resultado con formato visual ---
            if polaridad > 0.1:
                st.success(f"😊 **Sentimiento Positivo** (Polaridad: {polaridad:.2f})")
            elif polaridad < -0.1:
                st.error(f"😡 **Sentimiento Negativo** (Polaridad: {polaridad:.2f})")
            else:
                st.info(f"😐 **Sentimiento Neutro** (Polaridad: {polaridad:.2f})")
                
            # --- Información adicional explicada de forma simple ---
            with st.expander("Ver detalles técnicos del análisis"):
                st.write(f"**Polaridad ({polaridad:.2f}):** Indica qué tan positivo o negativo es el texto. Los valores cercanos a 1 son muy positivos y los cercanos a -1 son muy negativos.")
                st.write(f"**Subjetividad ({subjetividad:.2f}):** Indica qué tanta opinión personal tiene el texto frente a hechos objetivos. 0.0 es puramente objetivo y 1.0 es puramente subjetivo.")
                
        except Exception as e:
            # A veces la traducción automática de TextBlob puede fallar por problemas de conexión con su servidor
            st.error("No se pudo completar el análisis automático.")
            st.info("Prueba introduciendo un texto directamente en inglés para saltarte el paso de traducción, o verifica tu conexión a internet.")