# RoboMunch – Backend Server 2 (Cloud)

Django-based cloud backend for RoboMunch (EE471 Mini Project #4).
Deployed on Google Cloud VM via CI/CD pipeline.

## Endpoints

- `POST /get/resolution` → returns image width, height, resolution
- `POST /convert/grayscale` → converts image to grayscale, returns base64 PNG

## Request Format

```json
{
  "image": "<base64-encoded PNG string>"
}
```

## Run Locally

```bash
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8080
```

## Run with Docker

```bash
docker build -t robomunch-backend2 .
docker run -p 8080:8080 robomunch-backend2
```

## CI/CD

- `ci_version.yaml` → semantic versioning on push to main
- `ci_linting.yaml` → ruff lint check on pull requests
- `cd_deploy.yaml` → deploy to VM after CI passes
