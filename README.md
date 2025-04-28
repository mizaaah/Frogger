# Frogger

# 📜 Cahier des Charges du Projet Frogger

# 📑 Table des matières

- 📖 Introduction
- 🎯 Objectifs
- ✨ Fonctionnalités principales
- 🛠️ Architecture technique
- 🎨 Interface utilisateur
- ⚡ Performances
- 💻 Langages utilisés
- ⚠️ Mise en garde

---

## 1. 📖 Introduction

📝 NOTE  
Le projet **Frogger** consiste à développer un jeu d'arcade inspiré de *Crossy Road*, dans lequel le joueur doit faire traverser un personnage à travers routes, rivières et rails tout en évitant obstacles et dangers. L'objectif est de parcourir la plus grande distance possible sans mourir.

---

## 2. 🎯 Objectifs

✅ Proposer une expérience de jeu rapide, fluide et addictive.  
✅ Générer dynamiquement un terrain infini : routes, rivières, rails et plaines.  
✅ Implémenter des obstacles dynamiques : voitures, trains, rondins mouvants.  
✅ Mettre en place un système de score basé sur la progression du joueur.  
✅ Assurer un gameplay simple et intuitif.

---

## 3. ✨ Fonctionnalités principales

### 3.1 🏠 Écran de Jeu

- Présentation immédiate du personnage à l'écran.
- Déplacement du joueur sur une grille en 4 directions (haut, bas, gauche, droite).
- Scrolling dynamique du terrain à chaque avancée.

### 3.2 🚗 Obstacles dynamiques

- **Voitures** : obstacles rapides sur les routes, changement de vitesse et de direction.
- **Trains** : obstacles massifs sur les rails, très rapides mais espacés.
- **Rondins** : obstacles sur les rivières, nécessaires pour traverser, transportent le joueur.

### 3.3 🌊 Gestion de la rivière

- Nécessité d'être sur un rondin pour ne pas tomber dans l'eau.
- Rondins en mouvement qui glissent horizontalement.

### 3.4 🏆 Système de score

- Le score augmente à chaque ligne traversée avec succès.
- Affichage du score en temps réel en haut de l'écran.

---

## 4. 🛠️ Architecture technique

Technologies utilisées :

- 🎮 **Pygame** : moteur principal pour le rendu graphique, le son et la gestion des entrées clavier.
- 🧠 **Gestion interne** :
  - Système d'objets dynamiques (voitures, trains, rondins).
  - Génération procédurale du terrain.
  - Système de collisions précis.

---

## 5. 🎨 Interface utilisateur

Responsive Design (adapté au jeu sur ordinateur).

Éléments d'interface :

- 🖱️ Déplacement du joueur au clavier (flèches directionnelles).
- 🎯 Score affiché en permanence.
- 🎮 Rendu simple et coloré pour identifier rapidement les dangers (routes grises, rivières bleues, trains foncés, rondins bruns).

---

## 6. ⚡ Performances

Optimisations :

- ⏱️ Framerate stable à 30 FPS pour garantir la fluidité du gameplay.
- 🗂️ Optimisation du défilement et des objets hors écran pour libérer des ressources.
- 🚀 Chargement rapide au lancement du jeu (moins d'une seconde).

---

## 7. 💻 Langages utilisés

- 🐍 Python 3.11
- 🎮 Pygame 2.x

---

## 8. ⚠️ Mise en garde

⚠️ WARNING  
Ce projet est actuellement en phase de développement.  
Des fonctionnalités supplémentaires (menu principal, game over amélioré, musiques, skins personnalisés) peuvent être ajoutées dans les futures versions.  
Merci pour votre compréhension et votre soutien ! 🚀

---

# Répartition des tâches du projet

Voici la répartition des tâches entre les membres du groupe. Chaque développeur a des responsabilités spécifiques dans le projet.

## 🔴 **Développeur 1 : Gestion des éléments du jeu (logique de base)**

- **Responsabilités** :
  - Gestion du mouvement du joueur
  - Logique des obstacles (voitures, trains, buches)
  - Réinitialisation du jeu
  - Détection des collisions
- **Fichiers associés** :
  - `game.py`

---

## 🟢 **Développeur 2 : Affichage et visuel**

- **Responsabilités** :
  - Création de la fenêtre de jeu
  - Affichage des éléments du jeu (joueur, obstacles, score, arrière-plan)
  - Animation et mouvement des objets
- **Fichiers associés** :
  - `game.py`

---

## 🔵 **Développeur 3 : Gestion des paramètres et des constantes**

- **Responsabilités** :
  - Définition des constantes (taille de la fenêtre, couleurs, tailles des tuiles, etc.)
  - Réglages du jeu (vitesse des voitures, du joueur, règles du jeu, etc.)
  - Révision des valeurs et ajustements
- **Fichiers associés** :
  - `config.py`

---

## 🟡 **Développeur 4 : Gestion de la logique principale et boucle de jeu**

- **Responsabilités** :
  - Gestion de la boucle principale du jeu
  - Contrôles du joueur (mouvements via les touches directionnelles)
  - Gestion du score et de la progression
- **Fichiers associés** :
  - `main.py`

---

## 📊 **Outils de collaboration et gestion de projet**

- **Git & GitHub** : Utilisation de branches pour éviter les conflits. Chaque développeur travaille sur une fonctionnalité dans une branche, puis fusionne avec la branche principale.
- **Communication** : Réunions régulières pour discuter des avancements, résoudre les problèmes et tester les fonctionnalités.
- **Suivi des tâches** : Utilisation de Trello/Notion pour organiser et suivre l'avancement des tâches.

