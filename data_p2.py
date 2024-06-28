import sqlite3
import pandas as pd

DATABASE = "db_annuaire_stat.db"
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()


def creer_table_part2():


    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab2115_fait_naiss_deces(
        id INTEGER PRIMARY KEY ,
        direction TEXT,
        region TEXT,
        departement TEXT,
        sous_prefecture TEXT,
        annee TEXT,
        nbre_naiss_centr_princ INTEGER,
        nbre_naiss_centr_second INTEGER,
        nbre_total_naiss INTEGER,
       nbre_deces_centr_princ INTEGER,
        nbre_deces_centr_second INTEGER,
        nbre_total_deces INTEGER
        )
        '''
    )





    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab2114_fait_civi_deces(
        id INTEGER PRIMARY KEY ,
        direction TEXT,
        region TEXT,
        departement TEXT,
        sous_prefecture TEXT,
        annee TEXT,
        faits_civil TEXT,
        type_de_centre_civil TEXT,
        dans_les_delais_15_jour INTEGER,
        hors_delai_annee_cours INTEGER,
        hors_delai_des_annees_anteri INTEGER,
        total_faits_deces INTEGER
        )
        '''
    )


    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab2113_fait_civi_naiss(
        id INTEGER PRIMARY KEY ,
        direction TEXT,
        region TEXT,
        departement TEXT,
        sous_prefecture TEXT,
        annee TEXT,
        faits_civil TEXT,
        type_de_centre_civil TEXT,
        dans_les_delais_3_mois INTEGER,
        hors_delai_4_12_mois INTEGER,
        hors_delai_plus_de_12_mois INTEGER,
        total_faits_naissance INTEGER
        )
        '''
    )


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
        CREATE TABLE IF NOT EXISTS tab2111_fait_matr_civils(
        id INTEGER PRIMARY KEY ,
        direction TEXT,
        region TEXT,
        departement TEXT,
         annee TEXT,
        type_centre_civil TEXT,
        nbre_bien_commun INTEGER,
        nbre_bien_separe INTEGER
       
       

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
        CREATE TABLE IF NOT EXISTS tab218_maria_eta_civ_regim(
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
    df = pd.DataFrame(rows, columns=[
        'ID', 'Direction', 'Région', 'Année', 'Département', 'Sous-prefecture', 'Hommes', 'Femmes', 'Total sexe',
        'Densité'
    ])
    conn.close()
    return df





def enregistrer_tab218_maria_eta_civ_regim(direction, region, departement, annee, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tab218_maria_eta_civ_regim (direction, region, departement, annee, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (direction, region, departement, annee, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang))
    conn.commit()
    conn.close()

def obtenir_tab218_maria_eta_civ_regim():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab218_maria_eta_civ_regim')
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[
        'ID', 'Direction', 'Région', 'Département', 'Année', 'Couple ivoirien', 'Couple mixte', 'Couple étranger'
    ])
    conn.close()
    return df



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
    df = pd.DataFrame(rows, columns=[
        'ID', 'Direction', 'Région', 'Département', 'Sous-préfecture', 'Année', 'Fait civil',
        'Type de centre civil', 'Dans les délais (0-3 mois)', 'Hors délai (4-12 mois)',
        'Hors délai (>12 mois)', 'Total faits naissance'
    ])
    conn.close()
    return df


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
    df_table = pd.DataFrame(rows, columns=[
        "ID", "Direction régionale", "Région", "Année", "Tranche d'âge", "Nombre d'hommes", " Nombre de femmes",
        "Total sexe",
        "Rapport masculinité"
    ])
    conn.close()
    return df_table


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
    df_table = pd.DataFrame(rows, columns=[
        'ID', 'Direction régionale', 'Région', 'Année', 'Département', 'Sous-préfecture', 'Nombre hommes',
        ' Nombre de femmes', 'Total sexe',
        'rapport_masculinite'
    ])
    conn.close()
    return df_table


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
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Département", "Année", "Regime Matrimonial Bien Commun",
                                     "Regime Matrimonial Bien Separé"])
    df = df.astype({
        'Regime Matrimonial Bien Commun': 'int',
        'Regime Matrimonial Bien Separé': 'int'
        # Ajoutez des conversions pour d'autres colonnes si nécessaire
    })

    conn.close()
    return df













def enregistrer_tab2110_maria_centre_civil_dep(direction, region, departement, annee, centre_etat_civil, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tab2110_maria_centre_civil_dep (direction, region, departement, annee, centre_etat_civil, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (direction, region, departement, annee, centre_etat_civil, nat_coupl_ivoi, nat_coupl_mixte, nat_coupl_etrang))
    conn.commit()
    conn.close()
def obtenir_tab2110_maria_centre_civil_dep():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab2110_maria_centre_civil_dep')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Département", "Année", "Centre état civil", "Couple ivoirien", "Couple mixte", "Couple étranger"])
    conn.close()
    return df


def enregistrer_tab2111_fait_matr_civils(direction, region, departement, annee, type_centre_civil, nbre_bien_commun, nbre_bien_separe):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab2111_fait_matr_civils (direction, region, departement, annee, type_centre_civil, nbre_bien_commun, nbre_bien_separe)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, departement, annee, type_centre_civil, nbre_bien_commun, nbre_bien_separe)
    )
    conn.commit()
    conn.close()

def obtenir_tab2111_fait_matr_civils():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab2111_fait_matr_civils')
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[
        'ID', 'Direction', 'Region', 'Departement', 'Année', 'Type de centre civil', 'Régime de bien commun',
        'Régime de bien séparé'
    ])
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
    conn = sqlite3.connect('comptes_regionaux.db')  # Remplacez 'your_database.db' par le nom de votre base de données
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab2112_faits_civils')
    data = cursor.fetchall()
    df_data = pd.DataFrame(data, columns=['ID', 'Direction', 'Region', 'Departement', 'Sous-prefecture', 'Faits Civil', 'Type Etat Civil', 'Annee', 'Nombre Fait'])
    return df_data


def enregistrer_tab2113_fait_civi_naiss(direction, region, departement, sous_prefecture,annee, faits_civil, type_de_centre_civil,
                             dans_les_delais_3_mois, hors_delai_4_12_mois, hors_delai_plus_de_12_mois,
                             total_faits_naissance):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tab2113_fait_civi_naiss(direction, region, departement, sous_prefecture,annee, faits_civil, type_de_centre_civil, dans_les_delais_3_mois, hors_delai_4_12_mois, hors_delai_plus_de_12_mois, total_faits_naissance)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
    ''', (direction, region, departement, sous_prefecture,annee, faits_civil, type_de_centre_civil, dans_les_delais_3_mois,
          hors_delai_4_12_mois, hors_delai_plus_de_12_mois, total_faits_naissance))
    conn.commit()
    conn.close()


def obtenir_tab2113_fait_civi_naiss():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab2113_fait_civi_naiss')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Département", "Sous-préfecture", "Année","Faits Civil",
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


def enregistrer_tab2114_fait_civi_deces(direction, region, departement, sous_prefecture,annee, faits_civil, type_de_centre_civil, dans_les_delais_15_jour, hors_delai_annee_cours, hors_delai_des_annees_anteri, total_faits_deces):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab2114_fait_civi_deces (direction, region, departement, sous_prefecture,annee, faits_civil, type_de_centre_civil, dans_les_delais_15_jour, hors_delai_annee_cours, hors_delai_des_annees_anteri, total_faits_deces)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
        ''',
        (direction, region, departement, sous_prefecture,annee, faits_civil, type_de_centre_civil, dans_les_delais_15_jour, hors_delai_annee_cours, hors_delai_des_annees_anteri, total_faits_deces)
    )
    conn.commit()
    conn.close()

def obtenir_tab2114_fait_civi_deces():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab2114_fait_civi_deces')
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=[
        'ID', 'Direction', 'Région', 'Département', 'Sous-préfecture', 'Année', 'Faits civils', 'Type de centre civil',
        'Dans les délais 15 jours', 'Hors délai année en cours', 'Hors délai des années antérieures',
        'Total faits de décès'
    ])
    conn.close()
    return df


def enregistrer_tab2115_fait_naiss_deces(direction, region, departement, sous_prefecture, annee, nbre_naiss_centr_princ, nbre_naiss_centr_second, nbre_total_naiss, nbre_deces_centr_princ, nbre_deces_centr_second, nbre_total_deces):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab2115_fait_naiss_deces (direction, region, departement, sous_prefecture, annee, nbre_naiss_centr_princ, nbre_naiss_centr_second, nbre_total_naiss, nbre_deces_centr_princ, nbre_deces_centr_second, nbre_total_deces)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, departement, sous_prefecture, annee, nbre_naiss_centr_princ, nbre_naiss_centr_second, nbre_total_naiss, nbre_deces_centr_princ, nbre_deces_centr_second, nbre_total_deces)
    )
    conn.commit()
    conn.close()

def obtenir_tab2115_fait_naiss_deces():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab2115_fait_naiss_deces')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Département","Sous-préfecture", "Année", "Naissance enregistrées dans Centre principal",
                                     "Naissance enregistrées dans Centre secondaire","Naissance totale  enregistrée","Décès enregistrés dans Centre principal",
                                     "Décès enregistrés dans Centre secondaire","Décès total  enregistré"])
    conn.close()
    return df
