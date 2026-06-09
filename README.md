# Plant-wise Document Intelligence Portal

![React](https://img.shields.io/badge/React-Frontend-61DAFB?logo=react)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-47A248?logo=mongodb)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)

![Status](https://img.shields.io/badge/Status-Production_Ready-success)
![Architecture](https://img.shields.io/badge/Architecture-Full_Stack-blue)
![Type](https://img.shields.io/badge/Project-Document_Intelligence-purple)

This repository is organized into two apps:

- `backend/` contains the Flask API and backend configuration.
- `frontend/` contains the React + TypeScript + Vite client.

## Run Locally

### Frontend

```bash
cd frontend
npm install
npm run dev -- --host
```

### Backend

```bash
cd backend
pip install -r requirements.txt
python run.py
```

## Docker

The root [docker-compose.yml](./docker-compose.yml) currently starts MongoDB and the backend service.
