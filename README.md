# FINN — Financial Investment Agent

A focused, runnable investment intelligence prototype. FastAPI serves a custom responsive HTML/CSS/JavaScript client; SQLite persists watch preferences, acknowledgements and primary-source excerpts. No frontend build step or API key is needed.

## Run locally

Requires Python 3.10 or newer. Open a terminal inside this folder:

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000. Interactive API documentation: http://127.0.0.1:8000/docs.

## Demonstration walkthrough

1. Open Intelligence; review the lead and attention queue.
2. Search Portfolio for Infosys, filter sectors and sort by daily move.
3. Open Filing room; change 24 hours to 3 days to reveal the older dividend notice. Filter categories and acknowledge a filing.
4. Change volume or price thresholds in Watch rules. Return home to see recalculated alerts.
5. Open Research; ask a question before adding evidence to demonstrate abstention.
6. Expand Add primary-source evidence. Paste an actual passage from an annual report or transcript with its title, period, page and original URL. Ask a question containing relevant terms. Inspect the returned exact passage and open its citation.

## What works

- Eighteen diversified demonstration portfolio companies and four additional research choices.
- Custom ink/parchment/copper interface with responsive navigation and horizontally scrollable tables.
- Search, sector filter, sorting, digest time/category filters, routine disclosure collapse, acknowledgements.
- Configurable positive/negative price thresholds, volume multiple and announcement categories, persisted in SQLite.
- Generic ticker research using user-supplied evidence, lexical retrieval, exact passages and citations; no unsupported company knowledge.
- Explicit synthetic market/filing labels and missing-data states.

## Limitations — read before submitting

This is a focused prototype, not the full requested financial agent. All market figures and announcements are synthetic demonstration fixtures, dated 30 October 2026. Live NSE/BSE announcements, Yahoo EOD ingestion, automated PDF acquisition/extraction, LLM synthesis, quarterly financial extraction, management biographies, four-quarter narrative comparison and company comparison are not implemented. Source URLs and authenticity are supplied by the user, not independently verified. Retrieval is lexical and extractive, not semantic RAG or AI reasoning. Financial tables intentionally remain unavailable rather than inventing values. No unattended scheduler, authentication, multi-user isolation or production access control is implemented. Do not expose an unprotected deployment with private data. Browser screenshots, touch interactions and console checks require manual verification.

## Architecture and source discipline

`app/main.py` separates API endpoints, SQLite persistence, fixture data and retrieval in one small backend module. `static/app.js` contains client routes and rendering; `static/style.css` holds the custom responsive system. The only evidence available to research is stored against the requested ticker. Unrelated tickers cannot supply citations. Facts are verbatim excerpts; alert ratios are labelled calculations; scenario commentary is labelled interpretation. Missing evidence produces an explicit abstention. This deliberately avoids a model generating financial claims from memory.

`FINN_DB` optionally sets the database file path (default: `finn.db` beside this README). Environment variables must be set by your shell/hosting platform; `.env.example` is documentation, not automatically loaded. The database is excluded from Git. No secrets are required.

## API

- GET `/api/health`, `/api/portfolio`, `/api/alerts`
- GET `/api/digest?hours=24&category=all` (24, 72 or 168 hours)
- POST `/api/acknowledge/{id}`
- GET/PUT `/api/settings`
- POST `/api/evidence`; GET `/api/evidence/{ticker}`
- POST `/api/research` with `ticker` and `question`

See `/docs` for payload schemas and validation constraints.

## Tests

```sh
python -m unittest discover -s tests -v
node --check static/app.js
```

Tests cover portfolio size, filtering, invalid thresholds, persistence, acknowledgements, page delivery, no-evidence abstention, citation metadata and cross-company evidence isolation. They use a temporary database.

## Deploy

### Vercel demo

The repository includes `vercel.json` for FastAPI detection. Import `krith31/finn-investment-agent` into Vercel with the repository root as Root Directory. The application entrypoint is `app/main.py`. No API keys are required. Vercel mode stores SQLite in its temporary directory and displays a prominent storage warning: settings, acknowledgements and excerpts can reset or vary between function instances, and are shared between visitors. Do not enter private data. Durable multi-user use requires a hosted database and authentication. Deployment is only verified once a successful Vercel deployment and live HTTP checks have completed.

### Container with persistent storage

This Python application requires a container/Python host; static-only hosting cannot run its backend. Deployment has not been performed.

```sh
docker build -t finn .
docker volume create finn-data
docker run -d --name finn -p 8000:8000 -v finn-data:/data finn
```

For a container host, use this Dockerfile, port 8000, a persistent disk mounted at `/data`, and `FINN_DB=/data/finn.db`. Configure HTTPS and an authenticated access proxy before external use. Check `/api/health`, complete the demo workflow on a phone, then share the protected deployment URL. No cloud credentials are included. Container build itself has not been tested here.

## Implementation priorities

The source brief requires a working mobile-first prototype, repository, build history and covering note; its eight research outputs are a menu. The user requested a broader product. This submission implements the smallest reliable desk workflow and records remaining work explicitly. Next: official-source ingestion with retry/cache and document hashes; page-aware PDF chunks; validated period/unit-aware financial tables; structured, citation-checked model output; real guidance-versus-results analysis; authentication and scheduled EOD refresh.
