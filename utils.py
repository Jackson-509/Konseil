import csv, os
from flask_mail import Message
from config import CSV_FILE, MAIL_SETTINGS

def enregistrer_csv(data):
    """Enregistre une réservation dans le fichier CSV."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Nom", "Prénom", "Email", "Service", "Date", "Heure"])
        writer.writerow(data)

def envoyer_mail(mail, prenom, email, service, date, heure):
    """Envoie un email de confirmation de réservation."""
    msg = Message(
        subject="Confirmation de votre réservation",
        sender=MAIL_SETTINGS['MAIL_DEFAULT_SENDER'],
        recipients=[email],
        body=f"""Bonjour {prenom},

Votre réservation pour le service « {service} » le {date} à {heure} a bien été prise en compte.

Merci et à bientôt,
L'équipe Cabinet Conseil
"""
    )
    mail.send(msg)
