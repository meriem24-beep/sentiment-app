# sentiment-app :

Application fil rouge du cours *Développement et déploiement d'applications intelligentes*.

Ce dépôt grandit chaque semaine ; la semaine 1 met en place le cadrage et l'environnement. Rien n'est jeté.

## Démarrage rapide

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Puis vérifiez :

```powershell
python scripts/check_setup.py
python -m pytest -q
```

Les scripts `scripts/setup.sh` (Linux, macOS, Git Bash) et `scripts/setup.ps1` (Windows) font l'installation et le diagnostic.

## API versionnée et sécurisée (TP2)

Le projet expose une API FastAPI avec une version historique et une API versionnée `/v1`.

### Lancement de l'API

Dans un premier terminal, à la racine du projet :

```powershell
uvicorn api.main:app --reload
```

L'API est accessible à l'adresse :

```text
http://127.0.0.1:8000
```

La documentation interactive est disponible sur :

```text
http://127.0.0.1:8000/docs
```

### Routes versionnées

| Méthode | Route | Accès |
| --- | --- | --- |
| GET | `/v1/health` | Public |
| POST | `/v1/predict` | Client ou administrateur |
| GET | `/v1/modele` | Administrateur uniquement |

L'authentification utilise des clés API. Deux rôles sont disponibles : `client` et `admin`.

Les routes historiques (`/`, `/health`, `/predict`) sont conservées pour assurer la compatibilité avec les anciens clients.

### Configuration

Copiez le fichier d'exemple :

```powershell
Copy-Item .env.example .env
```

Modifiez ensuite `.env` avec vos propres clés API et votre configuration locale.

Les variables principales sont :

- `API_KEYS` : clés API associées aux rôles `client` et `admin`.
- `CORS_ORIGINS` : origines autorisées pour les requêtes du navigateur.
- `API_KEY` : ancienne variable conservée pour la compatibilité, si elle est utilisée par la configuration du serveur.
- `API_URL` : paramètre de configuration du serveur ou des outils qui l'utilisent ; le client web fourni permet de saisir directement l'adresse de l'API dans son interface.

Dans le client web, l'adresse de l'API est initialisée à `http://127.0.0.1:8000`. La clé API est saisie dans un champ masqué et transmise au serveur dans l'en-tête `X-API-Key`. Elle n'est ni enregistrée ni envoyée à un autre service.

**Important :** le fichier `.env` contient des informations confidentielles. Il ne doit jamais être ajouté au dépôt Git. Utilisez `.env.example` pour partager uniquement les paramètres d'exemple.

## Client web (TP2)

Une interface web en HTML et JavaScript permet de saisir un avis et d'obtenir une prédiction de sentiment à partir de l'API.

### Lancement du client web

Dans un deuxième terminal :

```powershell
python -m http.server 5500 --directory web
```

Ouvrez ensuite le navigateur à l'adresse :

```text
http://localhost:5500
```

L'interface communique avec l'API et utilise une clé API de rôle `client`.

L'application peut retourner trois résultats :
- `POSITIF`
- `NEGATIF`
- `INDETERMINE` : le niveau de confiance est insuffisant et l'avis doit être vérifié par un humain.

## Modèle et interfaces

Le projet utilise un modèle de classification de sentiment fondé sur TF-IDF et la régression logistique.

Le seuil d'abstention permet de ne pas produire de décision automatique lorsque la confiance du modèle est insuffisante.

Les interfaces disponibles sont :

- `web/` : client web JavaScript (TP2).
- `ui/` : interface Streamlit (TP5).
- `sentiment_app/` : package Python et interface en ligne de commande.

## Tests

Les tests Python sont exécutés avec :

```powershell
python -m pytest -q
```

Les tests du client web JavaScript sont exécutés avec Node.js :

```powershell
node --test web\client.test.mjs
```

Résultats obtenus sur la branche d'intégration TP2 :

- Python : 162 tests réussis et 2 tests `xfailed` (échecs attendus documentés).
- JavaScript : 12 tests réussis.

Les tests vérifient notamment les prédictions, l'authentification, les autorisations, les erreurs de l'API et le fonctionnement du client web.

## Par où commencer

| Fichier | Quand le lire |
| --- | --- |
| `MARCHE-A-SUIVRE.md` | Pendant le TP1 : étapes, contrôles et résultats attendus |
| `TP1-ENONCE.md` | L'énoncé du TP1 |
| `MARCHE-A-SUIVRE-TP2.md` | Les étapes de réalisation du TP2 |
| `TP2-ENONCE.md` | L'énoncé du TP2 |
| `TESTS.md` | La démarche de test en détail |
| `AIDE-GIT.md` | Les commandes Git du TP et la résolution d'un conflit |
| `DEPANNAGE.md` | Quand quelque chose échoue |
| `CHANGELOG.md` | Historique des évolutions du projet |
| `docs/` | Documentation des semaines et comptes rendus |
| `exemples/README.md` | Exemples complémentaires |

## Raccourcis

Sous Linux, macOS et Git Bash, un `Makefile` évite de retaper certaines commandes :

```bash
make setup
make check
make test
make help
```

## Structure

```text
sentiment-app/
├── api/                  # API FastAPI, sécurité et routes versionnées
├── sentiment_app/        # Package Python, prédiction et CLI
├── web/                  # Client web HTML/JavaScript et tests Node.js
├── ui/                   # Interface Streamlit
├── src/                  # Entraînement, évaluation, biais et explicabilité
├── tests/                # Tests Python
├── data/                 # Jeux de données
├── models/               # Modèles entraînés et métriques
├── scripts/              # Installation, diagnostic et scripts Git
├── docs/                 # Documentation et comptes rendus
├── exemples/             # Exemples du cours
├── notebooks/            # Notebooks
├── .env.example          # Exemple de configuration
├── .gitignore            # Fichiers exclus de Git
├── pyproject.toml        # Configuration et packaging Python
├── requirements.txt      # Dépendances du projet
├── requirements-dev.txt  # Dépendances de développement
├── pytest.ini            # Configuration pytest
├── Makefile              # Raccourcis de commandes
└── README.md             # Documentation principale
```

## Membres du binôme

| Rôle | Nom | Identifiant GitHub |
| --- | --- | --- | --- |
| Membre A | khoubbaz Meriem | [@meriem24-beep] | |



anciens membres (de tp1 a tp4)
| Membre B2 | amine doha | [@dohq25-beeep] | |
| Membre B1 | aya oubenadi | [@ayaoubenadi563] | |
