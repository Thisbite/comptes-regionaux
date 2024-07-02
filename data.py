import sqlite3
import pandas as pd
import hashlib

DATABASE = "db_annuaire_stat.db"
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

#cursor.execute("DROP TABLE existence_partis")
#cursor.execute("DROP TABLE tab_repa_deput_pol_sex_dep")
#cursor.execute("DROP TABLE tab_mair_recon_nvl_dep")

def enregistrer_utilisateur(username, password, role):
    password_hashed = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''INSERT OR IGNORE INTO utilisateurs (username, password, role)
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



    cursor.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE,
                        password TEXT,
                        role TEXT
                      )''')

    conn.commit()
    conn.close()



creer_table()



