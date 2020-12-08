from flask import Flask
from .config import Config
from .extensions import db, migrate
from .Membro_Equipe.model import Membro_Equipe
from .Pessoa.model import Pessoa
from .Projetos.model import Projeto

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    return app