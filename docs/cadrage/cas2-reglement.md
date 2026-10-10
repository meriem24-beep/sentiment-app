# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Permettre aux étudiants et au personnel de trouver des réponses fiables aux questions sur le règlement intérieur de l'établissement.

## Utilisateur final (obligatoire)
Les étudiants, enseignants et membres du personnel de l'établissement.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
Le RAG recherche les passages pertinents du règlement pour fonder la réponse sur des documents vérifiables (b). Il évite d'avoir besoin d'un grand jeu de données étiquetées pour apprendre chaque réponse (a). Le système doit citer ses sources et reconnaître quand le règlement ne permet pas de répondre.

## Données nécessaires et leur origine (obligatoire)
Le règlement intérieur officiel, ses annexes et les éventuelles versions mises à jour, fournis par l'établissement.

## Métrique de succès et seuil d'acceptation (obligatoire)
Évaluer la pertinence des réponses et la justesse des citations sur un jeu de questions validées. Objectif initial : au moins 90 % de réponses correctement sourcées

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une réponse erronée peut induire un étudiant en erreur sur ses droits ou obligations. Les réponses doivent citer les passages utilisés et les questions sensibles doivent être vérifiées auprès du service compétent.

## Risques éthiques ou de confidentialité (obligatoire)
Le système doit protéger les éventuelles données personnelles contenues dans les documents et ne pas inventer de règles absentes du règlement officiel.

## Approche écartée et pourquoi (facultatif)
Un modèle génératif seul est écarté car il peut produire des réponses non appuyées par le règlement et difficiles à vérifier.
