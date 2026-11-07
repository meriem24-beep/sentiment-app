# Semaine 6 : le paquet — travail individuel



## 1. Pourquoi le modèle n'est-il pas dans la roue ? Comment le paquet le trouve-t-il ?

Le modele entraîné (`sentiment.joblib`) nest pas inclus dans la roue afin de séparer le code de l'application de l'artefact généré pendant l'entraînment. Cela évite également d'imposer le stockage d'un modèle volumineux dans chaque instalation du paquet.

Le paquet recherche le modèle à l'emplacement `models/sentiment.joblib` par défaut, relativement à la racine du projet. Lorsque le paquet est installé indépendamment du dépôt, la variable d'environnement `SENTIMENT_MODELE` permet de préciser le chemin du fichier du modèle.

## 2. Qu'est-ce qui a changé dans api/model.py quand predict() est entré dans le paquet, et pourquoi est-ce mieux ?

La fonction de prédiction et le chargement du modèle ont été déplacés dans `sentiment_app/predict.py`. Le fichier `api/model.py` importe désormais ces fonctions depuis le paquet au lieu de maintenir une deuxième implémentation.

Cette organisation évite la duplication du code, facilite sa maintenance et permet de réutiliser la même logique de prédiction depuis l'API et la ligne de commande. Elle rend également le paquet plus indépendant de l'organisation interne du dépôt.

## 3. La roue installée hors du dépôt : qu'a-t-il fallu lui fournir, et pourquoi scikit-learn est-il épinglé dans pyproject.toml ?

Lors du test d'installation dans un environnement virtuel indépendant, il a fallu installer la roue, installer les dépendances nécessaires et fournir le chemin du modèle avec la variable `SENTIMENT_MODELE`, puisque le fichier du modèle n'est pas inclus dans la roue.

La vwrsion de scikit-learn est limite dans `pyproject.toml` à la série 1.5 (`>=1.5,<1.6`) afin de garantir la compatibilité avec le modèle sauvegardé. Les objets sérialisés avec joblib peuvent dépendre de la version de scikit-learn utilisée lors de leur entraînement. Il est donc important de conserver une version compatible pour éviter les erreurs au chargement.