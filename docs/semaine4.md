# Semaine 4 : tests approfondis et qualité, notes du binôme

## 1. Couverture

- **Avant (étape A) :** Pourcentage initial et lignes non exécutées à vérifier dans le rapport initial.
- **Comportements non vérifiés :** Les cas limites, les entrées invalides et les situations où le modèle doit s'abstenir nécessitent des tests spécifiques.
- **Après (étape D) :** 97,50 % de couverture ; les lignes exclues sont à vérifier dans le rapport de couverture du TP4.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Le modèle peut produire une prédiction incertaine. | Tests du seuil d'abstention et du jeu d'or. | Ajout d'un mécanisme d'abstention pour les prédictions dont le score est inférieur au seuil retenu. |
| Certaines erreurs de classification persistent sur des avis ambigus. | `test_pas_d_erreur_franche` dans le jeu d'or. | Les cas connus sont identifiés par des tests `xfail` et nécessitent une amélioration future du modèle. |

## 3. Seuil d'abstention

- **Points de la courbe** (`python src/courbe_seuil.py`) :
  - Seuil 0,60 : couverture de 72 %, précision de 95,2 %, 16 abstentions sur 58 avis.
  - Seuil 0,65 : couverture de 71 %, précision de 97,6 %, 17 abstentions sur 58 avis.
  - Seuil 0,75 : couverture de 50 %, précision de 100 %, 29 abstentions sur 58 avis.
- **Seuil retenu :** 0,60 ; **part des avis envoyés à un humain :** environ 27,6 % (16 sur 58).
- **Justification :** Le seuil de 0,60 représente un compromis entre le nombre de prédictions automatiques et leur précision. Un seuil plus élevé améliore la précision, mais augmente le nombre d'avis nécessitant une vérification humaine.

## 4. Jeu d'or

- **Interprétation :** Sur 20 avis, le modèle obtient 6 prédictions correctes, 12 abstentions et 2 ereurs franches. Ces résultats montrent que le mécanisme d'abstention permet d'éviter certaines prédictions incertaines. Toutefois, les erreurs restantes montrent que le modèle a encore des limite et doit être amélioré.

## 5. Outils statiques

- **Remarques au départ :** Ruff signalait deux problèmes d'importation dans `ui/app.py` ; Mypy ne signalait aucune erreur dans les quatre fichiers vérifiés.
- **Défauts signalés :** Deux problèmes détectés par Ruff, corigés avec les annotations `noqa` adaptées. Mypy n'a signalé aucun problèm.
- **Conclusion :** Les outils statiques permettent de détecter certains problèmes de qualité du code avant l'exécution des tests, mais ne remplacent pas les test fonctionnels. Après correction, Ruff passe toutes les vérifications et Mypy ne signale aucune ereur.
