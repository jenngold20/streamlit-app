import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Mundo Mágico de Harry Potter", page_icon=":sparkles:", layout="wide")

# Estilo CSS para la aplicación
st.markdown("""
    <style>
    .main {
        background-color: #f4f4f9;
        color: #444;
    }
    .stButton>button {
        color: #ffffff;
        background-color: #7f5af0;
    }
    .stSelectbox>div {
        color: #7f5af0;
    }
    .stMarkdown {
        color: #7f5af0;
    }
    .header {
        background-image: url('https://www.hp-lexicon.org/wp-content/uploads/2015/08/HogwartsCoA.png');
        background-size: cover;
        background-position: center;
        padding: 50px;
        text-align: center;
        color: #ffffff;
        font-size: 30px;
        font-weight: bold;
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
pages = ["Inicio", "Casas de Hogwarts", "Personajes Destacados", "Eventos Importantes", "Predicciones Futuras"]
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
        ]
    }

    characters_df = pd.DataFrame(characters_data)
    st.dataframe(characters_df)

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
