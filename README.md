# 🌴 Konseil - Cabinet de Conseil aux Antilles

Site vitrine moderne et responsive pour un cabinet de conseil spécialisé aux Antilles (Guadeloupe, Martinique).

## 🎯 Fonctionnalités

### Services proposés
- **Conseil en Stratégie et Pilotage** : Alignez vos projets avec des solutions d'optimisation et de pilotage efficaces
- **Création Digitale** : Sites vitrines, e-commerce et applications mobiles personnalisées
- **Adoptez l'IA** : Automatisez, gagnez du temps et réduisez vos dépenses grâce à l'IA
- **Analyse de Données** : Des dashboards interactifs pour suivre vos performances

### Pages du site
- **Accueil** : Présentation des services avec design moderne
- **Services** : Détail complet de chaque service proposé
- **Articles** : Blog avec articles sur l'économie, la technologie et l'environnement
- **Contact** : Formulaire de contact complet avec base de données

### Fonctionnalités techniques
- ✅ Design responsive (mobile-first)
- ✅ Base de données PostgreSQL (compatible Render)
- ✅ Formulaire de contact fonctionnel
- ✅ Système d'articles avec catégories
- ✅ Interface moderne avec Bootstrap 5
- ✅ Animations et interactions JavaScript
- ✅ Optimisé pour les performances

## 🚀 Déploiement sur Render

### Méthode 1 : Déploiement automatique (Recommandé)

1. **Fork ou clone ce repository** sur GitHub

2. **Connectez-vous à Render** : https://render.com

3. **Créez un nouveau Web Service** :
   - Cliquez sur "New +" → "Web Service"
   - Connectez votre repository GitHub
   - Sélectionnez le repository Konseil

4. **Configuration automatique** :
   - **Name** : `konseil-cabinet-conseil`
   - **Environment** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn app:app`
   - **Plan** : `Free`

5. **Variables d'environnement** (optionnel) :
   - `SECRET_KEY` : Clé secrète générée automatiquement
   - `DATABASE_URL` : Fournie automatiquement par Render

6. **Cliquez sur "Create Web Service"**

### Méthode 2 : Déploiement manuel

1. **Créez une base de données PostgreSQL** sur Render
2. **Créez un Web Service** avec les paramètres ci-dessus
3. **Liez la base de données** au service web
4. **Déployez**

### Configuration de la base de données

La base de données sera automatiquement initialisée avec :
- 4 articles d'exemple (Économie, Technologie, Environnement)
- 3 messages de contact d'exemple

## 🗄️ Base de données

### Structure
- **Table `contact`** : Messages du formulaire de contact
- **Table `article`** : Articles du blog avec catégories

### Initialisation
Le script `init_database.py` crée automatiquement :
- 4 articles d'exemple (Économie, Technologie, Environnement)
- 3 messages de contact d'exemple

## 📁 Structure du projet

```
Konseil-main/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── Procfile              # Configuration pour Render
├── runtime.txt           # Version Python
├── render.yaml           # Configuration automatique Render
├── build.sh              # Script de build
├── init_database.py      # Script d'initialisation de la DB
├── README.md            # Documentation
├── templates/           # Templates Jinja2
│   ├── base.html       # Template de base
│   ├── accueil.html    # Page d'accueil
│   ├── services.html   # Page des services
│   ├── articles.html   # Liste des articles
│   ├── article_detail.html # Détail d'un article
│   └── contact.html    # Page de contact
└── static/             # Fichiers statiques
    ├── css/
    │   └── style.css   # Styles personnalisés
    ├── js/
    │   └── script.js   # JavaScript interactif
    └── images/         # Images du site
```

## 🎨 Design et UX

### Technologies utilisées
- **Bootstrap 5** : Framework CSS responsive
- **Font Awesome** : Icônes modernes
- **CSS personnalisé** : Styles adaptés aux Antilles
- **JavaScript vanilla** : Interactions et animations

### Caractéristiques
- Design moderne et professionnel
- Couleurs adaptées au contexte antillais
- Navigation intuitive
- Animations fluides
- Optimisé mobile

## 🔧 Configuration

### Variables d'environnement Render
```bash
# Clé secrète Flask (générée automatiquement)
SECRET_KEY=your_secret_key_here

# URL de la base de données (fournie par Render)
DATABASE_URL=postgresql://user:password@host:port/database
```

### Personnalisation
- Modifier les couleurs dans `static/css/style.css`
- Ajouter des images dans `static/images/`
- Personnaliser les textes dans les templates

## 📱 Responsive Design

Le site est optimisé pour tous les appareils :
- **Mobile** : Navigation hamburger, contenu adapté
- **Tablet** : Layout intermédiaire
- **Desktop** : Design complet avec sidebar

## 🚀 Déploiement

### Sur Render (Recommandé)
1. Connecter le repository GitHub
2. Configuration automatique via `render.yaml`
3. Base de données PostgreSQL automatique
4. Déploiement automatique à chaque push

### Sur Heroku
1. Créer un `Procfile` :
```
web: gunicorn app:app
```
2. Déployer via Git

## 📊 Fonctionnalités avancées

### Formulaire de contact
- Validation côté client et serveur
- Stockage en base de données PostgreSQL
- Messages de confirmation
- Champs obligatoires et optionnels

### Système d'articles
- Catégorisation (Économie, Technologie, Environnement)
- Pagination automatique
- Filtrage par catégorie
- Articles similaires

### Performance
- Images optimisées
- CSS et JS minifiés
- Lazy loading des images
- Cache des ressources statiques

## 🛠️ Développement

### Ajouter un nouvel article
```python
from app import app, db, Article

with app.app_context():
    article = Article(
        titre="Nouvel article",
        categorie="Economie",
        resume="Résumé de l'article",
        contenu="<p>Contenu HTML de l'article</p>"
    )
    db.session.add(article)
    db.session.commit()
```

### Modifier le design
- Éditer `static/css/style.css`
- Modifier les templates dans `templates/`
- Ajouter des interactions dans `static/js/script.js`

## 📞 Support

Pour toute question ou support :
- 📧 Email : contact@konseil-antilles.fr
- 🌐 Site : https://konseil-antilles.fr

## 📄 Licence

Ce projet est développé pour Konseil - Cabinet de conseil aux Antilles.

---

**🌴 Konseil - Spécialistes en conseil aux Antilles**  
*Guadeloupe • Martinique* 