from src.markitdown import MarkItDown

# Test mit einer Excel-Datei
md = MarkItDown()
try:
    ergebnis = md.convert("deine_excel.xlsx")
    print(ergebnis)
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")