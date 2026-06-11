import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "chave_super_secreta")
    
    # Usar PostgreSQL se disponível, senão SQLite
    DATABASE_URL = os.getenv("DATABASE_URL")
    
    if DATABASE_URL:
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        # Fallback para SQLite (desenvolvimento)
        SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Uploads
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}