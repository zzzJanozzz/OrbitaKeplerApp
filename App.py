import streamlit as st
from translations import TRANSLATIONS

# --- Inyección de CSS para un diseño profesional y robusto ---
st.markdown("""
<style>
    /* Hacer el encabezado por defecto transparente en lugar de ocultarlo */
    [data-testid="stHeader"] {
        background-color: transparent;
    }
    /* Añadir espacio en la parte superior del contenido para que no quede debajo de nuestro encabezado personalizado */
    .main .block-container {
        padding-top: 2rem;
    }
    /* Aumentar el tamaño de la fuente de los enlaces de navegación */
    [data-testid="stSidebarNav"] ul li a {
        font-size: 22px !important;
        font-weight: 600 !important;
        margin-bottom: 10px !important;
    }
    /* Estilos para las tarjetas de llamada a la acción */
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%; /* Asegura que las tarjetas tengan la misma altura */
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(88, 166, 255, 0.2);
    }
    .card h3 {
        color: #58a6ff; /* Color primario de Streamlit */
    }
</style>
""", unsafe_allow_html=True)

# --- Inicialización de Idioma ---
if 'lang' not in st.session_state:
    st.session_state.lang = 'es'

def T(key):
    return TRANSLATIONS[st.session_state.lang].get(key, key)

# --- Configuración de la Página ---
st.set_page_config(page_title=T("home_page_title"), page_icon="🪐", layout="wide")

# --- Barra de Encabezado Personalizada ---
col1_header, col2_header = st.columns([0.7, 0.3])
with col1_header:
    st.title(T("welcome_title"))
with col2_header:
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
st.sidebar.success(T("sidebar_success"))

# --- Contenido Principal ---

# Sección de Bienvenida (Hero)
col1_hero, col2_hero = st.columns([2, 1]) 
with col1_hero:
    st.markdown(T("welcome_markdown"), unsafe_allow_html=True)
st.divider()

# Sección de Métricas Clave
st.header(T("key_metrics_header"))
col1_metrics, col2_metrics, col3_metrics = st.columns(3)
col1_metrics.metric(
    label=T("accuracy_label"), 
    value="98.43%", 
    help="Precisión del modelo optimizado en el set de datos de prueba."
)
col2_metrics.metric(
    label=T("planet_detection_rate"), 
    value="95.8%",
    help="Porcentaje de planetas reales que la IA identificó correctamente (440 de 459)."
)
col3_metrics.metric(
    label=T("signals_analyzed_label"), 
    value="9,564",
    help="Número total de Candidatos de Interés (KOI) de la misión Kepler que formaron nuestra base de datos."
)

st.divider()

# Sección de Llamadas a la Acción
col1_cta, col2_cta = st.columns(2)
with col1_cta:
    st.markdown(
        f"""
        <div class="card">
            <h3>{T("cta_prediction_header")}</h3>
            <p>{T("cta_prediction_text")}</p>
        </div>
        """, unsafe_allow_html=True
    )
with col2_cta:
     st.markdown(
        f"""
        <div class="card">
            <h3>{T("cta_performance_header")}</h3>
            <p>{T("cta_performance_text")}</p>
        </div>
        """, unsafe_allow_html=True
    )

