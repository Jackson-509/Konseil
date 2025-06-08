from flask import Flask, render_template, request, redirect, url_for, flash
import csv, os
from utils import send_email, init_mail
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

CSV_FILE = 'reservations.csv'

init_mail(app)  # ✅ Initialisation de Flask-Mail

def enregistrer_csv(data):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Nom", "Prénom", "Email", "Service", "Date", "Heure"])
        writer.writerow(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nom = request.form.get('lastname')
        prenom = request.form.get('firstname')
        email = request.form.get('email')
        service = request.form.get('service')
        date = request.form.get('date')
        heure = request.form.get('time')

        enregistrer_csv([nom, prenom, email, service, date, heure])
        send_email(email, nom, prenom, service, date, heure)  # ✅ Envoi de l’email

        flash("🎉 Réservation enregistrée avec succès !", "success")
        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
