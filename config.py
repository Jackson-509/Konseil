# config.py
import os

CSV_FILE = 'reservations.csv'
SECRET_KEY = 'top-secret-key'

# Config SMTP Gmail (si tu ajoutes les mails après)
MAIL_SETTINGS = {
    'MAIL_SERVER': 'smtp.gmail.com',
    'MAIL_PORT': 587,
    'MAIL_USE_TLS': True,
    'MAIL_USERNAME': 'ton.email@gmail.com',
    'MAIL_PASSWORD': 'mot_de_passe_application',
    'MAIL_DEFAULT_SENDER': ('Cabinet Conseil', 'ton.email@gmail.com')
}
