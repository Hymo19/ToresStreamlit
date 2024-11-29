import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titre de l'application
st.title("Application de manipulation et visualisation des données")

# Importer un fichier CSV
uploaded_file = st.file_uploader("Importer un fichier CSV", type="csv")

if uploaded_file:
    try:
        # Charger les données dans un DataFrame
        data = pd.read_csv(uploaded_file)

        # Afficher un aperçu des données
        st.subheader("Aperçu des données")
        st.write(data.head())

        # Afficher les statistiques descriptives
        st.subheader("Statistiques descriptives")
        st.write(data.describe())

        # Afficher la liste des colonnes
        st.subheader("Colonnes disponibles")
        st.write(data.columns.tolist())

        # Manipulations de base

        # Filtrer les données
        st.subheader("Filtrage des données")
        column_to_filter = st.selectbox("Sélectionnez une colonne à filtrer", data.columns)
        unique_values = data[column_to_filter].unique()
        selected_value = st.selectbox("Choisissez une valeur", unique_values)
        filtered_data = data[data[column_to_filter] == selected_value]
        st.write("Données filtrées :")
        st.write(filtered_data)

        # Trier les données
        st.subheader("Tri des données")
        column_to_sort = st.selectbox("Sélectionnez une colonne pour trier", data.columns)
        sort_order = st.radio("Ordre de tri", ("Ascendant", "Descendant"))
        ascending = True if sort_order == "Ascendant" else False
        sorted_data = data.sort_values(by=column_to_sort, ascending=ascending)
        st.write("Données triées :")
        st.write(sorted_data)

        # Ajouter une colonne
        st.subheader("Ajout d'une colonne")
        new_col_name = st.text_input("Nom de la nouvelle colonne")
        if new_col_name:
            initial_value = st.text_input("Valeur initiale pour la colonne")
            if initial_value:
                data[new_col_name] = initial_value
                st.write("Nouvelle colonne ajoutée :")
                st.write(data.head())

        # Visualisations de base

        # Histogramme
        st.subheader("Histogramme")
        numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
        column_for_histogram = st.selectbox("Sélectionnez une colonne numérique", numeric_columns)
        if column_for_histogram:
            fig, ax = plt.subplots()
            sns.histplot(data[column_for_histogram], bins=20, kde=True, ax=ax, color="skyblue")
            ax.set_title(f"Histogramme de {column_for_histogram}")
            ax.set_xlabel(column_for_histogram)
            ax.set_ylabel("Fréquence")
            st.pyplot(fig)

        # Heatmap des corrélations
        st.subheader("Carte de corrélation")
        if len(numeric_columns) > 1:
            fig, ax = plt.subplots()
            sns.heatmap(data[numeric_columns].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

        # Exporter les données
        st.subheader("Exporter les données")
        if st.button("Exporter sous CSV"):
            data.to_csv("donnees_modifiees.csv", index=False)
            st.success("Fichier exporté sous le nom 'donnees_modifiees.csv'")

    except Exception as e:
        st.error(f"Erreur lors de l'importation du fichier : {e}")
