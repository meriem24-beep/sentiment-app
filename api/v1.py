
"""API versionnée V1 : prédiction, authentification et informations du modèle."""
import json
import logging
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request

from api.model import SEUIL_ABSTENTION, SentimentClassifier
from api.schemas import (
    ErreurV1,
    HealthResponse,
    ModeleResponse,
    PredictRequest,
    PredictResponse,
)
from api.securite import exiger

logger = logging.getLogger("sentiment_api")

METRIQUES = Path(__file__).resolve().parents[1] / "models" / "metrics.json"

ERREURS: dict[int | str, dict] = {
    code: {"model": ErreurV1}
    for code in (401, 403, 422, 500, 503)
}

router = APIRouter(
    prefix="/v1",
    tags=["v1"],
    responses=ERREURS,
)


def classifier(request: Request) -> SentimentClassifier:
    """Récupère le classificateur chargé au démarrage."""
    clf = getattr(request.app.state, "classifier", None)

    if clf is None:
        raise HTTPException(
            status_code=503,
            detail="Modèle non chargé",
        )

    return clf


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Santé (public)",
)
def sante(clf: Annotated[SentimentClassifier, Depends(classifier)]) -> dict[str, str]:
    return {
        "status": "OK",
        "model": clf.model_name,
    }


@router.post(
    "/predict",
    response_model=PredictResponse,
    summary="Classer un avis (client, admin)",
    dependencies=[Depends(exiger("client", "admin"))],
)
def predire(
    corps: PredictRequest,
    clf: Annotated[SentimentClassifier, Depends(classifier)],
) -> dict:
    try:
        resultat = clf.predict(corps.text)
    except Exception:
        logger.exception("Erreur lors de la prédiction")
        raise HTTPException(
            status_code=500,
            detail="Erreur interne du serveur",
        ) from None

    # Ne pas journaliser le texte : il peut contenir des données personnelles.
    logger.info(
        "v1 predict -> %s (%.2f)",
        resultat["label"],
        resultat["score"],
    )

    return resultat


@router.get(
    "/modele",
    response_model=ModeleResponse,
    summary="Métriques du modèle (admin)",
    dependencies=[Depends(exiger("admin"))],
)
def modele(
    clf: Annotated[SentimentClassifier, Depends(classifier)],
) -> dict:
    metriques = (
        json.loads(METRIQUES.read_text(encoding="utf-8"))
        if METRIQUES.exists()
        else {}
    )

    return {
        "model": clf.model_name,
        "seuil_abstention": SEUIL_ABSTENTION,
        "metriques": metriques,
    }
