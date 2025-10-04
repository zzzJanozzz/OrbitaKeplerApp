# 🪐 Órbita Kepler: Cazador de Exoplanetas con IA

[![NASA Space Apps 2025](https://img.shields.io/badge/NASA%20Space%20Apps-2025-blue)](https://www.spaceappschallenge.org/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://orbitakepler.streamlit.app) 
**[English Version](#english-version) • [Versión en Español](#versión-en-español)**

**Órbita Kepler** es una plataforma web interactiva desarrollada para el **NASA International Space Apps Challenge 2025**. Nuestra solución utiliza un modelo de Machine Learning optimizado para analizar datos del Telescopio Espacial Kepler, identificar posibles exoplanetas y presentar los hallazgos de una manera visual e intuitiva.

![Captura de Pantalla de la App](https://i.imgur.com/5jDdTU8.png)
---
## <a name="versión-en-español"></a>🌎 Versión en Español

### Sobre el Proyecto

El Telescopio Espacial Kepler de la NASA nos ha proporcionado un "tsunami" de datos, monitoreando cientos de miles de estrellas en busca de tránsitos planetarios. El volumen y la complejidad de estos datos hacen que la revisión manual sea imposible. **Órbita Kepler** nace como una solución a este desafío, empleando Inteligencia Artificial para automatizar la detección de exoplanetas.

Nuestra plataforma no es solo un clasificador. Es una herramienta de descubrimiento de extremo a extremo que:
1.  **Filtra inteligentemente:** Utiliza un modelo de IA (Random Forest) con una precisión robusta del **98.43%** para distinguir entre falsos positivos y candidatos a exoplanetas.
2.  **Visualiza y Explica:** Transforma los datos abstractos en perfiles planetarios visuales, mostrando comparaciones de tamaño, análisis de la zona habitable y las características que influyeron en la decisión de la IA.
3.  **Conecta con la Ciencia Real:** Compara los candidatos con la base de datos oficial de la NASA para encontrar exoplanetas conocidos con características similares, proporcionando un contexto científico inmediato.

### Características Principales

* **IA Optimizada:** El modelo fue perfeccionado mediante **Ajuste de Hiperparámetros** (`GridSearchCV`) para evitar el sobreajuste y garantizar su robustez con datos nuevos.
* **Panel de Control Interactivo:** Una interfaz de usuario limpia y profesional construida con Streamlit, totalmente funcional en múltiples páginas.
* **Soporte Multilingüe:** Completa y fluida traducción entre Español e Inglés.
* **Visualizaciones Avanzadas:** Gráficos interactivos creados con Plotly para el perfil del candidato, incluyendo comparativas a escala y un innovador análisis visual de la zona habitable.
* **Transparencia del Modelo:** Muestra la importancia de cada característica en las predicciones, explicando el "porqué" detrás de las decisiones de la IA.

### Tecnología Utilizada

* **Lenguaje:** Python
* **Machine Learning:** Scikit-learn (RandomForestClassifier, GridSearchCV)
* **Análisis de Datos:** Pandas, NumPy
* **Aplicación Web:** Streamlit
* **Visualización de Datos:** Plotly
* **Alojamiento:** Streamlit Community Cloud & GitHub

### Cómo Ejecutar el Proyecto Localmente

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/zzzJanozzz/OrbitaKeplerApp.git](https://github.com/zzzJanozzz/OrbitaKeplerApp.git)
    cd OrbitaKeplerApp
    ```
2.  **Crear un entorno virtual (recomendado):**
    ```bash
    python -m venv .venv
    # En Windows: .venv\Scripts\activate
    # En MacOS/Linux: source .venv/bin/activate
    ```
3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Ejecutar la aplicación:**
    ```bash
    streamlit run App.py
    ```

### El Equipo

**Equipo Órbita Kepler** | Evento Local: Santa Rosa de Calamuchita

* Jano Nieva
* Leon Gemiani
* Máximo Amaya
* Maia Fernandez
* José Godoy

---
---

## <a name="english-version"></a>🇬🇧 English Version

### About The Project

NASA's Kepler Space Telescope has provided us with a "tsunami" of data, monitoring hundreds of thousands of stars for planetary transits. The volume and complexity of this data make manual review impossible. **Órbita Kepler** was born as a solution to this challenge, using Artificial Intelligence to automate the detection of exoplanets.

Our platform is not just a classifier. It is an end-to-end discovery tool that:
1.  **Filters Intelligently:** It uses an AI model (Random Forest) with a robust accuracy of **98.43%** to distinguish between false positives and exoplanet candidates.
2.  **Visualizes and Explains:** It transforms abstract data into visual planetary profiles, showcasing size comparisons, habitable zone analysis, and the features that influenced the AI's decision.
3.  **Connects to Real Science:** It compares candidates against NASA's official database to find known exoplanets with similar characteristics, providing immediate scientific context.

### Key Features

* **Optimized AI:** The model was fine-tuned using **Hyperparameter Tuning** (`GridSearchCV`) to prevent overfitting and ensure its robustness with new, unseen data.
* **Interactive Dashboard:** A clean and professional user interface built with Streamlit, fully functional across multiple pages.
* **Bilingual Support:** Complete and seamless translation between Spanish and English.
* **Advanced Visualizations:** Interactive charts created with Plotly for the candidate profile, including to-scale comparisons and an innovative visual analysis of the habitable zone.
* **Model Transparency:** Displays the importance of each feature in the predictions, explaining the "why" behind the AI's decisions.

### Technology Stack

* **Language:** Python
* **Machine Learning:** Scikit-learn (RandomForestClassifier, GridSearchCV)
* **Data Analysis:** Pandas, NumPy
* **Web Application:** Streamlit
* **Data Visualization:** Plotly
* **Hosting:** Streamlit Community Cloud & GitHub

### How To Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/zzzJanozzz/OrbitaKeplerApp.git](https://github.com/zzzJanozzz/OrbitaKeplerApp.git)
    cd OrbitaKeplerApp
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    # On Windows: .venv\Scripts\activate
    # On MacOS/Linux: source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    streamlit run App.py
    ```

### The Team

**Team Órbita Kepler** | Local Event: Santa Rosa de Calamuchita

* Jano Nieva
* Leon Gemiani
* Máximo Amaya
* Maia Fernandez
* José Godoy
