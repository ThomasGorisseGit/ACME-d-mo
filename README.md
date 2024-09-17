
# ACME Démo

## Introduction
ACME est une implémentation du standard oneM2M en python. Il est utilisable comme MiddleWare.
Dans cette petite demonstration, il fait le lien entre les requêtes envoyés par un Sensor et un Server contenant une API.

## Sommaire 
  - [ACME](#acme)
    - [Avec Docker](#avec-docker)
    - [Manuellement](#manuellement)
  - [Installation](#installation)
  - [Démarrage](#démarrage)

## ACME
### Avec Docker

Vous pouvez ensuite lancer **ACME** en utilisant l'image docker :
```bash
docker run -it -p 8080:8080 --rm --name acme-onem2m-cse ankraft/acme-onem2m-cse
```
### Manuellement
Installation de ACME via la  [Documentation](https://acmecse.net/setup/Installation/) 

## Installation 

Avant de démarrer la démo, veuillez installer les dépendances nécessaires :
- Python 3.11 ou +
- ACME (soit via Docker soit Manuellement)

Une fois que ces dépendances sont installées, vous pouvez démarrer la démo en suivant les étapes suivantes :


**Pour windows :**
``` 
python -m venv myenv && myenv\Scripts\activate
pip install -r requirements.txt
```
**Pour Linux et MacOS :** 
```
python3 -m venv myenv && source myenv/bin/activate
pip install -r requirements.txt
```

## Démarrage
L'application se décrit en 2 composants: 
- Le serveur qui contient une API qui ne fait que stocker en mémoire les données reçues
- Une simulation qui lance 2 faux capteurs qui produisent des données aléatoires

Pour démarrer l'application, vous devez lancer ACME, puis les 2 composants en parallèle.

**Server:**
```
python -m Server
``` 
**Sensor:**
```
python -m Sensor
```
