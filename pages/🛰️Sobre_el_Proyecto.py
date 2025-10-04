# pages/3_🛰️_Sobre_el_Proyecto.py
import streamlit as st
from translations import TRANSLATIONS

# --- Inyección de CSS ---
st.markdown("""
<style>
    [data-testid="stHeader"] {background-color: transparent;}
    .main .block-container {padding-top: 2rem;}
    [data-testid="stSidebarNav"] ul li a {
        font-size: 22px !important; font-weight: 600 !important; margin-bottom: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Inicialización de Idioma ---
if 'lang' not in st.session_state:
    st.session_state.lang = 'es'

def T(key):
    return TRANSLATIONS[st.session_state.lang].get(key, key)

# --- Configuración de la Página ---
st.set_page_config(page_title=T("about_page_title"), page_icon="🛰️", layout="wide")

# --- Barra de Encabezado Personalizada ---
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.title(T("about_title"))
with col2:
    selected_lang_option = st.radio(
        "Language", options=['🇪🇸 Español', '🇬🇧 English'], horizontal=True, 
        label_visibility="collapsed", index=1 if st.session_state.lang == 'en' else 0
    )
    new_lang = 'en' if 'English' in selected_lang_option else 'es'
    if st.session_state.lang != new_lang:
        st.session_state.lang = new_lang
        st.rerun()

# --- Barra Lateral ---
st.sidebar.title(T("sidebar_nav_title"))

# --- Contenido Principal ---
st.header(T("about_challenge_header"))
st.info(T("about_challenge_text"))

st.divider()

st.header(T("about_tech_header"))
st.markdown(T("about_tech_list"))

st.divider()

st.header(T("about_team_header"))
st.markdown(T("about_team_list"))