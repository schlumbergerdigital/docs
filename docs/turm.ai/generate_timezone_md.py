"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
'  Python Skript - Erstellt Markdown Datei mit allen möglichen Zeitzonen 
' 				
'  
' Benötigt: 
'				   			  
'					   
' Zur Verwendung mit:
' 
' Erstellt von:	Max Schwesig
' Version:	1.0.0
' Codierung:	UTF-8
' Stand:	13.02.2024	
' 
' Copyright (c) 2024 by schlumberger digital. Alle Rechte vorbehalten.
' www.schlumberger.digital
'*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
import os
import pytz
from datetime import datetime

subfolder_name = os.path.join("1 Verwendung","1 Mapping","Funktionen")

# Erstellen des vollständigen Pfades für den Unterordner
DIR_PATH =  os.path.dirname(os.path.realpath(__file__))
subfolder_path = os.path.join(DIR_PATH, subfolder_name)
os.makedirs(subfolder_path, exist_ok=True)
# Der Dateiname der Markdown-Datei
filename = os.path.join(subfolder_path, "04_functions_datetimezones.md")

# Öffnen der Markdown-Datei zum Schreiben
with open(filename, "w") as file:
    # Schreiben der Tabellenkopfzeile in die Datei
    file.write("# # Datum - Zeitzonenliste\n\n")
    file.write("| Zeitzone | UTC-Offset |\n")
    file.write("|----------|------------|\n")
    
    # Durchlaufen aller Zeitzonen und Schreiben jeder Zeitzone mit ihrem UTC-Offset in die Tabelle
    for timezone in pytz.all_timezones:
        tz_info = pytz.timezone(timezone)
        utc_offset = datetime.now(tz_info).strftime('%z')
        # Umwandlung des UTC-Offsets in ein lesbares Format
        utc_offset_formatted = f"{int(utc_offset[:-2]):+03d}:{utc_offset[-2:]}" if utc_offset else ""
        file.write(f"| {timezone} | {utc_offset_formatted} |\n")
