## 📌 Description

Ce projet permet d’analyser les mouvements d’un athlète à partir d’une vidéo en utilisant la computer vision.

Il détecte les points du corps (pose estimation), calcule des angles articulaires (ex: coude) et génère une vidéo annotée avec les résultats.

---

## 🚀 Fonctionnalités

- 📹 Lecture d’une vidéo (OpenCV)
- 🧍 Détection du squelette (MediaPipe)
- 📐 Calcul d’angles (ex: coude)
- 🖥️ Affichage en temps réel
- 💾 Export d’une vidéo annotée

---

## 🛠️ Technologies utilisées

- Python 3.12
- OpenCV
- MediaPipe
- NumPy

---

## 📂 Structure du projet

```
sports_project/
│
├── input/
│   └── test.mp4
├── output/
│   └── result.mp4
├── main.py
├── utils.py
└── README.md
```

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone <your-repo>
cd sports_project
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 3. Activer l’environnement

```bash
.\.venv\Scripts\activate
```

### 4. Installer les dépendances

```bash
pip install opencv-python mediapipe==0.10.21 numpy
```

---

## ▶️ Utilisation

1. Ajouter une vidéo dans :

```
input/test.mp4
```

2. Lancer le script :

```bash
python main.py
```

---

## 📊 Résultat

- Une fenêtre s’ouvre avec la vidéo et le squelette
- L’angle du coude est affiché
- Une vidéo est sauvegardée dans :

```
output/result.mp4
```

---

## 💡 Améliorations possibles

- Ajouter d’autres angles (genou, hanche)
- Exporter les données en CSV
- Créer un dashboard (Power BI / Streamlit)
- Analyse de performance sportive

---

## 👩‍💻 Auteur

Projet réalisé par **Fatine Ferdous**
