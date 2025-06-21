from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import os

app = Flask(__name__)

# Configuration de l'application
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///konseil.db')
if app.config['SQLALCHEMY_DATABASE_URI'].startswith('postgres://'):
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'].replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration de Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS', '1') == '1'
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL', '0') == '1'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'noreply.konseil@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply.konseil@gmail.com')

# Initialisation des extensions
db = SQLAlchemy(app)
mail = Mail(app)

# Modèles de base de données
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    entreprise = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_contact = db.Column(db.DateTime, default=datetime.utcnow)
    date_rendez_vous = db.Column(db.DateTime, nullable=True)
    statut = db.Column(db.String(20), default='nouveau')

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    date_publication = db.Column(db.DateTime, default=datetime.utcnow)
    auteur = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)

# Fonctions d'envoi d'emails
def envoyer_confirmation_rendez_vous(contact):
    """Envoie un email de confirmation au visiteur"""
    try:
        sujet = f"{os.environ.get('KONSEIL_MAIL_SUBJECT_PREFIX', '[Cabinet Konseil - confirmation]')} Demande de rendez-vous"
        
        msg = Message(
            subject=sujet,
            recipients=[contact.email],
            sender=os.environ.get('KONSEIL_MAIL_SENDER', 'noreply.konseil@gmail.com')
        )
        
        # Corps de l'email en HTML
        msg.html = render_template('emails/confirmation_rendez_vous.html', contact=contact)
        
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Erreur envoi confirmation: {e}")
        return False

def envoyer_notification_cabinet(contact):
    """Envoie une notification au cabinet concernant un nouveau prospect"""
    try:
        sujet = f"[Cabinet Konseil] Nouveau prospect - {contact.nom} - {contact.service}"
        
        msg = Message(
            subject=sujet,
            recipients=[os.environ.get('MAIL_USERNAME', 'noreply.konseil@gmail.com')],
            sender=os.environ.get('KONSEIL_MAIL_SENDER', 'noreply.konseil@gmail.com')
        )
        
        # Corps de l'email en HTML
        msg.html = render_template('emails/notification_cabinet.html', contact=contact)
        
        mail.send(msg)
        return True
    except Exception as e:
        print(f"Erreur envoi notification cabinet: {e}")
        return False

# Routes
@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/articles')
def articles():
    articles = Article.query.order_by(Article.date_publication.desc()).all()
    return render_template('articles.html', articles=articles)

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article_detail.html', article=article)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom = request.form['nom']
        email = request.form['email']
        telephone = request.form['telephone']
        entreprise = request.form['entreprise']
        service = request.form['service']
        message = request.form['message']
        date_rendez_vous = request.form.get('date_rendez_vous')
        
        # Conversion de la date de rendez-vous si fournie
        date_rdv = None
        if date_rendez_vous:
            try:
                date_rdv = datetime.strptime(date_rendez_vous, '%Y-%m-%dT%H:%M')
            except ValueError:
                date_rdv = None
        
        # Création du contact
        contact = Contact(
            nom=nom,
            email=email,
            telephone=telephone,
            entreprise=entreprise,
            service=service,
            message=message,
            date_rendez_vous=date_rdv
        )
        
        try:
            # Sauvegarde en base de données
            db.session.add(contact)
            db.session.commit()
            
            # Envoi des emails
            confirmation_envoyee = envoyer_confirmation_rendez_vous(contact)
            notification_envoyee = envoyer_notification_cabinet(contact)
            
            if confirmation_envoyee and notification_envoyee:
                flash('Votre demande a été envoyée avec succès ! Vous recevrez une confirmation par email.', 'success')
            elif confirmation_envoyee:
                flash('Votre demande a été envoyée. Une confirmation vous a été envoyée par email.', 'success')
            else:
                flash('Votre demande a été enregistrée. Nous vous contacterons bientôt.', 'success')
                
            return redirect(url_for('contact'))
            
        except Exception as e:
            db.session.rollback()
            flash('Une erreur est survenue. Veuillez réessayer.', 'error')
            print(f"Erreur sauvegarde contact: {e}")
    
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 