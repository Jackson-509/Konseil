import os

# 🔐 Clé secrète Flask
SECRET_KEY = os.getenv("SECRET_KEY")

# ✉️ Configuration email pour Flask-Mail
MAIL_SETTINGS = {
    'MAIL_SERVER': os.getenv('MAIL_SERVER', 'smtp.gmail.com'),
    'MAIL_PORT': int(os.getenv('MAIL_PORT', 587)),
    'MAIL_USE_TLS': os.getenv('MAIL_USE_TLS', 'True') == 'True',
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD')
}

# 📄 Fichier CSV utilisé pour sauvegarde locale
CSV_FILE = os.getenv("CSV_FILE", "reservations.csv")

# 🧠 Configuration de la base de données
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'reservations.db')

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{db_path}")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 🔐 Identifiants admin
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH")  # Doit être un hash sécurisé
