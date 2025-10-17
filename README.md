## 🌀 Conjecture de Syracuse — Visualisation en Python

Ce projet permet d’**explorer la conjecture de Syracuse** à partir d’un **nombre entier positif**.
Il affiche la **séquence** générée, des statistiques utiles comme le **temps de vol** et l’**altitude maximale**, et trace un **graphique** interactif de la trajectoire avec matplotlib.

#### 📦 Fonctionnalités
- Validation de l’**entrée utilisateur**

- Calcul de la **suite de Syracuse**

- Affichage des **statistiques** :

  - **Nombre d’étapes**

  - **Altitude maximale**

  - **Temps de vol** (nombre d’étapes au-dessus de la valeur initiale)

- **Visualisation graphique** avec matplotlib 

#### 🚀 Installation
Assurez-vous d’avoir **Python 3** installé, puis **installez la bibliothèque nécessaire** :

    pip install matplotlib

Pour lancer le script : 

    python conjecture.py

#### 🧱Structure du code
- **ask_for_number()** : demande et valide l’entrée utilisateur
- **syracuse_sequence(n)** : génère la suite et calcule le temps de vol
- **display_syracuse_sequence()** : affiche les résultats
- **plot_syracuse()** : trace le graphique avec matplotlib
- **main()** : point d’entrée du programme

#### 🧠 À propos de la conjecture
La **conjecture de Syracuse** stipule que pour tout **entier positif**, la suite définie par :

𝑛
→
𝑛
/
2
 si 
𝑛
 est pair

𝑛
→
3
𝑛+
1 si 
𝑛
 est impair 