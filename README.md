# WigleCheck - Recherche d'adresse MAC sur WiGLE

WigleCheck est un outil simple avec une interface graphique (créé en Python avec Tkinter) pour interroger l'API WiGLE. Il permet de retrouver des informations de géolocalisation pour une adresse MAC Wi-Fi ou Bluetooth donnée.



## Fonctionnalités

* Interface graphique.
* Recherche pour les adresses MAC Wi-Fi et Bluetooth.
* Formatage automatique de l'adresse MAC saisie.
* Affichage clair des informations retournées par l'API WiGLE (coordonnées, adresse, etc.).

## Installation et Configuration

Suivez ces étapes pour rendre le script fonctionnel.

### 1. Clonez le dépôt

Récupérez les fichiers du projet sur votre machine locale :
```bash
git clone [https://github.com/nicolasnt3-a11y/wiglecheck.git](https://github.com/nicolasnt3-a11y/wiglecheck.git)
cd wiglecheck
```

### 2. Installez les dépendances

[cite_start]Ce projet nécessite la bibliothèque `requests`[cite: 1]. Installez-la via pip :
```bash
pip install -r requirements.txt
```

### 3. Configurez vos identifiants API WiGLE

**Cette étape est obligatoire.** Vous devez ajouter vos propres identifiants API WiGLE directement dans le code pour que le script puisse s'authentifier.

1.  Ouvrez le fichier `main.py` avec un éditeur de texte.
2.  Repérez les lignes suivantes au début du fichier :
    ```python
    # ---- CONFIGURATION ----
    WIGLE_WIFI_URL = "[https://api.wigle.net/api/v2/network/search](https://api.wigle.net/api/v2/network/search)"
    WIGLE_BLUETOOTH_URL = "[https://api.wigle.net/api/v2/bluetooth/search](https://api.wigle.net/api/v2/bluetooth/search)"

    USERNAME = ""  # <-- AJOUTEZ VOTRE USERNAME ICI
    PASSWORD = ""  # <-- AJOUTEZ VOTRE PASSWORD ICI
    ```
3.  Insérez votre **API Name** et votre **API Token** de WiGLE entre les guillemets.



## Utilisation

Une fois la configuration terminée, lancez l'application avec la commande suivante :

```bash
python main.py
```

Entrez une adresse MAC, choisissez le type de réseau et cliquez sur "Rechercher".

## Licence

Ce projet est distribué sans licence. Vous êtes libre de l'utiliser, de le modifier et de le distribuer.