# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
<<<<<<< HEAD
Permettre aux étudiants et au personnel de trouver des réponses fiables aux questions sur le règlement intérieur de l'établissement.

## Utilisateur final (obligatoire)
Les étudiants, enseignants et membres du personnel de l'établissement.
=======

Répondre aux questions des étudiants sur le règlement intérieur en citant l'article exact sur lequel la réponse s'appuie.

## Utilisateur final (obligatoire)

Les étudiants, qui obtiennent une réponse immédiate à toute heure, et le secrétariat, qui traite aujourd'hui les mêmes questions une par une par courriel.
>>>>>>> fa6047e (Complete AI use case framing)

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
<<<<<<< HEAD
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
=======

(b) La réponse doit être vérifiable : chaque réponse affiche l'article et la page du règlement, ce qu'aucun modèle génératif seul ne garantit. (a) Aucune base de questions étiquetées n'existe, ce qui écarte l'apprentissage supervisé. (c) Quelques dizaines de questions par jour seulement, donc le coût par appel d'un modèle de langage reste acceptable.

## Données nécessaires et leur origine (obligatoire)

Le règlement intérieur en PDF et les notes de service publiées par la direction, documents publics de l'école, découpés en passages et indexés. Les textes sont mis à jour une fois par an, l'index est reconstruit à chaque révision.

## Métrique de succès et seuil d'acceptation (obligatoire)

Part de réponses correctes accompagnées de la citation exacte, mesurée sur un jeu de 20 questions réelles fournies par le secrétariat. Acceptation à partir de 0,90, et zéro réponse citant un article qui n'existe pas.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une réponse fausse induit l'étudiant en erreur sur ses droits ou ses obligations. L'interface affiche donc toujours l'extrait cité pour qu'il puisse vérifier lui-même, et rappelle que le secrétariat reste l'interlocuteur en cas de doute.

## Risques éthiques ou de confidentialité (obligatoire)

Les questions posées peuvent contenir un nom, un numéro d'étudiant ou une situation personnelle : aucune question n'est conservée après la réponse, et seuls les documents officiels entrent dans l'index.

## Approche écartée et pourquoi (facultatif)

Le modèle génératif seul : il produirait des réponses plausibles mais inventerait des numéros d'articles, ce qui est exactement le risque que (b) nous demande d'éliminer.
>>>>>>> fa6047e (Complete AI use case framing)
