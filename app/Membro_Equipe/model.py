from app.extensions import db

class Membro_Equipe(db.Model):
    __tablename__ = "membro_equipe"

    id_membro = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(10), nullable=False)

    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id_pessoa'))
    id_projeto = db.Column(db.Integer, db.ForeignKey('projeto.id_projeto'))