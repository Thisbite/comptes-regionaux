import streamlit as st
import data
import pandas as pd

# Titre de l'application
st.set_page_config(page_title="comptes regionaux", page_icon="👗", layout="wide")
st.title("Données des comptes régionaux : Section agriculture vivrière")

st.sidebar.title("Menu")
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    page = st.sidebar.selectbox("Choisir une page", ["Connexion"])
else:
    if st.session_state['role'] == 'admin':
        page = st.sidebar.selectbox("Choisir une page",
                                    ["Saisi de données", "Importer le fichier Excel", "Statistiques","Modifier données","Enregistrement"])
    elif st.session_state['role'] == 'employe':
        page = st.sidebar.selectbox("Choisir une page", ["Performance des Ouvriers"])

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

elif page == "Enregistrement" and st.session_state['logged_in']:
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





elif page=="Saisi de données":
    # Formulaire d'entrée de données
    with st.form("agriculture_vivriere_form"):
        direction = st.text_input("Direction")
        region = st.text_input("Région")
        annee = st.text_input("Année")
        codes = st.text_input("Codes")
        libelle_produit = st.text_input("Libellé du produit")
        quantite = st.number_input("Quantité", min_value=0.0)
        valeur = st.number_input("Valeur", min_value=0.0)
        prix_unitaire = st.number_input("Prix unitaire", min_value=0.0)
        superficie = st.number_input("Superficie", min_value=0.0)
        effectif = st.number_input("Effectif", min_value=0, step=1)
        masse_salariale = st.number_input("Masse salariale", min_value=0.0)

        submit_button = st.form_submit_button("Enregistrer")

    # Enregistrement des données lorsque le bouton est cliqué
    if submit_button:
        data.enregistrer_agriculture_vivirier(direction, region, annee, codes, libelle_produit, quantite, valeur,
                                              prix_unitaire, superficie, effectif, masse_salariale)
        st.success("Les données ont été enregistrées avec succès!")
elif page=="Importer le fichier Excel":
    # Section pour télécharger un fichier Excel et enregistrer les données dans la base de données
    st.subheader("Télécharger un fichier Excel")
    uploaded_file = st.file_uploader("Télécharger un fichier Excel", type=["xlsx"])

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "codes", "libelle_produit",
                            "quantite", "valeur", "prix_unitaire", "superficie",
                            "effectif", "masse_salariale"]

        if all(column in df.columns for column in expected_columns):
            # Afficher les données du fichier
            st.dataframe(df)

            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_agriculture_vivirier(
                        row['direction'], row['region'], row['annee'], row['codes'], row['libelle_produit'],
                        row['quantite'], row['valeur'], row['prix_unitaire'], row['superficie'],
                        row['effectif'], row['masse_salariale']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")
elif page=="Statistiques":
    st.subheader("Statistiques de la production de riz par région")
    df_riz = data.obtenir_statistiques_riz()
    st.write(df_riz)
    st.write("Statistique par code du produit")
    with st.form("code_form"):
        code = st.selectbox("Choisir le code",options=data.obtenir_code())
        submit_code = st.form_submit_button("Obtenir les statistiques")

    # Affichage des statistiques lorsque le bouton est cliqué
    if submit_code:
        df_statistiques = data.obtenir_statistiques_par_code(code)
        if not df_statistiques.empty:
            st.write("Statistiques de production pour le code:", code)
            st.write(df_statistiques)
        else:
            st.error("Aucune donnée trouvée pour ce code.")
      # Affichage des données enregistrées
    st.subheader("Notre base de données d'agriculture vivrière")
    df_enregistrees = data.obtenir_agriculture_vivriere()
    st.write(df_enregistrees)

elif page=="Modifier données":
    st.subheader("Modifier des enregistrements")
    with st.form("modify_form"):
        st.write("Recherche à partir d'ancienne données")
        direction = st.selectbox("Choisir la DR",options=data.obtenir_direction())
        annee = st.text_input("Année (pour trouver l'enregistrement à modifier)")
        code = st.selectbox("Choisir le code",options=data.obtenir_code())

        st.write("Entrez les nouvelles valeurs :")
        new_direction = st.text_input("Nouvelle direction")
        new_region = st.text_input("Nouvelle région")
        new_annee = st.text_input("Nouvelle année")
        new_code = st.text_input("Nouveau code")
        new_libelle_produit = st.text_input("Nouveau libellé du produit")
        new_quantite = st.number_input("Nouvelle quantité", min_value=0.0)
        new_valeur = st.number_input("Nouvelle valeur", min_value=0.0)
        new_prix_unitaire = st.number_input("Nouveau prix unitaire", min_value=0.0)
        new_superficie = st.number_input("Nouvelle superficie", min_value=0.0)
        new_effectif = st.number_input("Nouvel effectif", min_value=0, step=1)
        new_masse_salariale = st.number_input("Nouvelle masse salariale", min_value=0.0)

        submit_modify = st.form_submit_button("Modifier")

    # Modification des données lorsque le bouton est cliqué
    if submit_modify:
        new_values = (new_direction, new_region, new_annee, new_code, new_libelle_produit, new_quantite, new_valeur,
                      new_prix_unitaire, new_superficie, new_effectif, new_masse_salariale)
        data.modifier_agriculture_vivriere(direction, annee, code, new_values)
        st.success(
            f"Les données pour la direction '{direction}', l'année '{annee}' et le code '{code}' ont été modifiées avec succès!")

    # Affichage des données enregistrées

elif st.checkbox("Supprimer une données"):
    st.subheader("Supprimer des enregistrements")
    with st.form("delete_form"):
        direction = st.text_input("Direction")
        annee = st.text_input("Année")
        code = st.text_input("Code")
        submit_delete = st.form_submit_button("Supprimer")

    # Suppression des données lorsque le bouton est cliqué
    if submit_delete:
        data.supprimer_agriculture_vivriere(direction, annee, code)
        st.success(
            f"Les données pour la direction '{direction}', l'année '{annee}' et le code '{code}' ont été supprimées avec succès!")
