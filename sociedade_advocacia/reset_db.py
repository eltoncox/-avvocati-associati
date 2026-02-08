import os

DB_PATH = "sistema.db"

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print("Banco apagado com sucesso.")
else:
    print("Banco não existe.")
