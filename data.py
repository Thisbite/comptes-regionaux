import sqlite3
import pandas as pd
import hashlib

DATABASE = "db_annuaire_stat.db"


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
    # Existence de partie politique
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS existence_partis(
        id INTEGER PRIMARY KEY ,
        direction TEXT,
        region TEXT,
        partis_politique TEXT,
        statut_existence INTEGER,
        annee TEXT
        )
        '''
    )

    # Tableau 1.2.10: Superficie et nombre de village par sous-préfecture
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab_superf_nb_vil_dep(
        id INTEGER PRIMARY KEY,
        direction TEXT,
        region TEXT,
        annee TEXT,
        departement TEXT,
        sous_prefecture TEXT,
        superficie TEXT,
        nombre_village INTEGER



        )

        '''
    )

    # Tableau 1.2.9: Liste des sous-préfectures par département
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab_list_sous_pref_dep(
        id INTEGER PRIMARY KEY,
        direction TEXT,
        region TEXT,
        annee TEXT,
        departement TEXT,
        list_sous_pref_urbain TEXT,
        list_sous_pref_rural TEXT,
       nombre_sous_pref TEXT



        )

        '''
    )
    # Tableau 1.2.8: Répartition des députés par sexe et par partie politique

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab_repa_deput_pol_sex_dep(
        id INTEGER PRIMARY KEY,
        direction TEXT,
        region TEXT,
        annee TEXT,
        departement TEXT,
        partis_politique TEXT,
        hommes TEXT,
        femmes TEXT,
        total_sexe TEXT


        )

        '''
    )

    # Tableau 1.2.7 : Effectif des maires reconduits et nouvellement élus par département

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab_mair_recon_nvl_dep(
        id INTEGER PRIMARY KEY,
        direction TEXT,
        region TEXT,
        annee TEXT,
        departement TEXT,
        maire_nouveau INTEGER,
        maire_reconduit INTEGER



        )

        '''
    )

    # Tableau 1.2.6: Répartition des adjoints au maire par département, par sexe et par partie politique
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab_repa_adj_mai_dep_p(
        id INTEGER PRIMARY KEY,
        direction TEXT,
        region TEXT,
        annee TEXT,
        departement TEXT,
        partis_politique TEXT,
        hommes TEXT,
        femmes TEXT,
        total_sexe TEXT


        )

        '''
    )

    # Tableau 1.2.5: Répartition des maires par département, par sexe et par partie politique (on pourrait aussi voir l'évolution)
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab_repa_mair_dep_pol(
        id INTEGER PRIMARY KEY,
        direction TEXT,
        region TEXT,
        annee TEXT,
        departement TEXT,
        partis_politique TEXT,
        hommes TEXT,
        femmes TEXT,
        total_sexe TEXT


        )

        '''
    )

    # Tableau 1.2.4: Répartition régionale des postes de responsabilités occupés par les femmes dans les mairies
    # (maire, 1er adjoint au maire, 2ème adjoint au maire) sur les 5 derniers exercices municipaux

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab_repa_pos_mai_fem_dep(
        id INTEGER PRIMARY KEY,
        direction TEXT,
        region TEXT,
        annee TEXT,
        departement TEXT,
        fonction TEXT,
        total_sexe TEXT,
        femmes TEXT

        )

        '''
    )

    # Tableau 1.2.3: Effectif des maires élus  par département et par sexe sur les 5 derniers exercices municipaux

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS tab_effec_maire_depart(
        id INTEGER PRIMARY KEY,
        direction TEXT,
        region TEXT,
        annee TEXT,
        departement TEXT,
         total_sexe TEXT,
        femmes TEXT

        )

        '''
    )

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

    conn.commit()
    conn.close()


# Créer la table
creer_table()


# Fonction pour insérer des données dans la table

def enregistrer_tab_superf_nb_vil_dep(direction, region, annee, departement, sous_prefecture, superficie,
                                      nombre_village):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_superf_nb_vil_dep (direction, region, annee, departement,sous_prefecture,superficie,nombre_village)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, sous_prefecture, superficie, nombre_village)
    )
    conn.commit()
    conn.close()


# Fonction pour obtenir les données de la table
def obtenir_tab_superf_nb_vil_dep():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_superf_nb_vil_dep')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Département", "Sous-Préfecture",
                                     "Superficie(km2)", "Nombre de village"])
    conn.close()
    return df


def enregistrer_tab_list_sous_pref_dep(direction, region, annee, departement, list_sous_pref_urbain,
                                       list_sous_pref_rural, nombre_sous_pref):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_list_sous_pref_dep (direction, region, annee, departement, list_sous_pref_urbain, list_sous_pref_rural, nombre_sous_pref)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, list_sous_pref_urbain, list_sous_pref_rural, nombre_sous_pref)
    )
    conn.commit()
    conn.close()


# Fonction pour obtenir les données de la table
def obtenir_tab_list_sous_pref_dep():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_list_sous_pref_dep')
    data = cursor.fetchall()
    df = pd.DataFrame(data,
                      columns=["ID", "Direction", "Région", "Année", "Département", "Liste Sous-Préfecture Urbain",
                               "Liste Sous-Préfecture Rural", "Nombre Sous-Préf."])
    conn.close()
    return df


def enregistrer_tab_repa_deput_pol_sex_dep(direction, region, annee, departement, partis_politique, hommes, femmes,
                                           total_sexe):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_repa_deput_pol_sex_dep (direction, region, annee, departement, partis_politique, hommes, femmes, total_sexe)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, partis_politique, hommes, femmes, total_sexe)
    )
    conn.commit()
    conn.close()


# Fonction pour obtenir les données de la table
def obtenir_tab_repa_deput_pol_sex_dep():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_repa_deput_pol_sex_dep')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Département", "Partis Politique", "Hommes",
                                     "Femmes", "Total Sexe"])
    conn.close()
    return df


def enregistrer_tab_mair_recon_nvl_dep(direction, region, annee, departement, maire_nouveau, maire_reconduit):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_mair_recon_nvl_dep (direction, region, annee, departement, maire_nouveau, maire_reconduit)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, maire_nouveau, maire_reconduit)
    )
    conn.commit()
    conn.close()


def obtenir_tab_mair_recon_nvl_dep():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_mair_recon_nvl_dep')
    data = cursor.fetchall()
    df = pd.DataFrame(data,
                      columns=["ID", "Direction", "Région", "Année", "Département", "Maire Nouveau", "Maire Reconduit"])
    conn.close()
    return df


def enregistrer_tab_repa_adj_mai_dep_p(direction, region, annee, departement, partis_politique, hommes, femmes,
                                       total_sexe):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_repa_adj_mai_dep_p (direction, region, annee, departement, partis_politique, hommes, femmes, total_sexe)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, partis_politique, hommes, femmes, total_sexe)
    )
    conn.commit()
    conn.close()


def obtenir_tab_repa_adj_mai_dep_p():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_repa_adj_mai_dep_p')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Département", "Partis Politique", "Hommes",
                                     "Femmes", "Total Sexe"])
    conn.close()
    return df


def enregistrer_tab_repa_mair_dep_pol(direction, region, annee, departement, partis_politique, hommes, femmes,
                                      total_sexe):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_repa_mair_dep_pol (direction, region, annee, departement, partis_politique, hommes, femmes, total_sexe)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, partis_politique, hommes, femmes, total_sexe)
    )
    conn.commit()
    conn.close()


def obtenir_tab_repa_mair_dep_pol():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_repa_mair_dep_pol')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Département", "Partis Politique", "Hommes",
                                     "Femmes", "Total Sexe"])
    conn.close()
    return df


def enreg_tab_repa_post_mai_fem_dep(direction, region, annee, departement, fonction, total_sexe, femmes):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_repa_pos_mai_fem_dep (direction, region, annee, departement, fonction, total_sexe, femmes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, fonction, total_sexe, femmes)
    )
    conn.commit()
    conn.close()


def obtenir_tab_repa_post_mai_fem_dep():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_repa_pos_mai_fem_dep')
    data = cursor.fetchall()
    df = pd.DataFrame(data,
                      columns=["ID", "Direction", "Région", "Année", "Département", "Fonction", "Total Sexe", "Femmes"])
    conn.close()
    return df


def enregistrer_tab_effec_maire_depart(direction, region, annee, departement, total_sexe, femmes):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_effec_maire_depart (direction, region, annee, departement, total_sexe, femmes)
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, departement, total_sexe, femmes)
    )
    conn.commit()
    conn.close()


def obtenir_tab_effec_maire_depart():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_effec_maire_depart')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Département", "Total Sexe", "Femmes"])
    conn.close()
    return df


def enregistrer_tab_respo_pltq_dep(direction, region, annee, partis_politique, departement, hommes, femmes, total_sexe):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO tab_n_respo_poltque_depart_sex (direction, region, annee, partis_politique, departement, hommes, femmes, total_sexe)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (direction, region, annee, partis_politique, departement, hommes, femmes, total_sexe)
    )
    conn.commit()
    conn.close()


def obtenir_tab_respo_poltque_depart_sex():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tab_n_respo_poltque_depart_sex')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Année", "Partis Politique", "Département", "Hommes",
                                     "Femmes", "Total Sexe"])
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


def enregistrer_existence_partis(direction, region, partis_politique, annee, statut_existence):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO existence_partis(direction, region, partis_politique, annee,statut_existence)
        VALUES(?,?,?,?,?)
    ''', (direction, region, partis_politique, annee, statut_existence))
    conn.commit()
    conn.close()


def obtenir_existence_partis():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM existence_partis')
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["ID", "Direction", "Région", "Partis Politique", "Année ", "Statut d'existence"])
    conn.close()
    return df



