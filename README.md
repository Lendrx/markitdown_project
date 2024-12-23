# 🚀 MarkItDown

Konvertiere und analysiere deine Datendateien mit Python - einfach, schnell und leistungsstark!

## ⚡️ Schnellstart

```python
from markitdown import MarkItDown

# Einfache Konvertierung
md = MarkItDown()
ergebnis = md.convert("verkaufsdaten.xlsx")
print(ergebnis)

# Mit KI-gestützter Analyse
from openai import OpenAI
client = OpenAI()
md_ai = MarkItDown(llm_client=client)
ergebnis = md_ai.convert("produkt_bild.jpg")
print(ergebnis)
```

## 🎯 Das kannst du damit machen

### 📊 Excel-Analyse
```python
ergebnis = md.convert("daten.xlsx")
# Liefert dir:
# - Wichtige Statistiken
# - Top-Performer
# - Trendanalyse
# - Regionale Auswertung
# - Zeitreihenanalyse
```

### 📸 Bildverarbeitung
```python
ergebnis = md.convert("bild.jpg")
# Bietet:
# - KI-gestützte Beschreibungen
# - EXIF-Metadaten
# - Visuelle Inhaltsanalyse
```

### 📄 Dokumentenverarbeitung
```python
ergebnis = md.convert("dokument.pdf")
# Erstellt:
# - Textextraktion
# - Strukturanalyse
# - Inhaltszusammenfassung
```

## 🛠 Installation

```bash
pip install -r requirements.txt
```

## 💡 Beispiele

Schau dir `beispiele/` an für:
- 📈 Verkaufsdatenanalyse
- 🤖 KI-gestützte Bildbeschreibungen
- 📊 Automatische Berichtserstellung

## 📚 Technische Details

Das Projekt demonstriert:
- Datenverarbeitung mit Pandas
- Statistische Analysen
- KI-Integration
- Automatisierte Berichtserstellung

## 🤝 Mitmachen

Beiträge sind willkommen! Du kannst:
- Issues erstellen
- Pull Requests einreichen
- Features vorschlagen

## 📝 Lizenz

MIT