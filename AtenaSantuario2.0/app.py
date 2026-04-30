# =========================
# 🚀 IMPORTS
# =========================
from flask import Flask
import pymysql

# 🔹 IMPORTANDO OS MODELS NOVOS
from models.database import db, Cavaleiro, Curiosidade

# 🔹 IMPORTANDO ROTAS
from controllers import routes

# =========================
# ⚙️ CONFIG
# =========================
DB_NAME = 'cdz'  # nome novo do banco

app = Flask(__name__, template_folder='views')

# 🔹 CONFIG MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# =========================
# 🔗 ROTAS
# =========================
routes.init_app(app)

# =========================
# 🛢️ INICIALIZAÇÃO DO BANCO
# =========================
if __name__ == '__main__':

    # 🔹 CRIAR BANCO SE NÃO EXISTIR
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
            print("✅ Banco de dados criado ou já existente!")
    except Exception as error:
        print(f"❌ Erro ao criar banco: {error}")
    finally:
        connection.close()

    # 🔹 INICIAR SQLAlchemy
    db.init_app(app)

    # 🔹 CRIAR TABELAS
    with app.app_context():
        db.create_all()
        print("✅ Tabelas criadas com sucesso!")

    # =========================
    # ▶️ RODAR APP
    # =========================
    app.run(port=5000, debug=True)