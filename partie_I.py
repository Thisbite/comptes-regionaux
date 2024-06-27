import  streamlit as st
import pandas as pd
import  data

def partie_I_annuaire():
    page_tab121_existence_part_pol()

    return






def page_tab121_existence_part_pol():
    st.write("Tableau 1.2.1 Existence des partis  politiques par département ")
    # Section pour télécharger un fichier Excel

    uploaded_file = st.file_uploader("Importer les données Excel ", type=["xlsx"], key="existence_partis")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "partis_politique", "annee", "statut_existence"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data.enregistrer_existence_partis(
                        row['direction'], row['region'], row['partis_politique'],
                        row['annee'], row["statut_existence"]
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")
    return


def page_tab122_nbre_respo_depart():
    st.write("Tableau 1.2.2: Nombre de responsables départementaux  des partis politiques selon le sexe  dans la région")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"], key="tab_respo_politique")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
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

    return

def page_tab123_effe_maire_elu_dep():
    st.write("Tableau 1.2.3: Effectif des maires élus  par département et par sexe en  exercices municipaux")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"],
                                     key="tab_effec_maire_depart")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
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


    return

def page_tab124_repart_post_reg_fem():
    st.write(
        "Tableau 1.2.4: Répartition régionale des postes de responsabilités occupés par les femmes dans les mairies (maire, 1er adjoint au maire, 2ème adjoint au maire) aux exercices municipaux ")
    uploaded_file = st.file_uploader("Importer les données", type=["xlsx"],
                                     key="tab_repa_post_mai_fem_dep")
    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
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

    return
def page_tab125_repart_maire_pol_sexe():
    st.write(
        "Tableau 1.2.5: Répartition des maires par département, par sexe et par partie politique ")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"],
                                     key="tab_repa_mair_dep_pol")

    if uploaded_file is not None:
        # Lire le fichier Excel
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
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

    return

def page_tab126_reaprt_adjoin_sexe():
    st.write("Tableau 1.2.6: Répartition des adjoints au maire par département, par sexe et par partie politique ")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"],
                                     key="tab_repa_adj_mai_dep_p")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
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

    return






def page_tab217_effe_maire_recon():
    st.write("Tableau 1.2.7 : Effectif des maires reconduits et nouvellement élus par département")
    uploaded_file = st.file_uploader("Importer les données ", type=["xlsx"],
                                     key="tab_mair_recon_nvl_dep")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
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


def page_tab128_repart_depute():
    st.write("Tableau 1.2.8: Répartition des députés par sexe et par partie politique")
    uploaded_file = st.file_uploader("Importer des données (format Excel)", type=["xlsx"])

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
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



def page_tab129_list_sousp():
    st.write("Tableau 1.2.9: Liste des sous-préfectures par département")
    uploaded_file = st.file_uploader("Importer des données (format Excel)", type=["xlsx"], key="tab129")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
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





def page_tab1210_superficie_nbre_vlage():
    st.write("Tableau 1.2.10: Superficie et nombre de village par sous-préfecture")
    uploaded_file = st.file_uploader("Importer des données (format Excel)", type=["xlsx"], key="tab1210")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
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
