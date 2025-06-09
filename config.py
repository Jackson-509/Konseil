import os

# 🔐 Clé secrète Flask (lue depuis l'environnement)
SECRET_KEY = os.getenv("SECRET_KEY_CONFIG")

# ✉️ Paramètres mail (lus depuis l'environnement)
MAIL_SETTINGS = {
    'MAIL_SERVER': os.getenv('MAIL_SERVER', 'smtp.gmail.com'),
    'MAIL_PORT': int(os.getenv('MAIL_PORT', 587)),
    'MAIL_USE_TLS': os.getenv('MAIL_USE_TLS', 'True') == 'True',
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD')
}

# 📄 Chemin CSV (optionnel)
CSV_FILE = os.getenv("CSV_FILE", "reservations.csv")
