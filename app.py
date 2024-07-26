import streamlit as st
import pandas as pd
import random
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

#pip install streamlit
#pip install IPython
#pip install google-generativeai

GOOGLE_API_KEY= 'AIzaSyC2kzAGBY1e74SKdz4yE9jLl-qsV3DC0w0'

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro')

# Configuración de la página
st.set_page_config(page_title="Mundo Mágico de Harry Potter", page_icon=":sparkles:", layout="wide")

# Estilo CSS para la aplicación
st.markdown("""
 <style>
    .main {
        background-color: #f9f3e8; /* Fondo claro y cálido */
        color: #333333; /* Texto oscuro para buen contraste */
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
        background-color: #8a2b8d; /* Fondo de la barra lateral */
        color: #ffffff;
    }
    .sidebar .sidebar-content .stButton>button {
        color: #ffffff;
        background-color: #5d1e5a; /* Color para los botones de la barra lateral */
    }
    </style>
        
    """, unsafe_allow_html=True)

# Imagen de encabezado
st.markdown('<div class="header">Mundo Mágico de Harry Potter</div>', unsafe_allow_html=True)

# Título y descripción de la aplicación
st.title("Bienvenido")
st.markdown("""
Bienvenido al mundo mágico de Harry Potter. Explora las casas de Hogwarts, descubre personajes destacados, eventos importantes, y predicciones sobre el futuro de nuestros personajes favoritos.
""")

# Barra lateral de navegación
st.sidebar.title("Navegación")
pages = ["Inicio", "Casas de Hogwarts", "Personajes Destacados", "Eventos Importantes", "Predicciones Futuras", "Encuesta de Popularidad", "Trivia de Harry Potter con IA", "Generador de Hechizos Aleatorios", "Generador de Nombres Mágicos"]
page = st.sidebar.selectbox("Selecciona una página:", pages)

# Función para mostrar la página de inicio
def show_home():
    st.header("Inicio")
    st.markdown("""
    Sumérgete en el mundo mágico de Harry Potter. Aquí podrás explorar las diferentes casas de Hogwarts, conocer más sobre los personajes más queridos, y revisar los eventos más importantes de la saga.
    """)

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

    for i in range(len(characters_data["Personaje"])):
        st.subheader(characters_data["Personaje"][i])
        st.image(characters_data["Imagen"][i], width=150)
        st.markdown(characters_data["Descripción"][i])

# Función para mostrar eventos importantes
def show_events():
    st.header("Eventos Importantes")
    st.markdown("""
    Revive algunos de los eventos más importantes en el universo de Harry Potter.
    """)

    events_data = {
        "Evento": ["La Batalla de Hogwarts", "El Torneo de los Tres Magos", "La Caída de Voldemort", "La Profecía"],
        "Fecha": ["1998", "1994", "1997", "1980"],
        "Descripción": [
            "La batalla final entre los magos y Voldemort en Hogwarts.",
            "Un torneo mágico que reúne a los mejores magos de tres escuelas.",
            "El momento en que Voldemort finalmente es derrotado.",
            "La profecía que predice el enfrentamiento entre Harry y Voldemort."
        ]
    }

    events_df = pd.DataFrame(events_data)
    st.dataframe(events_df)

# Función para mostrar predicciones futuras
def show_predictions():
    st.header("Predicciones Futuras")
    st.markdown("""
    ¿Qué depara el futuro para nuestros personajes favoritos?
    """)

    predictions = [
        "Harry Potter seguirá defendiendo el mundo mágico de nuevas amenazas.",
        "Hermione Granger se convertirá en una destacada Ministra de Magia.",
        "Ron Weasley encontrará la estabilidad en su vida familiar y profesional.",
        "Albus Dumbledore será recordado como uno de los más grandes magos de todos los tiempos.",
        "Severus Snape será recordado por sus sacrificios y redención."
    ]

    for prediction in predictions:
        st.markdown(f"- {prediction}")

# Función para la encuesta de popularidad
def show_survey():
    st.header("Encuesta de Popularidad")
    st.markdown("""
    Participa en nuestra encuesta sobre tus personajes y eventos favoritos.
    """)

    characters = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Albus Dumbledore", "Severus Snape"]
    selected_character = st.selectbox("Selecciona tu personaje favorito:", characters)
    st.write(f"Has seleccionado: {selected_character}")

    events = ["La Batalla de Hogwarts", "El Torneo de los Tres Magos", "La Caída de Voldemort", "La Profecía"]
    selected_event = st.selectbox("Selecciona tu evento favorito:", events)
    st.write(f"Has seleccionado: {selected_event}")

# Función para la trivia de Harry Potter con IA
def show_trivia():
    st.header("Trivia de Harry Potter con IA")

    prompt = "Genera una pregunta de trivia sobre Harry Potter."
    response = genai.generate(prompt=prompt, model=model)
    question = response.text

    st.subheader("Pregunta:")
    st.write(question)

    answer = st.text_input("Tu respuesta:")

    if st.button("Enviar Respuesta"):
        st.write("Gracias por tu participación.")

# Función para el generador de hechizos aleatorios
def show_spell_generator():
    st.header("Generador de Hechizos Aleatorios")

    spells = ["Expelliarmus", "Lumos", "Accio", "Alohomora", "Avada Kedavra"]
    random_spell = random.choice(spells)

    st.write(f"Tu hechizo aleatorio es: {random_spell}")

# Función para el generador de nombres mágicos
def show_name_generator():
    st.header("Generador de Nombres Mágicos")

    name_prompt = "Genera un nombre mágico único."
    response = genai.generate(prompt=name_prompt, model=model)
    magical_name = response.text

    st.write(f"Tu nombre mágico es: {magical_name}")

# Mostrar la página seleccionada
if page == "Inicio":
    show_home()
elif page == "Casas de Hogwarts":
    show_houses()
elif page == "Personajes Destacados":
    show_characters()
elif page == "Eventos Importantes":
    show_events()
elif page == "Predicciones Futuras":
    show_predictions()
elif page == "Encuesta de Popularidad":
    show_survey()
elif page == "Trivia de Harry Potter con IA":
    show_trivia()
elif page == "Generador de Hechizos Aleatorios":
    show_spell_generator()
elif page == "Generador de Nombres Mágicos":
    show_name_generator()
