# Changelog

## Turm.ai Changelog
alle Aktualisierungen vom Turm.ai

### 15.4.0 <small> - 17.07.2024</small> { id="15.4.0" }

<b><small>Feature</small></b>    

 - Es ist nun möglich formatierte Texte wie HTML, XML, Markdown und RTF in einfachen Text zu wandeln. Siehe [hier](<1 Verwendung/1 Mapping/Funktionen/11_functions_totext.md>)

 - @lookid deutlich ausgebaut: Es können nun auch Werte ausgegeben werden die keine ID sind. Dies wird dann verwendet wenn, z.B. eine App in einer Tabelle eine ID benötigt die gebraucht wird. siehe [hier](<1 Verwendung/1 Mapping/Funktionen/07_functions_lookupid.md>)


<b><small>Verbesserungen</small></b> 

- ecoDMS: Mutifaktor Anmeldung angepasst 


<b><small>Docu</small></b>

- Lookid Artikel erweitert [hier](<1 Verwendung/1 Mapping/Funktionen/07_functions_lookupid.md>)


### 15.3.1<small> - 20.06.2024</small> { id="15.3.1" }

<b><small>Verbesserungen</small></b> 

- Refactoring von Methoden für Numpy2
- ecoDMS Umlaute im Benutzername funktioniert
- MariaDB Connectionpool handling verbessert


### 15.3.0<small> - 18.06.2024</small> { id="15.3.0" }

<b><small>Feature</small></b>    

- Für Dokumente die via *turm File Api* abgelegt werden, kann nun bestimmt werden, dass diese bei Bedarf on the fly aus einer anderen geladen werden. 
  Bsp.: Ein PDF wird im Browser zum Turm hoch geladen, dabei bekommt die Datei eine *Turm file id*. Anschließend wird die Datei durch die KI bearbeitet und in einem DMS abgelegt.
  Nun fordert eine andere App diese Datei mit der *Turm file id* an. Der Turm lädt dann in dem Moment die Datei aus dem DMS und stellt 
  sie der anderen Anwendung zur Verfügung.    
  Der Aufruf funktioniert mit allen Apps die Dokumente verwalten können, nicht nur DMS Systeme. 

<b><small>Verbesserungen</small></b> 

- KI: steht ein Dokument länger als 1 Stunde auf *Pending* wird es ebenfalls als fehlgeschlagen intertrepiert und im nächsten Redo wiederholt 



### 15.2.4<small> - 17.06.2024</small> { id="15.2.4" }


<b><small>Verbesserungen</small></b> 

- Performance Steigerung: Bis zu 150% schnellere Insert/ Updates mit externen Zuorndungen 
- Bug: Import von Mapping Einstellungen wurden teilweise falsch übernommen, wurde gefixt



### 15.2.3<small> - 13.06.2024</small> { id="15.2.3" }

<b><small>Feature</small></b>    

- smartki: diverse Nummer (header_order_number,header_order_confirmation_numbers,header_delivery_note_numbers,payment_methods) werden nun zusammengefasst übergeben. 


<b><small>Verbesserungen</small></b> 

- ecoDMS Feature: Kein Ändern von Attributen, wenn schon identisch zu bestehender Klassifikation ist, bisher wurde in ecoDMS dann eine Revision vermerkt
- ecoDMS Feature: Unterstützung für Multifaktor Authenifizierung
- ecoDMS Bug: File ID wird nicht gespeichert, wenn über mehrere Verknüpfungen aktualisiert wird
- smartki: Überspringen von defekten Pdfs z.B. 0Kb  
- Lexoffice Feature: Async Cooldown wenn Ratelimit erreicht wird. (Performance Steigerung)
- EspoCRM: Nach Upsert Aktuallisieren der Internen Daten
- SQL Injetion Schutz erweitert
- Bug Workflow Editor: Zeigt keine Meldung über erfolgeichem speichern
- Bei User Sperre: Counter Fehlanmeldung wird auf 0 gesetzt und Aktiv false gesetzt

 
 

### 15.2.2<small> - 11.06.2024</small> { id="15.2.2" }

<b><small>Feature</small></b> 

- Externe Zuondungen können nun im Mapping hinterlegt werden: so können Attribute wie z.B. Email Adresse, Kundennummer usw. 
verwendet werden um Daten automatisch zuzuonden. siehe [hier](<1 Verwendung/1 Mapping/mapping_fremdid.md>)



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

- Requirements aktualisiert
- Lizenzen erweitert
- Fehlermeldung 404 beim KI Upload behoben
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
