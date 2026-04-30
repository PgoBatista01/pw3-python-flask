from flask_sqlalchemy import SQLAlchemy
#carregando o sqlalchemy em uma variavel
db = SQLAlchemy()

#criando uma classe para representar a entidade Games no banco
class Game(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    plataforma = db.Column(db.String(150))
    prego = db.Column(db.Float)
    quantidade = db.Column(db.Integer)
    
    #inicializado as variaveis na classe 
def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
    self.titulo = titulo
    self.ano = ano
    self.categoria = categoria
    self.plataforma = plataforma
    self.preco = preco
    self.quantidade = quantidade