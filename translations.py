# translations.py

TRANSLATIONS = {
    'es': {
        # Títulos de página
        "app_title": "Cazador de Exoplanetas IA",
        "home_page_title": "Inicio - Cazador de Exoplanetas IA",
        "prediction_page_title": "Predicción Interactiva",
        "performance_page_title": "Rendimiento del Modelo",
        "about_page_title": "Sobre el Proyecto",
        "tech_info_page_title": "Información Técnica",
        "candidate_profile_title": "🪐 Perfil del Candidato Planetario",

        # Barra lateral y comunes
        "sidebar_nav_title": "🚀 Navegación",
        "sidebar_header": "🛰️ Parámetros de la Señal",
        "sidebar_success": "Selecciona una página arriba.",
        "example_select_label": "Cargar datos de ejemplo:",
        "manual_input_option": "(Introducir manualmente)",
        "confirmed_exoplanet_option": "Exoplaneta Confirmado (Kepler-227 c)",
        "false_positive_option": "Falso Positivo Conocido",
        "predict_button": "✨ Predecir ahora",
        "expander_flags": "Flags de Falso Positivo",
        "expander_stellar": "Parámetros Estelares",
        
        # Página Principal (app.py)
        "welcome_title": "🔭 Bienvenido al Cazador de Exoplanetas IA",
        "welcome_markdown": """
        Este es el panel de control para el proyecto del **NASA Space Apps Challenge 2025**.
        
        Nuestra herramienta utiliza un modelo de **Inteligencia Artificial (Random Forest)** para analizar datos del Telescopio Kepler y predecir si una señal corresponde a un exoplaneta real.
        
        **👈 Usa la navegación para explorar:**
        """,
        "nasa_poster_caption": "Póster del Exoplanet Travel Bureau de la NASA para el sistema TRAPPIST-1.",
        "key_metrics_header": "Métricas Clave del Proyecto",
        "accuracy_label": "Precisión del Modelo",
        "planet_detection_rate": "Tasa de Detección de Planetas",
        "signals_analyzed_label": "Señales Analizadas",
        "cta_prediction_header": "✨ Predicción Interactiva",
        "cta_prediction_text": "Usa nuestra IA en tiempo real para clasificar una nueva señal planetaria y descubre qué tipo de mundo podría ser.",
        "cta_performance_header": "📊 Rendimiento del Modelo",
        "cta_performance_text": "Explora las estadísticas detalladas y la matriz de confusión para entender cómo 'piensa' nuestro modelo.",

        # Página de Predicción
        "prediction_title": "✨ Predicción Interactiva",
        "prediction_intro": "Usa los controles en la barra lateral para introducir los datos de una señal y obtener una clasificación de la IA.",
        "prediction_results_header": "Resultado del Análisis",
        "gauge_title": "Probabilidad de ser Exoplaneta",
        "diagnosis_success": "**Diagnóstico: ALTA PROBABILIDAD DE EXOPLANETA** 🪐",
        "diagnosis_error": "**Diagnóstico: PROBABLE FALSO POSITIVO** 🛰️",
        "diagnosis_explanation": "La IA analizó las 16 características de la señal para llegar a esta conclusión.",
        "model_confidence_text": "La confianza del modelo en que esta señal es un exoplaneta es del",
        "feature_importance_header": "¿En qué se basó la IA para decidir?",
        "feature_importance_text": "Este gráfico muestra qué características fueron más influyentes para esta predicción específica.",
        "info_awaiting_input": "Por favor, introduce los parámetros en la barra lateral y presiona 'Predecir ahora'.",

        # Página de Rendimiento
        "performance_title": "📊 Rendimiento del Modelo",
        "performance_intro": "Esta página muestra la evaluación de nuestro modelo de IA contra un set de datos de prueba que nunca vio durante el entrenamiento.",
        "optimized_model_comment": "Modelo Optimizado y Robusto",
        "estimator_comment": "200 estimadores (árboles).",
        "optimization_process_header": "El Proceso de Optimización (Hyperparameter Tuning)",
        "optimization_process_text": "Para asegurar la máxima fiabilidad, realizamos un proceso llamado **Ajuste de Hiperparámetros**.",
        "overfitting_challenge_header": "El Desafío del Sobreajuste (Overfitting)",
        "overfitting_challenge_text": "Un modelo puede **memorizar** los datos de entrenamiento, fallando con datos nuevos. Nuestro modelo original tenía una precisión del **98.50%**, pero queríamos asegurarnos de que no estuviera sobreajustado.",
        "perfect_config_header": "Buscando la Configuración Perfecta",
        "perfect_config_text": "Probamos **27 combinaciones** de 'reglas' (hiperparámetros). La mejor configuración encontrada fue:",
        "conclusion_header": "Conclusión: Un Modelo Más Inteligente, No Solo con Mejor Nota",
        "conclusion_text": "El nuevo modelo optimizado tiene una precisión del **98.43%**. Aunque es una fracción más bajo, este modelo es **significativamente mejor** y más **robusto**.",
        "confusion_matrix_header": "Matriz de Confusión",
        "detailed_error_analysis_header": "Análisis Detallado de Errores",
        "fp_analysis_text": "- **Falsos Positivos (2):** La IA dio solo 2 'falsas alarmas', no haciendo perder tiempo a los científicos.",
        "fn_analysis_text": "- **Falsos Negativos (19):** La IA no detectó 19 planetas de un total de **459 planetas reales** en el set de prueba. Esto representa una tasa de éxito del **95.8%**.",
        "confusion_matrix_caption": "Matriz de Confusión en el set de prueba (1404 ejemplos).",
        
        # Página Sobre el Proyecto
        "about_title": "🛰️ Sobre el Proyecto",
        "about_challenge_header": "Desafío: 'Un Mundo Lejano: Caza de Exoplanetas con IA'",
        "about_challenge_text": "Este proyecto fue desarrollado para el **NASA International Space Apps Challenge 2025**.",
        "about_tech_header": "La Tecnología",
        "about_tech_list": """
        - **Lenguaje:** Python
        - **Librerías Principales:**
            - **Scikit-learn:** Para construir y entrenar el modelo de Machine Learning (Random Forest).
            - **Optimización del Modelo:** Se utilizó `GridSearchCV` para realizar un ajuste de hiperparámetros y encontrar el modelo más robusto.
            - **Pandas:** Para la manipulación y limpieza de datos.
            - **Streamlit:** Para construir esta aplicación web interactiva.
            - **Plotly:** Para las visualizaciones de datos avanzadas.
        """,
        "about_team_header": "El Equipo",
        "about_team_list": """
        **Nombre del Equipo:** Órbita Kepler
        - Jano Nieva
        - Leon Gemiani
        - Máximo Amaya
        - Maia Fernandez
        - José Godoy
        
        **Evento Local:** Santa Rosa de Calamuchita
        """,
        
        # Página de Información Técnica
        "tech_info_title": "ℹ️ Información Técnica y Científica",
        "exoplanet_header": "¿Qué es un Exoplaneta?",
        "exoplanet_text": "Un **exoplaneta** es un planeta que orbita una estrella diferente a nuestro Sol.",
        "light_curve_header": "El Método de Tránsito y las Curvas de Luz",
        "light_curve_text_1": "El **método de tránsito** detecta planetas al medir la diminuta caída de brillo de una estrella cuando un planeta pasa por delante.",
        "light_curve_graph_title": "Ejemplo de una Curva de Luz Idealizada",
        "light_curve_text_2": "Cuando graficamos el brillo de una estrella, la caída causada por un tránsito crea una **curva de luz**.",
        "how_ai_thinks_header": "¿Cómo 'Piensa' nuestra IA?",
        "how_ai_thinks_text_1": "Nuestro modelo no procesa imágenes, sino **características numéricas** extraídas de los datos.",
        "how_ai_thinks_text_2": "**Analogía del Detective:** La IA analiza las **pistas (features)**, como la profundidad o duración del tránsito, para aprender patrones.",
        "how_to_use_model_header": "¿Cómo se puede usar nuestro modelo?",
        "how_to_use_model_text_1": "Actúa como un **filtro inteligente de alta velocidad** para que los científicos enfoquen su tiempo en los candidatos más prometedores.",
        "how_to_use_model_text_2": "El archivo `modelo_caza_planetas_optimizado.joblib` es portable y puede ser usado en otras investigaciones.",
        
        # Página de Perfil del Candidato
        "candidate_profile_intro": "Esta página genera visualizaciones para ayudarnos a entender qué tipo de mundo podría ser un candidato.",
        "candidate_profile_disclaimer": "Mostrando perfil para un candidato de ejemplo (Kepler-227 c).",
        "size_comparison_header": "Comparación de Tamaño Relativo",
        "habitable_zone_header": "Análisis de la Zona Habitable",
        "habitable_zone_success": "¡El candidato está en la 'Zona Ricitos de Oro' de su estrella, donde podría existir agua líquida!",
        "habitable_zone_warning": "El candidato está fuera de la Zona Habitable (demasiado caliente o demasiado frío para agua líquida).",
        "similarity_header": "Similitud con Planetas Conocidos",
        "similarity_success": "El candidato más similar en la base de datos de la NASA es **{name}**.",
        "csv_error_text": "Error: No se pudo encontrar el archivo 'exoplanetas_conocidos.csv'.",
        "planet_comparison_title": "Comparación de Tamaño: Candidato vs. Planetas del Sistema Solar",
        "habitable_zone_analysis_title": "Análisis de la Zona Habitable del Sistema Estelar",
        "too_hot_label": "Demasiado Caliente",
        "habitable_label": "Habitable",
        "too_cold_label": "Demasiado Frío",
        "star_label": "Estrella",
        "candidate_label": "Candidato",
        "size_comparison_text": "Este candidato tiene un radio **{radio:.2f} veces** el de la Tierra."
    },
    'en': {
        # Page Titles
        "app_title": "AI Exoplanet Hunter",
        "home_page_title": "Home - AI Exoplanet Hunter",
        "prediction_page_title": "Interactive Prediction",
        "performance_page_title": "Model Performance",
        "about_page_title": "About the Project",
        "tech_info_page_title": "Technical Information",
        "candidate_profile_title": "🪐 Planetary Candidate Profile",

        # Sidebar and Common
        "sidebar_nav_title": "🚀 Navigation",
        "sidebar_header": "🛰️ Signal Parameters",
        "sidebar_success": "Select a page above.",
        "example_select_label": "Load example data:",
        "manual_input_option": "(Enter manually)",
        "confirmed_exoplanet_option": "Confirmed Exoplanet (Kepler-227 c)",
        "false_positive_option": "Known False Positive",
        "predict_button": "✨ Predict Now",
        "expander_flags": "False Positive Flags",
        "expander_stellar": "Stellar Parameters",
        
        # Home Page (app.py)
        "welcome_title": "🔭 Welcome to the AI Exoplanet Hunter",
        "welcome_markdown": """
        This is the dashboard for the **NASA Space Apps Challenge 2025** project.
        
        Our tool uses an **Artificial Intelligence (Random Forest)** model to analyze data from the Kepler Telescope and predict if a signal corresponds to a real exoplanet.
        
        **👈 Use the navigation to explore:**
        """,
        "nasa_poster_caption": "NASA's Exoplanet Travel Bureau poster for the TRAPPIST-1 system.",
        "key_metrics_header": "Key Project Metrics",
        "accuracy_label": "Model Accuracy",
        "planet_detection_rate": "Planet Detection Rate",
        "signals_analyzed_label": "Signals Analyzed",
        "cta_prediction_header": "✨ Interactive Prediction",
        "cta_prediction_text": "Use our AI in real-time to classify a new planetary signal and discover what kind of world it might be.",
        "cta_performance_header": "📊 Model Performance",
        "cta_performance_text": "Explore the detailed statistics and confusion matrix to understand how our model 'thinks'.",
        
        # Prediction Page
        "prediction_title": "✨ Interactive Prediction",
        "prediction_intro": "Use the controls in the sidebar to input signal data and get a classification from the AI.",
        "prediction_results_header": "Analysis Result",
        "gauge_title": "Probability of being an Exoplanet",
        "diagnosis_success": "**Diagnosis: HIGH PROBABILITY OF EXOPLANET** 🪐",
        "diagnosis_error": "**Diagnosis: LIKELY A FALSE POSITIVE** 🛰️",
        "diagnosis_explanation": "The AI analyzed the 16 signal features to reach this conclusion.",
        "model_confidence_text": "The model's confidence that this signal is an exoplanet is",
        "feature_importance_header": "What was the basis for the AI's decision?",
        "feature_importance_text": "This chart shows which features were most influential for this specific prediction.",
        "info_awaiting_input": "Please enter the parameters in the sidebar and press 'Predict Now'.",
        
        # Performance Page
        "performance_title": "📊 Model Performance",
        "performance_intro": "This page displays the evaluation of our AI model against a test dataset it never saw during training.",
        "optimized_model_comment": "Optimized and Robust Model",
        "estimator_comment": "200 estimators (trees).",
        "optimization_process_header": "The Optimization Process (Hyperparameter Tuning)",
        "optimization_process_text": "To ensure maximum reliability, we performed a process called **Hyperparameter Tuning**.",
        "overfitting_challenge_header": "The Challenge of Overfitting",
        "overfitting_challenge_text": "A model can **memorize** training data, failing with new data. Our original model had **98.50%** accuracy, but we wanted to ensure it wasn't overfitted.",
        "perfect_config_header": "Searching for the Perfect Configuration",
        "perfect_config_text": "We tested **27 different combinations** of 'rules' (hyperparameters). The best configuration found was:",
        "conclusion_header": "Conclusion: A Smarter Model, Not Just a Better Grade",
        "conclusion_text": "The new, optimized model has an accuracy of **98.43%**. While fractionally lower, this model is **significantly better** and more **robust**.",
        "confusion_matrix_header": "Confusion Matrix",
        "detailed_error_analysis_header": "Detailed Error Analysis",
        "fp_analysis_text": "- **False Positives (2):** The AI made only 2 'false alarms', not wasting scientists' time.",
        "fn_analysis_text": "- **False Negatives (19):** The AI missed 19 planets out of a total of **459 real planets** in the test set. This represents a success rate of **95.8%**.",
        "confusion_matrix_caption": "Confusion Matrix on the test set (1404 examples).",
        
        # About Page
        "about_title": "🛰️ About the Project",
        "about_challenge_header": "Challenge: 'A Distant World: Exoplanet Hunting with AI'",
        "about_challenge_text": "This project was developed for the **NASA International Space Apps Challenge 2025**.",
        "about_tech_header": "Technology Stack",
        "about_tech_list": """
        - **Language:** Python
        - **Main Libraries:**
            - **Scikit-learn:** To build and train the Machine Learning model (Random Forest).
            - **Model Optimization:** `GridSearchCV` was used to perform hyperparameter tuning to find the most robust model.
            - **Pandas:** For data manipulation and cleaning.
            - **Streamlit:** To build this interactive web application.
            - **Plotly:** For advanced data visualizations.
        """,
        "about_team_header": "The Team",
        "about_team_list": """
        **Team Name:** Órbita Kepler
        - Jano Nieva
        - Leon Gemiani
        - Máximo Amaya
        - Maia Fernandez
        - José Godoy
        
        **Local Event:** Santa Rosa de Calamuchita
        """,
        
        # Technical Information Page
        "tech_info_title": "ℹ️ Technical & Scientific Information",
        "exoplanet_header": "What is an Exoplanet?",
        "exoplanet_text": "An **exoplanet** is a planet that orbits a star other than our Sun.",
        "light_curve_header": "The Transit Method and Light Curves",
        "light_curve_text_1": "The **transit method** detects planets by measuring the tiny dip in a star's brightness when a planet passes in front.",
        "light_curve_graph_title": "Example of an Idealized Light Curve",
        "light_curve_text_2": "When we plot a star's brightness, the dip caused by a transit creates a **light curve**.",
        "how_ai_thinks_header": "How Does Our AI 'Think'?",
        "how_ai_thinks_text_1": "Our model processes **numerical features** extracted from the data, not images.",
        "how_ai_thinks_text_2": "**Detective Analogy:** The AI analyzes **clues (features)**, like transit depth or duration, to learn patterns.",
        "how_to_use_model_header": "How Can Our Model Be Used?",
        "how_to_use_model_text_1": "It acts as a **high-speed, intelligent filter** to help scientists focus on the most promising candidates.",
        "how_to_use_model_text_2": "The `modelo_caza_planetas_optimizado.joblib` file is portable and can be used in other research.",
        
        # Candidate Profile Page
        "candidate_profile_intro": "This page generates visualizations to help us understand what kind of world a candidate might be.",
        "candidate_profile_disclaimer": "Showing profile for an example candidate (Kepler-227 c).",
        "size_comparison_header": "Relative Size Comparison",
        "habitable_zone_header": "Habitable Zone Analysis",
        "habitable_zone_success": "The candidate is in its star's 'Goldilocks Zone', where liquid water could exist!",
        "habitable_zone_warning": "The candidate is outside the Habitable Zone (either too hot or too cold for liquid water).",
        "similarity_header": "Similarity to Known Planets",
        "similarity_success": "The most similar candidate in the NASA database is **{name}**.",
        "csv_error_text": "Error: Could not find 'exoplanetas_conocidos.csv' file.",
        "planet_comparison_title": "Size Comparison: Candidate vs. Solar System Planets",
        "habitable_zone_analysis_title": "Stellar System Habitable Zone Analysis",
        "too_hot_label": "Too Hot",
        "habitable_label": "Habitable",
        "too_cold_label": "Too Cold",
        "star_label": "Star",
        "candidate_label": "Candidate",
        "size_comparison_text": "This candidate has a radius **{radio:.2f} times** that of Earth."
    }
}