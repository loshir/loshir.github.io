# loshir.github.io (Flask app)

Short: this repository contains a small Flask app (`app.py`) rendering templates in `templates/`.

One-line Render deploy (quick):

Connect this repo on Render and set Build Command `pip install -r requirements.txt`, Start Command `gunicorn app:app`.

Quick deployment guides

- Render (recommended):
  1. Go to https://render.com and create a new **Web Service**.
 2. Connect your GitHub account and select `loshir/loshir.github.io`.
  3. Set the **Build Command** to:

     pip install -r requirements.txt

  4. Set the **Start Command** to:

     gunicorn app:app

  5. Render will set the `PORT` environment variable automatically; no change needed in app code. Add any secrets (see below) in the Render dashboard under Environment.

- Railway (alternative):
  1. Create a new project at https://railway.app and choose "Deploy from GitHub".
 2. Select this repo and set the **Build Command** to `pip install -r requirements.txt` and the **Start Command** to `gunicorn app:app`.

Sample environment variables (set these in your provider's dashboard):

- `SECRET_KEY` — Flask secret (if you add session features)
- `DATABASE_URL` — DB connection string, if used
- `FLASK_ENV=production` — optional

Notes and next steps

- The repository previously contained a committed `venv/`; I stopped tracking that and added `.gitignore`.
- `requirements.txt` was generated minimally (Flask, gunicorn). If your app uses more packages, update it by activating your local virtualenv and running `pip freeze > requirements.txt` then commit and push.
- If you prefer Vercel (serverless), I can add a small `api/` wrapper and `vercel.json` but Render/Railway are much simpler for a standard Flask WSGI app.

If you want, I can create the Render service for you (I cannot do that directly — you must sign in to Render) and provide the exact settings to paste into the Render UI.

---
Last updated: 29 November 2025
# loshir.github.io