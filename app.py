import os
from flask import Flask, render_template, request, redirect, url_for, flash, session, Response
from utils import enregistrer_csv, envoyer_mail, init_mail
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URI, ADMIN_USERNAME, ADMIN_PASSWORD_HASH
from models import db, Reservation
from werkzeug.security import check_password_hash
from collections import Counter
import csv
from io import StringIO

# ⚙️ Initialisation de l'app Flask
app = Flask(__name__)
app.secret_key = SECRET_KEY

# 📂 Création du dossier instance/ si besoin
instance_path = os.path.join(os.path.dirname(__file__), 'instance')
os.makedirs(instance_path, exist_ok=True)

# 🧠 Config SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# ✉️ Initialiser Flask-Mail
init_mail(app)

# 🗃️ Création de la base si elle n’existe pas
with app.app_context():
    db.create_all()
    print(f"✅ Base de données utilisée : {app.config['SQLALCHEMY_DATABASE_URI']}")

# 🌐 Page d'accueil + formulaire de réservation
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nom = request.form.get('lastname')
        prenom = request.form.get('firstname')
        email = request.form.get('email')
        service = request.form.get('service')
        date = request.form.get('date')
        heure = request.form.get('time')

        # ✅ Enregistrement CSV + mail
        enregistrer_csv([nom, prenom, email, service, date, heure])
        envoyer_mail(prenom, email, service, date, heure)

        # ✅ Enregistrement base SQLite
        reservation = Reservation(
            nom=nom,
            prenom=prenom,
            email=email,
            service=service,
            date=date,
            heure=heure
        )
        db.session.add(reservation)
        db.session.commit()

        flash("🎉 Réservation enregistrée avec succès !", "success")
        return redirect(url_for('index'))

    return render_template('index.html')

# 🔐 Connexion admin
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, pwd):
            session['logged_in'] = True
            return redirect(url_for('admin'))
        flash("Identifiants incorrects", "error")
    return render_template('login.html')

# 🔓 Déconnexion
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("Déconnecté", "info")
    return redirect(url_for('login'))

# 🗂️ Page admin - voir les réservations
@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    reservations = Reservation.query.all()
    return render_template('admin.html', reservations=reservations)

# 📊 Dashboard de statistiques
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    reservations = Reservation.query.all()
    services = [r.service for r in reservations]
    dates = [r.date for r in reservations]

    service_count = Counter(services)
    date_count = Counter(dates)

    return render_template("dashboard.html", service_count=service_count, date_count=date_count)

# 📥 Export CSV des réservations
@app.route('/export')
def export():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    reservations = Reservation.query.all()

    si = StringIO()
    writer = csv.writer(si)
    writer.writerow(['Nom', 'Prénom', 'Email', 'Service', 'Date', 'Heure'])

    for r in reservations:
        writer.writerow([r.nom, r.prenom, r.email, r.service, r.date, r.heure])

    output = si.getvalue()
    si.close()

    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=reservations.csv"}
    )

# 📄 Pages légales
@app.route('/cgu')
def cgu():
    return render_template('cgu.html')

@app.route('/mentions-legales')
def mentions_legales():
    return render_template('mentions-legales.html')

@app.route('/politique-confidentialite')
def politique_confidentialite():
    return render_template('politique-confidentialite.html')

@app.route('/parametres-cookies')
def parametres_cookies():
    return render_template('parametres-cookies.html')

# 🚀 Lancement local ou via Render
#if __name__ == '__main__':
 #   port = int(os.environ.get("PORT", 5000))
  #  app.run(host='0.0.0.0', port=port)
