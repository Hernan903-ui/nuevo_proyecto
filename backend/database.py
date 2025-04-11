from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Inicialización de la base de datos con SQLAlchemy
db = SQLAlchemy()

def init_database(app: Flask):
    """
    Configura la base de datos con los parámetros del archivo de configuración Flask.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/inventory_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializa la sesión de la base de datos
    db.init_app(app)

    # Crear tablas si no existen
    with app.app_context():
        db.create_all()
        print("Tablas creadas exitosamente (si no existían).")

# Alternativa para manejar sesiones manualmente (opcional)
def create_scoped_session(database_uri):
    """
    Crea una sesión controlada para manejar las conexiones manualmente.
    """
    engine = create_engine(database_uri, convert_unicode=True)
    session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    return scoped_session(session_factory)