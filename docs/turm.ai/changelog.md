# Changelog

## Turm.ai Changelog
alle Aktuallisierungen vom Turm.ai

### 15.2.1<small> - 07.05.2024</small> { id="15.2.1" }

<b><small>Feature</small></b> 

- Tabellennamen können nun mit einem Klick in die Zwischenablage kopiert werden.


<b><small>Verbesserungen</small></b> 

- Upload Oberfläche zeigt nun deutlich die Fehler an, wenn Upload scheitert
- Loginname mit Umlauten wird nun akzeptiert
- Uploaddata kann nun mit Parametern übergeben werden:
  ```create_table=false``` verhindert das eine neue Tabelle 
  angelegt wird wenn nicht vorhanden.
  ```workflow=Mein Workflow Name``` startet neuen Workflow 


<b><small>Intern</small></b> 

- Requirements aktuallisiert
- Lizenzen erweitert
- Fehlermeldung 404 beim KI Upload bebhoben
- Kein After Upload Execute wenn, kein Schritt danach benötigt wird
- Prüfung der Uploddata Entity angaben

<b><small>Intern</small></b> 
- Doku für Intern angewendet

### 15.2.0<small> - 03.05.2024</small> { id="15.2.0" }

<b><small>Feature</small></b> 

- Import von Excel und CSV direkt im Turm über die Weboberfläche (schiff upload direkt im Turm integriert)Siehe [hier](<3 FAQ/FAQ/Datenupload.md>)  (TOP!)
- Übersetzungen für Felder eingeführt: Es können nun Sprechende Namen für Datenbank Felder importiert werden. '
  Das ist v.a. bei alten Datenbanken praktisch die keine aussagekräftigen Felder haben. Siehe [hier](<3 FAQ/FAQ/Feldbeschreibung.md>).
- Spalten Namen können nun aus der Tabelle mit einem Klick in die Zwischenablage kopiert werden.


### 15.1.2<small> - 02.05.2024</small> { id="15.1.2" }

<b><small>Feature</small></b> 

- Dieses Changelog eingeführt
- Softenging Webware Schnittstelle veröffentlicht
  
<b><small>Verbesserungen</small></b> 

- Keine externe Abhängigkeiten von JSDELIVER im Swaggerui mehr