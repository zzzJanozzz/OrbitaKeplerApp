import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from translations import TRANSLATIONS
import math

# --- Inyección de CSS y Configuración de Página ---
st.markdown("""
<style>
    [data-testid="stHeader"] {background-color: transparent;}
    .main .block-container {padding-top: 2rem;}
    [data-testid="stSidebarNav"] ul li a {font-size: 22px !important; font-weight: 600 !important; margin-bottom: 10px !important;}
</style>
""", unsafe_allow_html=True)

# --- Inicialización de Idioma ---
if 'lang' not in st.session_state: st.session_state.lang = 'es'
def T(key, **kwargs): return TRANSLATIONS[st.session_state.lang].get(key, key).format(**kwargs)

st.set_page_config(page_title=T("candidate_profile_title"), page_icon="🪐", layout="wide")

# --- Funciones de Carga de Datos y Visualización ---
@st.cache_data
def load_known_planets():
    try:
        df_known = pd.read_csv('exoplanetas_mini.csv', comment='#')
        return df_known
    except FileNotFoundError:
        return None

def create_size_comparison_chart(candidate_radius_earth):
    # Datos de planetas del sistema solar (radios en radios terrestres)
    solar_system = {'Mercury': 0.38, 'Venus': 0.95, 'Earth': 1.0, 'Mars': 0.53, 'Jupiter': 11.2, 'Saturn': 9.45, 'Uranus': 4.0, 'Neptune': 3.88}
    
    planets = list(solar_system.keys())
    radii = list(solar_system.values())
    
    planets.insert(2, T("candidate_label")) # Insertar candidato junto a la Tierra
    radii.insert(2, candidate_radius_earth)
    
    colors = ['gray', 'orange', 'royalblue', 'darkorange', 'brown', 'goldenrod', 'lightblue', 'darkblue']
    colors.insert(2, 'red')

    fig = go.Figure(data=[go.Bar(
        x=planets,
        y=radii,
        marker_color=colors,
        text=[f'{r:.1f}x' for r in radii],
        textposition='auto',
    )])
    fig.update_layout(
        title=T("planet_comparison_title"),
        xaxis_title="Planeta",
        yaxis_title="Radio (Radios Terrestres)",
        template="plotly_dark",
        yaxis_type="log" # Escala logarítmica para manejar grandes diferencias
    )
    return fig

def create_habitable_zone_chart(candidate_dist_au, star_teff):
    # Estimación simple de la Zona Habitable
    inner_bound = math.sqrt(star_teff / 5800) * 0.95
    outer_bound = math.sqrt(star_teff / 5800) * 1.37

    fig = go.Figure()
    # Barra de fondo que representa el espacio
    fig.add_trace(go.Bar(y=['Sistema'], x=[outer_bound * 1.5], orientation='h', marker_color='rgba(13, 17, 23, 1)', hoverinfo='none'))
    # Zona Fría
    fig.add_trace(go.Bar(y=['Sistema'], x=[outer_bound * 1.5 - outer_bound], base=outer_bound, orientation='h', marker_color='rgba(88, 166, 255, 0.3)', name=T("too_cold_label")))
    # Zona Habitable
    fig.add_trace(go.Bar(y=['Sistema'], x=[outer_bound - inner_bound], base=inner_bound, orientation='h', marker_color='rgba(0, 204, 150, 0.5)', name=T("habitable_label")))
    # Zona Caliente
    fig.add_trace(go.Bar(y=['Sistema'], x=[inner_bound], orientation='h', marker_color='rgba(255, 127, 80, 0.5)', name=T("too_hot_label")))
    
    # Estrella y Planeta
    fig.add_trace(go.Scatter(y=['Sistema'], x=[0], mode='markers', marker_symbol='star', marker_size=30, marker_color='gold', name=T("star_label")))
    fig.add_trace(go.Scatter(y=['Sistema'], x=[candidate_dist_au], mode='markers', marker_symbol='circle', marker_size=20, marker_color='red', name=T("candidate_label")))

    fig.update_layout(
        title=T("habitable_zone_analysis_title"),
        barmode='stack',
        template="plotly_dark",
        xaxis_title="Distancia a la Estrella (UA)",
        yaxis_title="",
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    fig.update_yaxes(showticklabels=False)
    return fig

# --- Barra de Encabezado ---
col1_header, col2_header = st.columns([0.7, 0.3])
with col1_header:
    st.title(T("candidate_profile_title"))
with col2_header:
    selected_lang_option = st.radio("Language", options=['🇪🇸 Español', '🇬🇧 English'], horizontal=True, label_visibility="collapsed", index=1 if st.session_state.lang == 'en' else 0)
    new_lang = 'en' if 'English' in selected_lang_option else 'es'
    if st.session_state.lang != new_lang:
        st.session_state.lang = new_lang
        st.rerun()

# --- Barra Lateral ---
st.sidebar.title("🚀 Navegación")
st.sidebar.success(T("sidebar_success"))

# --- Contenido Principal ---
st.markdown(T("candidate_profile_intro"))
st.info(T("candidate_profile_disclaimer"))

# Datos de ejemplo (simulando que vienen de la página de predicción)
candidate_data = {
    'koi_prad': 2.83,    # Radio planetario en radios terrestres
    'koi_period': 54.41, # Periodo orbital en días
    'koi_srad': 0.92,    # Radio estelar en radios solares
    'koi_steff': 5455,   # Temperatura estelar en K
}

# Convertir periodo a distancia orbital (Ley de Kepler simplificada)
# Asumiendo masa estelar = 1 masa solar
candidate_dist_au = (candidate_data['koi_period'] / 365.25)**(2/3)

# --- Visualizaciones ---
st.header(T("size_comparison_header"))
st.markdown(T("size_comparison_text", radio=candidate_data['koi_prad']))
st.plotly_chart(create_size_comparison_chart(candidate_data['koi_prad']), use_container_width=True)

st.header(T("habitable_zone_header"))
st.plotly_chart(create_habitable_zone_chart(candidate_dist_au, candidate_data['koi_steff']), use_container_width=True)
if candidate_dist_au >= (math.sqrt(candidate_data['koi_steff'] / 5800) * 0.95) and candidate_dist_au <= (math.sqrt(candidate_data['koi_steff'] / 5800) * 1.37):
    st.success(T("habitable_zone_success"))
else:
    st.warning(T("habitable_zone_warning"))

st.header(T("similarity_header"))
df_exoplanetas = load_known_planets()

if df_exoplanetas is not None:
    # Llenar valores faltantes para poder hacer cálculos
    df_exoplanetas_filled = df_exoplanetas[['pl_name', 'pl_rade', 'pl_orbper']].dropna()
    
    # Calcular diferencia
    df_exoplanetas_filled['diff'] = abs(df_exoplanetas_filled['pl_rade'] - candidate_data['koi_prad']) + \
                                     abs(df_exoplanetas_filled['pl_orbper'] - candidate_data['koi_period']) * 0.01 # Ponderar menos el periodo
    
    # Encontrar el más similar
    most_similar = df_exoplanetas_filled.sort_values('diff').iloc[0]
    st.success(T("similarity_success", name=most_similar['pl_name']))
else:
    st.error(T("csv_error_text"))