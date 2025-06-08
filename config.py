import os

# Clé secrète Flask sécurisée via variable d'environnement
SECRET_KEY = os.getenv('SECRET_KEY')

# Fichier CSV de réservation
CSV_FILE = 'reservations.csv'

# Configuration SMTP sécurisée
MAIL_SETTINGS = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': os.getenv('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD'),
    'MAIL_DEFAULT_SENDER': (os.getenv('MAIL_SENDER_NAME'), os.getenv('MAIL_USERNAME'))
}
