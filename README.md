#  deck_of_cards_gimp

Ein universelles, plattformübergreifendes **GIMP-Plugin zur Erstellung individueller Spielkarten**.  
Entwickelt für Künstler*innen, Musiker*innen, Labels, Lehrer*innen oder Geschichtenerzähler –  
vollständig lokal, modular, zukunftssicher – und mit Haltung.

---

##  Zielsetzung

- Plugin für **GIMP 3.0.4 oder höher**
- Plattformübergreifend für **Linux (ArchLinux)** und **Windows 11 Pro**
- **macOS-Support geplant** ab Herbst 2025
- **Kein Support für GIMP 2.10 oder frühere Versionen**
- Lokalisierbar (gettext-basiert), **mit Mehrsprachigkeit von Anfang an**
- Vollständig **offline & datenschutzfreundlich**
- Nutzbar auch für Kinder, Kreative ohne Technikkenntnisse

---

## 🛠️ Features (aktueller Stand)

- Integration direkt im GIMP-Menü: `Deck of Cards > Export Card`
- Exportiert sichtbare Ebenen als PNG mit Alphakanal
- Konfigurierbarer Exportpfad & Dateinamenpräfix
- Lokalisierungsbereit via `gettext`
- Zukunft: Maske erkennen, Ebenenfilter, Textfelder, Vorlagensystem

---

##  Projektstruktur (geplant)

deck_of_cards_gimp/
├── gimp-plugin/
│ ├── deck_export.py # Hauptplugin (Python-Fu)
│ └── utils.py # Helferfunktionen (Alpha, Ebenen etc.)
├── templates/ # XCF-Kartenvorlagen mit Ebenenmasken
├── output/ # Exportierte Karten
├── gui/ # (optional) Gradio/GTK-Frontend
├── locale/ # Sprachdateien (.mo / .po / .pot)
│ └── de/uk/en/...
├── docs/
│ ├── gimp3_compatibility.md
│ └── l10n_plan.md
├── stanztool/ # (optional) Zusatztools z. B. für Batch
└── README.md


---

##  Mehrsprachigkeit

Das Plugin ist **lokalisierbar mit gettext**.

| Sprache       | Kürzel | Status     |
|---------------|--------|------------|
| 🇬🇧 Englisch   | `en`   | ✅ Standard & Fallback |
| 🇩🇪 Deutsch    | `de`   | 🛠️ in Arbeit           |
| 🇺🇦 Ukrainisch | `uk`   | 🛠️ in Arbeit           |
| ❌ Russisch    | `ru`   | **bewusst ausgeschlossen** |

> Wer andere Sprachen benötigt, kann das Projekt gerne forken oder beitragen.

---

##  Plattformstatus

| Plattform       | Status           | Besonderheit                            |
|----------------|------------------|-----------------------------------------|
| Linux (Arch)   | ✅ aktiv getestet | Hauptentwicklungsplattform              |
| Windows 11 Pro | ✅ aktiv getestet | Pfadhandling & Dateirechte geprüft      |
| macOS (real)   | 🔒 geplant        | Testphase ab Herbst 2025 (Mac Mini)     |
| Hackintosh     | 🚫 ausgeschlossen | Kein valides Testszenario               |

---

##  Beispiel für Plugin-Registrierung (lokalisierbar)

```python
import gettext
gettext.install("deck_of_cards", localedir="locale")
_ = gettext.gettext

register(
    "deck_of_cards_export",
    _("Export current visible layers as a card PNG"),
    _("Exports the visible layers of the current image as a transparent card (PNG)"),
    "Kir Nova",
    "MIT License",
    "2025",
    _("Export Card..."),
    "*",
    [],
    [],
    export_card,
    menu=_("<Image>/Deck of Cards")
)

