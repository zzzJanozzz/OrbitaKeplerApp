# pages/4_ℹ️_Información_Técnica.py
import streamlit as st
import plotly.graph_objects as go
import numpy as np
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
if 'lang' not in st.session_state: st.session_state.lang = 'es'
def T(key): return TRANSLATIONS[st.session_state.lang].get(key, key)

# --- Configuración de la Página ---
st.set_page_config(page_title=T("tech_info_page_title"), page_icon="ℹ️", layout="wide")

# --- Barra de Encabezado ---
st.sidebar.title("🚀 Navegación")
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.title(T("tech_info_title"))
with col2:
    selected_lang_option = st.radio("Language", options=['🇪🇸 Español', '🇬🇧 English'], horizontal=True, label_visibility="collapsed", index=1 if st.session_state.lang == 'en' else 0)
    new_lang = 'en' if 'English' in selected_lang_option else 'es'
    if st.session_state.lang != new_lang: st.session_state.lang = new_lang; st.rerun()

# --- Contenido Principal ---

st.header(T("exoplanet_header"))
st.markdown(T("exoplanet_text"))

st.markdown("---")

st.header(T("light_curve_header"))
st.markdown(T("light_curve_text_1"))

# Gráfico interactivo de una curva de luz
tiempo = np.linspace(-3, 3, 500)
brillo_base = 1.0
profundidad = 0.01
duracion = 2.0
brillo = brillo_base - profundidad * np.exp(-((tiempo / (duracion/2))**6))

fig = go.Figure()
fig.add_trace(go.Scatter(x=tiempo, y=brillo, mode='lines', line=dict(color='royalblue', width=3)))
fig.update_layout(
    title=T("light_curve_graph_title"),
    xaxis_title="Tiempo (horas desde el centro del tránsito)",
    yaxis_title="Brillo Relativo de la Estrella",
    yaxis_range=[0.985, 1.005]
)
st.plotly_chart(fig, use_container_width=True)
st.markdown(T("light_curve_text_2"))

st.markdown("---")

st.header(T("how_ai_thinks_header"))
st.markdown(T("how_ai_thinks_text_1"))
st.info(T("how_ai_thinks_text_2"))

st.markdown("---")

st.header(T("how_to_use_model_header"))
st.markdown(T("how_to_use_model_text_1"))
st.code("modelo = joblib.load('modelo_caza_planetas.joblib')\nprediccion = modelo.predict(nuevos_datos)", language="python")
st.markdown(T("how_to_use_model_text_2"))
