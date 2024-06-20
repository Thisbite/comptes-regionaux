import streamlit as st
import  data_p2
import data
import pandas as pd

import partie_I


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
                                    ["Annuaire statistique","Nouveau utilisateur"])


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

    st.markdown("<h2 style='color: blue;'>Partie I : Présentation Générale de la région</h2>", unsafe_allow_html=True)
    st.write(" Cette partie 1 de l'annuaire présente en général les données administrative des régions")
    if st.checkbox("Afficher les tableaux de données"):
        partie_I.partie_I_annuaire()

    st.markdown("<h2 style='color: blue;'>Partie II : Statistiques Démographiques      et Sociales    </h2>", unsafe_allow_html=True)
    # Charger le fichier Excel

    # Charger le fichier Excel

    st.write("Tableau 2.1.7: Evolution de la population de la région ,par département et par sexe sur les  années")
    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab217_evolu_pop_reg_dep")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "sous_prefecture", "hommes", "femmes",
                            "total_sexe", "densite"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab217_evolu_pop_reg_dep(
                        row['direction'], row['region'], row['annee'], row['departement'],
                        row['sous_prefecture'], row['hommes'], row['femmes'], row['total_sexe'], row['densite']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    # Afficher les données de la table
    if st.button('Afficher les données de la table'):
        rows = data_p2.obtenir_tab217_evolu_pop_reg_dep()
        df_table = pd.DataFrame(rows, columns=[
            'id', 'direction', 'region', 'annee', 'departement', 'sous_prefecture', 'hommes', 'femmes', 'total_sexe',
            'densite'
        ])
        st.write('Données de la table tab217_evolu_pop_reg_dep:')
        st.dataframe(df_table)
