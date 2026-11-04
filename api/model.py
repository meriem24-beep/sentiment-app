
"""Raccord entre l'API et le modèle entraîné au TP2."""
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / "src"))

from predict import charger_modele, predict as _predict  # noqa: E402, I001

SEUIL_ABSTENTION = 0.60


class SentimentClassifier:
    """Enveloppe du modèle TP2 avec abstention."""

    model_name = "tfidf-logreg (TP2, models/sentiment.joblib)"

    def __init__(self) -> None:
        charger_modele()

    def predict(self, text: str) -> dict:
        """Renvoie POSITIVE, NEGATIVE ou INDETERMINE."""
        resultat = _predict(text)
        pipeline = charger_modele()

        vecteur = pipeline.named_steps["tfidf"].transform([text])
        inconnu = vecteur.nnz == 0

        if inconnu or resultat["score"] < SEUIL_ABSTENTION:
            label = "INDETERMINE"
        else:
            label = resultat["label"].upper()

        return {
            "label": label,
            "score": resultat["score"],
            "text": text[:100],
        }


def load_model() -> SentimentClassifier:
    """Construit le classifier."""
    return SentimentClassifier()
