import os
from flask import Flask, render_template, request, redirect, url_for, flash
from utils import enregistrer_csv, envoyer_mail, init_mail
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Initialiser Flask-Mail
init_mail(app)

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
        envoyer_mail(prenom, email, service, date, heure)  # ✅ Envoie le mail

        flash("🎉 Réservation enregistrée avec succès !", "success")
        return redirect(url_for('index'))
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

