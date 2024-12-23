import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Startdatum festlegen
start_date = datetime(2024, 1, 1)

# Daten generieren
data = {
    'Datum': [],
    'Produkt': [],
    'Kategorie': [],
    'Verkaufsmenge': [],
    'Preis_pro_Einheit': [],
    'Gesamtumsatz': [],
    'Region': []
}

# Produkte und ihre Preise
produkte = {
    'Laptop': 899.99,
    'Monitor': 299.99,
    'Tastatur': 49.99,
    'Maus': 29.99,
    'Drucker': 199.99
}

regionen = ['Nord', 'Süd', 'Ost', 'West']

# 15 Tage Verkaufsdaten generieren
for i in range(15):
    datum = start_date + timedelta(days=i)
    # 3 Verkäufe pro Tag
    for _ in range(3):
        produkt = np.random.choice(list(produkte.keys()))
        menge = np.random.randint(1, 21)
        preis = produkte[produkt]
        
        data['Datum'].append(datum)
        data['Produkt'].append(produkt)
        data['Kategorie'].append('Elektronik')
        data['Verkaufsmenge'].append(menge)
        data['Preis_pro_Einheit'].append(preis)
        data['Gesamtumsatz'].append(round(menge * preis, 2))
        data['Region'].append(np.random.choice(regionen))

# DataFrame erstellen
df = pd.DataFrame(data)

# Als Excel speichern
df.to_excel('verkaufsdaten_2024.xlsx', index=False)

print("Excel-Datei 'verkaufsdaten_2024.xlsx' wurde erstellt!")
print("\nÜberblick über die Daten:")
print(df.head())
print("\nStatistische Zusammenfassung:")
print(df.describe())