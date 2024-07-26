import streamlit as st
import pandas as pd
import random
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

#pip install streamlit
#pip install IPython
#pip install google-generativeai

GOOGLE_API_KEY= ''


genai.configure(api_key=GOOGLE_API_KEY)
model= genai.GenerativeModel('gemini-1.0-pro')


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
pages = ["Inicio", "Casas de Hogwarts", "Personajes Destacados", "Eventos Importantes", "Predicciones Futuras", "Encuesta de Popularidad", "Trivia de Harry Potter","Generador de Hechizos Aleatorios", "Generador de Nombres Mágicos" ]
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
    Revive algunos de los eventos más importantes que tuvieron lugar en el mundo mágico de Harry Potter.
    """)

    events_data = {
        "Evento": ["La Batalla de Hogwarts", "El Torneo de los Tres Magos", "La Fundación de Hogwarts"],
        "Descripción": [
            "La batalla final entre el bien y el mal en la escuela.",
            "Competencia mágica entre tres escuelas de magia.",
            "La creación de la escuela de magia más famosa del mundo."
        ]
    }

    events_df = pd.DataFrame(events_data)
    st.dataframe(events_df)

# Función para mostrar predicciones futuras
def show_predictions():
    st.header("Predicciones Futuras")
    st.markdown("""
    ¿Qué les depara el futuro a nuestros personajes favoritos? Aquí te mostramos algunas predicciones sobre el mundo mágico.
    """)

    st.markdown("""
    - **Harry Potter:** Seguirá luchando por la justicia y la igualdad en el mundo mágico.
    - **Hermione Granger:** Posiblemente se convierta en Ministra de Magia, liderando reformas importantes.
    - **Ron Weasley:** Con su habilidad táctica, podría abrir su propia tienda de artículos mágicos exitosamente.
    - **Neville Longbottom:** Continuará su carrera en la enseñanza, inspirando a nuevas generaciones de magos y brujas.
    - **Draco Malfoy:** Trabajará para cambiar la percepción pública de su familia, contribuyendo positivamente a la sociedad mágica.
    """)

# Función para mostrar la encuesta de popularidad
def show_poll():
    st.header("Encuesta de Popularidad")
    st.markdown("""
    ¡Vota por tu personaje favorito de Harry Potter!
    """)
    
    characters = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Albus Dumbledore", "Severus Snape"]
    votes = {char: 0 for char in characters}
    
    selected_character = st.selectbox("Selecciona tu personaje favorito:", characters)
    if st.button("Votar"):
        votes[selected_character] += 1
        st.success(f"¡Has votado por {selected_character}!")
    
    st.write("Resultados de la Encuesta:")
    for character, count in votes.items():
        st.write(f"{character}: {count} votos")
           

# Función para mostrar el trivia
def show_trivia():
    st.header("Trivia de Harry Potter")
    st.markdown("""
    ¡Pon a prueba tus conocimientos sobre el mundo mágico de Harry Potter!
    """)

    questions = [
        {"question": "¿Cuál es el nombre completo de Harry Potter?", "options": ["Harry James Potter", "Harry John Potter", "Harry Robert Potter"], "answer": "Harry James Potter"},
        {"question": "¿Quién es el director de Hogwarts al inicio de la saga?", "options": ["Albus Dumbledore", "Severus Snape", "Minerva McGonagall"], "answer": "Albus Dumbledore"},
        {"question": "¿Qué hechizo se usa para desarmar a un oponente?", "options": ["Expelliarmus", "Avada Kedavra", "Stupefy"], "answer": "Expelliarmus"}
    ]

    score = 0
    for q in questions:
        st.subheader(q["question"])
        selected_option = st.radio("Elige una opción:", q["options"])
        if st.button("Enviar Respuesta", key=q["question"]):
            if selected_option == q["answer"]:
                st.success("¡Correcto!")
                score += 1
            else:
                st.error("Incorrecto. La respuesta correcta es: " + q["answer"])
            st.write("Tu puntuación actual es: " + str(score) + "/" + str(len(questions)))


# Función para mostrar el generador de hechizos
def show_spell_generator():
    st.header("Generador de Hechizos Aleatorios")
    st.markdown("""
    Descubre un hechizo mágico aleatorio cada vez que hagas clic en el botón.
    """)

    spells = {
        "Expelliarmus": "Hechizo para desarmar a un oponente.",
        "Lumos": "Hechizo para iluminar la punta de la varita.",
        "Avada Kedavra": "Hechizo de la muerte, uno de los Tres Hechizos Imperdonables.",
        "Accio": "Hechizo para atraer objetos hacia el lanzador.",
        "Expecto Patronum": "Hechizo para conjurar un Patronus y repeler Dementores."
    }

    if st.button("Generar Hechizo"):
        spell_name = random.choice(list(spells.keys()))
        spell_description = spells[spell_name]
        st.write(f"**Hechizo:** {spell_name}")
        st.write(f"**Descripción:** {spell_description}")


# Función para generar nombres mágicos aleatorios
def generate_magic_name():
    prefixes = ["Al", "El", "Va", "Ro", "Ma", "Sy", "Ga", "Le", "Di", "Ze"]
    infixes = ["nar", "mor", "ven", "lor", "ris", "zom", "ral", "tar", "don", "bel"]
    suffixes = ["ius", "or", "en", "ar", "an", "on", "is", "us", "el", "ir"]

    prefix = random.choice(prefixes)
    infix = random.choice(infixes)
    suffix = random.choice(suffixes)
    
    return f"{prefix}{infix}{suffix}"

# Función para mostrar el generador de nombres mágicos
def show_magic_name_generator():
    st.header("Generador de Nombres Mágicos")
    st.markdown("""
    ¡Descubre un nombre mágico único cada vez que hagas clic en el botón!
    """)

    if st.button("Generar Nombre Mágico"):
        magic_name = generate_magic_name()
        st.write(f"**Nombre Mágico Generado:** {magic_name}")

# Añadir la opción al menú de navegación
pages.append("Generador de Nombres Mágicos")

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
    show_poll()
elif page == "Trivia de Harry Potter":
    show_trivia()
elif page == "Generador de Hechizos Aleatorios":
    show_spell_generator()
elif page == "Generador de Nombres Mágicos":
    show_magic_name_generator()
