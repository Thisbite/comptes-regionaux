import streamlit as st
import data_p2
import data
import pandas as pd
import note_method as nm
import partie_I
import partie_II

# Configuration de la page
st.set_page_config(page_title="Comptes Régionaux", page_icon="📊", layout="wide")

# CSS pour styliser le contenu
st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf, #2e7bff);
        color: white;
    }
    .sidebar .sidebar-content h2 {
        color: white;
    }
    .reportview-container {
        background: #f5f5f5;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #2e7bcf;
    }
    </style>
    """, unsafe_allow_html=True)

# Afficher le logo de l'entreprise
st.image("images.png", width=200)  # Remplacez "images.png" par le chemin réel de votre logo

# Titre de l'application
st.title("Plateforme de saisie des données des Annuaires Statistiques")
st.write("------------------------------------------------------------")

# Sidebar menu
st.sidebar.title("Menu")
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    page = st.sidebar.selectbox("Choisir une page", ["Note de saisie", "Connexion"])
else:
    if st.session_state['role'] == 'superviseur':
        page = st.sidebar.selectbox("Choisir une page",
                                    ["Annuaire statistique", "Nouveau utilisateur"])

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
                st.experimental_rerun()
            else:
                st.error("Nom d'utilisateur ou mot de passe incorrect.")
elif page == "Note de saisie":
    nm.presentation()

elif page == "Nouveau utilisateur" and st.session_state['logged_in']:
    st.header("Enregistrement des Utilisateurs")

    with st.form("enregistrement_utilisateur"):
        username = st.text_input("Nom d'utilisateur")
        password = st.text_input("Mot de passe", type="password")
        role = st.selectbox("Rôle", ["superviseur", "agent"])
        submitted = st.form_submit_button("Enregistrer")

        if submitted:
            if username and password and role:
                data.enregistrer_utilisateur(username, password, role)
                st.success("Utilisateur enregistré avec succès.")
            else:
                st.error("Veuillez remplir tous les champs.")

elif page == "Annuaire statistique":
    st.markdown("<h2 style='color: #2e7bcf;'>Partie I : Présentation Générale de la région</h2>", unsafe_allow_html=True)
    st.write("Cette partie 1 de l'annuaire présente en général les données administratives des régions")
    if st.checkbox("Afficher les tableaux de la première partie"):
        partie_I.partie_I_annuaire()

    st.markdown("<h2 style='color: #2e7bcf;'>Partie II : Statistiques Démographiques et Sociales</h2>", unsafe_allow_html=True)
    if st.checkbox("Afficher les tableaux de la deuxième partie", key="TAB2CH"):
        partie_II.partie_II_annuaire()

    # Charger le fichier Excel
