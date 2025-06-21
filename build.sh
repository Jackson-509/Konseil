#!/usr/bin/env bash
# Script de build pour Render

echo "🚀 Démarrage du build Konseil..."

# Installer les dépendances
echo "📦 Installation des dépendances..."
pip install -r requirements.txt

# Initialiser la base de données si nécessaire
echo "🗄️  Initialisation de la base de données..."
python init_database.py

echo "✅ Build terminé avec succès !" 