from app.extensions import db

class Pessoa(db.Model):
    __tablename__ = "pessoa"

    id_pessoa = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    especial = db.Column(db.String(50), default="")
    carga_horaria =  db.Column(db.Integer, default=0)
    numero_de_projetos = db.Column(db.Integer, default=0)
    telefone = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)

    equipe = db.relationship('Membro_Equipe', backref='equipe_pessoas')


