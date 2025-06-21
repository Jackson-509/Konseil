#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'initialisation de la base de données Konseil
Ajoute des données d'exemple pour les articles et contacts
Compatible avec Render et PostgreSQL
"""

from app import app, db, Article, Contact
from datetime import datetime, timedelta
import os

def init_database():
    """Initialise la base de données avec des données d'exemple"""
    
    with app.app_context():
        # Créer les tables
        db.create_all()
        
        # Vérifier si des données existent déjà
        if Article.query.first():
            print("⚠️  Des articles existent déjà dans la base de données.")
            return
        
        print("🚀 Initialisation de la base de données Konseil...")
        
        # Articles d'exemple
        articles_data = [
            {
                'titre': 'L\'économie numérique aux Antilles : opportunités et défis',
                'categorie': 'Economie',
                'image': 'https://via.placeholder.com/800x400/007bff/ffffff?text=Economie+Numerique+Antilles',
                'resume': 'Découvrez les opportunités et défis de la transformation digitale pour les entreprises antillaises dans un contexte économique en pleine évolution.',
                'contenu': '''
                <h2>Introduction</h2>
                <p>L'économie numérique représente une opportunité majeure pour les Antilles françaises. Dans un contexte de mondialisation et de digitalisation accélérée, les entreprises locales doivent s'adapter pour rester compétitives.</p>
                
                <h3>Les enjeux de la transformation digitale</h3>
                <p>La transformation digitale aux Antilles présente des défis spécifiques :</p>
                <ul>
                    <li>Infrastructure numérique à développer</li>
                    <li>Formation des compétences digitales</li>
                    <li>Adaptation aux nouvelles technologies</li>
                    <li>Intégration dans l'écosystème numérique régional</li>
                </ul>
                
                <h3>Opportunités pour les entreprises</h3>
                <p>Les entreprises antillaises peuvent bénéficier de :</p>
                <ul>
                    <li>Nouveaux marchés accessibles via le digital</li>
                    <li>Optimisation des processus internes</li>
                    <li>Amélioration de la relation client</li>
                    <li>Réduction des coûts opérationnels</li>
                </ul>
                
                <h3>Conclusion</h3>
                <p>L'adoption des technologies numériques est essentielle pour la compétitivité des entreprises antillaises. Un accompagnement spécialisé peut faciliter cette transition.</p>
                '''
            },
            {
                'titre': 'L\'IA au service des PME : guide pratique',
                'categorie': 'Technologie',
                'image': 'https://via.placeholder.com/800x400/28a745/ffffff?text=IA+PME+Guide',
                'resume': 'Comment l\'intelligence artificielle peut transformer les petites et moyennes entreprises et améliorer leur productivité.',
                'contenu': '''
                <h2>Qu'est-ce que l'IA pour les PME ?</h2>
                <p>L'intelligence artificielle n'est plus réservée aux grandes entreprises. Les PME peuvent aujourd'hui bénéficier de solutions IA accessibles et adaptées à leurs besoins.</p>
                
                <h3>Applications concrètes</h3>
                <p>Voici quelques applications pratiques de l'IA pour les PME :</p>
                <ul>
                    <li><strong>Automatisation des tâches répétitives :</strong> Traitement de factures, gestion des emails</li>
                    <li><strong>Service client intelligent :</strong> Chatbots pour répondre aux questions fréquentes</li>
                    <li><strong>Analyse prédictive :</strong> Anticipation des tendances de vente</li>
                    <li><strong>Optimisation des processus :</strong> Amélioration de l'efficacité opérationnelle</li>
                </ul>
                
                <h3>Mise en œuvre étape par étape</h3>
                <ol>
                    <li>Identifier les processus à automatiser</li>
                    <li>Choisir les outils IA appropriés</li>
                    <li>Former les équipes</li>
                    <li>Implémenter progressivement</li>
                    <li>Mesurer et optimiser</li>
                </ol>
                
                <h3>Bénéfices attendus</h3>
                <p>L'adoption de l'IA peut apporter :</p>
                <ul>
                    <li>Réduction de 30% des coûts opérationnels</li>
                    <li>Amélioration de 40% de la productivité</li>
                    <li>Meilleure satisfaction client</li>
                    <li>Avantage concurrentiel</li>
                </ul>
                '''
            },
            {
                'titre': 'Tech verte aux Antilles : solutions durables',
                'categorie': 'Environnement',
                'image': 'https://via.placeholder.com/800x400/ffc107/000000?text=Tech+Verte+Antilles',
                'resume': 'Les solutions technologiques pour un développement durable dans les Caraïbes et leur impact sur l\'environnement local.',
                'contenu': '''
                <h2>Développement durable aux Antilles</h2>
                <p>Les Antilles font face à des défis environnementaux uniques. La technologie verte offre des solutions innovantes pour un développement durable.</p>
                
                <h3>Enjeux environnementaux locaux</h3>
                <p>Les principaux défis environnementaux aux Antilles :</p>
                <ul>
                    <li>Gestion des déchets et recyclage</li>
                    <li>Énergies renouvelables</li>
                    <li>Protection de la biodiversité marine</li>
                    <li>Adaptation au changement climatique</li>
                </ul>
                
                <h3>Solutions technologiques vertes</h3>
                <h4>Énergies renouvelables</h4>
                <p>L'énergie solaire et éolienne sont particulièrement adaptées au climat antillais :</p>
                <ul>
                    <li>Panneaux solaires intelligents</li>
                    <li>Systèmes de stockage d'énergie</li>
                    <li>Gestion intelligente de la consommation</li>
                </ul>
                
                <h4>Gestion intelligente des ressources</h4>
                <p>Technologies pour optimiser l'utilisation des ressources :</p>
                <ul>
                    <li>Capteurs IoT pour le monitoring environnemental</li>
                    <li>Systèmes de gestion d'eau intelligents</li>
                    <li>Optimisation des chaînes logistiques</li>
                </ul>
                
                <h3>Impact économique</h3>
                <p>L'adoption de technologies vertes peut :</p>
                <ul>
                    <li>Créer de nouveaux emplois</li>
                    <li>Réduire les coûts énergétiques</li>
                    <li>Attirer des investissements durables</li>
                    <li>Améliorer l'image de marque des entreprises</li>
                </ul>
                
                <h3>Conclusion</h3>
                <p>La technologie verte représente une opportunité unique pour les Antilles de concilier développement économique et protection environnementale.</p>
                '''
            },
            {
                'titre': 'Transformation digitale : guide pour les entreprises antillaises',
                'categorie': 'Economie',
                'image': 'https://via.placeholder.com/800x400/dc3545/ffffff?text=Transformation+Digitale',
                'resume': 'Un guide complet pour accompagner les entreprises antillaises dans leur transformation digitale et leur adaptation aux nouvelles technologies.',
                'contenu': '''
                <h2>Pourquoi se digitaliser ?</h2>
                <p>La transformation digitale n'est plus une option mais une nécessité pour survivre dans l'économie moderne. Les entreprises antillaises doivent s'adapter rapidement.</p>
                
                <h3>Étapes de la transformation digitale</h3>
                <h4>1. Diagnostic et audit</h4>
                <p>Évaluer la maturité digitale actuelle de l'entreprise :</p>
                <ul>
                    <li>Analyse des processus existants</li>
                    <li>Évaluation des compétences numériques</li>
                    <li>Identification des opportunités d'amélioration</li>
                </ul>
                
                <h4>2. Définition de la stratégie</h4>
                <p>Élaborer une feuille de route claire :</p>
                <ul>
                    <li>Objectifs de transformation</li>
                    <li>Priorités d'investissement</li>
                    <li>Planning de mise en œuvre</li>
                </ul>
                
                <h4>3. Formation et accompagnement</h4>
                <p>Préparer les équipes au changement :</p>
                <ul>
                    <li>Formation aux nouveaux outils</li>
                    <li>Accompagnement au changement</li>
                    <li>Développement des compétences</li>
                </ul>
                
                <h3>Technologies clés</h3>
                <p>Les technologies essentielles pour la transformation :</p>
                <ul>
                    <li><strong>Cloud Computing :</strong> Flexibilité et réduction des coûts</li>
                    <li><strong>Big Data :</strong> Analyse et prise de décision</li>
                    <li><strong>IA et Machine Learning :</strong> Automatisation intelligente</li>
                    <li><strong>IoT :</strong> Connectivité et monitoring</li>
                </ul>
                
                <h3>Mesurer le succès</h3>
                <p>Indicateurs de performance à suivre :</p>
                <ul>
                    <li>Productivité des employés</li>
                    <li>Satisfaction client</li>
                    <li>Réduction des coûts</li>
                    <li>Nouveaux revenus générés</li>
                </ul>
                '''
            }
        ]
        
        # Ajouter les articles
        for article_data in articles_data:
            article = Article(**article_data)
            db.session.add(article)
        
        # Messages de contact d'exemple
        contacts_data = [
            {
                'nom': 'Dupont',
                'prenom': 'Marie',
                'email': 'marie.dupont@email.com',
                'service': 'Création Digitale',
                'date': datetime.now().date() + timedelta(days=7),
                'heure': '14:00',
                'message': 'Bonjour, je souhaite créer un site e-commerce pour ma boutique de produits locaux en Guadeloupe. Pouvez-vous me contacter pour discuter du projet ?'
            },
            {
                'nom': 'Martin',
                'prenom': 'Jean-Pierre',
                'email': 'jp.martin@entreprise.fr',
                'service': 'Conseil en Stratégie et Pilotage',
                'date': datetime.now().date() + timedelta(days=3),
                'heure': '10:00',
                'message': 'Nous cherchons un accompagnement pour optimiser nos processus internes et améliorer notre productivité. Merci de nous recontacter.'
            },
            {
                'nom': 'Rousseau',
                'prenom': 'Sophie',
                'email': 'sophie.rousseau@tech-antilles.com',
                'service': 'Adoptez l\'IA',
                'date': datetime.now().date() + timedelta(days=14),
                'heure': '16:00',
                'message': 'Intéressée par l\'intégration de solutions IA dans notre entreprise. Nous aimerions en savoir plus sur vos services.'
            }
        ]
        
        # Ajouter les contacts
        for contact_data in contacts_data:
            contact = Contact(**contact_data)
            db.session.add(contact)
        
        # Sauvegarder les changements
        db.session.commit()
        
        print("✅ Base de données initialisée avec succès !")
        print(f"📰 {len(articles_data)} articles créés")
        print(f"📧 {len(contacts_data)} messages de contact créés")
        print("\n🌴 Konseil - Cabinet de conseil aux Antilles")
        print("📧 Contact: contact@konseil-antilles.fr")

if __name__ == '__main__':
    init_database() 