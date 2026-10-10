# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Identifier et classer les avis négatifs afin d'aider l'équipe à prioriser les réclamations nécessitant une réponse rapide.

## Utilisateur final (obligatoire)
L'équipe du service client ou les responsables de la qualité.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
Le machine learning peut apprendre à classer les avis à partir d'exemples étiquetés (a) et traiter un grand volume d'avis à un coût raisonnable par requête (c). Les performances doivent être évaluées sur des données de test représentatives.

## Données nécessaires et leur origine (obligatoire)
Des avis clients historiques, anonymisés autant que possible, avec des catégories validées par l'équipe, par exemple livraison, qualité ou service client.

## Métrique de succès et seuil d'acceptation (obligatoire)
Mesurer la précision, le rappel et le F1-score sur un jeu de test indépendant. Objectif initial : un F1-score macro d'au moins 0,80 avant utilisation opérationnelle.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Un avis peut être mal classé et une réclamation urgente peut être retardée. L'équipe doit pouvoir corriger les catégories et vérifier les cas prioritaires.

## Risques éthiques ou de confidentialité (obligatoire)
Les avis peuvent contenir des noms ou des informations personnelles. Il faut limiter les données collectées, anonymiser les exemples et vérifier que le modèle ne défavorise pas certains groupes de clients.

## Approche écartée et pourquoi (facultatif)
Les règles métier seules sont écartées car les avis peuvent exprimer des problèmes variés avec des formulations très différentes.
