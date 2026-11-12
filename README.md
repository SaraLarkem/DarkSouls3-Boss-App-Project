# ⚔️ Dark Souls III Boss Tracker

A fan-made **Dark Souls III Boss Tracker** built with **Python (PyQt5)**.
Track your progress through every boss fight: view lore, weaknesses, and phase tips, with music, visuals, and Dark Souls-style messages.

> *"Heir of Fire Destroyed."*

---

## 🧭 Overview

This desktop app lets you:

- Keep track of which bosses you've defeated
- View boss lore, locations, and weaknesses
- Get phase-by-phase combat tips
- Listen to the Dark Souls III main theme as you play
- Watch your completion progress update as you go

---

## 🎮 Features

- 🗺️ **Boss Information Viewer**: see lore, location, and weaknesses
- ⚔️ **Defeat Tracker**: mark defeated bosses and track completion percentage
- 💡 **Tips Popups**: view phase 1 and phase 2 strategies
- 🎵 **Background Music**: play or pause the Dark Souls III main theme
- 🔥 **Victory Messages**: Dark Souls-style popups
- 🔁 **Progress Reset**: start over anytime

---

## 🧩 Project Structure

```text
DarkSouls3-Boss-App-Project/
├── README.md
└── PythonProject/
    ├── darksoulsAPP.py        # Main PyQt5 app logic and GUI (entry point)
    ├── darksoulsAPP_ui.py     # Auto-generated PyQt5 UI file
    ├── boss.py                # Boss class and JSON loader
    ├── boss_data.py           # JSON load/save helpers
    ├── data/
    │   └── databoss.json      # Boss data and saved progress
    ├── images/                # Boss artwork (e.g. abyss_watchers.jpg)
    └── music/
        └── main_theme.wav     # Background theme music
```

---

## ⚙️ Installation & Setup

### Requirements

- Python 3.10 or newer
- PyQt5

### 1. Clone the repository

```bash
git clone https://github.com/SaraLarkem/DarkSouls3-Boss-App-Project.git
cd DarkSouls3-Boss-App-Project
```

### 2. Install dependencies

```bash
pip install PyQt5
```

### 3. Run the app

```bash
python PythonProject/darksoulsAPP.py
```

---

## 🕹️ Usage Tips

- Select a boss to view details and lore
- Check the **Defeated** box to mark a boss as beaten
- Check the **Tips** box to view combat strategies
- Use the **Reset** button to clear your progress
- Enjoy the background music and progress bar as you go

Your progress is saved to `PythonProject/data/databoss.json`.

---

## 🧰 Built With

- 🐍 Python 3.10+
- 🎨 PyQt5 (Qt Widgets, Multimedia)
- 💾 JSON (boss data and saved progress)
- 🎵 QMediaPlayer (background audio)

---

## ⚠️ Disclaimer

This is an unofficial fan project and is not affiliated with or endorsed by FromSoftware or Bandai Namco.
