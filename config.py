import os

# Clé secrète Flask
SECRET_KEY = 'top-secret-key'

# Fichier CSV de réservation
CSV_FILE = 'reservations.csv'

# Configuration SMTP pour Gmail
MAIL_SETTINGS = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': 'info.aristil.jackson@gmail.com',
    'MAIL_PASSWORD': 'O1j1#l92',  # 🔐 À remplacer par ton mot de passe d’application Gmail
    'MAIL_DEFAULT_SENDER': ('Cabinet Conseil', 'info.aristil.jackson@gmail.com')
}

