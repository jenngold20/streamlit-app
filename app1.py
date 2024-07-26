import streamlit as st
import google.generativeai as genai

# Configuración de la API de Google Generative AI
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# Crear el modelo generativo de Google AI
model = genai.GenerativeModel(model_name='gemini-1.5-flash')

def consulta_dumbledore(consulta):
    contexto = (
        "Eres Albus Dumbledore, el director de Hogwarts. "
        "Un usuario realizará preguntas sobre el mundo de Harry Potter. "
        "Responde de forma sabia y en el estilo característico de Dumbledore, "
        "brindando información valiosa y orientada a la temática del universo de Harry Potter."
    )
    prompt = contexto + "\nPregunta: " + consulta
    respuesta = model.generate_content(prompt)
    return respuesta.text

# Título de la aplicación
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Harry_Potter_logo.svg/2560px-Harry_Potter_logo.svg.png", width=200)
st.header('Consulta a Dumbledore', divider='rainbow')
st.subheader("Un espacio para resolver tus dudas sobre el mundo de Harry Potter.")
st.write("por Jennifer")

# Crear solapas
tabs = st.tabs(["Inicio", "Sobre Dumbledore", "Tu Consulta"])

# Solapa de Inicio
with tabs[0]:
    st.header("Inicio")
    st.markdown("""
    Bienvenido a ***Consulta a Dumbledore***. Esta aplicación está diseñada para responder tus preguntas sobre el mágico mundo de Harry Potter.  
    Pregunta a Dumbledore sobre cualquier aspecto del universo de Harry Potter, y recibirás respuestas sabias y detalladas.
                
    """)
    st.divider()

# Solapa Sobre Dumbledore
with tabs[1]:
    st.header("Sobre Dumbledore")

    st.markdown("""
    Albus Dumbledore es el director de Hogwarts y uno de los personajes más sabios y respetados del mundo de Harry Potter.  
    Puedes preguntarle sobre cualquier aspecto del mundo mágico, desde hechizos y criaturas hasta historia y personajes.
    """)

    st.divider()

# Solapa de Consulta
with tabs[2]:
    st.header("Tu Consulta")

    # Espacio de preguntas del usuario
    st.write("Puedes hacer tus preguntas sobre el mundo de Harry Potter a continuación. Dumbledore te responderá con su sabiduría y conocimientos.")
    consulta = st.text_area("Ingresa tu consulta:")

    # Botón para enviar la consulta
    if st.button("Consultar"):
        if consulta:
            respuesta = consulta_dumbledore(consulta)
            st.markdown("***Respuesta de Dumbledore:***")
            st.write(respuesta)
        else:
            st.write("Por favor, ingresa una consulta.")
