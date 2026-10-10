# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Aider le personnel de la pharmacie à détecter les ordonnances incomplètes avant de délivrer un médicament.

## Utilisateur final (obligatoire)
Le pharmacien ou le préparateur en pharmacie qui vérifie les ordonnances.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
Les règles métier permettent de vérifier des champs obligatoires de manière explicable et à faible coût par requête (c). Comme une erreur peut avoir des conséquences sur la sécurité du patient (d), les alertes doivent être vérifiables par un professionnel.

## Données nécessaires et leur origine (obligatoire)
Les champs de l'ordonnance, les informations réglementaires nécessaires et la liste des éléments obligatoires, provenant de sources autorisées et validées par la pharmacie

## Métrique de succès et seuil d'acceptation (obligatoire)
Mesurer le taux de détection des ordonnances incomplètes sur un jeu de cas validés. Objectif initial : détecter au moins 95 % des cas incomplets, avec validation humaine avant toute décision.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une omission peut retarder une prise en charge ou conduire à une délivrance inappropriée. Le pharmacien doit examiner les alertes et prendre la décision finale.

## Risques éthiques ou de confidentialité (obligatoire)
Les ordonnances contiennent des données de santé sensibles. Il faut limiter les accès, protéger les données et éviter d'utiliser des données personnelles sans autorisation.

## Approche écartée et pourquoi (facultatif)
Un modèle génératif seul est écarté car des règles explicites sont plus simples à vérifier pour contrôler la présence des champs obligatoires.
