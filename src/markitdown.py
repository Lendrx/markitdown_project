from pathlib import Path
import pandas as pd
import numpy as np
from typing import Optional, Dict, Any

class MarkItDown:
    """
    Eine Data Science Klasse zur Analyse und Konvertierung von Daten in Markdown.
    
    Features:
    - Automatische Datenerkennung und -verarbeitung
    - Statistische Analysen und Zusammenfassungen
    - Trend- und Mustererkennung
    - Formatierte Ausgabe in Markdown
    
    Data Science Konzepte:
    - Datenaufbereitung mit Pandas
    - Statistische Analysen
    - Gruppierung und Aggregation
    - Zeitreihenanalyse
    """
    
    def __init__(self, advanced_stats: bool = False):
        """
        Initialisiert den MarkItDown Converter.
        
        Args:
            advanced_stats (bool): Aktiviert erweiterte statistische Analysen
        """
        self.advanced_stats = advanced_stats
    
    def _calculate_basic_stats(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Berechnet grundlegende statistische Kennzahlen.
        
        Data Science Relevanz:
        - Deskriptive Statistik
        - Numerische Zusammenfassungen
        - Zentrale Tendenz und Streuung
        """
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        stats = {
            'Datensätze': len(df),
            'Zeitraum': f"{df['Datum'].min()} bis {df['Datum'].max()}",
            'Gesamtumsatz': df['Gesamtumsatz'].sum(),
            'Durchschnittlicher Umsatz': df['Gesamtumsatz'].mean(),
            'Standardabweichung Umsatz': df['Gesamtumsatz'].std(),
        }
        return stats
    
    def _analyze_trends(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Führt Trendanalysen durch.
        
        Data Science Relevanz:
        - Zeitreihenanalyse
        - Trendidentifikation
        - Wachstumsraten
        """
        # Tägliche Veränderung
        daily_sales = df.groupby('Datum')['Gesamtumsatz'].sum()
        trends = {
            'Trend': 'steigend' if daily_sales.is_monotonic_increasing else 'variierend',
            'Max_Umsatz_Tag': daily_sales.idxmax(),
            'Min_Umsatz_Tag': daily_sales.idxmin(),
            'Wachstumsrate': ((daily_sales.iloc[-1] / daily_sales.iloc[0]) - 1) * 100
        }
        return trends
        
    def convert(self, datei_pfad: str) -> str:
        """
        Konvertiert Excel zu Markdown mit umfassender Analyse.
        
        Args:
            datei_pfad (str): Pfad zur Excel-Datei
            
        Returns:
            str: Markdown-formatierte Analyse
        
        Data Science Relevanz:
        - Datenimport und -verarbeitung
        - Automatisierte Berichtserstellung
        - Datenvisualisierung in Textform
        """
        # Daten einlesen
        df = pd.read_excel(datei_pfad)
        
        # Statistiken berechnen
        stats = self._calculate_basic_stats(df)
        trends = self._analyze_trends(df)
        
        # Analyse erstellen
        analyse = f"""
# 📊 Data Science Analyse der Verkaufsdaten

## 📈 Basis-Statistiken
- Anzahl Datensätze: {stats['Datensätze']}
- Analysezeitraum: {stats['Zeitraum']}
- Gesamtumsatz: {stats['Gesamtumsatz']:,.2f} €
- Durchschnittlicher Umsatz: {stats['Durchschnittlicher Umsatz']:,.2f} €
- Standardabweichung: {stats['Standardabweichung Umsatz']:,.2f} €

## 📊 Trend-Analyse
- Genereller Trend: {trends['Trend']}
- Bester Tag: {trends['Max_Umsatz_Tag'].strftime('%Y-%m-%d')}
- Schlechtester Tag: {trends['Min_Umsatz_Tag'].strftime('%Y-%m-%d')}
- Wachstumsrate: {trends['Wachstumsrate']:.1f}%

## 🏆 Top 3 Produkte nach Umsatz
{df.groupby('Produkt')['Gesamtumsatz'].sum().sort_values(ascending=False).head(3).to_markdown()}

## 📍 Regionale Verteilung
{df.groupby('Region')['Gesamtumsatz'].sum().to_markdown()}

## 📉 Umsatzentwicklung
{df.groupby('Datum')['Gesamtumsatz'].sum().to_markdown()}
"""

        if self.advanced_stats:
            # Korrelationsanalyse für numerische Spalten
            numeric_df = df.select_dtypes(include=[np.number])
            analyse += f"""
## 📊 Korrelationsanalyse
{numeric_df.corr().to_markdown()}
"""
            
        return analyse