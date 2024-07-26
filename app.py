import streamlit as st
import pandas as pd
import random
import requests
# import google.generativeai as genai




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
                color: #f9f3e8;
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
st.title("Bienvenido")
st.markdown("""
Bienvenido al mundo mágico de Harry Potter. Explora las casas de Hogwarts, descubre personajes destacados
""")

# Barra lateral de navegación
st.sidebar.title("Navegación")
pages = ["Inicio", "Casas de Hogwarts", "Personajes Destacados", "Encuesta de Popularidad", "Trivia de Harry Potter","Generador de Hechizos Aleatorios", "Generador de Nombres Mágicos"]
page = st.sidebar.selectbox("Selecciona una página:", pages)

# Función para mostrar la página de inicio
def show_home():
    st.header("Inicio")
    st.markdown("""
    Sumérgete en el mundo mágico de Harry Potter. Aquí podrás explorar las diferentes casas de Hogwarts, conocer más sobre los personajes más queridos.
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
            "https://cdn.leonardo.ai/users/24acd355-eb8c-4f53-9ed7-2f62a1535ea1/generations/0b415f30-cb7c-4033-b0da-5c6358c278f1/Default_Create_an_image_of_Severus_Snape_the_complex_and_haunted_0.jpg"
        ]
    }

    characters_df = pd.DataFrame(characters_data)
    st.dataframe(characters_df)

    st.markdown("### Conoce Más")
    if st.button("Más Información"):
        st.write("Aquí puedes encontrar detalles adicionales sobre cada personaje.")

# Función para mostrar encuesta de popularidad
def show_survey():
    st.header("Encuesta de Popularidad")
    st.markdown("""
    Participa en nuestra encuesta para votar por tu personaje favorito.
    """)

    characters = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Albus Dumbledore", "Severus Snape"]
    vote = st.radio("¿Cuál es tu personaje favorito?", characters)

    if st.button("Votar"):
        st.write(f"¡Gracias por votar por {vote}!")

# Función para mostrar trivia de Harry Potter
def show_trivia():
    st.header("Trivia de Harry Potter")
    st.markdown("""
    ¡Ponte a prueba con nuestra trivia sobre Harry Potter!
    """)

    trivia_questions = [
        {"question": "¿Cuál es el nombre de la varita de Harry Potter?", "options": ["Elder Wand", "Elder Wand", "Deathstick", "The Wand of Destiny"], "answer": "Elder Wand"},
        {"question": "¿Qué criatura mágica puede cambiar de forma para adaptarse a los miedos de las personas?", "options": ["Boggart", "Dementor", "Hippogriff", "Thestral"], "answer": "Boggart"}
    ]

    for q in trivia_questions:
        st.write(f"**Pregunta:** {q['question']}")
        answer = st.radio("Elige una opción:", q['options'])
        if st.button("Enviar Respuesta"):
            if answer == q['answer']:
                st.write("¡Correcto!")
            else:
                st.write("Incorrecto. La respuesta correcta es:", q['answer'])

# Función para mostrar generador de hechizos aleatorios
def show_spell_generator():
    st.header("Generador de Hechizos Aleatorios")
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

    if spells:
        spell = random.choice(spells)
        st.write(f"**Hechizo:** {spell['name']}")
        st.write(f"**Descripción:** {spell['description']}")
    else:
        st.write("No hay hechizos disponibles en este momento.")

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
elif page == "Generador de Hechizos Aleatorios":
    show_spell_generator()
elif page == "Generador de Nombres Mágicos":
    show_name_generator()
