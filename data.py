import sqlite3
import pandas as pd
import hashlib

DATABASE = "comptes_regionaux.db"


def enregistrer_utilisateur(username, password, role):
    password_hashed = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO utilisateurs (username, password, role)
                      VALUES (?, ?, ?)''', (username, password_hashed, role))
    conn.commit()
    conn.close()

def verifier_utilisateur(username, password):
    password_encoded = password.encode('utf-8')
    password_hashed = hashlib.sha256(password_encoded).hexdigest()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM utilisateurs WHERE username=? AND password=?''', (username, password_hashed))
    user = cursor.fetchone()
    conn.close()
    if user:
        return {'id': user[0], 'username': user[1], 'role': user[3]}
    return None



def creer_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

# Tableau 1.2.2 nombre de responsables politique departementaux
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab_n_respo_poltque_depart_sex(
        id INTEGER PRIMARY KEY,
        direction TEXT,
        region TEXT,
        annee TEXT,
        partis_politique TEXT,
        departement TEXT,
        hommes TEXT,
        femmes TEXT,
        total_sexe TEXT
        
        )
        
        '''
    )






    cursor.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT,
                        role TEXT
                      )''')

# Faits civiques sur les naissance
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS existence_partis(
        id INTEGER PRIMARY KEY ,
        direction TEXT,
        region TEXT,
        partis_politique TEXT,
        Annee_2015 TEXT,
        Annee_2016 TEXT,
        Annee_2017 TEXT,
        Annee_2018 TEXT,
        Annee_2019 TEXT
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

    conn.commit()
    conn.close()




# Créer la table
creer_table()


def enregistrer_tab_respo_pltq_dep(direction,region,annee,partis_politique,departement,hommes,femmes,total_sexe):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_n_respo_poltque_depart_sex (direction, region, annee, partis_politique, departement, hommes, femmes, total_sexe)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee,partis_politique, departement, hommes, femmes,total_sexe)
    )
    conn.commit()
    conn.close()

def obtenir_tab_respo_poltque_depart_sex():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_n_respo_poltque_depart_sex')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Partis Politique", "Département", "Hommes", "Femmes", "Total Sexe"])
    conn.close()
    return df





def obtenir_region():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT region FROM agriculture_vivrieres ')
    dat = cursor.fetchall()
    conn.close()
    region = [row[0] for row in dat]
    return region

def obtenir_direction():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT direction FROM agriculture_vivrieres ')
    dat = cursor.fetchall()
    conn.close()
    direction = [row[0] for row in dat]
    return direction



def enregistrer_existence_partis(direction, region, partis_politique, annee_2015, annee_2016, annee_2017, annee_2018, annee_2019):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO existence_partis(direction, region, partis_politique, Annee_2015, Annee_2016, Annee_2017, Annee_2018, Annee_2019)
        VALUES(?,?,?,?,?,?,?,?)
    ''', (direction, region, partis_politique, annee_2015, annee_2016, annee_2017, annee_2018, annee_2019))
    conn.commit()
    conn.close()

def obtenir_existence_partis():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM existence_partis')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Partis Politique", "Année 2015", "Année 2016", "Année 2017", "Année 2018", "Année 2019"])
    conn.close()
    return df



def enregistrer_faits_civils(direction, region, departement, sous_prefecture, faits_civil, type_de_centre_civil, dans_les_delais_3_mois, hors_delai_4_12_mois, hors_delai_plus_de_12_mois, total_faits_naissance):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO faits_civils(direction, region, departement, sous_prefecture, faits_civil, type_de_centre_civil, dans_les_delais_3_mois, hors_delai_4_12_mois, hors_delai_plus_de_12_mois, total_faits_naissance)
        VALUES(?,?,?,?,?,?,?,?,?,?)
    ''', (direction, region, departement, sous_prefecture, faits_civil, type_de_centre_civil, dans_les_delais_3_mois, hors_delai_4_12_mois, hors_delai_plus_de_12_mois, total_faits_naissance))
    conn.commit()
    conn.close()


def obtenir_faits_civils():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM faits_civils')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Département", "Sous-préfecture", "Faits Civil", "Type de Centre Civil", "Dans les délais (3 mois)",
                                     "Hors délai (4-12 mois)", "Hors délai (plus de 12 mois)", "Total Faits Naissance"])
    df = df.astype({
        'Dans les délais (3 mois)': 'string',
        'Hors délai (4-12 mois)':'string',
        'Hors délai (plus de 12 mois)':'string',
        'Total Faits Naissance':'string'
        # Ajoutez des conversions pour d'autres colonnes si nécessaire
    })

    conn.close()
    return df
