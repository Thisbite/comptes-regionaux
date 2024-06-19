import streamlit as st
import data
import pandas as pd
from io import BytesIO

# Titre de l'application
st.set_page_config(page_title="comptes regionaux", page_icon="👗", layout="wide")
st.title("Base de données des annuaires statistiques")

st.sidebar.title("Menu")
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    page = st.sidebar.selectbox("Choisir une page", ["Connexion"])
else:
    if st.session_state['role'] == 'admin':
        page = st.sidebar.selectbox("Choisir une page",
                                    ["Nouveau utilisateur","Annuaire statistique"])


if page == "Connexion":
    st.header("Connexion des Utilisateurs")

    with st.form("connexion_utilisateur"):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        submitted = st.form_submit_button("Se connecter")

        if submitted:
            user = data.verifier_utilisateur(username, password)
            if user:
                st.session_state['logged_in'] = True
                st.session_state['role'] = user['role']  # Store the user role
                st.success("Connexion réussie.")
                st.rerun()
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect.")

elif page == "Nouveau utilisateur" and st.session_state['logged_in']:
    st.header("Enregistrement des Utilisateurs")

    with st.form("enregistrement_utilisateur"):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        role = st.selectbox("Rôle", ["admin", "agent"])
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            if username and password and role:
                data.enregistrer_utilisateur(username, password, role)
                st.success("Utilisateur enregistré avec succès.")
            else:
                st.error("Veuillez remplir tous les champs.")


elif page== "Annuaire statistique":

    st.write("Existence des partis  politiques par département de 2015-2019")
    # Section pour télécharger un fichier Excel

    uploaded_file = st.file_uploader("Importer les données Excel ", type=["xlsx"],key="existence_partis")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "partis_politique", "Annee_2015", "Annee_2016", "Annee_2017",
                            "Annee_2018", "Annee_2019"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_existence_partis(
                        row['direction'], row['region'], row['partis_politique'],
                        row['Annee_2015'], row['Annee_2016'], row['Annee_2017'],
                        row['Annee_2018'], row['Annee_2019']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")


    st.write("Naissances enregistrées et parvenus au niveau central selon le type de centre de la Région  par Département et par Sous-Préfecture en 2019")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"],key="faits_naissace")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "departement", "sous_prefecture", "faits_civil",
                            "type_de_centre_civil", "dans_les_delais_3_mois", "hors_delai_4_12_mois",
                            "hors_delai_plus_de_12_mois", "total_faits_naissance"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_faits_civils(
                        row['direction'], row['region'], row['departement'], row['sous_prefecture'],
                        row['faits_civil'], row['type_de_centre_civil'], row['dans_les_delais_3_mois'],
                        row['hors_delai_4_12_mois'], row['hors_delai_plus_de_12_mois'], row['total_faits_naissance']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")


    st.write("Nombre de responsables départementaux  des partis politiques selon le sexe  dans la région")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"], key="tab_respo_politique")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "partis_politique", "departement", "hommes", "femmes",
                            "total_sexe"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_tab_respo_pltq_dep(
                        row['direction'], row['region'], row['annee'], row['partis_politique'], row['departement'],
                        row['hommes'], row['femmes'], row['total_sexe']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")


    #st.subheader("Tableau 1.2.1: Existence des partis  politiques par département sur les 5 dernières années 2015-2019")

    #st.write("1=présent ; 0=absent")
    #st.write(data.obtenir_existence_partis())

    #st.subheader("Tableau 2.1.13 : Naissances enregistrées et parvenus au niveau central selon le type de centre de la Région du Poro par Département et par Sous-Préfecture en 2019")
    #st.write(data.obtenir_faits_civils())
    #st.write(data.obtenir_tab_respo_poltque_depart_sex())