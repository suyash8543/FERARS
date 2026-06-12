Deployment instructions

Backend (Render):

- Ensure `requirements.txt` and `runtime.txt` are at repo root.
- Render build command (example):

```
pip install -r requirements.txt && python backend/setup_database.py
```

- Start command (Render / Procfile):

```
gunicorn backend.server:app --bind 0.0.0.0:$PORT --workers 1 --timeout 120
```

Frontend (Vercel):

- The `frontend/` directory contains the static site. On Vercel choose the `frontend` folder as the project root, or connect the repo and set the project root to `frontend`.
- No build step required for plain HTML/CSS/JS.
- `frontend/vercel.json` is included to force a static deployment.

Local testing:

1. Create a virtualenv and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\activate on Windows
pip install -r requirements.txt
```

2. Initialize DBs and start backend:

```bash
python backend/setup_database.py
python backend/server.py
```

3. Serve frontend by opening `frontend/index.html` in a browser or use a static server.
