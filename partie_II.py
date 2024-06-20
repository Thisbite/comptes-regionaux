import data_p2
import  streamlit as st
import pandas as pd


def partie_II_annuaire():
    st.write("Tableau 2.1.1: Population de la région , par Département et par sous-préfecture")
    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab211_pop_dep_sous_pref_sex")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "sous_prefecture", "hommes", "femmes",
                            "total_sexe", "rapport_masculinite"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab211_pop_dep_sous_pref_sex(
                        row['direction'], row['region'], row['annee'], row['departement'],
                        row['sous_prefecture'], row['hommes'], row['femmes'],
                        row['total_sexe'], row['rapport_masculinite']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    # Afficher les données de la table
    if st.button('Afficher les données de la table'):
        rows = data_p2.obtenir_tab211_pop_dep_sous_pref_sex()
        df_table = pd.DataFrame(rows, columns=[
            'id', 'direction', 'region', 'annee', 'departement', 'sous_prefecture', 'hommes', 'femmes', 'total_sexe',
            'rapport_masculinite'
        ])
        st.write('Données de Population de la région , par Département et par sous-préfecture')
        st.dataframe(df_table)

    st.write("Tableau 2.1.2: Répartition  de la population de la région  du Poro par grand  groupe d’âge selon le sexe")

    # Charger le fichier Excel
    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab212_repa_pop_grou_age")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "groupe_age", "hommes", "femmes", "total_sexe",
                            "rapport_masculinite"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab212_repa_pop_grou_age(
                        row['direction'], row['region'], row['annee'], row['groupe_age'],
                        row['hommes'], row['femmes'], row['total_sexe'], row['rapport_masculinite']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    # Afficher les données de la table
    if st.button('Afficher les données de la table'):
        rows = data_p2.obtenir_tab212_repa_pop_grou_age()
        df_table = pd.DataFrame(rows, columns=[
            'id', 'direction', 'region', 'annee', 'groupe_age', 'hommes', 'femmes', 'total_sexe', 'rapport_masculinite'
        ])
        st.write('Données de la répartition  de la population de la région ,par grand  groupe d’âge selon le sexe')
        st.dataframe(df_table)

    st.write("Tableau 2.1.3: Population du département  par tranche d'âge selon la sous-préfecture et le sexe")
    # Charger le fichier Excel
    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab213_pop_dep_tranc_s_pref_sex")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "sous_prefecture", "tranche_age", "hommes",
                            "femmes", "total_sexe"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab213_pop_dep_tranc_s_pref_sex(
                        row['direction'], row['region'], row['annee'], row['departement'],
                        row['sous_prefecture'], row['tranche_age'], row['hommes'], row['femmes'], row['total_sexe']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    # Afficher les données de la table
    if st.button('Afficher les données de la table'):
        rows = data_p2.obtenir_tab213_pop_dep_tranc_s_pref_sex()
        df_table = pd.DataFrame(rows, columns=[
            'id', 'direction', 'region', 'annee', 'departement', 'sous_prefecture', 'tranche_age', 'hommes', 'femmes',
            'total_sexe'
        ])
        st.write('Données de la table tab213_pop_dep_tranc_s_pref_sex:')
        st.dataframe(df_table)

    return