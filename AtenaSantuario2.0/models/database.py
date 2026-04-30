from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# =========================
# 🛡️ TABELA CAVALEIROS
# =========================
class Cavaleiro(db.Model):
    __tablename__ = 'cavaleiros'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    armadura = db.Column(db.String(150))
    signo = db.Column(db.String(50))
    afiliacao = db.Column(db.String(100))
    status = db.Column(db.String(50))
    tecnicas = db.Column(db.String(200))
    poder = db.Column(db.String(150))
    personalidade = db.Column(db.String(150))

    def __init__(self, nome, armadura, signo, afiliacao, status, tecnicas, poder, personalidade):
        self.nome = nome
        self.armadura = armadura
        self.signo = signo
        self.afiliacao = afiliacao
        self.status = status
        self.tecnicas = tecnicas
        self.poder = poder
        self.personalidade = personalidade


# =========================
# 📚 TABELA CURIOSIDADES
# =========================
class Curiosidade(db.Model):
    __tablename__ = 'curiosidades'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    conteudo = db.Column(db.Text, nullable=False)

    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo