from src.markitdown import MarkItDown

def main():
    try:
        # MarkItDown initialisieren
        md = MarkItDown()
        
        # Excel analysieren
        ergebnis = md.convert("verkaufsdaten_2024.xlsx")
        
        # Ergebnis ausgeben
        print(ergebnis)
        
        # Optional: Ergebnis in Datei speichern
        with open("analyse_ergebnis.md", "w", encoding="utf-8") as f:
            f.write(ergebnis)
            print("\n✅ Analyse wurde in 'analyse_ergebnis.md' gespeichert!")
            
    except Exception as e:
        print(f"❌ Fehler: {e}")

if __name__ == "__main__":
    main()