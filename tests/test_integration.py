
"""Tests d'intégration : l'API telle qu'elle tourne vraiment (TP4, étape D)."""

import pytest
from fastapi.testclient import TestClient

MODELE = __import__("pathlib").Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"


@pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")
def test_demarrage_reel_charge_le_modele():
    """D.1 : le lifespan charge le modèle au démarrage."""
    from api.main import app

    with TestClient(app) as client:
        reponse = client.get("/health")

    assert reponse.status_code == 200
    assert "TP2" in reponse.json()["model"]


def test_modele_absent_refuse_demarrage(monkeypatch, tmp_path):
    """D.2 : un modèle absent empêche le démarrage de l'API."""
    import predict
    from api.main import app

    monkeypatch.setattr(predict, "MODELE", tmp_path / "modele_inexistant.joblib")
    predict.charger_modele.cache_clear()

    try:
        with pytest.raises(FileNotFoundError):
            with TestClient(app):
                pass
    finally:
        predict.charger_modele.cache_clear()


@pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")
def test_modele_non_charge_repond_503(monkeypatch):
    """D.3 : /health et /predict répondent 503 si le modèle est absent."""
    from api.main import app

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", None)

        health = client.get("/health")
        prediction = client.post("/predict", json={"text": "Très bon produit"})

    assert health.status_code == 503
    assert prediction.status_code == 503


@pytest.mark.skipif(not MODELE.exists(), reason="modèle non produit : python src/train.py")
@pytest.mark.parametrize(
    "exception",
    [
        RuntimeError("panne du modèle"),
        ValueError("bug interne"),
    ],
    ids=["runtime-error", "value-error"],
)
def test_modele_en_panne_repond_500(monkeypatch, exception):
    """D.4 : toute exception interne du modèle produit une réponse 500."""

    from api.main import app

    class ModeleEnPanne:
        model_name = "modele-test"

        def predict(self, text):
            raise exception

    with TestClient(app) as client:
        monkeypatch.setattr(app.state, "classifier", ModeleEnPanne())
        reponse = client.post("/predict", json={"text": "Très bon produit"})

    assert reponse.status_code == 500
    assert "bug interne" not in reponse.text
    assert "panne du modèle" not in reponse.text
