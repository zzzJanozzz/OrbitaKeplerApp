# pages/2_📊_Rendimiento_del_Modelo.py
import streamlit as st
from translations import TRANSLATIONS

# --- Inyección de CSS para un diseño profesional y robusto ---
st.markdown("""
<style>
    /* Hacer el encabezado por defecto transparente en lugar de ocultarlo */
    [data-testid="stHeader"] {
        background-color: transparent;
    }
    /* Añadir espacio en la parte superior del contenido */
    .main .block-container {
        padding-top: 2rem;
    }
    /* Aumentar el tamaño de la fuente de los enlaces de navegación */
    [data-testid="stSidebarNav"] ul li a {
        font-size: 22px !important;
        font-weight: 600 !important;
        margin-bottom: 10px !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Inicialización de Idioma ---
if 'lang' not in st.session_state:
    st.session_state.lang = 'es'

def T(key):
    return TRANSLATIONS[st.session_state.lang].get(key, key)

# --- Configuración de la Página ---
st.set_page_config(page_title=T("performance_page_title"), page_icon="📊", layout="wide")

# --- Barra de Encabezado Personalizada ---
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.title(T("performance_title"))
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
st.sidebar.title("🚀 Navegación")

# --- Contenido Principal ---
st.markdown(T("performance_intro"))

st.header(T("key_metrics_header"))
metric_col1, metric_col2 = st.columns(2)
metric_col1.metric(T("accuracy_label"), "98.43%", T("optimized_model_comment"))
metric_col2.metric(T("model_label"), "Random Forest", T("estimator_comment"))

st.markdown("---")

st.header(T("optimization_process_header"))
st.markdown(T("optimization_process_text"))
st.subheader(T("overfitting_challenge_header"))
st.markdown(T("overfitting_challenge_text"))
st.subheader(T("perfect_config_header"))
st.markdown(T("perfect_config_text"))
st.code("""
{
  'max_depth': 20,
  'min_samples_leaf': 2,
  'n_estimators': 200
}
""", language="json")
st.success(T("conclusion_header"))
st.markdown(T("conclusion_text"))

st.markdown("---")

st.header(T("confusion_matrix_header"))
st.image('matriz_confusion.png', caption=T("confusion_matrix_caption"))
st.subheader(T("detailed_error_analysis_header"))
st.markdown(T("fp_analysis_text"))
st.markdown(T("fn_analysis_text"))
