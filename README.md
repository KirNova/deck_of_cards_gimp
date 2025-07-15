# Rabenschatten: The Deckmaker

Ein modulares Werkzeugset zur Erstellung von individuellen Spielkarten, basierend auf GIMP, Python und optionaler GUI-Erweiterung. Entwickelt für künstlerische, musikalische oder erzählerische Kartendecks (z. B. für Rabenschatten Records, Storytelling, Tarot oder Sammelkarten).

##  Funktionen

1. **Kartenvorlagen-System** (GIMP/XCF):
   - Einheitliche Kartengröße (z. B. 825×1125px @ 300DPI)
   - Platzhalter für: Symbole, Text, Projektnamen, visuelle Elemente
   - Unterstützung für 13 individuelle Masken (z. B. für verschiedene Fraktionen, Projekte oder Designs)

2. **Karten-Stanz-Werkzeug** (Python):
   - Auswahl per Werkzeugmaske (rund, rechteckig, benutzerdefiniert)
   - Automatische Freistellung & Export (mit oder ohne Transparenz)
   - GPU/CUDA-Unterstützung für skalierbare Verarbeitung
   - Batch-Verarbeitung kompletter Decks

3. **Zukunft: GUI-Erweiterung (Gradio oder GTK)**
   - Kinderfreundlich
   - Drag & Drop für Bilder + Maske auswählen
   - Automatisches Exportieren in Druck- oder Webformate

##  Projektstruktur (geplant)

deckmaker/
├── templates/ # .xcf / .svg Masken (Kartenrahmen, Symbole etc.)
├── stanztool/ # Python-Tool zur automatisierten Freistellung
│ ├── export.py
│ └── config.yaml # Größe, DPI, Exportformate etc.
├── gui/ # (optional) grafische Oberfläche
├── output/ # Exportierte Karten
└── README.md # Diese Datei

yaml
Kopieren
Bearbeiten

##  Ziel

Ein langlebiges, wiederverwendbares und lokal ausführbares System, das:
- Ohne Cloud oder Onlinebindung funktioniert
- Auch von Kindern (12+, z. B. Lilas Noctis) bedienbar ist
- Als kreatives Fundament für Musik-, Kunst- oder Rollenspielprojekte dient

---

> **Aktueller Status:** Projektstart (Phase: Struktur & GIMP-Masken)
