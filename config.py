import os
from dotenv import load_dotenv

# 🌍 Charge les variables d'environnement depuis le fichier .env
load_dotenv()

# 🔐 Clé secrète Flask
SECRET_KEY = os.getenv('SECRET_KEY')

# 📄 Chemin vers le fichier CSV (optionnel si tu utilises SQLite/SQLAlchemy)
CSV_FILE = os.getenv('CSV_FILE', 'reservations.csv')

# ✉️ Configuration mail (ex: pour envoi de confirmation de réservation)
MAIL_SETTINGS = {
    'MAIL_SERVER': os.getenv('MAIL_SERVER', 'smtp.gmail.com'),
    'MAIL_PORT': int(os.getenv('MAIL_PORT', 587)),
    'MAIL_USE_TLS': os.getenv('MAIL_USE_TLS', 'True') == 'True',
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD'),
    'MAIL_DEFAULT_SENDER': (
        os.getenv('MAIL_SENDER_NAME', 'Konseil Contact'),
        os.getenv('MAIL_USERNAME')
    )
}

# 🧠 Configuration base de données (SQLite par défaut, sinon PostgreSQL via Render)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'reservations.db')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{db_path}')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 🔐 Identifiants admin (pour accès au tableau de bord)
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')  # Nom d'utilisateur par défaut
ADMIN_PASSWORD_HASH = os.getenv('ADMIN_PASSWORD_HASH')  # À générer avec werkzeug.security
