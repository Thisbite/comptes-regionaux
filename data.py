import sqlite3
import pandas as pd
import hashlib

DATABASE = "comptes_regionaux.db"

def creer_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS agriculture_vivrieres(
        id INTEGER PRIMARY KEY ,
        direction TEXT,
        region TEXT,
        annee TEXT,
        codes TEXT,
        libelle_produit TEXT,
        quantite REAL,
        valeur REAL,
        prix_unitaire REAL,
        superficie REAL,
        effectif INTEGER,
        masse_salariale REAL 
        )
        '''
    )

    cursor.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT,
                        role TEXT
                      )''')

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

def enregistrer_agriculture_vivirier(direction, region, annee, codes, libelle_produit, quantite, valeur,
                                     prix_unitaire, superficie, effectif, masse_salariale):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO agriculture_vivrieres(direction, region, annee, codes, libelle_produit, quantite, valeur, prix_unitaire, superficie, effectif, masse_salariale)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)''', (
        direction, region, annee, codes, libelle_produit, quantite, valeur, prix_unitaire, superficie, effectif, masse_salariale)
    )
    conn.commit()
    conn.close()

def obtenir_agriculture_vivriere():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM agriculture_vivrieres')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Codes", "Libellé du produit",
                                     "Quantité", "Valeur", "Prix unitaire", "Superficie",
                                     "Effectifs employés", "Masse salariale"])
    conn.close()
    return df

# Créer la table
creer_table()

def obtenir_statistiques_riz():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT region, annee, SUM(quantite) as quantite
        FROM agriculture_vivrieres
        WHERE codes = 'A01001000'
        GROUP BY region, annee
        ORDER BY quantite DESC
    ''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["region", "Année", "quantite"])
    conn.close()
    return df

def obtenir_statistiques_par_code(code):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT region, annee, SUM(quantite) as quantite
        FROM agriculture_vivrieres
        WHERE codes = ?
        GROUP BY region, annee
        ORDER BY annee, quantite DESC
    ''', (code,))
    dat = cursor.fetchall()
    df = pd.DataFrame(dat, columns=["region", "Année", "quantite"])
    conn.close()
    return df

def modifier_agriculture_vivriere(direction, annee, code, new_values):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE agriculture_vivrieres
        SET direction = ?, region = ?, annee = ?, codes = ?, libelle_produit = ?, quantite = ?, valeur = ?, prix_unitaire = ?, superficie = ?, effectif = ?, masse_salariale = ?
        WHERE direction = ? AND annee = ? AND codes = ?
    ''', (*new_values, direction, annee, code))
    conn.commit()
    conn.close()

def supprimer_agriculture_vivriere(direction, annee, code):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM agriculture_vivrieres
        WHERE direction = ? AND annee = ? AND codes = ?
    ''', (direction, annee, code))
    conn.commit()
    conn.close()

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

def obtenir_code():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT codes FROM agriculture_vivrieres ')
    dat = cursor.fetchall()
    conn.close()
    codes = [row[0] for row in dat]
    return codes

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
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Département", "Sous-préfecture", "Faits Civil", "Type de Centre Civil", "Dans les délais (3 mois)", "Hors délai (4-12 mois)", "Hors délai (plus de 12 mois)", "Total Faits Naissance"])
    conn.close()
    return df
