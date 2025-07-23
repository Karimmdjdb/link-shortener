# Link Shortener API

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

A minimal FastAPI backend for URL shortening.  
This API allows you to save links, retrieve the full URL from a short link, and check the database connection.

---

## Endpoints

### Check database connection

```http
GET /db-check
```
Returns 200 OK if the API can connect to the database.

---

### Retrieve the original URL

```http
GET /{short_url}
```
Returns the original long URL corresponding to the provided short code.

---

### Save a new link

```http
POST /save
Content-Type: application/json
Body: {"url": "https://example.com"}
```

Response:
```json
{
  "short_url": "abcdef",
  "url": "https://example.com"
}
```

---

## Usage

You can run the API locally or using Docker.  
By default, the app listens on port **8000**.

### Run locally

Make sure you have Python and FastAPI installed.

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Build and run with Docker

You can build the image using the provided Dockerfile and run the API in a container:

```bash
docker build -t link-shortener-api .
docker run -p 8000:8000 link-shortener-api
```

---

## Features

- Minimal FastAPI codebase
- Simple database check endpoint
- Generate and store short URLs
- Retrieve long URLs by short code
- Docker support for easy deployment

---

## Limitations & Improvements

> [!WARNING]
> No user authentication, analytics, or rate limiting yet.  
> The project currently does not handle link expiration or duplicate URLs.

Planned improvements:
- Add authentication
- Track link usage/analytics
- Support for link expiration

---

## License

MIT
