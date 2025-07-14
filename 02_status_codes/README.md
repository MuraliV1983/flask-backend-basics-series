# 02 - HTTP Status Codes in Flask API

This example demonstrates how to return proper HTTP status codes with API responses.

## Status Codes Used:
- ✅ 200 OK – Resource returned successfully
- ✅ 201 Created – New resource created
- ❌ 400 Bad Request – Missing/Invalid input
- ❌ 404 Not Found – Resource does not exist

## Endpoints:
- `GET /users/<id>` – Returns a user or 404
- `POST /users` – Creates user or returns 400

## Sample POST:
```json
{
  "name": "New User"
}

Run:
pip install -r requirements.txt
python app.py
