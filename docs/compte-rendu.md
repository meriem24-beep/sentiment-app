# Compte rendu global des TP1 à TP3

**Projet :** Classification automatique des avis clients en français
**Membres du trinôme :**
- KHOBBAZ Meriem — [@meriem24-beep]
- AMINE Doha — [@dohq25-beeep]
- OUBENADI Aya — [@ayaoubenadi563]

**Dépôt GitHub :** https://github.com/meriem24-beep/sentiment-app
**Date :** 27/10/2026

## 1. Le besoin et son cadrage

Les entreprises reçoivent de nombreux avis clients après l’achat d’un produit ou l’utilisation d’un service. La lecture manuelle de tous ces avis peut demander baucoup de temps, notamment lorsque les commentaires sont nombreux. Il est donc utile de disposer d’un outil qui aide à repérer rapidement les avis positifs et négatifs afin de mieux organiser leur traitement.

L’objectif de ce projet est de développer une application capable de classifier automatiquement un avis rédigé en françai#. Le modèle doit attribuer à chaque texte une classe positive ou négative. L’application permet également de traiter un fichier CSV contenant plusieurs avis et d’afficher une synthèse des résultats. Elle constitue une aide à l’analyse, et non un remplacement complet de la décision humaine.

Pour ce besoin, nous avons retenu une approche d’apprentissage supervisé. Cette méthode est adaptée lorsque des exemples de textes sont déjà associés à des étiquettes connues. Le modèle apprend les régularités présentes dans ces exemples, puis les utilise pour prédire la classe de nouveaux avis.

Notre choix repose sur quatre critères.

**a) Disponibilité des données étiquetées.** Le projet utilise un jeu de démonstration équilibré et le jeu de données Allociné. Ces données permettent d’entraîner le modèle sur des avis associés à une polarité. Les données de démonstration sont utiles pour tester le fonctionnement du projet, tandis que le jeu Allociné permet une évaluation plus importante.

**b) Vérifiabilité.** Les performances peuvent être mesurées sur des données de test séparées des données d’entraînement. Nous utilisons notamment le F1 macro, l’accuracy, le rappel des avis négatifs et la matrice de confusion. Ces mesures permettent de dépasser une simple impression obtenue en testant quelques phrases dans l’interface.

**c) Coût par requête.** Une fois entraîné, le modèle peut prédire la polarité d’un texte sans nécessiter un nouvel entraînement pour chaque avis. Cette propriété permet de traiter plusieurs commentaires dans un fichier CSV. Le coût réel dépend toutefois de l’environnement d’exécution et du volume de données.

**d) Conséquence d’une erreur.** Un avis négatif classé à tort comme positif peut ne pas être transmis assez rapidement au service client. À l’inverse, un avis positif classé comme négatif peut mobiliser inutilement un agent. Les erreurs ne sont donc pas toutes équivalentes du point de vue métier. Pour cette raison, l’application présente également une indication d’incertitude afin de faciliter une vérification humaine lorsque la confiance du modèle est insuffisante.

## 2. L’architecture du dépôt

Le dépôt GitHub organise le projet en plusieurs répertoires, chacun ayant un rôle précis.

- `src/` contient les scripts liés à la préparation des données, à l’entraînement et à l’évaluation du modèle.
- `data/` contient les données utilisées pour les expériences et les tests.
- `models/` contient les résultats de mesure et les artefacts du modèle.
- `tests/` regroupe les tests automatisés.
- `ui/` contient le code de l’application Streamlit et les fonctions utilisées par l’interface.
- `docs/` contient les documents de suivi et le compte rendu.

Cette organisation sépare le traitement des données, la modélisation, l’interface et la documentation. Elle facilite la recherche des fichier et la maintenance du projet.

Les fichiers nécessaires pour comprendre et reproduire le travail ne sont pas tous de même nature. Le fichier `models/metrics.json` est suivi par Git, car il conserve les résultats mesurés, notamment la taille des jeux d’entraînement et de test, le F1 macro, l’accuracy et le rappel des avis négatifs. Il permet de retrouver les résultats sans devoir se fier uniquement à des notes personnelles.

À l’inverse, le fichier `models/sentiment.joblib` est un artefact généré par l’entraînement et n’a pas vocation à être versionné dans ce dépôt. Le modèle peut être volumineux et doit être régénéré à partir du code et des données appropriés. Cette séparation limite la taille du dépôt et évite de suivre inutilement des fichiers générés. Les données et artefacts exclus doivent néanmoins pouvoir être recréés ou obtenus selon les instructions du projet.

Le contrôle de version permet aussi de conserver l’historique des modifications. Les tests automatisés apportent une vérification supplémentaire : ils permettent de détecter des régressions lorsqu’une fonction est modifiée. Enfin, le dépôt contient les instructions nécessaires pour exécuter le projet et documenter les étapes réalisées.

## 3. Le modèle et ses résultats

Le projet comprend deux expériences principales : une expérience sur les données de démonstration et une autre sur le jeu de données Allociné.

### 3.1. Expérience sur les données de démonstration

Le jeu de démonstration contient 290 avis : 145 positifs et 145 négatifs. L’équilibre entre les deux classes facilite une première évaluation, car aucune classe n’est majoritaire dans ce jeu.

Le modèle est évalué sur un ensemble de test distinct des données utilisées pour l’entraînement. L’expérience utilise 232 avis pour l’entraînement et 58 pour le test. La séparation est réalisée avec un état aléatoire fixé afin de rendre l’expérience plus reproductible.

Le pipeline transforme les textes en caractéristiques numériques à l’aide d’une représentation fondée sur les mots, puis entraîne un classificateur. Cette représentation permet à un algorithme classique d’apprentissage automatique de travailler sur des textes. Elle reste cependant limitée : elle ne comprend pas nécessairement le contexte, l’ironie ou la relation entre toutes les parties d’une phrase.

Sur les 58 avis de test, le modèle obtient un F1 macro de 0,879, soit environ 87,9 %. L’accuracy calculée à partir de la matrice de confusion est également de 51/58, soit environ 87,9 %.

La matrice de confusion est la suivante :

| Classe réelle | Prédit négatif | Prédit positif |
|---|---:|---:|
| Négatif | 27 | 2 |
| Positif | 5 | 24 |

Pour les avis réellement négatifs, 27 sont correctement reconnus et 2 sont classés à tort comme positifs. Le rappel de la classe négative est donc de 27/29, soit environ 93,1 %. Pour les avis réellement positifs, 24 sont correctement reconnus et 5 sont classés à tort comme négatifs. Au total, le modèle commet 7 erreurs sur les 58 avis de test.

Cees résultats montrent que le modèle fonctionne correctement sur ce jeu de démonstration, mais ils ne suffisent pas à garantir les mêmes performances sur tous les avis réels. Le jeu est relativement petit et ne représente pas nécessairement toute la diversité des formulations utilisées par les clients.

### 3.2. Expérience sur Allociné

Une seconde expérience a été menée sur le jeu de données Allociné. Elle utilise 20 000 avis, répartis en 16 000 avis d’entraînement et 4 000 avis de test. Le vocabulaire obtenu contient 149 529 caractéristiques.

Les mesures enregistrées dans `models/metrics.json` sont les suivantes :

| Indicateur | Résultat |
|---|---:|
| Nombre d’avis d’entraînement | 16 000 |
| Nombre d’avis de test | 4 000 |
| F1 macro | 0,9205 |
| Accuracy | 0,9205 |
| Rappel des avis négatifs | 0,9113 |

Le F1 macro de 0,9205 indique un bon compromis entre précision et rappel calculé séparément pour les classes avant leur moyenne. L’accuracy de 0,9205 signifie que 92,05 % des avis du test sont correctement classés. Le rappel négatif de 0,9113 signifie que le modèle retrouve environ 91,13 % des avis réellement négatifs.

Le rappel négatif est particulièrement intéressant pour notre besoin, car il mesure la capacité à détecter les commentaires défavorables. Il reste néanmoins inférieur à 100 % : certains avis négatifs peuvent encore être manqués.

Les résultats sur Allociné sont supérieurs à ceux de la petite expérience de démonstration. Le nombre plus important d’exemples fournit au modèle davantage de données d’apprentissage. Cependant, les deux expériences ne doivent pas être comparées comme si elles portaient exactement sur la même distribution de textes. Les résultats dépendent des données utilisées, de leur diversité et de la répartition entre entraînement et test.

## 4. L’analyse des erreurs

Une bonne accuracy ne signifie pas que toutes les prédictions sont correctes. L’analyse des erreurs permet de comprendre les limites du modèle et d’identifier les améliorations possibles.

Sur les données de démonstration, deux avis réellement négatifs sont classés comme positifs. Ces erreurs sont importantes pour le cas d’usage, car elles peuvent conduire à sous-estimer l’insatisfaction d’un client. Cinq avis positifs sont, à l’inverse, classés comme négatifs. Cette seconde catégorie d’erreurs peut entraîner une vérification inutile par un agent.

Un exemple représentatif est l’avis suivant : « Le service était impeccable au début, mais finalement le produit est cassé et je suis très déçu. » Cet avis commence par une expression positive, puis présente un problème et une conclusion négative. Le modèle prédit une classe négative avec une confiance de 73 %.

Cet exemple montre que les avis peuvent contenir plusieurs signaux de polarité. Une représentation basée sur les mots peut reconnaître certains termes associés à une opinion, mais elle ne comprend pas toujours parfaitement leur ordre, les négations, les changements de ton ou le contexte. Le résultat dépend également des exemples présents dans les données d’entraînement.

Une première amélioration serait d’enrichir les données avec davantage d’avis variés, notamment des commentaires mixtes, ironiques ou contenant des formulations moins courantes. Une deuxième possibilité serait de comparer différentes représentations du texte et différents classificateurs. Un modèle contextuel pourrait être étudié dans une expérience ultérieure, à condition de mesurer son gain réel et son coût supplémentaire.

Enfin, l’analyse devrait être réalisée sur les erreurs des deux classes et pas uniquement sur les avis négatifs. L’objectif est de comprendre les erreurs récurrentes et de déterminer lesquelles ont le plus de conséquences dans l’utilisation de l’application.

## 5. L’interface et le seuil d’incertitude

L’interface a été développée avec Streamlit. Elle comprend trois onglets : **Un avis**, **Un fichier CSV** et **Comment ça marche**.

Le premier onglet permet de saisir un avis et d’obtenir une prédiction positive ou négative avec une indication de confiance. Le deuxième permet d’importer un fichier CSV et d’afficher une synthèse des prédictions, une distribution des classes, un tableau des résultats et une possibilité de téléchargement. Le troisième présente le fonctionnement général de l’outil.

Le traitement par fichier permet de passer d’une analyse individuelle à une utilisstion sur un ensemble d’avis. La distribution des prédictions aide à repérer la part d’avis négatifs détectés. Elle doit toutefois être interprétée avec prudence : une prédiction du modèle n’est pas nécessairement la vraie étiquette de l’avis. Pour calculer une performance réelle, il faut comparer les prédictions à des étiquettes de référence disponibles.

L’application utilise le seuil `SEUIL_INCERTITUDE = 0.60`. Lorsque la confiance de la prédiction est inférieure à ce seuil, l’avis est signalé « à vérifier ». L’objectif est de transmettre à un humain les cas pour lesquels le modèle est moins sûr de sa décision.

Lors des essais manuels, l’avis « Excellent produit, qualité parfaite, livraison rapide et service impeccable. Je suis très satisfait. » a été classé positif avec une confiance de 82 %. L’avis « Produit horrible, mauvaise qualité, livraison très lente. Je suis extrêmement déçu et je ne recommande pas du tout. » a été classé négatif avec une confiance de 77 %. L’avis mixte présenté dans la section précédente a été classé négatif avec une confiance de 73 %. Aucun de ces trois exemples n’a été signalé « à vérifier », car leurs confiances dépassaient 60 %.

Le nombre exact d’avis du jeu de démonstration signalés « à vérifier » doit être calculé à partir des prédictions sur ce jeu. Il ne figure pas dans `models/metrics.json`, qui conserve les métriques globales du modèle. **Cette valeur doit être ajoutée après calcul avant la remise finale.** Il ne serait pas rigoureux de déduire ce nombre à partir des seuls trois exemples manuels.

Le seuil représente un compromis métier. Avec un seuil plus élevé, davantage d’avis risquent d’être envoyés à un agent, ce qui peut augmenter le travail de vérification mais aussi permettre de cntrôler plus de cas incertains. Avec un seuil plus faible, moins d’avis sont transmis, ce qui économise du temps mais peut laisser passer des prédictions peu fiables. Le meilleur seuil dépend donc du coût d’une erreur et de la capacité des agents à traiter les avis signalés.

## 6. Ce qui a échoué et les limites rencontrées

Le développement a demandé de mettre en place un environnement Python cohérent, d’installer les dépendances nécessaires et de vérifier la disponibilité du modèle utilisé par l’application. Ces étapes sont indispensables pour reproduire l’exécution sur une autre machine, mais elles peuvent prendre du temps lorsque l’environnement n’est pas encore configuré.

Une autre difficulté concerne la nature des avis. Les phrases très positives ou très négatives sont généralement plus simples à classer que les avis mixtes, les commentaires ambigus ou ceux dans lesquels une expression positive est suivie d’un prooblème. Les erreurs observées rappellent qu’un classificateur de sentiment ne comprend pas nécessairement toutes les nuances du langage.

Le projet distingue également les tests automatisés et les essais manuels. Les tests automatisés vérifient les comportements prévus par le code, tandis que les essais manuels permettent d’observer l’application dans des situations concrètes. Les deux sont nécessaires : une application peut réussir ses tests tout en produisant des prédictions imparfaites sur certains textes.

La validation automatisée a été exécutée avec `python -m pytest -q` et a donné **45 tests réussis** lors de la dernière vérification. Ce résultat confirme que les tests du projet passent dans l’environnement utilisé. Il ne constitue toutefois pas une preuve que toutes les prédictions sonte correctes, ni que le logiciel est exempt de tout défaut.

## 7. Ce que nous ferions autrement

Pour une prochaine version, nous commencerions par définir plus précisément les critères d’évaluation associés au besoin métier. En particulier, nous suivrions le rappel des avis négatifs et le nombre d’avis envoyés à la vérification humaine, plutôt que de nous limiter à l’accuracy globale.

Nous comparerions plusieurs seuils d’incertitude sur un jeu de validation séparé. Pour chacun, nous mesurerions le nombre d’avis à vérifier et les erreurs restantes. Cette comparaison permettrait de choisir un seuil sur la base de résultats observables et du temps disponible pour les agents.

Nous élargirions également les tests à des avis mixtes, à des négations, à des formulations ironiques et à des textes très courts. Une analyse qualitative des erreurs aiderait à déterminer si les problèmes viennent principalement du vocabulaire, du manque de données ou des limites de la représentation utilisée.

Enfin, nous améliorerions la documentation de reproduction en indiquant clairement les commandes d’installation, d’entraînement, d’évaluation et de lancement de l’interface. Les métriques seraient conservées dans un fichier versionné, tandis que les artefacts générés seraient gérés séparément. Cette organisation rendrait les résultats plus faciles à vérifier et à reproduire.

## 8. Répartition du travail

| Membre | Contribution |
|---|---|
| KHOBBAZ Meriem — @meriem24-beep | Contribution principale au développement et à l’intégration du projet, résolution des difficultés techniques et coordination de l’avancement. |
| AMINE Doha — @dohq25-beeep | Participation à la vérification de l’application, aux tests et à la documentation du projet. |
| OUBENADI Aya — @ayaoubenadi563 | Participation aux essais, à la relecture du compte rendu et à la vérification des éléments de remise. |

Cette répartition doit refléter le travail réellement effectué par chaque membre et être ajustée si nécessaire avant la remise finale.

**Décalration d’utilisation de l’intelligence artificielle :** Un assistant d’intelligence artificielle a été utilisé pour aider à structurer et à rédiger ce compte renduu
