# TP2 — Analyse des erreurs et évaluation du modèle

## 1. Résultats de l'évaluation

Le modèle de classification de sentiments a été évalué sur 58 avis de test. Il obtient une accuracy de 0,879 et un F1-score macro de 0,879.

La matrice de confusion indique :
- 27 avis négatifs correctement classés comme négatifs ;
- 2 avis négatifs classés à tort comme positifs ;
- 24 avis positifs correctement classés comme positifs ;
- 5 avis positifs classés à tort comme négatifs.

Le modèle commet donc 7 erreurs sur les 58 avis évalués.

## 2. Analyse des erreurs

Certains avis contiennent à la fois des éléments positifs et négatifs. Par exemple, un avis peut commencer par signaler un problème de livraison ou un produit défectueux, puis terminer par une appréciation positive.

Le modèle peut alors se tromper sur le sentiment global de l'avis, car certains mots positifs ou négatifs influencent fortement sa prédiction.

## 3. Limites du modèle

Le modèle utilise une représentation de type sac de mots (*bag-of-words*). Il prend en compte les mots présents dans un avis, mais ne comprend pas correctement leur ordre ni les relations entre eux.

Il peut donc avoir des difficultés à interpréter :
- les phrases contenant une opposition, comme « mais » ou « sauf que » ;
- les avis qui mélangent des sentiments positifs et négatifs ;
- le contexte dans lequel un mot est utilisé.

## 4. Améliorations possibles

Pour améliorer les résultats, on pourrait :
- utiliser des unigrammes et des bigrammes afin de mieux tenir compte de certaines expressions ;
- disposer d'un jeu de données plus grand et plus varié ;
- tester d'autres algorithmes de classification ;
- utiliser un modèle de langage pré-entraîné capable de mieux prendre en compte le contexte.

## 5. Conclusion

Le modèle atteint le seuil de F1-score fixé pour cette étape, avec un score de 0,879 supérieur à 0,85. Cependant, les 7 erreurs observées montrent que les avis ambigus ou contenant des sentiments opposés restent difficiles à classifier.
