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
    if st.button('Afficher les données de la table',key="tb214"):
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
    if st.button('Afficher les données de la table',key="tab214A"):
        rows = data_p2.obtenir_tab213_pop_dep_tranc_s_pref_sex()
        df_table = pd.DataFrame(rows, columns=[
            'id', 'direction', 'region', 'annee', 'departement', 'sous_prefecture', 'tranche_age', 'hommes', 'femmes',
            'total_sexe'
        ])
        st.write('Données de la table tab213_pop_dep_tranc_s_pref_sex:')
        st.dataframe(df_table)

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
    if st.button('Afficher les données de la table',key="tab214AAB"):
        rows = data_p2.obtenir_tab217_evolu_pop_reg_dep()
        df_table = pd.DataFrame(rows, columns=[
            'id', 'direction', 'region', 'annee', 'departement', 'sous_prefecture', 'hommes', 'femmes', 'total_sexe',
            'densite'
        ])
        st.write('Données de la table tab217_evolu_pop_reg_dep:')
        st.dataframe(df_table)

    st.write(
        "Naissances enregistrées et parvenus au niveau central selon le type de centre de la Région  par Département et par Sous-Préfecture en 2019")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"], key="faits_naissace")

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
                    data_p2.enregistrer_faits_civils(
                        row['direction'], row['region'], row['departement'], row['sous_prefecture'],
                        row['faits_civil'], row['type_de_centre_civil'], row['dans_les_delais_3_mois'],
                        row['hors_delai_4_12_mois'], row['hors_delai_plus_de_12_mois'], row['total_faits_naissance']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")

    st.write("Tableau 2.1.8: Mariage selon l'état civil et le régime des biens par région")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab219_maria_eta_civ_regim")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "nat_coupl_ivoi", "nat_coupl_mixte",
                            "nat_coupl_etrang"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données",key="tab219FF"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab219_maria_eta_civ_regim(
                        row['direction'], row['region'], row['annee'], row['departement'],
                        row['nat_coupl_ivoi'], row['nat_coupl_mixte'], row['nat_coupl_etrang']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    st.write("Tableau 2.1.9: Mariage selon le régime matrimonial par région")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab219_maria_regim")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "departement", "annee", "reg_mat_bien_com", "reg_mat_bien_sep"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab219_maria_regim(
                        row['direction'], row['region'], row['departement'], row['annee'],
                        row['reg_mat_bien_com'], row['reg_mat_bien_sep']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    st.write("Tableau 2.1.10: Mariages par centre civil et département")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab2110_maria_centre_civil_dep")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "departement", "annee", "centre_etat_civil", "nat_coupl_ivoi",
                            "nat_coupl_mixte", "nat_coupl_etrang"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_maria_centre_civil_dep(
                        row['direction'], row['region'], row['departement'], row['annee'],
                        row['centre_etat_civil'], row['nat_coupl_ivoi'], row['nat_coupl_mixte'], row['nat_coupl_etrang']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    return


