# Semaine 4 : tests approfondis et qualité, notes du binôme

## 1. Couverture

- **Avant (étape A) :** [À compléter avec le pourcentage initial] ; lignes jamais exécutées : [à compléter].
- **Comportements non vérifiés :** [Préciser les comportements qui n'étaient couverts par aucun test].
- **Après (étape D) :** 97,50 % de couverture ; lignes exclues de la mesure : [à compléter selon le rapport de couverture].

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| [Défaut constaté pendant les tests] | [Test correspondant] | [Correction effectuée] |
| [Autre défaut, si applicable] | [Test correspondant] | [Correction effectuée] |

## 3. Seuil d'abstention

- **Points de la courbe** (`python src/courbe_seuil.py`) : [Ajouter deux ou trois points réels].
- **Seuil retenu :** [Valeur réelle] ; **part des avis envoyés à un humain :** [Pourcentage réel].
- **Justification :** [Expliquer le compromis entre les prédictions automatiques et les avis nécessitant une vérification humaine].

## 4. Jeu d'or

- **Bilan** (`python src/bilan_jeu_or.py`) : justes [nombre], abstentions [nombre], erreurs franches déclarées [nombre].
- **Interprétation :** [Expliquer ce que les résultats indiquent sur la fiabilité du modèle et ses limites].

## 5. Outils statiques

- **Remarques au départ :** Ruff [résultat initial] ; Mypy [résultat initial].
- **Défauts signalés :** [Nombre de défauts de la partie 2 détectés par Ruff et Mypy].
- **Conclusion :** Les outils statiques permettent de détecter certains problèmes de qualité du code avant l'exécution des tests, mais ne remplacent pas les tests fonctionnels.
