def presentation():
    import streamlit as st



    st.markdown("""
    ### Présentation de l'application de saisie
    - **Application web et interactive**
    - **Application liée à une base de données Sqlite3**
    - **Langage de requête : SQL, [Python](https://colab.research.google.com/drive/1oBqwcSMb4YTrn0NFUiQzJCiZ65uIay_S?hl=fr#scrollTo=OplM7o6w0vdS), R,Stata etc...**
    """)

    # Processus de saisie
    st.header("Processus de saisie")
    st.markdown("""
    1. **Avoir le document Word de l'annuaire statistique**
    2. **Avoir le canevas Excel**
    3. **Identifier le tableau à saisie**
    4. **Identifier la feuille Excel correspondante**
    5. **Copier coller les données de Word vers Excel**
    6. **Importer le fichier Excel sur la plateforme**
    7. **Sélectionner la feuille dans la liste déroulante des feuilles Excel**
    8. **Cliquer sur "Enregistrement de données"**
    """)

    # Processus de téléchargement des données
    st.header("Processus de téléchargement des données")
    st.markdown("""
    1. **Cocher "obtenir les données"**
    2. **Choisir les références de la donnée**
    3. **Cliquer sur "Rechercher la donnée" et télécharger le résultat**
    """)

    # Processus de modification
    st.header("Processus de modification")
    st.markdown("""
    1. **Entamer le processus d'obtenir une donnée et regarder dans la colonne "ID"**
        - **Ce numéro correspond à la ligne**
    2. **Cocher "Modifier une ligne"**
    3. **Rechercher le numéro "ID" dans la liste déroulante**
    4. **Faire la modification**
    """)
    return

    # Lancer l'application avec: streamlit run app.py
