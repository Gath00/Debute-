import webbrowser
import datetime
import os
import shutil
import sqlite3
import requests
from verif_url import is_valid_url, urls


date_now = datetime.datetime.now()
HEADERS ={ "User_Agent": "Mozilla/5.0 (Macintosh; Intel MacOS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" }

def ouverture_nav(url):
    webbrowser.open(url)

def historique_nav():
    chrome_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\History'
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
            
    return file
    

while True:
    print("Bienvenue dans le menu principal !\n")
    
    print("Faites un choix parmi ceux qui sont proposés : ")
    print("---"*4)
    
    choix = input("Choisissez parmi :\n(1) : Ouvrir le navigateur: \n(2) : Voir l'historique de navigation: \n(3) : créer une page web et l'ouvrir: \nRéponse: ")
    
    if choix.lower() == "1" or choix.lower() == "ouvrir le navigateur":
        bas = input("Ouvrir le navigateur de base : Google (yes/no) : ")
        
        if bas.lower() == "yes":
            ouverture_nav("https://www.google.com")
            break
        
        elif bas.lower() == 'no':
            choix_1 = input("Entrez le nom du site: ")
            ouverture_nav("http:/www." + choix_1 + ".com")
            
            with open("cache_nav.txt", "a") as cache:
                cache.write("--------------------"*4 + "\n")
                
                cache.write(f"{date_now} : {choix_1}\n")
                
                cache.write("--------------------"*4 + "\n")
            
        else:
            print("Erreur")
    
    elif choix.lower() == "2" or choix.lower() == "historique":
        historique = input("Voulez-vous voir l'historique de navigation ?  (yes/no)")
        
        if historique.lower() == "yes":
            historique_nav()
            print("L'historique a été crée: ouvre le fichier texte(browser_history.txt) pour le consulter")
            print("Bonne visite")
            
        elif historique.lower()=="no":
            try:
                match input("Voulez-vous scrapper ou pas ?(yes/no) : "):
                    case "yes":
                        print("Scrapper en cours...")
                        lien = input("Entrez l'url correcte du site: ")
                        match lien:
                            case "https://www.google.com/":
                                print("On ne vous autorise pas à récupérer le contenu de la page")
                            case "":
                                print("Scrapper en cours...\nOups vous n'avez entré aucune donnée!")
                                break
                            
                        if is_valid_url(lien):
                            print("Scrapper en cours...")
                            reponse = requests.get(lien, headers=HEADERS)
                            reponse.encoding = reponse.apparent_encoding
                                
                            if reponse.status_code==200:
                                html = reponse.text
                                with open("scrap.html", "w") as file:
                                    file.write(html)
                                        
                            else:
                                print("Erreur 404")
                                                      
            except Exception:
                print("Erreur")
                
    elif choix.lower() == "3" or choix.lower()=="créer une page web":
        print("Site en cours de création: Veuillez patienter")
        
                    