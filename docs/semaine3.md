# TP3 — Interface Streamlit et analyse des sentiments

## 1. Objectif

L'objectif de TP3 est de développer et tester une interface Streamlit permettant de prédire le sentiment d'un avis client et d'analyser plusieurs avis à partir d'un fichier CSV.

## 2. Tests de l'interface

L'application Streamlit a été lancée avec la commande `streamlit run ui/app.py` et accessible à l'adresse locale `http://localhost:8501`.

Les tests réalisés sont les suivants :

- **Avis positif :** la prédiction affichée était positive.
- **Avis négatif :** la prédiction affichée était négative.
- **Import CSV :** le fichier `data/demo_reviews.csv` a été importé et les résultats d'analyse ont été affichés.

## 3. Seuil de confiance

Le seuil de confiance utilisé est de 0,60. Une prédiction dont la confiance est inférieure à ce seuil doit être signalée pour une vérification humaine, selon le fonctionnement prévu par l'application.

Ce mécanisme permet de limiter les décisions automatiques lorsque le modèle est peu sûr de sa prédiction.

## 4. Tests de l’interface

J’ai testé l’application Streamlit avec plusieurs avis clients. Les résultats des prédictions sont affichés dans l’interface.

### Test 1 : avis positif

![Test d’un avis positif](images/devia/Screenshot(820).png)

### Test 2 : autre avis positif

![Résultat d’un avis positif](images/devia/Screenshot(822).png)

### Test 3 : avis négatif

![Test d’un avis négatif](images/devia/Screenshot(821).png)

### Test 4 : avis client

![Résultat d’un avis client](images/devia/Screenshot(819).png)

### Test 5 : analyse des données CSV

![Résultats de l’analyse CSV](images/devia/Screenshot(823).png)

Ces captures d’écran montrent l’interface de l’application, les prédictions de sentiment et les résultats de l’analyse CSV.

## 5. Tests automatisés

La commande `python -m pytest -q` a été exécutée.

![Résultat de la commande `python -m pytest -q`](images/devia/image.png)

Résultat : **45 tests réussis, aucun échec**.

## 6. Conclusion

L'application Streamlit fonctionne pour les tests individuels et l'importation d'un fichier CSV. Les tests automatisés passent tous. Le seuil de confiance permet d'identifier les prédictions qui nécessitent une vérification humaine, conformément à la logique de l'application.
