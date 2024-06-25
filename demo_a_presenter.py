import sqlite3
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connexion à la base de données
conn = sqlite3.connect('comptes_regionaux.db')
cursor = conn.cursor()

def enregistrement_tab2112_fait(direction, region, departement, sous_prefecture, faits_civil, type_etat_civil, annee, nombre_fait):
    cursor.execute('''
        INSERT INTO tab2112_faits_civils (direction, region, departement, sous_prefecture, faits_civil, type_etat_civil, annee, nombre_fait)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (direction, region, departement, sous_prefecture, faits_civil, type_etat_civil, annee, nombre_fait))
    conn.commit()

def obtenir_tab2112_fait():
    cursor.execute('SELECT * FROM tab2112_faits_civils')
    data = cursor.fetchall()
    df_data = pd.DataFrame(data, columns=['ID', 'Direction', 'Region', 'Departement', 'Sous-prefecture', 'Faits Civil', 'Type Etat Civil', 'Annee', 'Nombre Fait'])
    return df_data

def page_tab2112_faits_civils():
    # Ajouter du CSS pour styliser la page
    st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            color: #333;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: #f0f2f6;
        }
        header {
            background-color: #004080;
            color: white;
            padding: 10px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
        .stButton button {
            background-color: #004080;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .stFileUploader label {
            color: #004080;
            font-weight: bold;
        }
        .stDataFrame {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    st.header("Importation des Faits Civils (Tab2112)")

    uploaded_file = st.file_uploader("Choisissez un fichier Excel", type=["xlsx"])

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)
        st.write("Aperçu du fichier importé:")
        st.dataframe(df)

        if st.button("Enregistrer dans la base de données"):
            for index, row in df.iterrows():
                enregistrement_tab2112_fait(
                    row['direction'],
                    row['region'],
                    row['departement'],
                    row['sous_prefecture'],
                    row['faits_civil'],
                    row['type_etat_civil'],
                    row['annee'],
                    row['nombre_fait']
                )
            st.success("Les données ont été enregistrées avec succès.")

    if st.button("Afficher les données enregistrées"):
        data = obtenir_tab2112_fait()
        st.write("Données enregistrées dans la base de données:")
        st.dataframe(data)

def page_statistique_faits_civils():
    # Ajouter du CSS pour styliser la page
    st.markdown("""
    <style>
        body {
            background-color: #f0f2f6;
            color: #333;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background-color: #f0f2f6;
        }
        header {
            background-color: #004080;
            color: white;
            padding: 10px 0;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
        .stButton button {
            background-color: #004080;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .stDataFrame {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    st.header("Statistiques des Faits Civils (Tab2112)")

    # Obtenir les données
    df = obtenir_tab2112_fait()

    st.subheader("Aperçu des Données")
    st.dataframe(df)


    st.subheader("Visualisations")

    # Sélectionner les filtres
    annee = st.selectbox("Choisir l'année", options=df['Annee'].unique())
    depart = st.selectbox("Choisir la sous-préfecture", options=df['Sous-prefecture'].unique())

    df_filtered = df[(df['Annee'] == annee) & (df['Sous-prefecture'] == depart)]

    st.write("Données Filtrées")
    st.dataframe(df_filtered)


# Exécuter les pages

