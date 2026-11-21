
"""API REST du classifier de sentiment (TP3 + TP2 versionné)."""
import logging
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from api import v1
from api.model import load_model
from api.schemas import HealthResponse, PredictRequest, PredictResponse
from api.securite import charger_cles

# Charge les variables du fichier .env sans écraser celles déjà définies.
load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger("sentiment_api")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Charge le modèle et vérifie la configuration au démarrage."""
    logger.info("Démarrage de l'API...")

    nb_cles = len(charger_cles())

    if nb_cles == 0:
        logger.warning(
            "Aucune clé API configurée : les routes /v1 protégées répondront 401."
        )

    app.state.classifier = load_model()

    logger.info(
        "Modèle chargé : %s ; %d clé(s) API",
        app.state.classifier.model_name,
        nb_cles,
    )

    yield

    logger.info("Arrêt de l'API")


app = FastAPI(
    title="Sentiment Analysis API",
    description=(
        "Classifie le sentiment d'un avis en français. "
        "Les nouvelles routes versionnées utilisent une clé API."
    ),
    version="1.2.0",
    lifespan=lifespan,
)


# CORS : seules les origines du client web sont autorisées.
ORIGINES = [
    origine.strip()
    for origine in os.environ.get(
        "CORS_ORIGINS",
        "http://localhost:5500,http://127.0.0.1:5500",
    ).split(",")
    if origine.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINES,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "X-API-Key"],
)

# Activation des nouvelles routes.
app.include_router(v1.router)


# ---------------------------------------------------------------------
# Gestion uniforme des erreurs sous /v1.
# ---------------------------------------------------------------------

CODES = {
    400: "REQUETE_INVALIDE",
    401: "NON_AUTHENTIFIE",
    403: "ACCES_REFUSE",
    404: "INTROUVABLE",
    405: "METHODE_NON_AUTORISEE",
    422: "ENTREE_INVALIDE",
    500: "ERREUR_INTERNE",
    503: "MODELE_INDISPONIBLE",
}


def _erreur_v1(
    statut: int,
    message: str,
    champs: list[dict] | None = None,
    en_tetes: dict[str, str] | None = None,
) -> JSONResponse:
    """Construit le format d'erreur standard de la V1."""
    corps = {
        "erreur": {
            "code": CODES.get(statut, f"HTTP_{statut}"),
            "message": message,
            "champs": champs or [],
        }
    }

    return JSONResponse(
        corps,
        status_code=statut,
        headers=en_tetes,
    )


@app.exception_handler(StarletteHTTPException)
async def erreur_http(
    request: Request,
    exc: StarletteHTTPException,
) -> Response:
    """Normalise les erreurs V1 sans modifier les anciennes routes."""
    if request.url.path.startswith("/v1"):
        return _erreur_v1(
            exc.status_code,
            str(exc.detail),
            en_tetes=getattr(exc, "headers", None),
        )

    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def erreur_validation(
    request: Request,
    exc: RequestValidationError,
) -> Response:
    """Normalise les erreurs de validation uniquement sous /v1."""
    if request.url.path.startswith("/v1"):
        champs = [
            {
                "champ": ".".join(str(element) for element in erreur["loc"]),
                "message": erreur["msg"],
            }
            for erreur in exc.errors()
        ]

        return _erreur_v1(
            422,
            "Entrée refusée par le contrat de l'API",
            champs,
        )

    return await request_validation_exception_handler(request, exc)


# ---------------------------------------------------------------------
# Anciennes routes conservées pour la compatibilité.
# ---------------------------------------------------------------------

def _classifier():
    """Récupère le classificateur chargé."""
    clf = getattr(app.state, "classifier", None)

    if clf is None:
        raise HTTPException(
            status_code=503,
            detail="Modèle non chargé",
        )

    return clf


@app.get("/", summary="Accueil")
async def root():
    return {
        "message": "Sentiment Analysis API",
        "docs": "/docs",
        "health": "/health",
        "version": "/v1",
    }


@app.get(
    "/health",
    response_model=HealthResponse,
    summary="Santé de l'API",
)
async def health_check():
    """Vérifie que le modèle est chargé."""
    return {
        "status": "OK",
        "model": _classifier().model_name,
    }


@app.post(
    "/predict",
    response_model=PredictResponse,
    summary="Classifier un texte (dépréciée)",
    deprecated=True,
)
async def predict(
    request: PredictRequest,
    response: Response,
):
    """Ancienne route conservée pour les clients existants."""
    response.headers["Deprecation"] = "true"
    response.headers["Link"] = '</v1/predict>; rel="successor-version"'

    clf = _classifier()

    try:
        result = clf.predict(request.text)
    except Exception:
        logger.exception("Erreur lors de la prédiction")
        raise HTTPException(
            status_code=500,
            detail="Erreur interne du serveur",
        ) from None

    logger.info(
        "predict: %r -> %s (%.2f)",
        request.text[:50],
        result["label"],
        result["score"],
    )

    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )
