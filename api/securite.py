
"""Authentification par clé API et autorisation par rôle."""
import os
import secrets
from collections.abc import Callable
from typing import Annotated, Literal

from fastapi import Depends, Header, HTTPException, Security
from fastapi.security import APIKeyHeader

Role = Literal["client", "admin"]

LONGUEUR_MIN = 16

EN_TETE = APIKeyHeader(
    name="X-API-Key",
    auto_error=False,
    description="Clé API ; le rôle associé détermine les accès.",
)

NON_AUTHENTIFIE = {"WWW-Authenticate": "APIKey"}


def charger_cles(brut: str | None = None) -> dict[str, Role]:
    """Charge les clés API depuis API_KEYS."""
    brut = os.environ.get("API_KEYS", "") if brut is None else brut
    cles: dict[str, Role] = {}

    for entree in filter(None, (m.strip() for m in brut.split(","))):
        cle, separateur, role = entree.rpartition(":")

        if not separateur or role not in ("client", "admin"):
            raise ValueError("Rôle inconnu ou format invalide dans API_KEYS.")

        if len(cle) < LONGUEUR_MIN:
            raise ValueError(
                f"Clé trop courte dans API_KEYS "
                f"({len(cle)} caractères, minimum {LONGUEUR_MIN})."
            )

        cles[cle] = role

    return cles


def identifier(
    cle: Annotated[str | None, Security(EN_TETE)],
) -> Role:
    """Authentifie l'appelant à partir de sa clé API."""
    if not cle:
        raise HTTPException(
            status_code=401,
            detail="Clé d'API manquante : en-tête X-API-Key",
            headers=NON_AUTHENTIFIE,
        )

    for connue, role in charger_cles().items():
        if secrets.compare_digest(cle.encode(), connue.encode()):
            return role

    raise HTTPException(
        status_code=401,
        detail="Clé d'API invalide",
        headers=NON_AUTHENTIFIE,
    )


def exiger(*autorises: Role) -> Callable[[Role], Role]:
    """Construit une dépendance qui vérifie les rôles autorisés."""

    def verifier(
        role: Annotated[Role, Depends(identifier)],
    ) -> Role:
        if role not in autorises:
            raise HTTPException(
                status_code=403,
                detail=f"Accès refusé au rôle « {role} »",
            )
        return role

    return verifier


# Compatibilité avec les anciens noms utilisés dans le projet.
def _charger_cles() -> dict[str, Role]:
    return charger_cles()


def verifier_api_key(
    x_api_key: str | None = Header(default=None, alias="X-API-Key"),
) -> Role:
    """Ancienne fonction d'authentification."""
    if not x_api_key:
        raise HTTPException(
            status_code=401,
            detail="Clé API manquante.",
            headers=NON_AUTHENTIFIE,
        )

    for connue, role in charger_cles().items():
        if secrets.compare_digest(x_api_key, connue):
            return role

    raise HTTPException(
        status_code=401,
        detail="Clé API invalide.",
        headers=NON_AUTHENTIFIE,
    )


def exiger_role(role_requis: str):
    """Ancienne fonction de vérification des rôles."""
    return exiger(role_requis)
