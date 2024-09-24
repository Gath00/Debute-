import webbrowser
import os
import datetime


temps = datetime.datetime.now()

#info jour/heure/année/seconde/minute

jour = temps.day
heure = temps.hour
annee = temps.year
seconde = temps.second
minute = temps.minute
mois = temps.month

#création d'une fonction d'ouverture du navigateur

def open_browser(url):
    webbrowser.open(url)

# Exemple d'utilisation
avis = input("Entrez le nom du site: ")
Sites = ["youtube",
 "gmail",
 "google",
 "fitgirl-repack",
 ]

try:
    if avis.lower() in Sites:
        open_browser("http://www." + avis + ".com")
        
    elif avis.lower() not in Sites:
        open_browser("http://www." + avis + ".com")
        with open("sites_visités.txt", "a") as site:
            site.write(f"Visite : {avis} |heure: {str(heure)} : {str(minute)}  : {str(seconde)} |Date: {str(jour)}/{str(mois)}/{str(annee)}\n")
            
except Exception:
    print("Les sites entrés ne sont pas valides.\n Veuillez réessayer, s'il vous plaît.!!")
    print("Le navigateur va se lancer pour vous permettre d'entrer votre site...")
    open_browser("http://www." + Sites[2] + ".com")
    