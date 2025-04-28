# Frogger

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

## 🔴 **Développeur 1 : Logique des éléments et du joueur**
- **Responsabilités** :
  - **Mouvement du joueur** : Créer et gérer les fonctions permettant de déplacer le joueur avec les touches directionnelles (haut, bas, gauche, droite).
  - **Gestion des obstacles** : Définir la logique des collisions avec les obstacles (voitures, trains, buches).
  - **Réinitialisation du jeu** : Créer la fonction pour recommencer le jeu.
  - **Score et progression** : Augmenter le score et gérer la progression du joueur dans le jeu.
- **Fichiers associés** :
  - `game.py` (mouvement du joueur, collisions, réinitialisation, score)
  
---

## 🟢 **Développeur 2 : Affichage et animations**
- **Responsabilités** :
  - **Fenêtre de jeu** : Création de la fenêtre avec Pygame (dimensions, arrière-plan).
  - **Affichage des éléments** : Dessiner les objets du jeu (joueur, obstacles, score).
  - **Animation des objets** : Gérer le déplacement des objets (voitures, trains, buches) à l'écran.
  - **Effets visuels** : Ajouter des effets visuels (par exemple, animations ou changements de couleur pour les collisions).
- **Fichiers associés** :
  - `game.py` (affichage du joueur et des objets)
  - `main.py` (pour l'affichage général)

---

## 🔵 **Développeur 3 : Gestion des configurations et des paramètres**
- **Responsabilités** :
  - **Fichier de configuration** : Créer et gérer un fichier `config.py` pour définir toutes les constantes du jeu (dimensions, couleurs, taille des tuiles, etc.).
  - **Paramètres du jeu** : Ajuster les valeurs pour équilibrer la difficulté, définir la vitesse des véhicules et obstacles, et d'autres réglages du jeu.
  - **Révision des paramètres** : S'assurer que les paramètres sont cohérents et ajustés pour une expérience fluide et amusante.
- **Fichiers associés** :
  - `config.py` (toutes les configurations et constantes du jeu)

---

## 🟡 **Développeur 4 : Gestion de la boucle principale et des événements**
- **Responsabilités** :
  - **Boucle principale** : Créer la boucle principale qui gère l'affichage du jeu et les interactions en continu (mouvements, collisions, mise à jour des éléments).
  - **Événements du jeu** : Gérer les événements (tels que les pressions de touches, la fermeture de la fenêtre, les interactions avec les objets).
  - **Contrôles utilisateur** : Implémenter les contrôles du joueur via les touches directionnelles.
  - **Débogage et tests** : Vérifier que les événements sont bien pris en charge et que tout fonctionne correctement.
- **Fichiers associés** :
  - `main.py` (la boucle principale et les événements)

---

## 📊 **Répartition des tâches :**

| **Tâche/Partie**                        | **Développeur Responsable** | **Fichier(s) associé(s)**           |
|-----------------------------------------|-----------------------------|-------------------------------------|
| **Mouvement du joueur et logique des obstacles**   | 🔴 Développeur 1           | `game.py`                          |
| **Affichage des éléments et animation**              | 🟢 Développeur 2           | `game.py`, `main.py`               |
| **Paramètres de configuration et ajustements**      | 🔵 Développeur 3           | `config.py`                        |
| **Boucle principale et gestion des événements**      | 🟡 Développeur 4           | `main.py`                          |

---

## 📋 **Outils de collaboration et gestion de projet** :

- **Git & GitHub** : Utilisation de branches pour éviter les conflits. Chaque développeur travaille sur une fonctionnalité dans une branche, puis fusionne avec la branche principale.
- **Réunions régulières** : Organisez des réunions pour vérifier l'avancement, résoudre les problèmes, et tester le jeu ensemble.
- **Suivi des tâches** : Utilisation de Trello ou Notion pour organiser et suivre l'avancement des tâches et les ajuster si nécessaire.