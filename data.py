import sqlite3
import pandas as pd
import hashlib
conn = sqlite3.connect("comptes_regionaux.db")
cursor = conn.cursor()

def creer_table():
    # Table agriculture vivrière
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







    conn.commit()

def enregistrer_agriculture_vivirier(direction, region, annee, codes, libelle_produit, quantite, valeur,
                                     prix_unitaire, superficie, effectif, masse_salariale):
    cursor.execute('''
        INSERT INTO agriculture_vivrieres(direction, region, annee, codes, libelle_produit, quantite, valeur, prix_unitaire, superficie, effectif, masse_salariale)
        VALUES(?,?,?,?,?,?,?,?,?,?,?)''', (
        direction, region, annee, codes, libelle_produit, quantite, valeur, prix_unitaire, superficie, effectif, masse_salariale)
    )
    conn.commit()

def obtenir_agriculture_vivriere():
    cursor.execute('SELECT * FROM agriculture_vivrieres')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Codes", "Libellé du produit",
                                     "Quantité", "Valeur", "Prix unitaire", "Superficie",
                                     "Effectifs employés", "Masse salariale"])
    return df

# Créer la table
creer_table()


def obtenir_statistiques_riz():
    cursor.execute('''
        SELECT region, annee, SUM(quantite) as quantite
        FROM agriculture_vivrieres
        WHERE codes = 'A01001000'
        GROUP BY region, annee
        ORDER BY quantite DESC
    ''')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["region", "Année", "quantite"])
    return df

def obtenir_statistiques_par_code(code):
    cursor.execute('''
        SELECT region, annee, SUM(quantite) as quantite
        FROM agriculture_vivrieres
        WHERE codes = ?
        GROUP BY region, annee
        ORDER BY annee,quantite DESC
    ''', (code,))
    dat = cursor.fetchall()
    df = pd.DataFrame(dat, columns=["region", "Année", "quantite"])
    return df



def modifier_agriculture_vivriere(direction, annee, code, new_values):
    cursor.execute('''
        UPDATE agriculture_vivrieres
        SET direction = ?, region = ?, annee = ?, codes = ?, libelle_produit = ?, quantite = ?, valeur = ?, prix_unitaire = ?, superficie = ?, effectif = ?, masse_salariale = ?
        WHERE direction = ? AND annee = ? AND codes = ?
    ''', (*new_values, direction, annee, code))
    conn.commit()



def supprimer_agriculture_vivriere(direction, annee, code):
    cursor.execute('''
        DELETE FROM agriculture_vivrieres
        WHERE direction = ? AND annee = ? AND codes = ?
    ''', (direction, annee, code))
    conn.commit()



def enregistrer_utilisateur(username, password, role):
    password_hashed = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('''INSERT INTO utilisateurs (username, password, role)
                      VALUES (?, ?, ?)''', (username, password_hashed, role))
    conn.commit()

#enregistrer_utilisateur("admin2","admin2", "admin")
def verifier_utilisateur(username, password):
    password_encoded = password.encode('utf-8')
    password_hashed = hashlib.sha256(password_encoded).hexdigest()
    cursor.execute('''SELECT * FROM utilisateurs WHERE username=? AND password=?''', (username, password_hashed))
    user = cursor.fetchone()
    if user:
        return {'id': user[0], 'username': user[1], 'role': user[3]}
    return None

def obtenir_region():
    cursor.execute('SELECT DISTINCT region FROM agriculture_vivrieres ')
    dat=cursor.fetchall()
    region=[row[0] for row in dat]
    return region
def obtenir_direction():
    cursor.execute('SELECT DISTINCT direction FROM agriculture_vivrieres ')
    dat=cursor.fetchall()
    direction=[row[0] for row in dat]
    return direction


def obtenir_code():
    cursor.execute('SELECT DISTINCT codes FROM agriculture_vivrieres ')
    dat=cursor.fetchall()
    codes=[row[0] for row in dat]
    return codes
