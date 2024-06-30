install.packages("DBI")
install.packages("RSQLite")
library(DBI)
library(RSQLite)
#Mon environnement de travail
#"/Users/mac/Desktop/Projet Konhin Yamousso/GithubProjet/streamlit-test-v2/streamlitV3"
# Mon chemin d'accès
db_path1 <- "db_annuaire_stat.db"
db_path<-"comptes_regionaux.db"

# Établir la connexion
con <- dbConnect(RSQLite::SQLite(), dbname = db_path)
#Afficher la liste des tableaux ou tables
tables <- dbListTables(con)
print(tables)

# Exploiter une table ou un tableau
table_name <- "tab2113_fait_civi_naiss"  
df <- dbReadTable(con, table_name)
# Afficher les premières lignes de la table
print(head(df))  

#Vue simple
View(df)
# Obtenir la liste des noms des colonnes de la table
columns <- dbListFields(con, table_name)
print(columns)
# Transformer ma variable
df$nbre_naiss_centr_princ <- as.numeric(df$nbre_naiss_centr_princ)
summary(df)
