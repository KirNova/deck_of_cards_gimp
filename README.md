# 🃏 deck_of_cards_gimp

Ein universelles, plattformübergreifendes **GIMP-Plugin zur Erstellung individueller Spielkarten**.  
Entwickelt für Künstler*innen, Musiker*innen, Geschichtenerzähler*innen, Labels oder Designer*innen –  
vollständig lokal, modular und zukunftssicher.

---

## 🎯 Zielsetzung

- Entwickelt für **GIMP 3.0.4+**
- Kompatibel mit **Linux (ArchLinux)** & **Windows 11 Pro**
- **macOS-Support geplant** ab Herbst 2025 (Testphase mit Mac Mini)
- **Kein Support für GIMP 2.10 oder älter**
- Vollständig lokal nutzbar (kein Cloud- oder Online-Zwang)
- **Geeignet für Kinder und Kreative ohne Codekenntnisse**
- Modular aufgebaut und Open Source

---

## 🛠️ Funktionen (in Arbeit)

- Plugin für GIMP, aufrufbar über Menü (`Rabenschatten > Exportiere Karte`)
- Exportiert sichtbare Ebenen als transparente PNG-Karte
- Unterstützt Alpha-Kanal automatisch
- Konfigurierbarer Exportpfad und Dateinamen-Präfix
- Zukunft: Ebenen-Filter, Maske wählen, Text-Felder, GUI etc.

---

## 📁 Projektstruktur (Startversion)

deck_of_cards_gimp/
├── gimp-plugin/ # Hauptplugin-Code
│ ├── deck_export.py
│ └── utils.py
├── templates/ # .xcf-Vorlagen mit Masken & Platzhaltern
├── output/ # Hier landen exportierte Karten
├── gui/ # (optional) Gradio/GTK GUI-Erweiterung
├── docs/ # Dokumentation & Kompatibilitätsinfos
│ └── gimp3_compatibility.md
├── stanztool/ # (geplant) Tools außerhalb von GIMP
├── README.md # Diese Datei


---

## 🧪 Plattformstatus

| Plattform       | Status           | Besonderheit                            |
|----------------|------------------|-----------------------------------------|
| Linux (Arch)   | ✅ aktiv getestet | Hauptentwicklungsplattform              |
| Windows 11 Pro | ✅ aktiv getestet | Pfadhandling & Exportverhalten geprüft  |
| macOS (real)   | 🔒 geplant        | Kommt ab Herbst 2025 mit Mac Mini       |
| Hackintosh     | ❌ ausgeschlossen | Kein zuverlässiges Testsystem           |

---

## 📌 Hinweis zur GIMP-Version

> Dieses Plugin ist **nur kompatibel mit GIMP 3.0.4 oder höher**.  
> Ältere Versionen (z. B. GIMP 2.10.x) werden **nicht unterstützt**.  
>  
> Wer dieses Plugin findet und nutzen will, sollte die aktuelle GIMP-Version von [gimp.org](https://www.gimp.org) installieren.

---

## 🦇 Projektphasen

- [x] Grundplugin (`deck_export.py`)
- [ ] `.xcf`-Vorlagen mit Ebenenstruktur
- [ ] Erweiterung: Ebenenauswahl, Maske, Textinjektion
- [ ] GUI-Frontend (optional)
- [ ] macOS-Testphase (Herbst 2025)
- [ ] Veröffentlichung im GIMP Plugin-Index

---

## 🤝 Mitwirken

Jede Hilfe willkommen – sei es mit Testberichten, macOS-Feedback oder Erweiterungsideen.  
Forks, Pull Requests oder Issues sind ausdrücklich erwünscht!

---

## 🖤 Warum dieses Projekt?

Weil Kreativität keine Lizenzkosten braucht.  
Weil Open Source bleiben muss.  
Weil du deine Karten selbst schreiben solltest – auf deine Weise.

**Ein Projekt von [Kir Nova](https://github.com/KirNova)** für die Community.  
Veröffentlicht unter der **MIT-Lizenz**.
