# Comentário no Python
# Importando o Flask para a aplicação
from flask import Flask, render_template
#importanto PYMYSQL
import pymysql
#criando um nomw para o banco
from models.database import db,Game
DB_NAME = 'thegames'

#Importando o controller
from controllers import routes
# Carregando o Flask na variável "app"
# Declarando variável no Python
app = Flask(__name__, template_folder='views')
# Variáveis com __ são variáveis de ambiente do Python
# __name__ representa o nome da aplicação
# CRIANDO A ROTA PRINCIPAL DO SITE

#passando o nome do banco para o flask
app.config['DATABASE_NAME'] = DB_NAME
#passando o endereço do banco para o flask-SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'

app.config['SECRET_KEY'] = 'paulinha'
routes.init_app(app)
# Iniciando o servidor na porta 5000
if __name__ == '__main__':
    # conectando ao mysql para criar o banco de dados
    #passando os dados de conexao
    connection = pymysql.connect(host='localhost',user='root',password='',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            #enviando a query
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
            print("o banco de dados esta criado!")
    except Exception as error:
        print(f"ocorreu um erro ao criar o banco de dados! {error}")
    finally:
        connection.close()
        
    #inicializando o FLASK-SQLALCHEMY 
    db.init_app(app=app)
    #enviando a requisição para criar as tabelas
    with app.test_request_context():
        db.create_all()
        #inicializando  o servidor
    # Verificando se o arquivo gravado em __name__ é o arquivo principal
    app.run(port=5000, debug=True)
# O método .run() inicia o servidor
