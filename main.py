import importlib

def import_or_install(package):
    try:
        importlib.import_module(package)
        print(f"{package} déjà installé.")
    except ImportError:
        print(f"{package} non trouvé. Installation en cours...")
        import subprocess
        subprocess.check_call(['pip', 'install', package])

# Exemple d'utilisation :
packages_to_install = ['requests', 'beautifulsoup4', 'numpy', 'pywifi', 'django', 'matplotlib']

print(f"Installer les packages : {packages_to_install}")

try:
    match input("Oui ou Non: "):
        case 'Oui':
            for package in packages_to_install:
                import_or_install(package)
            
        case 'Non':
            librairie = input('Entrez le nom de la librairie ou du package: ')
            for package in librairie:
                import_or_install(librairie)
            
except Exception:
    print('Erreur')

#for package in packages_to_install:
    #import_or_install(package)
