import sys
from pathlib import Path

import pandas as pd
import streamlit as st

# Add the project root to Python's import path
RACINE = Path(__file__).resolve().parents[1]

if str(RACINE) not in sys.path:
    sys.path.insert(0, str(RACINE))

from ui import client, graphiques  # noqa: E402, I001


st.set_page_config(
    page_title="Analyse de sentiment",
    page_icon="💬",
    layout="wide",
)

st.title("Analyse de sentiment des avis clients")

# Connexion à l'API
session = client.creer_session()
etat = client.sante(session)

if not etat.ok:
    st.error(etat.message)
    st.stop()

st.caption(f"API prête · Modèle : {etat.message}")

onglet_avis, onglet_lot, onglet_aide = st.tabs(
    ["Un avis", "Un fichier CSV", "Comment ça marche"]
)

# --------------------------------------------------
# Onglet 1 : analyse d'un seul avis
# --------------------------------------------------

with onglet_avis:
    texte = st.text_area(
        "Avis à analyser",
        "Livraison rapide, produit conforme.",
        height=130,
    )

    if st.button("Analyser", type="primary"):
        resultat = client.predire(session, texte)

        if not resultat.ok:
            st.warning(resultat.message)

        elif resultat.label == "POSITIVE":
            st.success("Le modèle détecte un sentiment positif.")
            st.metric(
                "Avis positif",
                f"{resultat.score:.0%}",
            )

        elif resultat.label == "NEGATIVE":
            st.error("Le modèle détecte un sentiment négatif.")
            st.metric(
                "Avis négatif",
                f"{resultat.score:.0%}",
            )

        elif resultat.label == "INDETERMINE":
            st.warning("Le modèle n'est pas suffisamment sûr de sa prédiction.")
            st.metric(
                client.VERDICTS["INDETERMINE"],
                f"{resultat.score:.0%}",
            )
            st.info(
                "La confiance est inférieure au seuil d'abstention. "
                "Cet avis doit être vérifié par un humain."
            )

        if resultat.ok and resultat.score is not None:
            st.progress(float(resultat.score))


# --------------------------------------------------
# Onglet 2 : analyse d'un fichier CSV
# --------------------------------------------------

with onglet_lot:
    st.write(
        "Importez un fichier CSV contenant une colonne "
        "`review` avec les avis clients."
    )

    st.caption("Exemple disponible : data/avis_exemple.csv")

    fichier = st.file_uploader(
        "Choisir un fichier CSV",
        type=["csv"],
    )

    if fichier is not None:
        try:
            df = pd.read_csv(fichier)

            colonne_avis = next(
                (col for col in ["review", "text"] if col in df.columns),
                None,
)

            if colonne_avis is None:
                st.error(
                    "Le fichier doit contenir une colonne nommée 'review' ou 'text'."
                )
            elif df.empty:
                st.warning("Le fichier CSV ne contient aucun avis.")
            else:
                textes = df[colonne_avis].fillna("").astype(str).tolist()
                reponses = client.predire_lot(session, textes)

                df["prediction"] = [
                    r.label if r.ok else "REFUS OU ERREUR"
                    for r in reponses
                ]

                df["verdict"] = [
                    client.VERDICTS.get(r.label, r.message)
                    if r.ok
                    else r.message
                    for r in reponses
                ]

                df["confiance"] = [
                    f"{r.score:.0%}" if r.score is not None else ""
                    for r in reponses
                ]

                resume = client.resumer(reponses)

                total = len(reponses)
                positifs = resume.get("POSITIVE", 0)
                negatifs = resume.get("NEGATIVE", 0)
                indetermines = resume.get("INDETERMINE", 0)
                erreurs = resume.get("REFUS OU ERREUR", 0)

                st.subheader("Résultats de l'analyse")

                c1, c2, c3, c4 = st.columns(4)

                c1.metric("Avis analysés", total)
                c2.metric("Avis positifs", positifs)
                c3.metric("Avis négatifs", negatifs)
                c4.metric("À vérifier / erreurs", indetermines + erreurs)

                st.subheader("Répartition des sentiments")

                statistiques = pd.Series(
                    {
                        "Positifs": positifs,
                        "Négatifs": negatifs,
                        "Indéterminés": indetermines,
                        "Refus ou erreurs": erreurs,
                    }
                )

                st.bar_chart(statistiques)

                colonne_confiances = st.container()
                colonne_confiances.caption("Confiance du modèle, par tranche")
                colonne_confiances.bar_chart(
                    graphiques.histogramme_confiances(reponses)
                )

                st.subheader("Détail des avis")

                st.dataframe(
                    df,
                    use_container_width=True,
                )

                st.download_button(
                    label="Télécharger les résultats CSV",
                    data=df.to_csv(index=False).encode("utf-8-sig"),
                    file_name="resultats.csv",
                    mime="text/csv",
                )

        except (ValueError, pd.errors.ParserError) as erreur:
            st.error(f"Impossible de lire le fichier CSV : {erreur}")


# --------------------------------------------------
# Onglet 3 : explication
# --------------------------------------------------

with onglet_aide:
    st.markdown(
        """
**Architecture de l'application**

L'interface Streamlit communique avec le backend FastAPI
à travers le module `ui/client.py`.

**Fonctionnement**

1. L'interface vérifie que l'API est disponible.
2. L'utilisateur saisit un avis ou importe un fichier CSV.
3. Le client HTTP envoie les textes à l'API.
4. Le modèle analyse les avis et renvoie ses prédictions.
5. L'interface affiche les résultats.

**Gestion de l'incertitude**

Lorsque le modèle n'est pas suffisamment sûr de sa prédiction,
il renvoie le verdict `INDETERMINE`.

L'avis est alors signalé pour vérification humaine.

**Gestion des erreurs**

L'interface affiche des messages explicites lorsque le texte
est invalide, que le modèle n'est pas chargé ou que l'API
est inaccessible.
        """
    )
