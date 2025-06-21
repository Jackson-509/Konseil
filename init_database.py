#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'initialisation de la base de données Konseil
Ajoute des données d'exemple pour les articles et contacts
Compatible avec Render et PostgreSQL
"""

from app import app, db, Contact, Article
from datetime import datetime

def init_database():
    with app.app_context():
        # Supprimer toutes les tables existantes
        db.drop_all()
        
        # Créer toutes les tables
        db.create_all()
        
        # Ajouter des contacts d'exemple
        contacts = [
            Contact(
                nom="Jean Dupont",
                email="jean.dupont@entreprise.com",
                telephone="+590 590 12 34 56",
                entreprise="Entreprise Antillaise SARL",
                service="Conseil en Stratégie",
                message="Bonjour, nous souhaitons développer une stratégie digitale pour notre entreprise. Pouvez-vous nous accompagner ?",
                date_contact=datetime.now(),
                statut="nouveau"
            ),
            Contact(
                nom="Marie Martin",
                email="marie.martin@startup.fr",
                telephone="+590 590 98 76 54",
                entreprise="Startup Innovation",
                service="Création Digitale",
                message="Nous avons besoin d'un site web moderne pour notre startup. Avez-vous des créneaux disponibles ?",
                date_contact=datetime.now(),
                statut="nouveau"
            ),
            Contact(
                nom="Pierre Durand",
                email="pierre.durand@commerce.com",
                telephone="+590 590 11 22 33",
                entreprise="Commerce Local",
                service="Adoption IA",
                message="Intéressé par l'automatisation de notre service client avec l'IA. Pouvez-vous nous expliquer les possibilités ?",
                date_contact=datetime.now(),
                statut="nouveau"
            )
        ]
        
        for contact in contacts:
            db.session.add(contact)
        
        # Ajouter des articles d'exemple
        articles = [
            Article(
                titre="La transformation digitale aux Antilles : enjeux et opportunités",
                contenu="""
                <p>La transformation digitale représente un défi majeur pour les entreprises antillaises. 
                Dans un contexte insulaire, les enjeux sont multiples : connectivité, formation, adaptation 
                des processus...</p>
                
                <h3>Les défis spécifiques aux Antilles</h3>
                <p>Les entreprises antillaises font face à des défis uniques :</p>
                <ul>
                    <li>Connectivité internet parfois limitée</li>
                    <li>Formation des équipes aux nouvelles technologies</li>
                    <li>Adaptation des processus aux spécificités locales</li>
                    <li>Gestion des contraintes logistiques insulaires</li>
                </ul>
                
                <h3>Les opportunités</h3>
                <p>Malgré ces défis, les opportunités sont nombreuses :</p>
                <ul>
                    <li>Marché en forte croissance</li>
                    <li>Besoin d'innovation dans tous les secteurs</li>
                    <li>Potentiel d'export vers la Caraïbe</li>
                    <li>Développement de l'économie numérique</li>
                </ul>
                
                <p>Chez Konseil, nous accompagnons les entreprises antillaises dans cette transformation 
                en tenant compte des spécificités locales et en proposant des solutions adaptées.</p>
                """,
                categorie="Transformation Digitale",
                date_publication=datetime.now(),
                auteur="Équipe Konseil",
                image_url="https://via.placeholder.com/800x400/0d6efd/ffffff?text=Transformation+Digitale"
            ),
            Article(
                titre="L'intelligence artificielle : un levier de croissance pour les PME",
                contenu="""
                <p>L'intelligence artificielle n'est plus réservée aux grandes entreprises. 
                Les PME peuvent également en bénéficier pour optimiser leurs processus et 
                améliorer leur compétitivité.</p>
                
                <h3>Applications concrètes pour les PME</h3>
                <p>Voici quelques applications pratiques de l'IA pour les petites et moyennes entreprises :</p>
                
                <h4>1. Service client automatisé</h4>
                <p>Les chatbots intelligents peuvent gérer les demandes récurrentes, 
                libérant du temps pour les équipes commerciales.</p>
                
                <h4>2. Analyse prédictive</h4>
                <p>L'IA peut analyser les données clients pour prédire les tendances 
                et optimiser les stocks.</p>
                
                <h4>3. Automatisation des tâches répétitives</h4>
                <p>De nombreuses tâches administratives peuvent être automatisées 
                grâce à l'IA.</p>
                
                <h3>Comment commencer ?</h3>
                <p>La mise en place de l'IA doit être progressive :</p>
                <ol>
                    <li>Identifier les processus les plus adaptés</li>
                    <li>Former les équipes</li>
                    <li>Commencer par des projets pilotes</li>
                    <li>Étendre progressivement</li>
                </ol>
                
                <p>Notre équipe d'experts vous accompagne dans cette démarche 
                d'adoption de l'IA.</p>
                """,
                categorie="Intelligence Artificielle",
                date_publication=datetime.now(),
                auteur="Expert IA Konseil",
                image_url="https://via.placeholder.com/800x400/28a745/ffffff?text=Intelligence+Artificielle"
            ),
            Article(
                titre="Stratégie digitale : les 5 étapes clés pour réussir",
                contenu="""
                <p>Une stratégie digitale réussie nécessite une approche structurée 
                et méthodique. Voici les 5 étapes essentielles pour transformer 
                votre entreprise.</p>
                
                <h3>Étape 1 : Audit et diagnostic</h3>
                <p>Commencer par un audit complet de votre situation actuelle :</p>
                <ul>
                    <li>Analyse de votre présence en ligne</li>
                    <li>Évaluation de vos processus internes</li>
                    <li>Étude de votre concurrence</li>
                    <li>Identification des opportunités</li>
                </ul>
                
                <h3>Étape 2 : Définition des objectifs</h3>
                <p>Fixer des objectifs SMART (Spécifiques, Mesurables, Atteignables, 
                Réalistes, Temporels) :</p>
                <ul>
                    <li>Augmentation du chiffre d'affaires</li>
                    <li>Amélioration de l'expérience client</li>
                    <li>Optimisation des processus</li>
                    <li>Réduction des coûts</li>
                </ul>
                
                <h3>Étape 3 : Élaboration de la stratégie</h3>
                <p>Développer une stratégie cohérente avec vos objectifs :</p>
                <ul>
                    <li>Choix des canaux digitaux</li>
                    <li>Définition du plan d'action</li>
                    <li>Allocation des ressources</li>
                    <li>Planning de mise en œuvre</li>
                </ul>
                
                <h3>Étape 4 : Mise en œuvre</h3>
                <p>Exécuter votre stratégie de manière progressive :</p>
                <ul>
                    <li>Développement des solutions</li>
                    <li>Formation des équipes</li>
                    <li>Tests et ajustements</li>
                    <li>Déploiement</li>
                </ul>
                
                <h3>Étape 5 : Suivi et optimisation</h3>
                <p>Mesurer les résultats et optimiser en continu :</p>
                <ul>
                    <li>Suivi des KPIs</li>
                    <li>Analyse des performances</li>
                    <li>Ajustements stratégiques</li>
                    <li>Amélioration continue</li>
                </ul>
                
                <p>Chez Konseil, nous vous accompagnons à chaque étape de votre 
                transformation digitale avec une approche personnalisée et adaptée 
                au contexte antillais.</p>
                """,
                categorie="Stratégie",
                date_publication=datetime.now(),
                auteur="Consultant Stratégie Konseil",
                image_url="https://via.placeholder.com/800x400/dc3545/ffffff?text=Stratégie+Digitale"
            )
        ]
        
        for article in articles:
            db.session.add(article)
        
        # Valider toutes les modifications
        db.session.commit()
        
        print("✅ Base de données initialisée avec succès !")
        print(f"📊 {len(contacts)} contacts d'exemple ajoutés")
        print(f"📝 {len(articles)} articles d'exemple ajoutés")

if __name__ == "__main__":
    init_database() 