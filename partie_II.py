import data_p2
import  streamlit as st
import pandas as pd


def partie_II_annuaire():
    page_tab211_pop_region_depart()
    page_tab212_repart_pop_group_age()
    page_tab_213_pop_depart_sous()
    page_tab217_evolution_pop()
    page_tab218_mariage_commun_bien()
    page_tab219_mariage_matrimon()
    page_tab2110_mariage_civil()
    page_tab2111_fait_matr_civils()
    page_tab2112_fait_civil()
    page_tab2113_naiss_enreg_reg_dep()
    page_tab2114_fait_civi_deces()
    page_tab2115_fait_naiss_deces()
    return



def page_tab211_pop_region_depart():

    st.write("Tableau 2.1.1: Population de la région , par Département et par sous-préfecture")
    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab211_pop_dep_sous_pref_sex")

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
            'ID', 'Direction régionale', 'Région', 'Année', 'Département', 'Sous-préfecture', 'Nombre hommes', ' Nombre de femmes', 'Total sexe',
            'rapport_masculinite'
        ])
        st.write('Données de Population de la région , par Département et par sous-préfecture')
        st.dataframe(df_table)



def page_tab212_repart_pop_group_age():
    st.write("Tableau 2.1.2: Répartition  de la population de la région  du Poro par grand  groupe d’âge selon le sexe")

    # Charger le fichier Excel
    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab212_repa_pop_grou_age")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)


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

    if st.button('Afficher les données de la table',key="tab212AA"):
        rows = data_p2.obtenir_tab212_repa_pop_grou_age()
        df_table = pd.DataFrame(rows, columns=[
            "ID", "Direction régionale", "Région", "Année", "Tranche d'âge","Nombre d'hommes"," Nombre de femmes","Total sexe",
            "Rapport masculinité"
        ])
        st.write('Données de Population de la région , par Département et par sous-préfecture')
        st.dataframe(df_table)


    return



def page_tab_213_pop_depart_sous():
    st.write("Tableau 2.1.3: Population du département  par tranche d'âge selon la sous-préfecture et le sexe")
    st.write("Les tableaux tab213 jusqu'à tab216 sont contenus dans tab213. Ce sont des données de population désagrégé par sous-préfecture")
    # Charger le fichier Excel
    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab213_pop_dep_tranc_s_pref_sex")

    if uploaded_file is not None:

        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

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

    if st.button('Afficher les données de la table',key="tab213_pop"):
        rows = data_p2.obtenir_tab211_pop_dep_sous_pref_sex()
        df_table = pd.DataFrame(rows, columns=[
            "ID", "Direction régionale", "Région", "Année", "Tranche d'âge","Nombre d'hommes"," Nombre de femmes","Total sexe"

        ])
        st.write('Données de Population de la région , par Département et par sous-préfecture')
        st.dataframe(df_table)

    return


'''
Les tableaux tab213 jusqu'à tab216 sont contenus dans tab213. Ce sont des données de population désagrégé par sous-préfecture
'''
def page_tab217_evolution_pop():


    st.write("Tableau 2.1.7: Evolution de la population de la région ,par département et par sexe sur les  années")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab217_evolu_pop_reg_dep")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)


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
    if st.button('Afficher les données de la table',key="tab214AABT"):
        rows = data_p2.obtenir_tab217_evolu_pop_reg_dep()
        df_table = pd.DataFrame(rows, columns=[
            'ID', 'Direction', 'Région', 'Année', 'Département', 'Sous-prefecture', 'Hommes', 'Femmes', 'Total sexe',
            'Densité'
        ])
        st.write('Données de la table ')
        st.dataframe(df_table)

    return




def page_tab218_mariage_commun_bien():
    st.write("Tableau 2.1.8: Mariages enregistrés à l’état civil selon la nationalité par Département ")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab219_maria_eta_civ_regim")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "nat_coupl_ivoi", "nat_coupl_mixte",
                            "nat_coupl_etrang"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données", key="tab219FF"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab219_maria_eta_civ_regim(
                        row['direction'], row['region'], row['annee'], row['departement'],
                        row['nat_coupl_ivoi'], row['nat_coupl_mixte'], row['nat_coupl_etrang']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    if st.button('Afficher les données de la table', key="tab214AABC"):
        rows = data_p2.obtenir_maria_centre_civil_dep()
        df_table = pd.DataFrame(rows, columns=[
                    'ID', 'Direction', 'Région', 'Année', 'Département', 'Nombre de couple Nat ivoirienne',
            'Nombre de Couple de Nat mixte','Nombre de couple Nat étrangère'
                ])
        st.write('Données de la table ')
        st.dataframe(df_table)


    return




def page_tab219_mariage_matrimon():
    st.write("Tableau 2.1.9: Mariage selon le régime matrimonial par région")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab219_maria_regim")

    if uploaded_file is not None:

        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

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

    if st.button('Afficher les données de la table', key="tab214AABG"):
        rows =data_p2.obtenir_tab219_maria_regim()
        df_table = pd.DataFrame(rows, columns=[
                    'ID', 'Direction', 'Région', 'Année', 'Département','Régime matrimoniale bien commun','Régime matrimoniale bien séparé'
                ])
        st.write('Données de la table ')
        st.dataframe(df_table)

    return




def page_tab2110_mariage_civil():
    st.write("Tableau 2.1.10: Mariages par centre civil et département")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab2110_maria_centre_civil_dep")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

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

    # Afficher les données de la table
    if st.button('Afficher les données de la table', key="tab2110AAB"):
        rows = data_p2.obtenir_maria_centre_civil_dep()
        df_table = pd.DataFrame(rows, columns=[
            'ID', 'Direction', 'Région', 'Département', 'Année', 'Centre état civil', 'Couple ivoirien',
            'Couple mixte', 'Couple étranger'
        ])
        st.write('Données de la table tab2110_maria_centre_civil_dep:')
        st.dataframe(df_table)

    return





def page_tab2112_fait_civil():
    st.write(
        "Tableau 2.1.12 : Faits d'état civil enregistrés et parvenus au niveau central selon le type de centre de la Région")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab2112_faits_civils")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "departement", "sous_prefecture", "faits_civil", "type_etat_civil",
                            "annee", "nombre_fait"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrement_tab2112_fait(
                        row['direction'], row['region'], row['departement'], row['sous_prefecture'], row['faits_civil'],
                        row['type_etat_civil'], row['annee'], row['nombre_fait']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error(
                "Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    # Afficher les données de la table
    if st.button('Afficher les données de la table', key="tab2112AAB"):
        rows = data_p2.obtenir_tab2112_fait()
        df_table = pd.DataFrame(rows, columns=[
            'ID', 'Direction', 'Région', 'Département', 'Sous-préfecture', 'Fait civil', 'Type état civil',
            'Année', 'Nombre de faits'
        ])
        st.write('Données de la table tab2112_faits_civils:')
        st.dataframe(df_table)

    return


def page_tab2113_naiss_enreg_reg_dep():
    st.write("Tableau 2.1.13 : Naissances enregistrées et parvenues au niveau central selon le type de centre de la Région")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab2113_naissances")

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
        expected_columns = ["direction", "region", "departement", "sous_prefecture", "annee", "faits_civil",
                            "type_de_centre_civil", "dans_les_delais_3_mois", "hors_delai_4_12_mois",
                            "hors_delai_plus_de_12_mois", "total_faits_naissance"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab2113_fait_civi_naiss(
                        row['direction'], row['region'], row['departement'], row['sous_prefecture'], row['annee'],
                        row['faits_civil'], row['type_de_centre_civil'], row['dans_les_delais_3_mois'],
                        row['hors_delai_4_12_mois'], row['hors_delai_plus_de_12_mois'], row['total_faits_naissance']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    # Afficher les données de la table
    if st.button('Afficher les données de la table', key="tab2113AAB"):
        rows = data_p2.obtenir_tab2113_fait_civi_naiss()
        df_table = pd.DataFrame(rows, columns=[
            'ID', 'Direction', 'Région', 'Département', 'Sous-préfecture', 'Année', 'Fait civil',
            'Type de centre civil', 'Dans les délais (0-3 mois)', 'Hors délai (4-12 mois)',
            'Hors délai (>12 mois)', 'Total faits naissance'
        ])
        st.write('Données de la table tab2113_naissances:')
        st.dataframe(df_table)

    return



def page_tab2111_fait_matr_civils():
    st.write("Tableau 2.1.11 : Faits matrimoniaux enregistrés et parvenus au niveau central")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab2111_fait_matr_civils")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "departement", "annee", "type_centre_civil", "nbre_bien_commun", "nbre_bien_separe"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab2111_fait_matr_civils(
                        row['direction'], row['region'], row['departement'], row['annee'],
                        row['type_centre_civil'], row['nbre_bien_commun'], row['nbre_bien_separe']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    # Afficher les données de la table
    if st.button('Afficher les données de la table',key="tab2111AAZ"):
        rows = data_p2.obtenir_tab2111_fait_matr_civils()
        df_table = pd.DataFrame(rows, columns=[
            'ID', 'Direction', 'Region', 'Departement', 'Année', 'Type de centre civil', 'Régime de bien commun',
            'Régime de bien séparé'
        ])
        st.write('Données de la table tab2111_fait_matr_civils:')
        st.dataframe(df_table)

    return


def page_tab2114_fait_civi_deces():
    st.write("Tableau 2.1.14 : Faits d'état civil enregistrés pour les décès")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab2114_faits_deces")

    if uploaded_file is not None:

        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names)

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "departement", "sous_prefecture", "annee", "faits_civil", "type_de_centre_civil",
                            "dans_les_delais_15_jour", "hors_delai_annee_cours", "hors_delai_des_annees_anteri", "total_faits_deces"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab2114_fait_civi_deces(
                        row['direction'], row['region'], row['departement'], row['sous_prefecture'], row['annee'],
                        row['faits_civil'], row['type_de_centre_civil'], row['dans_les_delais_15_jour'],
                        row['hors_delai_annee_cours'], row['hors_delai_des_annees_anteri'], row['total_faits_deces']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    if st.button('Afficher les données de la table', key="tab2114AAB"):
        rows = data_p2.obtenir_tab2114_fait_civi_deces()
        df_table = pd.DataFrame(rows, columns=[
            'ID', 'Direction', 'Région', 'Département', 'Sous-préfecture', 'Année', 'Faits civils', 'Type de centre civil',
            'Dans les délais 15 jours', 'Hors délai année en cours', 'Hors délai des années antérieures', 'Total faits de décès'
        ])
        st.write('Données de la table tab2114_fait_civi_deces:')
        st.dataframe(df_table)

    return



def page_tab2115_fait_naiss_deces():
    st.write("Tableau 2.1.15 : Faits de naissances et de décès par centre civil et département")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab2115_fait_naiss_deces")

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
        expected_columns = ["direction", "region", "departement", "sous_prefecture", "annee", "nbre_naiss_centr_princ",
                            "nbre_naiss_centr_second", "nbre_total_naiss", "nbre_deces_centr_princ",
                            "nbre_deces_centr_second", "nbre_total_deces"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab2115_fait_naiss_deces(
                        row['direction'], row['region'], row['departement'], row['sous_prefecture'], row['annee'],
                        row['nbre_naiss_centr_princ'], row['nbre_naiss_centr_second'], row['nbre_total_naiss'],
                        row['nbre_deces_centr_princ'], row['nbre_deces_centr_second'], row['nbre_total_deces']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    # Afficher les données de la table
    if st.button('Afficher les données de la table', key="tab2115AAB"):
        rows = data_p2.obtenir_tab2115_fait_naiss_deces()
        df_table = pd.DataFrame(rows, columns=[
            'ID', 'Direction', 'Région', 'Département', 'Sous-préfecture', 'Année', 'Naissances centre principal',
            'Naissances centre secondaire', 'Total naissances', 'Décès centre principal', 'Décès centre secondaire',
            'Total décès'
        ])
        st.write('Données de la table tab2115_fait_naiss_deces:')
        st.dataframe(df_table)

    return
