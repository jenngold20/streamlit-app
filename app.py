import streamlit as st
import pandas as pd
import random
import requests

import google.generativeai as genai


model = genai.GenerativeModel(model_name='gemini-1.5-flash')

GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

##########################################################

genai.configure(api_key=GOOGLE_API_KEY)

# Configuración de la página
st.set_page_config(page_title="Mundo Mágico de Harry Potter", page_icon=":sparkles:", layout="wide")

# Función para el estilo CSS basado en el modo
def get_css(dark_mode):
    if dark_mode:
        return """
         <style>
            .main {
                background-color: #333333; /* Fondo oscuro */
                color: #f9f3e8; /* Texto claro */
            }
            .stButton>button {
                color: #333333;
                background-color: #f9f3e8; /* Botón claro */
            }
            .stSelectbox>div {
                color: #f9f3e8; /* Color para selectbox en modo oscuro */
            }
            .stMarkdown {
                color: #f9f3e8; /* Color para texto en markdown en modo oscuro */
            }
            .header {
                background-image: url('https://ideogram.ai/assets/image/lossless/response/TKf9Xk7PRPq2egXBavxMRQ');
                background-size: cover;
                background-position: center;
                padding: 50px;
                text-align: center;
                color: #f9f3e8; /* Color claro para el encabezado */
                font-size: 30px;
                font-weight: bold;
                border-bottom: 5px solid #f9f3e8; /* Línea inferior para el encabezado en modo oscuro */
            }
            .sidebar .sidebar-content {
                background-color: #555555; /* Fondo oscuro para la barra lateral */
                color: #f9f3e8;
            }
            .sidebar .sidebar-content .stButton>button {
                color: #555555;
                background-color: #f9f3e8; /* Color para los botones de la barra lateral en modo oscuro */
            }
            /* Agregar un estilo para los textos en selectbox y otros elementos */
            .stSelectbox div, .stTextInput input, .stTextArea textarea, .stRadio input[type="radio"] {
                color: #f9f3e8; /* Color claro para selectbox y otros elementos de texto */
            }
        </style>
        """
    else:
        return """
        <style>
            .main {
                background-color: #f9f3e8; /* Fondo claro */
                color: #333333; /* Texto oscuro */
            }
            .stButton>button {
                color: #ffffff;
                background-color: #8a2b8d; /* Color llamativo para botones */
            }
            .stSelectbox>div {
                color: #8a2b8d; /* Color para selectbox que coincide con el botón */
            }
            .stMarkdown {
                color: #8a2b8d; /* Color para texto en markdown */
            }
            .header {
                background-image: url('https://ideogram.ai/assets/image/lossless/response/TKf9Xk7PRPq2egXBavxMRQ');
                background-size: cover;
                background-position: center;
                padding: 50px;
                text-align: center;
                color: #ffffff;
                font-size: 30px;
                font-weight: bold;
                border-bottom: 5px solid #8a2b8d; /* Línea inferior para el encabezado */
            }
            .sidebar .sidebar-content {
                background-color: #E1C5F7; /* Fondo claro para la barra lateral */
                color: #8a2b8d;
            }
            .sidebar .sidebar-content .stButton>button {
                color: #8a2b8d;
                background-color: #E1C5F7; /* Color para los botones de la barra lateral */
            }
            /* Agregar un estilo para los textos en selectbox y otros elementos */
            .stSelectbox div, .stTextInput input, .stTextArea textarea, .stRadio input[type="radio"] {
                color: #333333; /* Color oscuro para selectbox y otros elementos de texto */
            }
        </style>
        """
       

# Estado de modo oscuro
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Botón para cambiar el modo
if st.sidebar.button("Cambiar Modo"):
    st.session_state.dark_mode = not st.session_state.dark_mode

# Aplicar estilo CSS
st.markdown(get_css(st.session_state.dark_mode), unsafe_allow_html=True)

# Imagen de encabezado
st.markdown('<div class="header">Mundo Mágico de Harry Potter</div>', unsafe_allow_html=True)

# Título y descripción de la aplicación
st.title("¡Bienvenido al Mundo Mágico de Harry Potter!")


# Barra lateral de navegación
st.sidebar.title("Descubre el mundo mágico")
pages = ["Inicio", "Consulta con Dumbledore", "Casas de Hogwarts", "Personajes Destacados", "Encuesta de Popularidad", "Trivia de Harry Potter","Generador de Hechizos", "Generador de Nombres Mágicos"]
page = st.sidebar.selectbox("Explora:", pages)

#  Footer
def footer():
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f5f5f5;
        text-align: center;
        padding: 10px;
        font-family: 'Garamond', serif;
        font-size: 14px;
        color: #333;
        border-top: 1px solid #ccc;
    }
    </style>
    <div class="footer">
        Creado por Jennifer Goldfeld 2024 | Prompt Engineer para programadores Coderhouse
    </div>
    """, unsafe_allow_html=True)
    
################################# INICIO ####################################

# Función para mostrar la página de inicio
def show_home():
    st.header("Inicio")
    st.markdown("""
    ¡Bienvenido a la sección de inicio de la aplicación Mundo Mágico de Harry Potter! Aquí te presentamos una visión general de lo que puedes hacer en nuestra aplicación.
    
    - **Consejos de Dumbledore**: Habla con el sabio Albus Dumbledore y recibe consejos inspiradores y sabiduría mágica para tu aventura en el mundo de Harry Potter.
    - **Casas de Hogwarts**: Explora y descubre cuál es tu casa ideal en Hogwarts.
    - **Personajes Destacados**: Aprende sobre los personajes más importantes de la saga.
    - **Encuesta de Popularidad**: Vota por tu personaje favorito y consulta los resultados.
    - **Trivia de Harry Potter**: Responde preguntas para demostrar tu conocimiento sobre el mundo mágico.
    - **Generador de Hechizos**: Crea hechizos al azar y aprende sobre sus efectos.
    - **Generador de Nombres Mágicos**: Descubre un nombre mágico único para tus propios personajes.
    """)
    
    st.image('https://cdn.leonardo.ai/users/24acd355-eb8c-4f53-9ed7-2f62a1535ea1/generations/f5d32e60-de07-4b88-9ae4-83ae715f80e1/Default_Genera_una_imagen_mgica_para_la_seccin_de_inicio_de_un_3.jpg', caption='Inicia tu camino mágico')
   

############## Consulta con Dumbledore ################## 

# Función para mostrar la página de consulta con Dumbledore

contexto = (
        "Eres Albus Dumbledore, el director de Hogwarts. "
        "Un usuario realizará preguntas sobre el mundo de Harry Potter. "
        "Responde de forma sabia y en el estilo característico de Dumbledore, "
        "brindando información valiosa y orientada a la temática del universo de Harry Potter."
    )

model = genai.GenerativeModel('gemini-1.0-pro')

def consultaDumbledore(contexto, consulta):
    prompt = f"{contexto}\n\nConsulta: {consulta}"
    respuesta_IA = model.generate_content(prompt)  
    return respuesta_IA.text
def show_dumbledore():
    st.header("Consulta con Dumbledore")
    st.markdown("""
    En esta sección puedes hacer preguntas a Albus Dumbledore y recibir respuestas sabias y reflexivas.
    """)
    st.image("https://cdn.leonardo.ai/users/24acd355-eb8c-4f53-9ed7-2f62a1535ea1/generations/bac0255b-3bfc-4054-bcb4-d34bc372099e/Default_Create_an_image_of_Albus_Dumbledore_the_wise_and_vener_2.jpg", 
             caption="Albus Dumbledore", width=400) 
    consulta = st.text_area("Ingresa tu consulta:")
    if st.button("Consultar"):
        if consulta:
            respuesta_IA = consultaDumbledore(contexto, consulta)
            st.markdown("***Respuesta de Albus Dumbledore:***")
            st.write(respuesta_IA)
        else:
            st.write("Por favor, ingresa una consulta.")   
            
############## Casas de Hogwarts ##################      
       
# Función para mostrar la página de casas de Hogwarts
def show_houses():
    st.header("Casas de Hogwarts")
    st.markdown("""
    En esta sección encontrarás información sobre las cuatro casas de Hogwarts: Gryffindor, Slytherin, Ravenclaw y Hufflepuff.
    """)

    houses_data = {
        "Casa": ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"],
        "Características": [
            "Valentía, coraje, determinación",
            "Astucia, ambición, liderazgo",
            "Inteligencia, creatividad, sabiduría",
            "Lealtad, trabajo duro, paciencia"
        ],
        "Fundador": ["Godric Gryffindor", "Salazar Slytherin", "Rowena Ravenclaw", "Helga Hufflepuff"]
    }

    houses_df = pd.DataFrame(houses_data)
    st.dataframe(houses_df)

    st.markdown("### Descubre tu Casa de Hogwarts")
    if st.button("Descubrir mi Casa"):
        # Definir casas con sus características
        houses = {
            "Gryffindor": "Valentía, coraje, determinación",
            "Slytherin": "Astucia, ambición, liderazgo",
            "Ravenclaw": "Inteligencia, creatividad, sabiduría",
            "Hufflepuff": "Lealtad, trabajo duro, paciencia"
        }

        # Seleccionar una casa aleatoria
        house = random.choice(list(houses.keys()))
        characteristics = houses[house]

        st.write(f"**Casa Seleccionada:** {house}")
        st.write(f"**Características:** {characteristics}")



############## Personajes destacados ################## 
# Función para mostrar personajes destacados
def show_characters():
    st.header("Personajes Destacados")
    st.markdown("""
    Descubre información sobre algunos de los personajes más destacados de la saga de Harry Potter.
    """)

    characters_data = {
        "Personaje": ["Harry Potter", "Hermione Granger", "Ron Weasley", "Albus Dumbledore", "Severus Snape"],
        "Descripción": [
            "El niño que vivió, conocido por derrotar a Voldemort.",
            "Una de las brujas más inteligentes de su generación.",
            "Leal amigo de Harry, siempre dispuesto a ayudar.",
            "Director de Hogwarts, uno de los magos más poderosos.",
            "Profesor de Pociones, conocido por su complejidad moral."
        ],
       "Imagen": [
            "https://cdn.leonardo.ai/users/24acd355-eb8c-4f53-9ed7-2f62a1535ea1/generations/122be6ec-0db1-4080-bb35-c6ec011bf9d4/Default_Create_an_image_of_Harry_Potter_the_iconic_young_wizar_2.jpg",
            "https://cdn.leonardo.ai/users/24acd355-eb8c-4f53-9ed7-2f62a1535ea1/generations/ef847676-9c6b-428a-b9d6-677511a6f15d/Default_Create_an_image_of_Hermione_Granger_the_brilliant_youn_1.jpg",
            "https://cdn.leonardo.ai/users/24acd355-eb8c-4f53-9ed7-2f62a1535ea1/generations/163c7e3d-1162-419d-b969-de7648ca586f/Default_Create_an_image_of_Ron_Weasley_the_loyal_and_brave_you_0.jpg",
            "https://cdn.leonardo.ai/users/24acd355-eb8c-4f53-9ed7-2f62a1535ea1/generations/bac0255b-3bfc-4054-bcb4-d34bc372099e/Default_Create_an_image_of_Albus_Dumbledore_the_wise_and_vener_2.jpg",
            "https://cdn.leonardo.ai/users/24acd355-eb8c-4f53-9ed7-2f62a1535ea1/generations/fa2518ba-7da9-4006-811a-71dbce3971a2/Default_Create_an_image_of_Severus_Snape_the_enigmatic_and_com_3.jpg"
        ]
    }

 # Iterar sobre los datos de los personajes y mostrar cada uno
    for i in range(len(characters_data["Personaje"])):
        st.subheader(characters_data["Personaje"][i])
        st.image(characters_data["Imagen"][i], width=200)  # Ajusta el ancho de la imagen a 200 píxeles
        st.write(characters_data["Descripción"][i])
        st.markdown("---")  # Separador entre personajes

# Inicializar el estado de la sesión para los votos
if 'votes' not in st.session_state:
    st.session_state.votes = {
        "Harry Potter": 0,
        "Hermione Granger": 0,
        "Ron Weasley": 0,
        "Albus Dumbledore": 0,
        "Severus Snape": 0
    }

############## Encuesta de popularidad ################## 
# Función para mostrar encuesta de popularidad
def show_survey():
    st.header("Encuesta de Popularidad")
    st.markdown("""
    Participa en nuestra encuesta para votar por tu personaje favorito.
    """)

    characters = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Albus Dumbledore", "Severus Snape"]
    vote = st.radio("¿Cuál es tu personaje favorito?", characters)

    if st.button("Votar"):
        # Incrementar el contador de votos para el personaje seleccionado
        st.session_state.votes[vote] += 1
        st.write(f"¡Gracias por votar por {vote}!")

    # Mostrar el conteo de votos
    st.markdown("### Resultados de la Encuesta")
    for character, count in st.session_state.votes.items():
        st.write(f"{character}: {count} votos")


############## Trivia de Harry Potter ################## 
#Sector Trivia 
def show_trivia():
    st.header("Trivia de Harry Potter")
    st.markdown("""
    ¡Ponte a prueba con nuestra trivia sobre Harry Potter!
    """)

    trivia_questions = [
        {"question": "¿Cuál es el nombre de la varita de Harry Potter?", "options": ["Elder Wand", "Deathstick", "The Wand of Destiny"], "answer": "Elder Wand"},
        {"question": "¿Qué criatura mágica puede cambiar de forma para adaptarse a los miedos de las personas?", "options": ["Boggart", "Dementor", "Hippogriff", "Thestral"], "answer": "Boggart"},
        {"question": "¿Cómo se llama la poción que permite cambiar de apariencia?", "options": ["Poción Multijugos", "Felix Felicis", "Veritaserum", "Amortentia"], "answer": "Poción Multijugos"},
        {"question": "¿Quién fue el fundador de Slytherin?", "options": ["Godric Gryffindor", "Helga Hufflepuff", "Rowena Ravenclaw", "Salazar Slytherin"], "answer": "Salazar Slytherin"},
        {"question": "¿Cuál es el patronus de Hermione?", "options": ["Nutria", "Ciervo", "Lobo", "Gato"], "answer": "Nutria"}
    ]

    # Inicializar puntos
    if 'score' not in st.session_state:
        st.session_state.score = 0
        st.session_state.answered_questions = 0

    for idx, q in enumerate(trivia_questions):
        st.write(f"**Pregunta {idx + 1}:** {q['question']}")
        answer = st.radio(f"Elige una opción para la pregunta {idx + 1}:", q['options'], key=f"radio_{idx}")
        if st.button(f"Enviar Respuesta para la pregunta {idx + 1}", key=f"button_{idx}"):
            if answer == q['answer']:
                st.session_state.score += 1
                st.write("¡Correcto!")
            else:
                st.write("Incorrecto. La respuesta correcta es:", q['answer'])
            st.session_state.answered_questions += 1

    # Mostrar puntuación final si se han respondido todas las preguntas
    if st.session_state.answered_questions == len(trivia_questions):
        st.write(f"Tu puntuación final es: {st.session_state.score}/{len(trivia_questions)}")


############## Generador de hechizos ################## 
# Función para mostrar generador de hechizos 
def show_spell_generator():
    st.header("Generador de Hechizos")
    st.markdown("""
    Genera un hechizo mágico al azar y descubre qué hace.
    """)

    # API para obtener datos de hechizos
    def get_spell_data():
        try:
            response = requests.get("https://hp-api.herokuapp.com/api/spells")
            spells = response.json()
            return spells
        except Exception as e:
            st.error("No se pudo obtener la información de los hechizos.")
            return []

    spells = get_spell_data()

    # Verificar si se obtuvieron los hechizos
    if spells:
        # Crear una clave para el botón basada en un identificador único
        if st.button("Generar otro hechizo"):
            # Seleccionar un hechizo aleatorio
            spell = random.choice(spells)
            st.write(f"**Hechizo:** {spell['name']}")
            st.write(f"**Descripción:** {spell['description']}")
    else:
        st.write("No hay hechizos disponibles en este momento.")

############## Generador de nombres mágicos ##################
# Función para mostrar generador de nombres mágicos
def show_name_generator():
    st.header("Generador de Nombres Mágicos")
    st.markdown("""
    ¿Buscas un nombre mágico para tu propio personaje? ¡Genera uno aquí!
    """)

    def generate_magic_name():
        prefixes = ["Alo", "Zin", "Mor", "Kal", "El", "Ser", "Val"]
        suffixes = ["indor", "oria", "thor", "alis", "ona", "ius", "ina"]
        return random.choice(prefixes) + random.choice(suffixes)

    if st.button("Generar Nombre Mágico"):
        name = generate_magic_name()
        st.write(f"**Nombre Mágico:** {name}")
        

############## Mostrar páginas seleccionadas ################## 
# Mostrar la página seleccionada
if page == "Inicio":
    show_home()
elif page == "Casas de Hogwarts":
    show_houses()
elif page == "Personajes Destacados":
    show_characters()
elif page == "Encuesta de Popularidad":
    show_survey()
elif page == "Trivia de Harry Potter":
    show_trivia()
elif page == "Generador de Hechizos":
    show_spell_generator()
elif page == "Generador de Nombres Mágicos":
    show_name_generator()
elif page == "Consulta con Dumbledore":
    show_dumbledore()