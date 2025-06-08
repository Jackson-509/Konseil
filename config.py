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

# 🗃️ Configuration base de données (SQLite par défaut, PostgreSQL sur Render)
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///instance/reservations.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 🔐 Identifiants admin (authentification)
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD_HASH = os.getenv('ADMIN_PASSWORD_HASH')  # Hash généré avec werkzeug
