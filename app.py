from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'votre_cle_secrete_ici')

# Configuration de la base de données pour Render
# Render fournit automatiquement DATABASE_URL pour PostgreSQL
database_url = os.environ.get('DATABASE_URL')
if database_url and database_url.startswith('postgres://'):
    # Render utilise postgres:// mais SQLAlchemy attend postgresql://
    database_url = database_url.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url or 'sqlite:///konseil.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèles de base de données
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    service = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    heure = db.Column(db.String(5), nullable=False)
    message = db.Column(db.Text)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    categorie = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(200))
    resume = db.Column(db.Text, nullable=False)
    contenu = db.Column(db.Text, nullable=False)
    date_creation = db.Column(db.DateTime, default=datetime.utcnow)

# Routes
@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/articles')
def articles():
    articles_list = Article.query.order_by(Article.date_creation.desc()).all()
    return render_template('articles.html', articles=articles_list)

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    article = Article.query.get_or_404(article_id)
    return render_template('article_detail.html', article=article)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        email = request.form['email']
        service = request.form['service']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        heure = request.form['heure']
        message = request.form['message']
        
        contact = Contact(
            nom=nom,
            prenom=prenom,
            email=email,
            service=service,
            date=date,
            heure=heure,
            message=message
        )
        
        db.session.add(contact)
        db.session.commit()
        
        flash('Votre message a été envoyé avec succès !', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Configuration pour Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 