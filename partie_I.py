import  streamlit as st
import pandas as pd
import  data

def partie_I_annuaire():
    st.write("Existence des partis  politiques par département de 2015-2019")
    # Section pour télécharger un fichier Excel

    uploaded_file = st.file_uploader("Importer les données Excel ", type=["xlsx"], key="existence_partis")

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

    st.write("Tableau 1.2.3: Effectif des maires élus  par département et par sexe en  exercices municipaux")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"],
                                     key="tab_effec_maire_depart")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "total_sexe", "femmes"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_tab_effec_maire_depart(
                        row['direction'], row['region'], row['annee'], row['departement'], row['total_sexe'],
                        row['femmes']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")

    st.write(
        "Tableau 1.2.4: Répartition régionale des postes de responsabilités occupés par les femmes dans les mairies (maire, 1er adjoint au maire, 2ème adjoint au maire) aux exercices municipaux ")
    uploaded_file = st.file_uploader("Importer les données", type=["xlsx"],
                                     key="tab_repa_post_mai_fem_dep")
    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "fonction", "total_sexe", "femmes"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enreg_tab_repa_post_mai_fem_dep(
                        row['direction'], row['region'], row['annee'], row['departement'], row['fonction'],
                        row['total_sexe'], row['femmes']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")

    # Option pour afficher les données enregistrées
    if st.checkbox("Afficher les données enregistrées"):
        df_data = data.obtenir_tab_repa_post_mai_fem_dep()
        st.dataframe(df_data)

    st.write(
        "Tableau 1.2.5: Répartition des maires par département, par sexe et par partie politique (on pourrait aussi voir l'évolution)")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"],
                                     key="tab_repa_mair_dep_pol")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "partis_politique", "hommes", "femmes",
                            "total_sexe"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_tab_repa_mair_dep_pol(
                        row['direction'], row['region'], row['annee'], row['departement'], row['partis_politique'],
                        row['hommes'], row['femmes'], row['total_sexe']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")

    # Option pour afficher les données enregistrées
    if st.checkbox("Afficher les données enregistrées", key="tab125"):
        df_data = data.obtenir_tab_repa_mair_dep_pol()
        st.dataframe(df_data)

    st.write("Tableau 1.2.6: Répartition des adjoints au maire par département, par sexe et par partie politique ")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"],
                                     key="tab_repa_adj_mai_dep_p")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "partis_politique", "hommes", "femmes",
                            "total_sexe"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_tab_repa_adj_mai_dep_p(
                        row['direction'], row['region'], row['annee'], row['departement'], row['partis_politique'],
                        row['hommes'], row['femmes'], row['total_sexe']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")

    # Option pour afficher les données enregistrées
    if st.checkbox("Afficher les données enregistrées", key="tab126"):
        df_data = data.obtenir_tab_repa_adj_mai_dep_p()
        st.dataframe(df_data)

    st.write("Tableau 1.2.7 : Effectif des maires reconduits et nouvellement élus par département")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"],
                                     key="tab_mair_recon_nvl_dep")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "maire_nouveau", "maire_reconduit"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_tab_mair_recon_nvl_dep(
                        row['direction'], row['region'], row['annee'], row['departement'], row['maire_nouveau'],
                        row['maire_reconduit']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")

    # Option pour afficher les données enregistrées
    if st.checkbox("Afficher les données enregistrées", key="tab127"):
        df_data = data.obtenir_tab_mair_recon_nvl_dep()
        st.dataframe(df_data)

    st.write("Tableau 1.2.8: Répartition des députés par sexe et par partie politique")
    uploaded_file = st.file_uploader("Importer des données (format Excel)", type=["xlsx"])

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "partis_politique", "hommes", "femmes",
                            "total_sexe"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_tab_repa_deput_pol_sex_dep(
                        row['direction'], row['region'], row['annee'], row['departement'], row['partis_politique'],
                        row['hommes'], row['femmes'], row['total_sexe']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")

    # Option pour afficher les données enregistrées
    if st.checkbox("Afficher les données enregistrées", key="tab128"):
        df_data = data.obtenir_tab_repa_deput_pol_sex_dep()
        st.dataframe(df_data)

    st.write("Tableau 1.2.9: Liste des sous-préfectures par département")
    uploaded_file = st.file_uploader("Importer des données (format Excel)", type=["xlsx"], key="tab129")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "list_sous_pref_urbain",
                            "list_sous_pref_rural", "nombre_sous_pref"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_tab_list_sous_pref_dep(
                        row['direction'], row['region'], row['annee'], row['departement'], row['list_sous_pref_urbain'],
                        row['list_sous_pref_rural'], row['nombre_sous_pref']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")

    # Option pour afficher les données enregistrées
    if st.checkbox("Afficher les données enregistrées", key="tabl129"):
        df_data = data.obtenir_tab_list_sous_pref_dep()
        st.dataframe(df_data)

    st.write("Tableau 1.2.10: Superficie et nombre de village par sous-préfecture")
    uploaded_file = st.file_uploader("Importer des données (format Excel)", type=["xlsx"], key="tab1210")

    if uploaded_file is not None:
        # Lire le fichier Excel
        df = pd.read_excel(uploaded_file)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "sous_prefecture",
                            "superficie", "nombre_village"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_tab_superf_nb_vil_dep(
                        row['direction'], row['region'], row['annee'], row['departement'], row['sous_prefecture'],
                        row['superficie'], row['nombre_village']
                    )
                st.success("Données enregistrées avec succès!")
        else:
            st.error("Le fichier Excel ne contient pas les colonnes requises.")

    # Option pour afficher les données enregistrées
    if st.checkbox("Afficher les données enregistrées", key="tabl1210"):
        df_data = data.obtenir_tab_superf_nb_vil_dep()
        st.dataframe(df_data)

    return