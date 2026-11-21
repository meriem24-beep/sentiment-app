
"""Tests des fonctions d'authentification et de compatibilité."""

import pytest
from fastapi import HTTPException


def test_est_role():
    from api.securite import est_role

    assert est_role("client") is True
    assert est_role("admin") is True
    assert est_role("inconnu") is False


def test_charger_cles_ancienne_fonction(monkeypatch):
    from api.securite import _charger_cles

    cle = "cle-test-securite-client-0001"
    monkeypatch.setenv("API_KEYS", f"{cle}:client")

    assert _charger_cles() == {cle: "client"}


def test_verifier_api_key_cle_manquante():
    from api.securite import verifier_api_key

    with pytest.raises(HTTPException) as erreur:
        verifier_api_key(None)

    assert erreur.value.status_code == 401
    assert erreur.value.detail == "Clé API manquante."


def test_verifier_api_key_cle_valide(monkeypatch):
    from api.securite import verifier_api_key

    cle = "cle-test-securite-client-0001"
    monkeypatch.setenv("API_KEYS", f"{cle}:client")

    assert verifier_api_key(cle) == "client"


def test_verifier_api_key_cle_invalide(monkeypatch):
    from api.securite import verifier_api_key

    monkeypatch.setenv(
        "API_KEYS",
        "cle-test-securite-client-0001:client",
    )

    with pytest.raises(HTTPException) as erreur:
        verifier_api_key("cle-inconnue")

    assert erreur.value.status_code == 401
    assert erreur.value.detail == "Clé API invalide."


def test_exiger_role_client():
    from api.securite import exiger_role

    verifier = exiger_role("client")

    assert verifier("client") == "client"


def test_exiger_role_admin():
    from api.securite import exiger_role

    verifier = exiger_role("admin")

    assert verifier("admin") == "admin"


def test_exiger_role_refuse_role_non_autorise():
    from api.securite import exiger_role

    verifier = exiger_role("admin")

    with pytest.raises(HTTPException) as erreur:
        verifier("client")

    assert erreur.value.status_code == 403


def test_exiger_role_inconnu():
    from api.securite import exiger_role

    with pytest.raises(ValueError, match="Rôle inconnu"):
        exiger_role("superadmin")
