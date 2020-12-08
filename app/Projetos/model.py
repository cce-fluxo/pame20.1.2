from app.extensions import db

class Projeto(db.Model):
    __tablename__ = 'projeto'

    id_projeto = db.Column(db.Integer, primary_key=True)
    data_inicio = db.Column(db.Date(), nullable=False)
    prazo = db.Column(db.Date(), nullable=False)
    coord = db.Column(db.String(3), nullable=False)
    descricao = db.Column(db.String(200), default="")

    equipe = db.relationship('Membro_Equipe', backref='equipe_projeto')


