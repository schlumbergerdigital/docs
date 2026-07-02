# Changelog

## Turm.ai Changelog
alle Aktualisierungen vom Turm.ai


### 17.9.1 <small> - 22.06.2026</small> { id="17.9.1" }


<b><small>Feature</small></b>    

- Mapplisten Unterstützung [Mapplisten](<1 Verwendung/1 Mapping/Funktionen/07_functions_maplist.md>)
- Syntax Checker bei Eingabe 
- Auctis Unterstützung
- Agilea Unterstützung
- Strike-System-Sicherheit eingeführt: Blacklisten von IPs, wenn auffällige Verbindungen festgestellt werden
- Möglichkeit, Dashboard selbst anzulegen
- Möglichkeit, Config selbst einzugeben 
- Grace Time kann nun pro App hinterlegt werden 
- User-Rechte auf Modul-Basis eingeführt 
- Bexio Schnittstelle implementiert 
- Email in Email kann nun auch gelesen werden 
- Mistral angebunden 
  
<b><small>Verbesserungen</small></b> 

- Security Hardening: Filter werden tiefer geprüft
- Multiworker Setup 
- Logfiles nun separate Ablage
- XML Parser verbessert 
- Only New Filter verbessert
- O365 Anbindung mit Graph verbessert
- HTML Injection Sicherheit verbessert 
- SQL Injection Sicherheit verbessert
- Strike System für 
- EspoCRM Löschen ermöglicht
- Clockodoo Fix 
- Diverse Fix ecoDMS 
- Imap System umgestellt auf async 
- Easybill Fix 
- Einführung HTTPX
- Windows: Switch der Async System Loop
- Argon2 hash nun standard 
- ELO Fix
- Hetzner Fix 
- Usermeldung im Upload, wenn keine Rechte vorhanden sind 
- Lexoffice Fix
- X-Rechnungen parser 
- Python mindest Version nun 3.13
  



### 16.0.0 <small> - 31.03.2025</small> { id="16.0.0" }


<b><small>Feature</small></b>    

- Vollständige Unterstützung von E-Rechnungen, sowohl in ZUGFeRD als auch X-Rechnung. 
- Einführung von Leuchtfeuer Tabellen: Ein zentraler Ort, um allgemeine Listen für alle Webapps synchron zu halten, z.B. Orderstrukturen 

<b><small>Verbesserungen</small></b> 

- Umstellung auf vollständige Async Kommunikation bei allen Webdiensten, Beschleunigung der Kommunikation somit mehr als 100% erhöht. 
  


### 15.5.0 <small> - 20.08.2024</small> { id="15.5.0" }

<b><small>Feature</small></b>    

- Workflows können nun einfach aus der Oberfläche an den Homebildschirm angeheftet werden. So können alle, die Zugriff auf die Oberfläche haben, diese Workflows einfach auslösen
- Clockodoo als App aufgenommen
- Microsoft Access mit Online und Schiff aufgenommen


<b><small>Verbesserungen</small></b> 

- Easybill: Kommunikation verbessert 
- Lexoffice: Diverse Verbesserungen in der Api kommunikation
- turm allgemein: auch falsch formatierte JSON-Objekte, also z.B. wenn mit ' statt mit " geschlossen wird, werden aufgelöst
- Bug: Parameter order by in der Oberfläche hat nicht sortiert (in der API schon) 

### 15.4.0 <small> - 17.07.2024</small> { id="15.4.0" }

<b><small>Feature</small></b>    

 - Es ist nun möglich formatierte Texte wie HTML, XML, Markdown und RTF in einfachen Text zu wandeln. Siehe [hier](<1 Verwendung/1 Mapping/Funktionen/11_functions_totext.md>)

 - @lookid deutlich ausgebaut: Es können nun auch Werte ausgegeben werden die keine ID sind. Dies wird dann verwendet wenn, z.B. eine App in einer Tabelle eine ID benötigt die gebraucht wird. siehe [hier](<1 Verwendung/1 Mapping/Funktionen/07_functions_lookupid.md>)


<b><small>Verbesserungen</small></b> 

- ecoDMS: Multifaktor Anmeldung angepasst 


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

- KI: steht ein Dokument länger als 1 Stunde auf *Pending*, wird es ebenfalls als fehlgeschlagen interpretiert und im nächsten Redo wiederholt 



### 15.2.4<small> - 17.06.2024</small> { id="15.2.4" }


<b><small>Verbesserungen</small></b> 

- Performance Steigerung: Bis zu 150% schnellere Insert/ Updates mit externen Zuordnungen 
- Bug: Import von Mapping Einstellungen wurde teilweise falsch übernommen, wurde gefixt



### 15.2.3<small> - 13.06.2024</small> { id="15.2.3" }

<b><small>Feature</small></b>    

- smartki: diverse Nummer (header_order_number,header_order_confirmation_numbers,header_delivery_note_numbers,payment_methods) werden nun zusammengefasst übergeben. 


<b><small>Verbesserungen</small></b> 

- ecoDMS Feature: Kein Ändern von Attributen, wenn schon identisch zu bestehender Klassifikation ist, bisher wurde in ecoDMS dann eine Revision vermerkt
- ecoDMS Feature: Unterstützung für Multifaktor Authentifizierung
- ecoDMS Bug: File ID wird nicht gespeichert, wenn über mehrere Verknüpfungen aktualisiert wird
- smartki: Überspringen von defekten PDFs z.B. 0Kb  
- Lexoffice Feature: Async Cooldown, wenn Ratelimit erreicht wird. (Performance Steigerung)
- EspoCRM: Nach Upsert Aktualisieren der Internen Daten
- SQL Injection Schutz erweitert
- Bug Workflow Editor: Zeigt keine Meldung über erfolgreichem speichern
- Bei User Sperre: Counter Fehlanmeldung wird auf 0 gesetzt und Aktiv false gesetzt

 
 

### 15.2.2<small> - 11.06.2024</small> { id="15.2.2" }

<b><small>Feature</small></b> 

- Externe Zuordnungen können nun im Mapping hinterlegt werden: So können Attribute wie z.B. Email Adresse, Kundennummer usw. 
verwendet werden, um Daten automatisch zuzuordnen. siehe [hier](<1 Verwendung/1 Mapping/mapping_fremdid.md>)



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
- Übersetzungen für Felder eingeführt: Es können nun sprechende Namen für Datenbank Felder importiert werden.
  Das ist v.a. bei alten Datenbanken praktisch, die keine aussagekräftigen Felder haben. Siehe [hier](<3 FAQ/FAQ/Feldbeschreibung.md>).
- Spalten Namen können nun aus der Tabelle mit einem Klick in die Zwischenablage kopiert werden.


### 15.1.2<small> - 02.05.2024</small> { id="15.1.2" }

<b><small>Feature</small></b> 

- Dieses Changelog eingeführt
- Softenging Webware Schnittstelle veröffentlicht
  
<b><small>Verbesserungen</small></b> 

- Keine externen Abhängigkeiten von JSDELIVER im Swaggerui mehr
