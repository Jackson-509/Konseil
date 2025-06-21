-- Script d'initialisation de la base de données Konseil
-- Compatible PostgreSQL pour Render

-- Création des tables (si elles n'existent pas déjà)
-- Note: Flask-SQLAlchemy crée automatiquement les tables, ce script ajoute des données d'exemple

-- Insertion d'articles d'exemple
INSERT INTO article (titre, categorie, image, resume, contenu, date_creation) VALUES
(
    'L''économie numérique aux Antilles : opportunités et défis',
    'Economie',
    'https://via.placeholder.com/800x400/007bff/ffffff?text=Economie+Numerique+Antilles',
    'Découvrez les opportunités et défis de la transformation digitale pour les entreprises antillaises dans un contexte économique en pleine évolution.',
    '<h2>Introduction</h2>
    <p>L''économie numérique représente une opportunité majeure pour les Antilles françaises. Dans un contexte de mondialisation et de digitalisation accélérée, les entreprises locales doivent s''adapter pour rester compétitives.</p>
    
    <h3>Les enjeux de la transformation digitale</h3>
    <p>La transformation digitale aux Antilles présente des défis spécifiques :</p>
    <ul>
        <li>Infrastructure numérique à développer</li>
        <li>Formation des compétences digitales</li>
        <li>Adaptation aux nouvelles technologies</li>
        <li>Intégration dans l''écosystème numérique régional</li>
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
    <p>L''adoption des technologies numériques est essentielle pour la compétitivité des entreprises antillaises. Un accompagnement spécialisé peut faciliter cette transition.</p>',
    CURRENT_TIMESTAMP
),
(
    'L''IA au service des PME : guide pratique',
    'Technologie',
    'https://via.placeholder.com/800x400/28a745/ffffff?text=IA+PME+Guide',
    'Comment l''intelligence artificielle peut transformer les petites et moyennes entreprises et améliorer leur productivité.',
    '<h2>Qu''est-ce que l''IA pour les PME ?</h2>
    <p>L''intelligence artificielle n''est plus réservée aux grandes entreprises. Les PME peuvent aujourd''hui bénéficier de solutions IA accessibles et adaptées à leurs besoins.</p>
    
    <h3>Applications concrètes</h3>
    <p>Voici quelques applications pratiques de l''IA pour les PME :</p>
    <ul>
        <li><strong>Automatisation des tâches répétitives :</strong> Traitement de factures, gestion des emails</li>
        <li><strong>Service client intelligent :</strong> Chatbots pour répondre aux questions fréquentes</li>
        <li><strong>Analyse prédictive :</strong> Anticipation des tendances de vente</li>
        <li><strong>Optimisation des processus :</strong> Amélioration de l''efficacité opérationnelle</li>
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
    <p>L''adoption de l''IA peut apporter :</p>
    <ul>
        <li>Réduction de 30% des coûts opérationnels</li>
        <li>Amélioration de 40% de la productivité</li>
        <li>Meilleure satisfaction client</li>
        <li>Avantage concurrentiel</li>
    </ul>',
    CURRENT_TIMESTAMP
),
(
    'Tech verte aux Antilles : solutions durables',
    'Environnement',
    'https://via.placeholder.com/800x400/ffc107/000000?text=Tech+Verte+Antilles',
    'Les solutions technologiques pour un développement durable dans les Caraïbes et leur impact sur l''environnement local.',
    '<h2>Développement durable aux Antilles</h2>
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
    <p>L''énergie solaire et éolienne sont particulièrement adaptées au climat antillais :</p>
    <ul>
        <li>Panneaux solaires intelligents</li>
        <li>Systèmes de stockage d''énergie</li>
        <li>Gestion intelligente de la consommation</li>
    </ul>
    
    <h4>Gestion intelligente des ressources</h4>
    <p>Technologies pour optimiser l''utilisation des ressources :</p>
    <ul>
        <li>Capteurs IoT pour le monitoring environnemental</li>
        <li>Systèmes de gestion d''eau intelligents</li>
        <li>Optimisation des chaînes logistiques</li>
    </ul>
    
    <h3>Impact économique</h3>
    <p>L''adoption de technologies vertes peut :</p>
    <ul>
        <li>Créer de nouveaux emplois</li>
        <li>Réduire les coûts énergétiques</li>
        <li>Attirer des investissements durables</li>
        <li>Améliorer l''image de marque des entreprises</li>
    </ul>
    
    <h3>Conclusion</h3>
    <p>La technologie verte représente une opportunité unique pour les Antilles de concilier développement économique et protection environnementale.</p>',
    CURRENT_TIMESTAMP
),
(
    'Transformation digitale : guide pour les entreprises antillaises',
    'Economie',
    'https://via.placeholder.com/800x400/dc3545/ffffff?text=Transformation+Digitale',
    'Un guide complet pour accompagner les entreprises antillaises dans leur transformation digitale et leur adaptation aux nouvelles technologies.',
    '<h2>Pourquoi se digitaliser ?</h2>
    <p>La transformation digitale n''est plus une option mais une nécessité pour survivre dans l''économie moderne. Les entreprises antillaises doivent s''adapter rapidement.</p>
    
    <h3>Étapes de la transformation digitale</h3>
    <h4>1. Diagnostic et audit</h4>
    <p>Évaluer la maturité digitale actuelle de l''entreprise :</p>
    <ul>
        <li>Analyse des processus existants</li>
        <li>Évaluation des compétences numériques</li>
        <li>Identification des opportunités d''amélioration</li>
    </ul>
    
    <h4>2. Définition de la stratégie</h4>
    <p>Élaborer une feuille de route claire :</p>
    <ul>
        <li>Objectifs de transformation</li>
        <li>Priorités d''investissement</li>
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
    </ul>',
    CURRENT_TIMESTAMP
),
(
    'Cybersécurité : protéger votre entreprise aux Antilles',
    'Technologie',
    'https://via.placeholder.com/800x400/6f42c1/ffffff?text=Cybersecurite+Antilles',
    'Les enjeux de cybersécurité pour les entreprises antillaises et les bonnes pratiques à adopter pour protéger vos données.',
    '<h2>Menaces cybernétiques aux Antilles</h2>
    <p>Les entreprises antillaises ne sont pas épargnées par les menaces cybernétiques. La protection des données est devenue cruciale.</p>
    
    <h3>Types de menaces</h3>
    <p>Les principales menaces auxquelles font face les entreprises :</p>
    <ul>
        <li><strong>Ransomware :</strong> Chiffrement des données contre rançon</li>
        <li><strong>Phishing :</strong> Tentatives d''escroquerie par email</li>
        <li><strong>Attaques par déni de service :</strong> Saturation des systèmes</li>
        <li><strong>Vol de données :</strong> Accès non autorisé aux informations</li>
    </ul>
    
    <h3>Bonnes pratiques de sécurité</h3>
    <h4>Protection des accès</h4>
    <ul>
        <li>Mots de passe forts et authentification à deux facteurs</li>
        <li>Gestion des droits d''accès</li>
        <li>Surveillance des connexions</li>
    </ul>
    
    <h4>Sauvegarde et récupération</h4>
    <ul>
        <li>Sauvegardes régulières et sécurisées</li>
        <li>Plan de reprise d''activité</li>
        <li>Tests de restauration</li>
    </ul>
    
    <h4>Sensibilisation des équipes</h4>
    <ul>
        <li>Formation à la cybersécurité</li>
        <li>Simulations d''attaques</li>
        <li>Procédures d''urgence</li>
    </ul>
    
    <h3>Solutions technologiques</h3>
    <p>Outils de protection recommandés :</p>
    <ul>
        <li>Antivirus et antimalware</li>
        <li>Pare-feu nouvelle génération</li>
        <li>Chiffrement des données</li>
        <li>Monitoring de sécurité</li>
    </ul>
    
    <h3>Conformité réglementaire</h3>
    <p>Respecter les réglementations en vigueur :</p>
    <ul>
        <li>RGPD pour la protection des données</li>
        <li>Normes sectorielles</li>
        <li>Audits de sécurité réguliers</li>
    </ul>',
    CURRENT_TIMESTAMP
),
(
    'Économie circulaire : modèle d''avenir pour les Antilles',
    'Environnement',
    'https://via.placeholder.com/800x400/20c997/ffffff?text=Economie+Circulaire',
    'Comment l''économie circulaire peut transformer le modèle économique des Antilles et créer de nouvelles opportunités durables.',
    '<h2>Qu''est-ce que l''économie circulaire ?</h2>
    <p>L''économie circulaire vise à éliminer les déchets et à réutiliser les ressources de manière continue, créant ainsi un système économique durable.</p>
    
    <h3>Principes de l''économie circulaire</h3>
    <ul>
        <li><strong>Réduire :</strong> Minimiser la consommation de ressources</li>
        <li><strong>Réutiliser :</strong> Prolonger la durée de vie des produits</li>
        <li><strong>Recycler :</strong> Transformer les déchets en nouvelles ressources</li>
        <li><strong>Réparer :</strong> Maintenir et restaurer les produits</li>
    </ul>
    
    <h3>Applications aux Antilles</h3>
    <h4>Secteur agricole</h4>
    <p>Transformation des déchets agricoles :</p>
    <ul>
        <li>Compostage des résidus organiques</li>
        <li>Production de biogaz</li>
        <li>Fertilisants naturels</li>
    </ul>
    
    <h4>Secteur touristique</h4>
    <p>Gestion durable du tourisme :</p>
    <ul>
        <li>Hôtels éco-responsables</li>
        <li>Circuits touristiques durables</li>
        <li>Restauration locale et bio</li>
    </ul>
    
    <h4>Secteur industriel</h4>
    <p>Optimisation des processus industriels :</p>
    <ul>
        <li>Récupération de chaleur</li>
        <li>Recyclage des matériaux</li>
        <li>Écoconception des produits</li>
    </ul>
    
    <h3>Bénéfices économiques</h3>
    <p>L''économie circulaire peut apporter :</p>
    <ul>
        <li>Réduction des coûts de production</li>
        <li>Création d''emplois locaux</li>
        <li>Nouvelles sources de revenus</li>
        <li>Réduction de la dépendance aux importations</li>
    </ul>
    
    <h3>Technologies d''appui</h3>
    <p>Solutions technologiques pour l''économie circulaire :</p>
    <ul>
        <li>Plateformes de partage et de réutilisation</li>
        <li>IoT pour le monitoring des ressources</li>
        <li>Blockchain pour la traçabilité</li>
        <li>IA pour l''optimisation des processus</li>
    </ul>
    
    <h3>Conclusion</h3>
    <p>L''économie circulaire représente une opportunité unique pour les Antilles de créer un modèle économique durable et résilient.</p>',
    CURRENT_TIMESTAMP
);

-- Insertion de quelques messages de contact d'exemple
INSERT INTO contact (nom, prenom, email, service, date, heure, message, date_creation) VALUES
(
    'Dupont',
    'Marie',
    'marie.dupont@email.com',
    'Création Digitale',
    CURRENT_DATE + INTERVAL '7 days',
    '14:00',
    'Bonjour, je souhaite créer un site e-commerce pour ma boutique de produits locaux en Guadeloupe. Pouvez-vous me contacter pour discuter du projet ?',
    CURRENT_TIMESTAMP
),
(
    'Martin',
    'Jean-Pierre',
    'jp.martin@entreprise.fr',
    'Conseil en Stratégie et Pilotage',
    CURRENT_DATE + INTERVAL '3 days',
    '10:00',
    'Nous cherchons un accompagnement pour optimiser nos processus internes et améliorer notre productivité. Merci de nous recontacter.',
    CURRENT_TIMESTAMP
),
(
    'Rousseau',
    'Sophie',
    'sophie.rousseau@tech-antilles.com',
    'Adoptez l''IA',
    CURRENT_DATE + INTERVAL '14 days',
    '16:00',
    'Intéressée par l''intégration de solutions IA dans notre entreprise. Nous aimerions en savoir plus sur vos services.',
    CURRENT_TIMESTAMP
);

-- Affichage des données insérées
SELECT 'Articles créés :' as info;
SELECT titre, categorie, date_creation FROM article ORDER BY date_creation DESC;

SELECT 'Messages de contact créés :' as info;
SELECT nom, prenom, service, date FROM contact ORDER BY date_creation DESC; 