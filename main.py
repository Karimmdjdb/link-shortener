import os
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import psycopg
import random
import string


# --- Environment variables
load_dotenv()
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# --- Constants
alphabet = string.ascii_letters + string.digits

# --- Config
app = FastAPI()

# --- Routes
@app.get("/db-check")
def  db_check():
    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        cur.close()
        conn.close()
        return JSONResponse(content={"message":"db connexion success !"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": e.__traceback__}, status_code=500)

@app.get("/{short_link}")
def get_full_link(short_link: str):
    try:
        conn = db_connect()
        with conn.cursor() as cur:
            cur.execute("SELECT full_url FROM links WHERE short_url=%s", (short_link,))
            row = cur.fetchone()
            res = row and row[0]
            cur.close()
        conn.close()
        content = {"url":res} if res is not None else {}
        status = 200 if res is not None else 404
        return JSONResponse(content=content, status_code=status)
    except Exception as e:
        return JSONResponse(content={"error": e.__traceback__}, status_code=500)

@app.post("/save")
async def save_new_link(request: Request):
    data = await request.json()
    short_link = ''.join(random.choices(alphabet, k=15))
    conn = db_connect()
    with conn.cursor() as cur:
        cur.execute("INSERT INTO links (full_url, short_url) values (%s, %s)", (data["link"], short_link))
        conn.commit()
        cur.close()
    conn.close()


# --- Helpers
def db_connect():
    return psycopg.connect(
        host= "localhost",
        port = 5432,
        dbname = POSTGRES_DB,
        user = POSTGRES_USER,
        password= POSTGRES_PASSWORD
    )