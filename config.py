import os

# 🔐 Clé secrète Flask
SECRET_KEY = os.getenv('SECRET_KEY')

# 📄 Fichier CSV (utilisé si tu continues à enregistrer localement aussi)
CSV_FILE = 'reservations.csv'

# ✉️ Configuration mail
MAIL_SETTINGS = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD'),
    'MAIL_DEFAULT_SENDER': (os.getenv('MAIL_SENDER_NAME'), os.getenv('MAIL_USERNAME'))
}

# 🧠 Chemin absolu pour la base SQLite (fix Render)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'reservations.db')

# 🗃️ Config DB (SQLite ou PostgreSQL via DATABASE_URL)
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f'sqlite:///{db_path}')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 🔐 Identifiants admin
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD_HASH = os.getenv('ADMIN_PASSWORD_HASH')  # Hash généré avec werkzeug
