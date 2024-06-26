import sqlite3
import pandas as pd

DATABASE = "comptes_regionaux.db"
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()




def creer_table_part2():
    # Tableau 2.1.12 : Faits d'état civil enregistrés et parvenus au niveau central selon le type de centre de la Région
    #                       du Poro par Département et Sous-Préfecture en 2019

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab2112_faits_civils(
        id INTEGER PRIMARY KEY ,
        direction TEXT,
        region TEXT,
        departement TEXT,
        sous_prefecture TEXT,
        faits_civil TEXT,
        type_etat_civil TEXT,
        annee TEXT,
        nombre_fait INTEGER

        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS faits_civils(
        id INTEGER PRIMARY KEY ,
        direction TEXT,
        region TEXT,
        departement TEXT,
        sous_prefecture TEXT,
        faits_civil TEXT,
        type_de_centre_civil TEXT,
        dans_les_delais_3_mois INTEGER,
        hors_delai_4_12_mois INTEGER,
        hors_delai_plus_de_12_mois INTEGER,
        total_faits_naissance INTEGER
        )
        '''
    )
    # Tableau 2.1.10 : Mariages enregistrés selon la nationalité et le type de centre d’état civil par Département de la Région du Poro  en 2019

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab2110_maria_centre_civil_dep(
            id INTEGER PRIMARY KEY,
            direction TEXT,
            region TEXT,
            departement TEXT, 
            annee TEXT,
            centre_etat_civil TEXT,
           nat_coupl_ivoi INTEGER,
            nat_coupl_mixte INTEGER,
            nat_coupl_etrang INTEGER
        )
        '''
    )

    # Tableau 2.1.9: Mariages enregistrés à l’état civil selon le régime matrimonial par Département de la

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab219_maria_regim(
            id INTEGER PRIMARY KEY,
            direction TEXT,
            region TEXT,
            departement TEXT, 
            annee TEXT,
           reg_mat_bien_com INTEGER,
            reg_mat_bien_sep INTEGER
        )
        '''
    )

    # Tableau 2.1.8: Mariages enregistrés à l’état civil selon la nationalité par Département en
    # Erreur de nommination de la table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab219_maria_eta_civ_regim(
            id INTEGER PRIMARY KEY,
            direction TEXT,
            region TEXT,
            departement TEXT, 
            annee TEXT,
           nat_coupl_ivoi INTEGER,
            nat_coupl_mixte INTEGER,
            nat_coupl_etrang INTEGER
        )
        '''
    )

    # Tableau 2.1.7: Evolution de la population de la région du PORO par département et par sexe sur les 5 dernières années
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab217_evolu_pop_reg_dep(
            id INTEGER PRIMARY KEY,
            direction TEXT,
            region TEXT,
            annee TEXT,
            departement TEXT,
            sous_prefecture TEXT,
            hommes INTEGER,
            femmes INTEGER,
            total_sexe INTEGER,
            densite REAL
        )
        '''
    )

    # Tableau 2.1.3: Population du département par tranche d'âge selon la sous-préfecture et le sexe
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab213_pop_dep_tranc_s_pref_sex(
            id INTEGER PRIMARY KEY,
            direction TEXT,
            region TEXT,
            annee TEXT,
            departement TEXT,
            sous_prefecture TEXT,
            tranche_age TEXT,
            hommes INTEGER,
            femmes INTEGER,
            total_sexe INTEGER
        )
        '''
    )

    # Tableau 2.1.2: Répartition de la population de la région du Poro par grand groupe d’âge selon le sexe
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab212_repa_pop_grou_age(
            id INTEGER PRIMARY KEY,
            direction TEXT,
            region TEXT,
            annee TEXT,
            groupe_age TEXT,
            hommes INTEGER,
            femmes INTEGER,
            total_sexe INTEGER,
            rapport_masculinite REAL
        )
        '''
    )

    # Tableau 2.1.1: Population de la région du Poro par Département et par sous-préfecture
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab211_pop_dep_sous_pref_sex(
            id INTEGER PRIMARY KEY,
            direction TEXT,
            region TEXT,
            annee TEXT,
            departement TEXT,
            sous_prefecture TEXT,
            hommes INTEGER,
            femmes INTEGER,
            total_sexe INTEGER,
            rapport_masculinite REAL
        )
        '''
    )

    conn.commit()
    conn.close()


# Créer la table
creer_table_part2()


# Les fonctions de la sections parties 2


def enregistrer_faits_civils(direction, region, departement, sous_prefecture, faits_civil, type_de_centre_civil,
                             dans_les_delais_3_mois, hors_delai_4_12_mois, hors_delai_plus_de_12_mois,
                             total_faits_naissance):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO faits_civils(direction, region, departement, sous_prefecture, faits_civil, type_de_centre_civil, dans_les_delais_3_mois, hors_delai_4_12_mois, hors_delai_plus_de_12_mois, total_faits_naissance)
        VALUES(?,?,?,?,?,?,?,?,?,?)
    ''', (direction, region, departement, sous_prefecture, faits_civil, type_de_centre_civil, dans_les_delais_3_mois,
          hors_delai_4_12_mois, hors_delai_plus_de_12_mois, total_faits_naissance))
    conn.commit()
    conn.close()


def obtenir_faits_civils():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM faits_civils')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Département", "Sous-préfecture", "Faits Civil",
                                     "Type de Centre Civil", "Dans les délais (3 mois)",
                                     "Hors délai (4-12 mois)", "Hors délai (plus de 12 mois)", "Total Faits Naissance"])
    df = df.astype({
        'Dans les délais (3 mois)': 'string',
        'Hors délai (4-12 mois)': 'string',
        'Hors délai (plus de 12 mois)': 'string',
        'Total Faits Naissance': 'string'
        # Ajoutez des conversions pour d'autres colonnes si nécessaire
    })

    conn.close()
    return df


def enregistrer_tab217_evolu_pop_reg_dep(direction, region, annee, departement, sous_prefecture, hommes, femmes,
                                         total_sexe, densite):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab217_evolu_pop_reg_dep (direction, region, annee, departement, sous_prefecture, hommes, femmes, total_sexe, densite)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, sous_prefecture, hommes, femmes, total_sexe, densite)
    )
    conn.commit()
    conn.close()


def obtenir_tab217_evolu_pop_reg_dep():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab217_evolu_pop_reg_dep')
    rows = cursor.fetchall()
    conn.close()
    return rows


def enregistrer_tab213_pop_dep_tranc_s_pref_sex(direction, region, annee, departement, sous_prefecture, tranche_age,
                                                hommes, femmes, total_sexe):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab213_pop_dep_tranc_s_pref_sex (direction, region, annee, departement, sous_prefecture, tranche_age, hommes, femmes, total_sexe)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, sous_prefecture, tranche_age, hommes, femmes, total_sexe)
    )
    conn.commit()
    conn.close()


def obtenir_tab213_pop_dep_tranc_s_pref_sex():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab213_pop_dep_tranc_s_pref_sex')
    rows = cursor.fetchall()
    conn.close()
    return rows


def enregistrer_tab212_repa_pop_grou_age(direction, region, annee, groupe_age, hommes, femmes, total_sexe,
                                         rapport_masculinite):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab212_repa_pop_grou_age (direction, region, annee, groupe_age, hommes, femmes, total_sexe, rapport_masculinite)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, groupe_age, hommes, femmes, total_sexe, rapport_masculinite)
    )
    conn.commit()
    conn.close()


def obtenir_tab212_repa_pop_grou_age():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab212_repa_pop_grou_age')
    rows = cursor.fetchall()
    conn.close()
    return rows


def enregistrer_tab211_pop_dep_sous_pref_sex(direction, region, annee, departement, sous_prefecture, hommes, femmes,
                                             total_sexe, rapport_masculinite):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab211_pop_dep_sous_pref_sex (direction, region, annee, departement, sous_prefecture, hommes, femmes, total_sexe, rapport_masculinite)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, sous_prefecture, hommes, femmes, total_sexe, rapport_masculinite)
    )
    conn.commit()
    conn.close()


def obtenir_tab211_pop_dep_sous_pref_sex():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab211_pop_dep_sous_pref_sex')
    rows = cursor.fetchall()
    conn.close()
    return rows


# Fonction d'enregistrement pour la table tab219_maria_eta_civ_regim
def enregistrer_tab219_maria_eta_civ_regim(direction, region, annee, departement, nat_coupl_ivoi, nat_coupl_mixte,
                                           nat_coupl_etrang):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tab219_maria_eta_civ_regim(direction, region, annee, departement, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang)
        VALUES(?,?,?,?,?,?,?)
    ''', (direction, region, annee, departement, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang))
    conn.commit()
    conn.close()


# Fonction pour obtenir les données de la table tab219_maria_eta_civ_regim
def obtenir_tab219_maria_eta_civ_regim():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab219_maria_eta_civ_regim')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Département", "Nat Coupl Ivoi",
                                     " Couple mixte de nationalité ", "Couple de nationalité etrangere"])
    df = df.astype({
        'Couple de nationalité ivoirienne': 'int',
        'Couple mixte de nationalité': 'int',
        'Couple de nationalité etrangere': 'int'
        # Ajoutez des conversions pour d'autres colonnes si nécessaire
    })

    conn.close()
    return df


def enregistrer_tab219_maria_regim(direction, region, departement, annee, reg_mat_bien_com, reg_mat_bien_sep):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tab219_maria_regim(direction, region, departement, annee, reg_mat_bien_com, reg_mat_bien_sep)
        VALUES(?,?,?,?,?,?)
    ''', (direction, region, departement, annee, reg_mat_bien_com, reg_mat_bien_sep))
    conn.commit()
    conn.close()


# Fonction pour obtenir les données de la table tab219_maria_regim
def obtenir_tab219_maria_regim():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab219_maria_regim')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Département", "Année", "Reg Mat Bien Com",
                                     "Reg Mat Bien Sep"])
    df = df.astype({
        'Reg Mat Bien Com': 'int',
        'Reg Mat Bien Sep': 'int'
        # Ajoutez des conversions pour d'autres colonnes si nécessaire
    })

    conn.close()
    return df


def enregistrer_maria_centre_civil_dep(direction, region, departement, annee, centre_etat_civil, nat_coupl_ivoi,
                                       nat_coupl_mixte, nat_coupl_etrang):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tab2110_maria_centre_civil_dep(direction, region, departement, annee, centre_etat_civil, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang)
        VALUES(?,?,?,?,?,?,?,?)
    ''', (direction, region, departement, annee, centre_etat_civil, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang))
    conn.commit()
    conn.close()


def obtenir_maria_centre_civil_dep():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab2110_maria_centre_civil_dep')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Département", "Année", "Centre État Civil",
                                     "Couple ivoirien", "Couple mixte", "Couple étranger"])
    df = df.astype({
        'Couple ivoirien': 'int',
        'Couple mixte': 'int',
        'Couple étranger': 'int'
        # Ajoutez des conversions pour d'autres colonnes si nécessaire
    })

    conn.close()
    return df



def enregistrement_tab2112_fait(direction, region, departement, sous_prefecture, faits_civil, type_etat_civil, annee, nombre_fait):
    conn = sqlite3.connect('comptes_regionaux.db')  # Remplacez 'your_database.db' par le nom de votre base de données
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tab2112_faits_civils (direction, region, departement, sous_prefecture, faits_civil, type_etat_civil, annee, nombre_fait)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (direction, region, departement, sous_prefecture, faits_civil, type_etat_civil, annee, nombre_fait))
    conn.commit()
    conn.close()


def obtenir_tab2112_fait():
    cursor.execute('SELECT * FROM tab2112_faits_civils')
    data = cursor.fetchall()
    df_data = pd.DataFrame(data, columns=['ID', 'Direction', 'Region', 'Departement', 'Sous-prefecture', 'Faits Civil', 'Type Etat Civil', 'Annee', 'Nombre Fait'])
    return df_data