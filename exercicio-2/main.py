import os
import psycopg2
from fastapi import FastAPI

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        dbname=os.getenv("DB_NAME", "orion_db")
    )

@app.get("/")
def read_root():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Cria a tabela caso não exista e insere um novo acesso
    cur.execute("CREATE TABLE IF NOT EXISTS acessos (id SERIAL PRIMARY KEY, mensagem TEXT);")
    cur.execute("INSERT INTO acessos (mensagem) VALUES ('Hello from Docker + Postgres!');")
    conn.commit()
    
    # Conta quantos registros existem para provar a persistência do volume
    cur.execute("SELECT COUNT(*) FROM acessos;")
    total_acessos = cur.fetchone()[0]
    
    cur.close()
    conn.close()
    
    return {
        "message": "Conectado ao banco com sucesso!",
        "total_acessos_gravados": total_acessos
    }