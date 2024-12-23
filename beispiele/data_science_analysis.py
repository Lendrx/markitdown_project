"""
Data Science Beispiel für MarkItDown
-----------------------------------

Dieses Beispiel zeigt verschiedene Data Science Konzepte:
1. Datenimport und -verarbeitung mit Pandas
2. Statistische Analysen
3. Trend-Erkennung
4. Automatisierte Berichtserstellung
"""

from src.markitdown import MarkItDown
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def erweiterte_analyse():
    # MarkItDown mit erweiterten Statistiken initialisieren
    md = MarkItDown(advanced_stats=True)
    
    try:
        # Basis-Analyse durchführen
        result = md.convert("verkaufsdaten_2024.xlsx")
        print("✅ Analyse erfolgreich!")
        print("\n", result)
        
        # Zusätzliche visuelle Analyse
        df = pd.read_excel("verkaufsdaten_2024.xlsx")
        
        # Verkaufstrend visualisieren
        plt.figure(figsize=(12, 6))
        daily_sales = df.groupby('Datum')['Gesamtumsatz'].sum()
        sns.lineplot(data=daily_sales)
        plt.title('Täglicher Umsatzverlauf')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('beispiele/umsatz_trend.png')
        
        # Ergebnis speichern
        with open("analyse_ergebnis.md", "w", encoding="utf-8") as f:
            f.write(result)
            print("\n📝 Ergebnis wurde in analyse_ergebnis.md gespeichert!")
            
    except Exception as e:
        print(f"❌ Fehler: {e}")

if __name__ == "__main__":
    erweiterte_analyse()