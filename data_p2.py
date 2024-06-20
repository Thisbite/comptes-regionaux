import sqlite3
import pandas as pd

DATABASE = "comptes_regionaux.db"



def creer_table_part2():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
#Tableau 2.1.7: Evolution de la population de la région du PORO par département et par sexe sur les 5 dernières années
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

def enregistrer_tab217_evolu_pop_reg_dep(direction, region, annee, departement, sous_prefecture, hommes, femmes, total_sexe, densite):
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



def enregistrer_tab213_pop_dep_tranc_s_pref_sex(direction, region, annee, departement, sous_prefecture, tranche_age, hommes, femmes, total_sexe):
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

def enregistrer_tab212_repa_pop_grou_age(direction, region, annee, groupe_age, hommes, femmes, total_sexe, rapport_masculinite):
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

def enregistrer_tab211_pop_dep_sous_pref_sex(direction, region, annee, departement, sous_prefecture, hommes, femmes, total_sexe, rapport_masculinite):
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
