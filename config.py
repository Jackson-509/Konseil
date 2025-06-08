import os

# Clé secrète Flask
SECRET_KEY = 'a37e82b963bf4b6aa5e0c720de78a922'

# Fichier CSV de réservation
CSV_FILE = 'reservations.csv'

# Configuration SMTP pour Gmail
MAIL_SETTINGS = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': 'info.aristil.jackson@gmail.com',
    'MAIL_PASSWORD': 'fiue vrep gjwz zsep',  # 🔐 À remplacer par ton mot de passe d’application Gmail
    'MAIL_DEFAULT_SENDER': ('Cabinet Conseil', 'info.aristil.jackson@gmail.com')
}