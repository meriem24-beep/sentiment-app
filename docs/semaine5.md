# Semaine 5 : l'interface, notes du binôme

> Trois questions, quelques phrases chacune. Répondez avec ce que vous avez observé.

## 1. Pourquoi l'interface n'importe-t-elle jamais `predict()` ni le fichier `.joblib` ?

Linterface Streamlit ne charge pas directement le modèle et n'effectue pas elle-même les prédictions. Elle communique avec le bckend FastAPI à travers le module ui/client.py, qui envoie les requêtes HTTP à l'API. Cette séparation permet de centraliser la logique de prédiction dans le backend, d'éviter la dupplication du code et de faciliter la maintenance de l'application.

## 2. Que montre l'interface quand le modèle hésite, et pourquoi est-ce mieux qu'un verdict forcé ?

Lorsque le modèle hésite, l'interface afiche le verdict « Je ne sais pas : à faire vérifier par un humain », accompagné d'un score de confiance de 52 % et d'un message indiquant que la confiance est inférieure au seuil d'abstention. Cette solution est préférable à un verdict forcé, car elle évite de présenter une prédiction incertaine comme une réponse fiable. Elle permet ainsi de confier les avis ambigus à une personne pour vérification.

## 3. Que voit l'utilisateur quand l'API tombe ? Et le fichier `data/avis_exemple.csv` : combien d'avis partent vers un humain ?

Lorsque l'API devient inaccessible, l'interface affiche un message d'erreur indiquant que le backend doit être démaré. Pour le fichier data/avis_exemple.csv, six avis sont analysés : trois sont classés positifs, deux négatifs et un indéterminé. Cet avis nésesite une vérification humaine.
