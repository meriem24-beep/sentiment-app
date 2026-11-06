# Fiche modèle : sentiment-app

## Identité du modèle

Le paquet sentiment-app version 0.6.0 utilise un modele de classification de sentiment basé sur TF-IDF et Logistic Regression. Le modèle a éte entraîné le 06/11/2026 avec scikit-learn 1.5.2 pour classer les avis en français selon leur polarité positive ou négative.

## Usage prévu

Ce modèle est destine à aider les équipes de relation client à analyser automatiqment les avis clients en français. Il permet de repérer les avis positifs et negatifs afin de faciliter leur tri et de prioriser les avis nécessitant une attention humaine.

## Usages exclus

Le modèle ne doit pas être utilisé pour prendre automatiquement des décisionde remboursement ou de sanction envers un client. Il ne doit pas non plus être utilisé pour des décisions médicales, juridiques ou financières, ni pour analyser des langues et des domaines qui ne sont pas représentés dans ses données d'entraînement.

## Données d'entraînement

Le modèle a été entraîné sur un jeu de démonstration contenant 290 avis en français, répartis entre 145 avis positifs et 145 avis négatifs. Le jeu comprend 232 avis d'entraînement et 58 avis de test. Les données concernent principalement des expériences de consommation et ne représentent pas nécessairement tous les secteurs, styles d'écriture ou profils de clients.

## Performances mesurées

Sur le jeu de test, le modèle obtient un F1 macro de 0.879, une accuracy de 0.8793 et un rappel des avis négatifs de 0.931. L'API utilise un seuil dabstention de 0.60 : les avis dont la confiance est insuffisante sont classés INDETERMINE et doivent être examinés par un humain. Sur le jeu d'or de 20 avis, 6 prédictions sont justes, 12 sont des abstentions et 2 sont des erreurs franches déclarées. Aucune erreur franche non déclarée n'a été observée.

## Limites connues

Le modèle peut rencontrer des difficultés avec les avis longs, les formulations ironiques et les changements de sentiment au cours d'une même phrase. L'analyse du TP2 montre qu'un avis contenant des éléments positifs et négatifs peut être mal classé. Le jeu d'or contient notamment deux erreurs franches connues sur des avis négatifs classés positifs. Le taux élevé d'abstention montre également que de nombreux avis nécessitent une vérification humaine.

## Biais mesurés

L'analyse du TP4 met en évidence des différences selon les caractéristiques linguistiques des avis. Les avis directs obtiennent une exactitude de 100 % sur 41 exemples, tandis que les avis contenant un retournement de sentiment obtiennent 58.8 % sur 17 exemples, avec 7 erreurs. Pour les avis longs, l'exactitude est de 74.1 % sur 27 exemples. Ces résultats indiquent une difficulté particulière avec les formulations complexes et les changements de sentiment.

## Explicabilité

L'analyse avec SHAP montre que certains terms contribuent fortement à la prédiction. Des expressions comme « impeccable », « livraison en avance » et « satisfait » favorisent la classe positive. Des termes comme « produit cassé », « arrivée » et « erronée » favorisent la classe négative. L'explication d'un avis contenant des éléments contradictoires montre que les contributions positives et négatives peuvent se compenser. Ces explications décrivent l'influence des termes sur le modèle, mais ne garantissent pas la justesse de sa décision.

## Conditions d'usage

Un humain doit vérifier tous les avis classés INDETERMINE ainsi que les avis associés à des décisions importantes pour le client. Il est recommandé de contrôler régulièrement un échantillon de prédictions positives et négatives et de surveiller les erreurs. Aucune décision ayant un impact important sur un client ne doit être prise uniquement sur la base de la prédiction du modèle.

## Maintenance

Le modèle doit être réentraîné lorsque de novelles données représentatives sont disponibles ou lorsque les performances diminuent. Le réentraînement et les tests doivent utiliser une version compatible et maîtrisée de scikit-learn, actuellement 1.5.2 dans l'environnement de référence. Le paquet permet de préciser le chemin du modèle avec la variable d'environnement SENTIMENT_MODELE. Après chaque réentraînement, les métriqus, les test et cette fiche doivent être mis à jour.