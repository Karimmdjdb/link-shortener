import os
from dotenv import load_dotenv
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import psycopg

load_dotenv()
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

app = FastAPI()

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



@app.get("/{link}")
def test(link: str):
    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("SELECT init FROM links WHERE short=%s", (link,))
        res = cur.fetchone()[0]
        print(res)
        cur.close()
        conn.close()
        return JSONResponse(content={"full-link":res}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": e.__traceback__}, status_code=500)

def db_connect():
    return psycopg.connect(
        host= "localhost",
        port = 5432,
        dbname = POSTGRES_DB,
        user = POSTGRES_USER,
        password= POSTGRES_PASSWORD
    )