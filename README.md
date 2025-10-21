
# ⚔️ Dark Souls III Boss Tracker

A fan-made **Dark Souls III Boss Tracker** built with **Python (PyQt5)**.  
Track your progress through every boss fight — view lore, weaknesses, and phase tips, complete with music, visuals, and authentic Dark Souls messages.  
> *“Heir of Fire Destroyed.”*

---

## 🧭 Overview

This desktop app lets you:
- Keep track of which bosses you’ve defeated  
- View boss lore, locations, and weaknesses  
- Get phase-by-phase combat tips  
- Listen to Dark Souls’ main theme as you play  
- Watch your completion progress update dynamically  

---

## 🎮 Features

- 🗺️ **Boss Information Viewer** — See lore, location, and weaknesses  
- ⚔️ **Defeat Tracker** — Mark defeated bosses and track completion percentage  
- 💡 **Tips Popups** — View phase 1 and phase 2 strategies  
- 🎵 **Background Music** — Play or pause the Dark Souls III main theme  
- 🔥 **Victory Messages** — Authentic Dark Souls-style popups  
- 🔁 **Progress Reset** — Start over anytime  

---

## 🧩 Project Structure

DarkSoulsApp/
│
├── darksoulsAPP.py # Main PyQt5 app logic and GUI
├── boss.py # Boss class and JSON data handler
│
├── data/
│ └── databoss.json # Boss data (location, lore, difficulty, etc.)
│
├── images/ # Boss artwork (e.g., abyss_watchers.jpg)
│
├── music/
│ └── main_theme.wav # Background theme music
│
└── PythonProject/
└── darksoulsAPP_ui.py # Auto-generated PyQt5 UI file


---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/dark-souls-tracker.git
cd dark-souls-tracker
pip install PyQt5
python darksoulsAPP.py

Usage Tips

Select a boss to view details and lore

Check the Defeated box to mark them as beaten

Click the Tips checkbox to view combat strategies

Use the Reset button to clear your progress

Enjoy the background music and progress animations!

🧰 Built With

🐍 Python 3.10

🎨 PyQt5 (Qt Widgets, Multimedia)

💾 JSON (for saving progress and boss data)

🎵 QMediaPlayer (for background audio)




