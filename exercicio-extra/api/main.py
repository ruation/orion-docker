import os
import psycopg2
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        dbname=os.getenv("DB_NAME", "orion_db")
    )

@app.get("/health")
def health_check():
    """Retorna o status da aplicação conforme exigido no desafio."""
    return {"status": "ok"}

@app.get("/")
def read_root():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS acessos (id SERIAL PRIMARY KEY, mensagem TEXT);")
    cur.execute("INSERT INTO acessos (mensagem) VALUES ('Hello from Extra Challenge!');")
    conn.commit()
    
    cur.execute("SELECT COUNT(*) FROM acessos;")
    total_acessos = cur.fetchone()[0]
    
    cur.close()
    conn.close()
    
    return {
        "message": "Stack completa (API + DB + Admin) operando com sucesso!",
        "total_acessos": total_acessos
    }