import sqlite3
import os
import shutil

# Chemin vers la base de données d'historique de Google Chrome
# Adapté à Windows, pourrait varier selon le système d'exploitation
# Assurez-vous de changer ce chemin selon votre configuration
chrome_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\History'

# Copier la base de données pour éviter les problèmes de verrouillage
try:
    shutil.copyfile(chrome_path, "./History")
    conn = sqlite3.connect("./History")
    cursor = conn.cursor()

    # Sélectionner les informations d'historique à partir de la table 'urls'
    cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls")
    results = cursor.fetchall()

    # Écrire les résultats dans un fichier texte
    with open('browser_history.txt', 'w', encoding='utf-8') as file:
        file.write("Historique du navigateur (Google Chrome):\n")
        file.write("URL | Titre | Nombre de visites | Dernière visite\n")
        for row in results:
            url = row[0]
            title = row[1]
            visit_count = row[2]
            last_visit_time = row[3]
            file.write(f"{url} | {title} | {visit_count} | {last_visit_time}\n")

    print("Historique du navigateur enregistré dans browser_history.txt")

except sqlite3.Error as e:
    print(f"Erreur SQLite : {e}")

finally:
    if conn:
        conn.close()
    if os.path.exists("./History"):
        os.remove("./History")  # Supprimer la copie de la base de données après utilisation
