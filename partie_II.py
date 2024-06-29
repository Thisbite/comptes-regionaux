import data_p2
import  streamlit as st
import pandas as pd


def partie_II_annuaire():
    st.write("******************************************************************")
    page_tab211_pop_region_depart()
    st.write("------------------------------------------------------------------")
    page_tab212_repart_pop_group_age()
    st.write("------------------------------------------------------------------")
    page_tab_213_pop_depart_sous()
    st.write("------------------------------------------------------------------")
    page_tab217_evolution_pop()
    st.write("------------------------------------------------------------------")
    page_tab218_maria_eta_civ_regim()
    st.write("------------------------------------------------------------------")
    page_tab219_mariage_matrimon()
    st.write("------------------------------------------------------------------")
    page_tab2110_mariage_civil()
    st.write("------------------------------------------------------------------")
    page_tab2111_fait_matr_civils()
    st.write("------------------------------------------------------------------")
    page_tab2112_fait_civil()
    st.write("------------------------------------------------------------------")
    page_tab2113_naiss_enreg_reg_dep()
    st.write("------------------------------------------------------------------")
    page_tab2114_fait_civi_deces()
    st.write("------------------------------------------------------------------")
    page_tab2115_fait_naiss_deces()
    st.write("******************************************************************")
    return



def page_tab211_pop_region_depart():
    st.write("Tableau 2.1.1: Population de la région, par Département et par sous-préfecture")

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
                doublon_detecte = False
                for _, row in df.iterrows():
                    success = data_p2.enregistrer_tab211_pop_dep_sous_pref_sex(
                        row['direction'], row['region'], row['annee'], row['departement'],
                        row['sous_prefecture'], row['hommes'], row['femmes'],
                        row['total_sexe'], row['rapport_masculinite']
                    )
                    if not success:
                        doublon_detecte = True

                if doublon_detecte:
                    st.warning("Certaines données ont déjà été enregistrées.")
                else:
                    st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    df = data_p2.obtenir_tab211_pop_dep_sous_pref_sex()

    if st.checkbox("Obtenir des données", key="tab211obtenir"):
        # Ajout des sélecteurs pour l'année, la région, le département et la sous-préfecture
        annees = df['Année'].unique()
        regions = df['Région'].unique()
        departements = df['Département'].unique()
        sous_prefectures = df['Sous-préfecture'].unique().tolist()
        sous_prefectures.append("None")

        selected_annee = st.selectbox("Choisir l'année", annees, key="tab211an")
        selected_region = st.selectbox("Choisir la région", regions, key="tab211regio")
        selected_dep = st.selectbox("Choisir le département", departements, key="tab211dep")
        selected_sous = st.selectbox("Choisir la sous-préfecture", sous_prefectures, key="tab211sou")

        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[((df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'] == selected_dep) & (df['Sous-préfecture'] == selected_sous))],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (
                        df['Département'] == selected_dep) & (df['Sous-préfecture'].isna())],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'].isna()) & (
                df['Sous-préfecture'].isna())]


        ]

        # Afficher les données de la table avec filtres
        if st.button('Recherche de données de la table', key="tab211AAB"):
            data_p2.supprimer_doublons_tab211_pop_dep_sous_pref_sex()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    # Sélection d'une ligne pour modification
    if st.checkbox("Modifier une ligne existante", key="tab211modiA"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'], key="tab211sel")

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Région'])
            annee = st.text_input("Année", selected_row['Année'])
            departement = st.text_input("Département", selected_row['Département'])
            sous_prefecture = st.text_input("Sous-préfecture", selected_row['Sous-préfecture'])
            hommes = st.number_input("Hommes", selected_row['Hommes'])
            femmes = st.number_input("Femmes", selected_row['Femmes'])
            total_sexe = st.number_input("Total sexe", selected_row['Total_sexe'])
            rapport_masculinite = st.number_input("Rapport masculinité", selected_row['Rapport_masculinite'])

            if st.button("Modifier la ligne", key="tab211modi"):
                success = data_p2.modifier_tab211_pop_dep_sous_pref_sex(
                    selected_id, direction, region, annee, departement, sous_prefecture, hommes, femmes,
                    total_sexe, rapport_masculinite
                )
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")
    return


def page_tab212_repart_pop_group_age():
    st.write("Tableau 2.1.2: Répartition de la population de la région du Poro par grand groupe d’âge selon le sexe")

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
        expected_columns = ["direction", "region", "annee", "groupe_age", "hommes", "femmes", "total_sexe", "rapport_masculinite"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                doublon_detecte = False
                for _, row in df.iterrows():
                    success = data_p2.enregistrer_tab212_repa_pop_grou_age(
                        row['direction'], row['region'], row['annee'], row['groupe_age'],
                        row['hommes'], row['femmes'], row['total_sexe'], row['rapport_masculinite']
                    )
                    if not success:
                        doublon_detecte = True

                if doublon_detecte:
                    st.warning("Certaines données ont déjà été enregistrées.")
                else:
                    st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    df = data_p2.obtenir_tab212_repa_pop_grou_age()

    # Obtenir des données avec des sélecteurs
    if st.checkbox("Obtenir des données", key="tab212obtenir"):
        # Ajout des sélecteurs pour l'année, la région et le groupe d'âge
        annees = df['Année'].unique()
        regions = df['Région'].unique()
        groupes_age = df["Tranche d'âge"].unique()

        selected_annee = st.selectbox("Choisir l'année", annees, key="tab212annee")
        selected_region = st.selectbox("Choisir la région", regions, key="tab212region")
        selected_groupe_age = st.selectbox("Choisir le groupe d'âge", groupes_age, key="tab212groupeage")

        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df["Tranche d'âge"] == selected_groupe_age)],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df["Tranche d'âge"].isna())],
            df[(df['Année'] == selected_annee) & (df['Région'].isna()) & (df["Tranche d'âge"].isna())],
            df[(df['Année'] == selected_annee) & (df['Région'].isna()) & (df["Tranche d'âge"].isna())]
        ]

        st.write("NB: Un double clique permet de supprimer les doublons")
        if st.button('Afficher les données de la table', key="tab212AAB"):
            data_p2.supprimer_doublons_tab212_repa_pop_grou_age()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    # Sélection d'une ligne pour modification
    if st.checkbox("Modifier une ligne existante", key="tab212modiA"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'], key="tab212sel")

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Région'])
            annee = st.text_input("Année", selected_row['Année'])
            groupe_age = st.text_input("Groupe d'âge", selected_row["Tranche d'âge"])
            hommes = st.number_input("Hommes", selected_row["Nombre d'hommes"])
            femmes = st.number_input("Femmes", selected_row["Nombre de femmes"])
            total_sexe = st.number_input("Total sexe", selected_row["Total sexe"])
            rapport_masculinite = st.number_input("Rapport masculinité", selected_row["Rapport masculinité"])

            if st.button("Modifier la ligne", key="tab212modi"):
                success = data_p2.modifier_tab212_repa_pop_grou_age(
                    selected_id, direction, region, annee, groupe_age, hommes, femmes, total_sexe, rapport_masculinite
                )
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")

    return







def page_tab_213_pop_depart_sous():
    st.write("Tableau 2.1.3: Population du département par tranche d'âge selon la sous-préfecture et le sexe")
    st.write("Les tableaux tab213 jusqu'à tab216 sont contenus dans tab213. Ce sont des données de population désagrégées par sous-préfecture")

    # Charger le fichier Excel
    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab213_pop_dep_tranc_s_pref_sex")

    if uploaded_file is not None:
        # Lire le fichier Excel et obtenir les noms des feuilles
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Sélecteur pour choisir la feuille
        sheet_name = st.selectbox("Choisir la feuille", sheet_names,key="tab213ses")

        # Lire la feuille choisie
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)

        # Afficher les données du fichier
        st.dataframe(df)

        # Vérifier les colonnes du fichier
        expected_columns = ["direction", "region", "annee", "departement", "sous_prefecture", "tranche_age", "hommes", "femmes", "total_sexe"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données",key="tab213be"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab213_pop_dep_tranc_s_pref_sex(
                        row['direction'], row['region'], row['annee'], row['departement'],
                        row['sous_prefecture'], row['tranche_age'], row['hommes'], row['femmes'], row['total_sexe']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    df = data_p2.obtenir_tab213_pop_dep_tranc_s_pref_sex()

    # Obtenir des données avec des sélecteurs
    if st.checkbox("Obtenir des données", key="tab213obtenir"):
        # Ajout des sélecteurs pour l'année, la région, le département et la sous-préfecture
        annees = df['Année'].unique()
        regions = df['Région'].unique()
        departements = df['Département'].unique()
        sous_prefectures = df['Sous-préfecture'].unique()

        selected_annee = st.selectbox("Choisir l'année", annees, key="tab213annee")
        selected_region = st.selectbox("Choisir la région", regions, key="tab213region")
        selected_dep = st.selectbox("Choisir le département", departements, key="tab213departement")
        selected_sous = st.selectbox("Choisir la sous-préfecture", sous_prefectures, key="tab213sousprefecture")

        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'] == selected_dep) & (df['Sous-préfecture'] == selected_sous)],

            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'].isna()) & (df['Sous-préfecture'] == selected_sous)]
        ]

        st.write("NB: Un double clique permet de supprimer les doublons")
        if st.button('Recherche de données de la table', key="tab213AAB"):
            data_p2.supprimer_doublons_tab213_pop_dep_tranc_s_pref_sex()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    # Sélection d'une ligne pour modification
    if st.checkbox("Modifier une ligne existante", key="tab213modiA"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'], key="tab213sel")

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['direction'])
            region = st.text_input("Région", selected_row['region'])
            annee = st.number_input("Année", selected_row['annee'])
            departement = st.text_input("Département", selected_row['departement'])
            sous_prefecture = st.text_input("Sous-préfecture", selected_row['sous_prefecture'])
            tranche_age = st.text_input("Tranche d'âge", selected_row['tranche_age'])
            hommes = st.text_input("Hommes", selected_row['hommes'])
            femmes = st.text_input("Femmes", selected_row['femmes'])
            total_sexe = st.text_input("Total sexe", selected_row['total_sexe'])

            if st.button("Modifier la ligne", key="tab213modi"):
                success = data_p2.modifier_tab213_pop_dep_tranc_s_pref_sex(
                    selected_id, direction, region, annee, departement, sous_prefecture, tranche_age, hommes, femmes, total_sexe
                )
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")

    return

'''
Les tableaux tab213 jusqu'à tab216 sont contenus dans tab213. Ce sont des données de population désagrégé par sous-préfecture
'''
def page_tab217_evolution_pop():
    st.write("Tableau 2.1.7: Evolution de la population de la région, par département et par sexe sur les années")

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
        expected_columns = ["direction", "region", "annee", "departement", "sous_prefecture", "hommes", "femmes", "total_sexe", "densite"]

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
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    df = data_p2.obtenir_tab217_evolu_pop_reg_dep()
    if st.checkbox("Obtenir des données", key="tab217obtenir"):
        # Ajout des sélecteurs pour l'année, la région, le département et la sous-préfecture
        annees = df['annee'].unique()
        regions = df['Région'].unique()
        departements = df['Département'].unique()
        sous_prefectures = df['sous_prefecture'].unique()

        selected_annee = st.selectbox("Choisir l'année", annees, key="tab217annee")
        selected_region = st.selectbox("Choisir la région", regions, key="tab217region")
        selected_dep = st.selectbox("Choisir le département", departements, key="tab217departement")


        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'] == selected_dep) ],

            df[(df['Année'] == selected_annee)  & (df['Région'] == selected_region) & (df['Département'].isna())]
        ]

        st.write("NB: Un double clique permet de supprimer les doublons")
        if st.button('Afficher les données de la table', key="tab217AAB"):
            data_p2.supprimer_doublons_tab217_evolu_pop_reg_dep()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    if st.checkbox("Modifier une ligne existante",key="tab217modiA"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'])

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Région'])
            annee = st.number_input("Année", selected_row['Année'])
            departement = st.text_input("Département", selected_row['Département'])
            sous_prefecture = st.text_input("Sous-préfecture", selected_row['Sous-prefecture'])
            hommes = st.text_input("Hommes", selected_row['Hommes'])
            femmes = st.text_input("Femmes", selected_row['Femmes'])
            total_sexe = st.text_input("Total sexe", selected_row['Total sexe'])
            densite = st.text_input("Densité", selected_row['Densité'])

            if st.button("Modifier la ligne",key="tab217modi"):
                success = data_p2.modifier_tab217_evolu_pop_reg_dep(selected_id, direction, region, annee, departement,
                                                            sous_prefecture, hommes, femmes, total_sexe, densite)
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")


    return



def page_tab218_maria_eta_civ_regim():
    st.write("Tableau 2.1.8 : Mariage par état civil et régime par région")

    uploaded_file = st.file_uploader("Importer les données Excel", type=["xlsx"], key="tab218_maria_eta_civ_regim")

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
        expected_columns = ["direction", "region", "departement", "annee", "nat_coupl_ivoi", "nat_coupl_mixte", "nat_coupl_etrang"]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                for _, row in df.iterrows():
                    data_p2.enregistrer_tab218_maria_eta_civ_regim(
                        row['direction'], row['region'], row['departement'], row['annee'],
                        row['nat_coupl_ivoi'], row['nat_coupl_mixte'], row['nat_coupl_etrang']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    df = data_p2.obtenir_tab218_maria_eta_civ_regim()
    if st.checkbox("Obtenir des données", key="tab218obtenir"):
        # Ajout des sélecteurs pour l'année, la région et le département
        annees = df['Année'].unique()
        regions = df['Région'].unique()
        departements = df['Département'].unique()

        selected_annee = st.selectbox("Choisir l'année", annees, key="tab218annee")
        selected_region = st.selectbox("Choisir la région", regions, key="tab218region")
        selected_dep = st.selectbox("Choisir le département", departements, key="tab218departement")

        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'] == selected_dep)],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'].isna())],
            df[(df['Année'] == selected_annee) & (df['Région'].isna()) & (df['Département'].isna())]
        ]

        # Afficher les données de la table avec filtres
        st.write("Un double clique permet de supprimer les doublons")
        if st.button('Recherche de données de la table', key="tab218AAB"):
            data_p2.supprimer_doublons_tab218_maria_eta_civ_regim()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    if st.checkbox("Modifier une ligne existante",key="tab218modi"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'])

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Région'])
            departement = st.text_input("Département", selected_row['Département'])
            annee = st.number_input("Année", selected_row['Année'])
            nat_coupl_ivoi = st.text_input("Couple ivoirien", selected_row['Couple ivoirien'])
            nat_coupl_mixte = st.text_input("Couple mixte", selected_row['Couple mixte'])
            nat_coupl_etrang = st.text_input("Couple étranger", selected_row['Couple étranger'])

            if st.button("Modifier la ligne"):
                success = data_p2.modifier_tab218_maria_eta_civ_regim(selected_id, direction, region, departement, annee,
                                                              nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang)
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")

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
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    df = data_p2.obtenir_tab219_maria_regim()
    if st.checkbox("Obtenir des données", key="tab219obtenir"):
        # Ajout des sélecteurs pour l'année, la région et le département
        annees = df['Année'].unique()
        regions = df['Région'].unique()
        departements = df['Département'].unique()

        selected_annee = st.selectbox("Choisir l'année", annees, key="tab219annee")
        selected_region = st.selectbox("Choisir la région", regions, key="tab219region")
        selected_dep = st.selectbox("Choisir le département", departements, key="tab219departement")

        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'] == selected_dep)],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'].isna())],
            df[(df['Année'] == selected_annee) & (df['Région'].isna()) & (df['Département'].isna())]
        ]

        # Afficher les données de la table avec filtres
        st.write("NB: Un double clique permet de supprimer les doublons")
        if st.button('Recherche données de la table', key="tab219AAB"):

            data_p2.supprimer_doublons_tab219_maria_regim()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    if st.checkbox("Modifier une ligne existante",key="tab219modi"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'])

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Région'])
            departement = st.text_input("Département", selected_row['Département'])
            annee = st.text_input("Année", selected_row['Année'])
            reg_mat_bien_com = st.text_input("Régime matrimonial bien commun",
                                               selected_row['Regime Matrimonial Bien Commun'])
            reg_mat_bien_sep = st.text_input("Régime matrimonial bien séparé",
                                               selected_row['Regime Matrimonial Bien Separé'])

            if st.button("Modifier la ligne"):
                success = data_p2.modifier_tab219_maria_regim(selected_id, direction, region, departement, annee,
                                                      reg_mat_bien_com, reg_mat_bien_sep)
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")

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
                    data_p2.enregistrer_tab2110_maria_centre_civil_dep(
                        row['direction'], row['region'], row['departement'], row['annee'],
                        row['centre_etat_civil'], row['nat_coupl_ivoi'], row['nat_coupl_mixte'], row['nat_coupl_etrang']
                    )
                st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    df = data_p2.obtenir_tab2110_maria_centre_civil_dep()
    if st.checkbox("Obtenir des données", key="tab2110obtenir"):
        # Ajout des sélecteurs pour l'année, la région, le département et la sous-préfecture
        annees = df['Année'].unique()
        regions = df['Région'].unique()
        departements = df['Département'].unique()


        selected_annee = st.selectbox("Choisir l'année", annees, key="tab2110annee")
        selected_region = st.selectbox("Choisir la région", regions, key="tab2110region")
        selected_dep = st.selectbox("Choisir le département", departements, key="tab2110departement")


        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'] == selected_dep) ],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'] == selected_dep)],

        ]

        st.write("NB: Un double clique supprime les doublons")
        if st.button('Recherche de  données de la table', key="tab2110AAB"):
            data_p2.supprimer_doublons_tab2110_maria_centre_civil_dep()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    if st.checkbox("Modifier une ligne existante",key="tab2110modi"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'])

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Région'])
            departement = st.text_input("Département", selected_row['Département'])
            annee = st.text_input("Année", selected_row['Année'])
            centre_etat_civil = st.text_input("Centre état civil", selected_row['Centre état civil'])
            nat_coupl_ivoi = st.text_input("Couple ivoirien", selected_row['Couple ivoirien'])
            nat_coupl_mixte = st.text_input("Couple mixte", selected_row['Couple mixte'])
            nat_coupl_etrang = st.text_input("Couple étranger", selected_row['Couple étranger'])

            if st.button("Modifier la ligne"):
                success = data_p2.modifier_tab2110_maria_centre_civil_dep(selected_id, direction, region, departement, annee,
                                                                  centre_etat_civil, nat_coupl_ivoi, nat_coupl_mixte,
                                                                  nat_coupl_etrang)
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")

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

    df = data_p2.obtenir_tab2111_fait_matr_civils()
    if st.checkbox("Obtenir des données", key="tab2111obtenir"):
        # Ajout des sélecteurs pour l'année, la région, le département et la sous-préfecture
        annees = df['Année'].unique()
        regions = df['Region'].unique()
        departements = df['Departement'].unique()


        selected_annee = st.selectbox("Choisir l'année", annees, key="tab2111anne")
        selected_region = st.selectbox("Choisir la région", regions, key="tab2111regio")
        selected_dep = st.selectbox("Choisir le département", departements, key="tab2111depar")


        # Filtrer les données en fonction des sélections

    # Afficher les données de la table

    # Filtrer les données en fonction des sélections


    # Afficher les données de la table avec filtres
        if st.button('Recherche de données de la table', key="tab2111AAZ"):
            data_p2.supprimer_doublons_tab2111_fait_matr_civils()
            filtered_dfs = [
                df[(df['Année'] == selected_annee) & (df['Region'] == selected_region) & (
                            df['Departement'] == selected_dep)],
                df[(df['Année'] == selected_annee) & (df['Region'] == selected_region) & (df['Departement'].isna())]
            ]
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    if st.checkbox("Modifier une ligne existante",key="tab2111modi"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'])

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Region'])
            departement = st.text_input("Département", selected_row['Departement'])
            annee = st.text_input("Année", selected_row['Année'])
            type_centre_civil = st.text_input("Type de centre civil", selected_row['Type de centre civil'])
            nbre_bien_commun = st.text_input("Régime de bien commun", selected_row['Régime de bien commun'])
            nbre_bien_separe = st.text_input("Régime de bien séparé", selected_row['Régime de bien séparé'])

            if st.button("Modifier la ligne"):
                success = data_p2.modifier_tab2111_fait_matr_civils(selected_id, direction, region, departement, annee,
                                                            type_centre_civil,
                                                            nbre_bien_commun, nbre_bien_separe)
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")


# Page Streamlit
def page_tab2112_fait_civil():
    st.write("Tableau 2.1.12 : Faits d'état civil enregistrés et parvenus au niveau central selon le type de centre de la Région")

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
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    df = data_p2.obtenir_tab2112_fait()
    if st.checkbox("Obtenir des données",key="tab2112obtenir"):
        # Ajout des sélecteurs pour l'année, la région, le département et la sous-préfecture
        annees = df['Annee'].unique()
        regions = df['Region'].unique()
        departements = df['Departement'].unique()
        sous_prefectures = df['Sous-prefecture'].unique()
        import numpy as np

        # Convertissez sous_prefectures en une liste Python
        sous_prefectures_list = sous_prefectures.tolist() if isinstance(sous_prefectures, np.ndarray) else list(
            sous_prefectures)
        sous_prefectures_list.append(None)
        depart_list = departements.tolist() if isinstance(departements, np.ndarray) else list(
            departements)
        depart_list.append(None)
        # Ajoutez None à la liste sous_prefectures_list


        selected_annee = st.selectbox("Choisir l'année", annees,key="tab2112anne")
        selected_region = st.selectbox("Choisir la région", regions,key="tab2112regio")
        selected_dep = st.selectbox("Choisir le département", depart_list,key="tab2112depar")
        selected_sous_prefecture = st.selectbox("Choisir la sous-préfecture", sous_prefectures_list, key="tab2112sous")

        # Filtrer les données en fonction des sélections
        filtered_dfs = [
        df[(df['Annee'] == selected_annee) & (df['Region'] == selected_region) & (df['Departement'] == selected_dep) & (
                    df['Sous-prefecture'] == selected_sous_prefecture)],
        df[(df['Annee'] == selected_annee) & (df['Region'] == selected_region) & (df['Departement'] == selected_dep) & (
            df['Sous-prefecture'].isna())],
        df[(df['Annee'] == selected_annee) & (df['Region'] == selected_region) & (df['Departement'].isna()) & (
            df['Sous-prefecture'].isna())]
        ]

    # Afficher les données de la table avec filtres
        st.write("NB: Un double clique permet de supprimer les doublons")
        if st.button('Recherche de  données de la table', key="tab2112AAB"):
            data_p2.supprimer_doublons_tab2112_fait()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    if st.checkbox("Modifier une ligne existante"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'])

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Region'])
            departement = st.text_input("Département", selected_row['Departement'])
            sous_prefecture = st.text_input("Sous-prefecture", selected_row['Sous-prefecture'])
            faits_civil = st.text_input("Faits Civil", selected_row['Faits Civil'])
            type_etat_civil = st.text_input("Type Etat Civil", selected_row['Type Etat Civil'])
            annee = st.text_input("Année", selected_row['Annee'])
            nombre_fait = st.text_input("Nombre Fait", selected_row['Nombre Fait'])

            if st.button("Modifier la ligne"):
                success = data_p2.modifier_tab2112_fait(selected_id, direction, region, departement, sous_prefecture,
                                                faits_civil,
                                                type_etat_civil, annee, nombre_fait)
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")
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

        # Afficher les données du fichier
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

    df = data_p2.obtenir_tab2113_fait_civi_naiss()
    if st.checkbox("Obtenir des données",key="tab2113obenir"):
        # Ajout des sélecteurs pour l'année, la région, le département et la sous-préfecture
        annees = df['Année'].unique()
        regions = df['Région'].unique()
        departements = df['Département'].unique()
        sous_prefectures = df['Sous-préfecture'].unique()

        selected_annee = st.selectbox("Choisir l'année", annees,key="tab2113anne")
        selected_region = st.selectbox("Choisir la région", regions,key="tab2113region")
        selected_dep = st.selectbox("Choisir le département", departements,key="tab2113depar")
        selected_sous_prefecture = st.selectbox("Choisir la sous-préfecture", sous_prefectures,key="tab2113sous")

        # Filtrer les données en fonction des sélections
        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (
                        df['Département'] == selected_dep) & (df['Sous-préfecture'] == selected_sous_prefecture)],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (
                        df['Département'] == selected_dep) & (df['Sous-préfecture'].isna())],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'].isna()) & (
                df['Sous-préfecture'].isna())]
        ]

        st.write("NB: Un double clique permet de supprimer les doublons")
        if st.button('Recherche de  données de la table', key="tab2112AAB"):
            data_p2.supprimer_doublons_tab2113_fait_civi_naiss()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    if st.checkbox("Modifier une ligne existante","tab2113modiA"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'])

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Région'])
            departement = st.text_input("Département", selected_row['Département'])
            sous_prefecture = st.text_input("Sous-préfecture", selected_row['Sous-préfecture'])
            annee = st.text_input("Année", selected_row['Année'])
            faits_civil = st.text_input("Faits Civil", selected_row['Faits Civil'])
            type_de_centre_civil = st.text_input("Type de Centre Civil", selected_row['Type de Centre Civil'])
            dans_les_delais_3_mois = st.text_input("Dans les délais (3 mois)",
                                                         selected_row['Dans les délais (3 mois)'])
            hors_delai_4_12_mois = st.text_input("Hors délai (4-12 mois)", selected_row['Hors délai (4-12 mois)'])
            hors_delai_plus_de_12_mois = st.text_input("Hors délai (plus de 12 mois)",
                                                             selected_row['Hors délai (plus de 12 mois)'])
            total_faits_naissance = st.text_input("Total Faits Naissance", selected_row['Total Faits Naissance'])

            if st.button("Modifier la ligne",key="tab2113modi"):
                success = data_p2.modifier_tab2113_fait_civi_naiss(selected_id, direction, region, departement,
                                                               sous_prefecture, annee,
                                                               faits_civil, type_de_centre_civil,
                                                               dans_les_delais_3_mois,
                                                               hors_delai_4_12_mois, hors_delai_plus_de_12_mois,
                                                               total_faits_naissance)
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")

        # Afficher les données de la table avec filtres
        if st.button('Recherche de données de la table', key="tab2113AAB"):
            data_p2.supprimer_doublons_tab2113_fait_civi_naiss()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    return



# Page Streamlit
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

    df = data_p2.obtenir_tab2114_fait_civi_deces()
    if st.checkbox("Obtenir des données",key="tab214obtenir"):
        # Ajout des sélecteurs pour l'année, la région, le département et la sous-préfecture
        annees = df['Année'].unique()
        regions = df['Région'].unique()
        departements = df['Département'].unique()
        sous_prefectures = df['Sous-préfecture'].unique()

        selected_annee = st.selectbox("Choisir l'année", annees,key="tab2114annee")
        selected_region = st.selectbox("Choisir la région", regions,key="tab2114region")
        selected_dep = st.selectbox("Choisir le département", departements,key="tab2114depart")
        selected_sous_prefecture = st.selectbox("Choisir la sous-préfecture", sous_prefectures,key="tab2114souspref")

        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (
                        df['Département'] == selected_dep) & (df['Sous-préfecture'] == selected_sous_prefecture)],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (
                        df['Département'] == selected_dep) & (df['Sous-préfecture'].isna())],
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) & (df['Département'].isna()) & (
                df['Sous-préfecture'].isna())]
        ]

        # Afficher les données de la table avec filtres
        st.write("NB: Un double clique supprime les données doublons")
        if st.button('Recherche de données de la table', key="tab2114AAB"):
            data_p2.supprimer_doublons_tab2114_fait_civi_deces()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    if st.checkbox("Modifier une ligne existante",key="tab2114modCh"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'])

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Region", selected_row['Région'])
            departement = st.text_input("Departement", selected_row['Département'])
            sous_prefecture = st.text_input("Sous-prefecture", selected_row['Sous-préfecture'])
            annee = st.text_input("Année", selected_row['Année'])
            faits_civil = st.text_input("Faits Civil", selected_row['Faits civils'])
            type_de_centre_civil = st.text_input("Type de Centre Civil", selected_row['Type de centre civil'])
            dans_les_delais_15_jour = st.number_input("Dans les délais 15 jours",
                                                      selected_row['Hors délai année en cours'])
            hors_delai_annee_cours = st.number_input("Hors délai année en cours",
                                                     selected_row['Hors délai année en cours'])
            hors_delai_des_annees_anteri = st.number_input("Hors délai des années antérieures",
                                                           selected_row['Hors délai des années antérieures'])
            total_faits_deces = st.number_input("Total faits décès", selected_row['Total faits de décès'])

            if st.button("Modifier la ligne"):
                success = data_p2.modifier_tab2114_fait_civi_deces(selected_id, direction, region, departement, sous_prefecture,
                                                           annee,
                                                           faits_civil, type_de_centre_civil, dans_les_delais_15_jour,
                                                           hors_delai_annee_cours, hors_delai_des_annees_anteri,
                                                           total_faits_deces)
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")

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
        expected_columns = [
            "direction", "region", "departement", "sous_prefecture", "annee",
            "nbre_naiss_centr_princ", "nbre_naiss_centr_second", "nbre_total_naiss",
            "nbre_deces_centr_princ", "nbre_deces_centr_second", "nbre_total_deces"
        ]

        if all(column in df.columns for column in expected_columns):
            # Bouton pour enregistrer les données dans la base de données
            if st.button("Enregistrer les données dans la base de données"):
                doublon_detecte = False
                for _, row in df.iterrows():
                    success = data_p2.enregistrer_tab2115_fait_naiss_deces(
                        row['direction'], row['region'], row['departement'], row['sous_prefecture'], row['annee'],
                        row['nbre_naiss_centr_princ'], row['nbre_naiss_centr_second'], row['nbre_total_naiss'],
                        row['nbre_deces_centr_princ'], row['nbre_deces_centr_second'], row['nbre_total_deces']
                    )
                    if not success:
                        doublon_detecte = True

                if doublon_detecte:
                    st.warning("Certaines données ont déjà été enregistrées.")
                else:
                    st.success("Les données du fichier ont été enregistrées avec succès!")
        else:
            st.error("Les colonnes du fichier ne correspondent pas aux colonnes attendues. Veuillez vérifier votre fichier.")

    df = data_p2.obtenir_tab2115_fait_naiss_deces()
    if st.checkbox("Obtenir des données", key="tab2115obtenir"):
        # Ajout des sélecteurs pour l'année, la sous-préfecture, le département et la région
        annees = df['Année'].unique()
        sous_prefectures = df['Sous-préfecture'].unique()
        departements = df['Département'].unique()
        regions = df['Région'].unique()

        selected_annee = st.selectbox("Choisir l'année", annees, key="tab2115anne")
        selected_region = st.selectbox("Choisir la région", regions, key="tab2115region")
        selected_dep = st.selectbox("Choisir le département", departements, key="tab2115departement")
        selected_sous_prefecture = st.selectbox("Choisir la sous-préfecture", sous_prefectures, key="tab2115souspre")

        # Filtrer les données en fonction des sélections
        filtered_dfs = [
            df[(df['Année'] == selected_annee) & (df['Région'] == selected_region) &
               (df['Département'] == selected_dep) & (df['Sous-préfecture'] == selected_sous_prefecture)],
            df[(df['Année'] == selected_annee) & (df['Département'] == selected_dep) & (df['Sous-préfecture'].isna())],
            df[(df['Année'] == selected_annee) & (df['Département'].isna()) & (df['Sous-préfecture'].isna())]
        ]
        st.write("NB: Un double clique supprime les données doublons")
        # Afficher les données de la table avec filtres
        if st.button('Recherche de données de la table', key="tab2115AAB"):
            data_p2.supprimer_doublons_tab2115_fait_naiss_deces()
            for filtered_df in filtered_dfs:
                if not filtered_df.empty:
                    st.dataframe(filtered_df)
                    break

    if st.checkbox("Modifier une ligne existante",key="tab2115chmodi"):
        selected_id = st.selectbox("Choisir l'ID de la ligne à modifier", df['ID'])

        if selected_id:
            selected_row = df[df['ID'] == selected_id].iloc[0]

            direction = st.text_input("Direction", selected_row['Direction'])
            region = st.text_input("Région", selected_row['Région'])
            departement = st.text_input("Département", selected_row['Département'])
            sous_prefecture = st.text_input("Sous-préfecture", selected_row['Sous-préfecture'])
            annee = st.number_input("Année", selected_row['Année'])
            nbre_naiss_centr_princ = st.number_input("Naissances Centre Principal",
                                                     selected_row['Naissance enregistrées dans Centre principal'])
            nbre_naiss_centr_second = st.number_input("Naissances Centre Secondaire",
                                                      selected_row['Naissance enregistrées dans Centre secondaire'])
            nbre_total_naiss = st.number_input("Total Naissances", selected_row['Naissance totale  enregistrée'])
            nbre_deces_centr_princ = st.number_input("Décès Centre Principal",
                                                     selected_row['Décès enregistrés dans Centre principal'])
            nbre_deces_centr_second = st.number_input("Décès Centre Secondaire",
                                                      selected_row['Décès enregistrés dans Centre secondaire'])
            nbre_total_deces = st.number_input("Total Décès", selected_row['Décès total  enregistré'])

            if st.button("Modifier la ligne",key="tab2115modi"):
                success = data_p2.modifier_tab2115_fait_naiss_deces(selected_id, direction, region, departement,
                                                            sous_prefecture, annee,
                                                            nbre_naiss_centr_princ, nbre_naiss_centr_second,
                                                            nbre_total_naiss,
                                                            nbre_deces_centr_princ, nbre_deces_centr_second,
                                                            nbre_total_deces)
                if success:
                    st.success("La ligne a été modifiée avec succès!")
                else:
                    st.error("Une erreur s'est produite lors de la modification de la ligne.")



    return
