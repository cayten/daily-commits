# Project Title

A concise one-liner about your project. Keep it crisp and outcome-focused.

## 🚀 Overview
Explain **what** this project does and **why** it exists. Add a short demo gif/screenshot later.

## 🧱 Tech Stack
- Python 3.11+
- FastAPI
- Pytest

## ⚙️ Getting Started

### 1) Create & activate a virtualenv
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Run the app
```bash
uvicorn src.main:app --reload
```

App will be available at: http://127.0.0.1:8000 (Docs: `/docs`)

## 📡 API Endpoints (starter)
- `GET /health` → returns `{ "status": "ok" }`
- `GET /users` → list users (in-memory)
- `POST /users` → create a user
- `GET /users/{id}` → fetch one
- `PUT /users/{id}` → update
- `DELETE /users/{id}` → delete

## ✅ Tests
```bash
pytest -q
```

## 🧪 CI (GitHub Actions)
A minimal CI workflow is included at `.github/workflows/ci.yml` to run tests on every push/PR.

## 🤝 Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md).

## 🔐 Security
See [SECURITY.md](SECURITY.md).

## 📜 License
[MIT](LICENSE)

---

Made with ❤️ by Canan Ayten Dörtkol.
