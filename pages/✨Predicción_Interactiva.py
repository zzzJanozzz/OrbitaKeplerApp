# pages/1_✨_Predicción_Interactiva.py
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
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

# --- Configuración y Carga ---
st.set_page_config(page_title=T("prediction_page_title"), page_icon="✨", layout="wide", initial_sidebar_state="expanded")
modelo = joblib.load('modelo_caza_planetas.joblib')

# (Diccionarios de ejemplo)
ejemplo_confirmado = { 'koi_fpflag_nt': 0, 'koi_fpflag_ss': 0, 'koi_fpflag_co': 0, 'koi_fpflag_ec': 0, 'koi_period': 54.41, 'koi_time0bk': 162.51, 'koi_impact': 0.58, 'koi_duration': 4.5, 'koi_depth': 874.8, 'koi_prad': 2.83, 'koi_teq': 443.0, 'koi_insol': 9.11, 'koi_model_snr': 25.8, 'koi_steff': 5455.0, 'koi_slogg': 4.46, 'koi_srad': 0.92 }
ejemplo_falso_positivo = { 'koi_fpflag_nt': 0, 'koi_fpflag_ss': 1, 'koi_fpflag_co': 0, 'koi_fpflag_ec': 0, 'koi_period': 19.89, 'koi_time0bk': 175.85, 'koi_impact': 0.96, 'koi_duration': 1.78, 'koi_depth': 10829.0, 'koi_prad': 14.60, 'koi_teq': 638.0, 'koi_insol': 39.30, 'koi_model_snr': 76.3, 'koi_steff': 5853.0, 'koi_slogg': 4.54, 'koi_srad': 0.86 }

# --- Barra Lateral ---
st.sidebar.title("🚀 Navegación") # ¡NUEVO TÍTULO!
with st.sidebar:
    st.header(T("sidebar_header"))
    opcion_ejemplo = st.selectbox(T("example_select_label"), [T("manual_input_option"), T("confirmed_exoplanet_option"), T("false_positive_option")])
    if opcion_ejemplo == T("confirmed_exoplanet_option"): datos_default = ejemplo_confirmado
    elif opcion_ejemplo == T("false_positive_option"): datos_default = ejemplo_falso_positivo
    else: datos_default = { 'koi_fpflag_nt': 0.0, 'koi_fpflag_ss': 0.0, 'koi_fpflag_co': 0.0, 'koi_fpflag_ec': 0.0, 'koi_period': 35.0, 'koi_time0bk': 135.0, 'koi_impact': 0.5, 'koi_duration': 5.0, 'koi_depth': 1500.0, 'koi_prad': 5.0, 'koi_teq': 1000.0, 'koi_insol': 300.0, 'koi_model_snr': 100.0, 'koi_steff': 5800.0, 'koi_slogg': 4.3, 'koi_srad': 1.1 }

    with st.form("input_form"):
        with st.expander(T("expander_flags"), expanded=True):
            koi_fpflag_nt = st.selectbox('Not Transit-Like', [0, 1], index=int(datos_default['koi_fpflag_nt']))
            koi_fpflag_ss = st.selectbox('Stellar Eclipse', [0, 1], index=int(datos_default['koi_fpflag_ss']))
            koi_fpflag_co = st.selectbox('Centroid Offset', [0, 1], index=int(datos_default['koi_fpflag_co']))
            koi_fpflag_ec = st.selectbox('Ephemeris Match', [0, 1], index=int(datos_default['koi_fpflag_ec']))
        koi_period = st.number_input('Periodo Orbital [días]', min_value=0.1, max_value=10000.0, value=datos_default['koi_period'], step=10.0)
        koi_duration = st.number_input('Duración del Tránsito [horas]', min_value=0.1, max_value=100.0, value=datos_default['koi_duration'], step=1.0)
        koi_depth = st.number_input('Profundidad del Tránsito [ppm]', min_value=1.0, max_value=200000.0, value=datos_default['koi_depth'], step=100.0)
        koi_prad = st.number_input('Radio Planetario [Radios Terrestres]', min_value=0.1, max_value=100.0, value=datos_default['koi_prad'], step=1.0)
        koi_teq = st.number_input('Temperatura de Equilibrio [K]', min_value=50.0, max_value=5000.0, value=datos_default['koi_teq'], step=50.0)
        koi_model_snr = st.number_input('Signal-to-Noise Ratio (SNR)', min_value=1.0, max_value=10000.0, value=datos_default['koi_model_snr'], step=10.0)
        with st.expander(T("expander_stellar")):
            koi_time0bk = st.number_input('Tiempo de Tránsito', min_value=100.0, max_value=2000.0, value=datos_default['koi_time0bk'], step=10.0)
            koi_impact = st.number_input('Parámetro de Impacto', min_value=0.0, max_value=2.0, value=datos_default['koi_impact'], step=0.1)
            koi_insol = st.number_input('Insolación [flujo terrestre]', min_value=0.0, max_value=1000000.0, value=datos_default['koi_insol'], step=100.0)
            koi_steff = st.number_input('Temperatura Estelar [K]', min_value=2000.0, max_value=10000.0, value=datos_default['koi_steff'], step=100.0)
            koi_slogg = st.number_input('Gravedad Superficial Estelar (log g)', min_value=1.0, max_value=6.0, value=datos_default['koi_slogg'], step=0.1)
            koi_srad = st.number_input('Radio Estelar [Radios Solares]', min_value=0.1, max_value=50.0, value=datos_default['koi_srad'], step=0.5)
        predict_button = st.form_submit_button(label=T("predict_button"), type="primary")

# --- Contenido Principal ---
col1, col2 = st.columns([0.7, 0.3])
with col1:
    st.title(T("prediction_title"))
with col2:
    selected_lang_option = st.radio("Language", options=['🇪🇸 Español', '🇬🇧 English'], horizontal=True, label_visibility="collapsed", index=1 if st.session_state.lang == 'en' else 0)
    new_lang = 'en' if 'English' in selected_lang_option else 'es'
    if st.session_state.lang != new_lang: st.session_state.lang = new_lang; st.rerun()

st.markdown(T("prediction_intro"))

if predict_button:
    # (El resto del código de predicción se mantiene igual)
    input_data = pd.DataFrame([{ 'koi_fpflag_nt': koi_fpflag_nt, 'koi_fpflag_ss': koi_fpflag_ss, 'koi_fpflag_co': koi_fpflag_co, 'koi_fpflag_ec': koi_fpflag_ec, 'koi_period': koi_period, 'koi_time0bk': koi_time0bk, 'koi_impact': koi_impact, 'koi_duration': koi_duration, 'koi_depth': koi_depth, 'koi_prad': koi_prad, 'koi_teq': koi_teq, 'koi_insol': koi_insol, 'koi_model_snr': koi_model_snr, 'koi_steff': koi_steff, 'koi_slogg': koi_slogg, 'koi_srad': koi_srad }])
    prediction = modelo.predict(input_data)
    probability = modelo.predict_proba(input_data)[0][1]

    st.header(T("prediction_results_header"))
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        fig = go.Figure(go.Indicator(mode = "gauge+number", value = probability * 100, title = {'text': T("gauge_title")}, domain = {'x': [0, 1], 'y': [0, 1]}, gauge = {'axis': {'range': [None, 100]}, 'steps' : [{'range': [0, 50], 'color': "lightgray"}, {'range': [50, 100], 'color': "royalblue"}], 'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 98}}))
        st.plotly_chart(fig, use_container_width=True)
    with res_col2:
        if prediction[0] == 1: st.success(T("diagnosis_success"))
        else: st.error(T("diagnosis_error"))
        st.write(T("diagnosis_explanation"))
        st.write(f"{T('model_confidence_text')} **{probability*100:.2f}%**.")
    st.markdown("---")
    st.subheader(T("feature_importance_header"))
    st.write(T("feature_importance_text"))
    importances = pd.DataFrame({'feature': input_data.columns, 'importance': modelo.feature_importances_}).sort_values('importance', ascending=False)
    st.bar_chart(importances.set_index('feature'))
else:
    st.info(T("info_awaiting_input"))
