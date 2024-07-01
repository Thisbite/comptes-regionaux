def presentation():
    import streamlit as st



    st.markdown("""
    ### Présentation de l'application de saisie
    - **Application web et interactive**
    - **Application liée à une base de données Sqlite3**
    - **Langage de requête : SQL, [Python](https://colab.research.google.com/drive/1oBqwcSMb4YTrn0NFUiQzJCiZ65uIay_S?usp=sharing), R,Stata etc...**
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
    2. **Choisir la localité de la donnée**
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

    #Architecture des données
    st.header("Processus de conception du canevas Excel")
    st.markdown("""
      1. **Analyse du tableau Word**
      2. **Idenfication des variables pertinentes**
      3. **Liste des variables pertinentes**
      4. **Choix des variables à partir de la permanence d'un annuaire à un autre**
      5. **Transformation des noms des variables en des noms informatiques**
      6. **Création de la feuille Excel en portant en colonne le noms des variables**
      7. **Nomination de la feuille Excel par le nom du tableau transformé**
      
      """
                )
    st.markdown("""
        <style>
        .example-container {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .example-title {
            font-size: 24px;
            font-weight: bold;
            color: #333;
            margin-bottom: 20px;
        }
        .example-caption {
            font-size: 18px;
            font-weight: normal;
            color: #666;
            margin-top: 10px;
        }
        .example-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 80%;
            margin-top: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Créer le cadre de l'exemple
    st.markdown('<div class="example-container">', unsafe_allow_html=True)

    # Ajouter le contenu de l'exemple
    st.markdown('<div class="example-title">Exemple de transformation du tableau Word en canevas Excel</div>',
                unsafe_allow_html=True)
    st.write("Le tableau Word")
    st.image("nom_word.png", caption="Le tableau Word", use_column_width=True, output_format='auto')
    st.write("Résultat en canevas Excel")
    st.image("nom_excel.png", use_column_width=True, output_format='auto')

    # Fermer le cadre de l'exemple
    st.markdown('</div>', unsafe_allow_html=True)

    return

    # Lancer l'application avec: streamlit run app.py
