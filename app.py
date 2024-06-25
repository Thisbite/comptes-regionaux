import streamlit as st
import  data_p2
import data
import pandas as pd
import demo_a_presenter as dm
import partie_I
import partie_II

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
                                    ["Demo","Annuaire statistique","Nouveau utilisateur"])


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
    if st.checkbox("Afficher les données",key="TAB2CH"):
        partie_II.partie_II_annuaire()

    # Charger le fichier Excel








elif page=="Demo":
    dm.page_tab2112_faits_civils()
    dm.page_statistique_faits_civils()




