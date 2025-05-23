# Changelog

alle Aktualisierungen vom arkivado ecoDMS Tool 

## 11.15 - <small>23.05.2025</small> { id="11.15" }


<b><small>Feature</small></b> 

- Komplettes Umschreiben der HTTP Engin auf Async Calls
- Datev Kassenbelege als Kassenbeleg zu exportieren
- Der Fehlerbericht enthält einen Link zum Dokument (bisher nur Interner HTML Link unterstützt)
- Bei Steuererprüfung im fehlerfall auf standard setzen: ```set_default_tax_on_tax_error``` siehe [hier](<3. Konfiguration/005config_datevexport.md>)

  
<b><small>Verbesserungen</small></b> 

- Datev Export ab Stufe 2 untersützt nun Sach und Personen Konten
- Datev Export ab Stufe 2 unterstützt nun auch den BuchungsCode
- Datev Steuerprüfung von negativen Werden in Gutschriften werden nun  korrekt geprüft. 
- Verbesserter Umgang mit nicht exitierenden Status / Typen 
 

<b><small>Docu</small></b> 

- Funktionen ergänzt siehe [hier](<2. Verwendung/001funktionen.md>)
- Artikel für Klassifizierung verfasst, siehe [hier](<3. Konfiguration/007config_klassifizierung.md>)
- Artikel für Berrechtigungen geschrieben, siehe [hier](<5. Wissenswertes/FAQ/Berechtigungen setzen.md>)


## 11.14  - <small>17.03.2025</small> { id="11.14" }


<b><small>Feature</small></b> 

- Es ist nun möglich Filter zu erstellen und ohne Export Attribute zu ändern. Z.B. Dokumente anhand von Filtern in Ornder zu verschieben. siehe [hier](<3. Konfiguration/007config_klassifizierung.md>)
- Es ist nun möglich Berrechtigungen zu setzen oder stehen zu lassen. [hier](<5. Wissenswertes/FAQ/Berechtigungen setzen.md>)

  
<b><small>Verbesserungen</small></b> 

- Mit ```STRG + J ``` kann nun die aktuelle JSON Datei im Standard Editor geöffnet werden. 
- SEPA Export kann nun auch mit Filtern versehen werden
- Datev: Mehr logging 
- SEPA Fehlender Rechnungsbetrag führt dazu dass Buchung übersprungen wird 
- Datev: Rechnungsdatumsparser verbessert, wenn Feld kein Datumsfeld ist. 
- Intern: Verwendet nun Python 3.13
- Intern: Refactoring für großes Async Update
 

<b><small>Docu</small></b> 

- Funktionen ergänzt siehe [hier](<2. Verwendung/001funktionen.md>)
- Artikel für Klassifizierung verfasst, siehe [hier](<3. Konfiguration/007config_klassifizierung.md>)
- Artikel für Berrechtigungen geschrieben, siehe [hier](<5. Wissenswertes/FAQ/Berechtigungen setzen.md>)


## 11.13  - <small>12.02.2025</small> { id="11.13" }


<b><small>Verbesserungen</small></b> 

- Bug Datev:  Absturz wenn Kein Belegdatum geschickt wird
- Verbesserung: ecoDMS beim zurückschreiben keine NUll Werte, da dies in neuer Version nicht mehr gestattet sind.
- Verbesserung Datev: Meldung wenn kein Datum hinterlegt ist
- Verbesserung: Meldung wenn in Konfig Datev gestartet wird ohne das Einträge vorhanden sind
- Verbesserung: Ordner Verarbeitung intern verbessert


<b><small>Docu</small></b> 


- Datev Extf Anleitung: Header angepasst siehe [hier](<4. Vorlagen/Datev EXTF.md>)
- Anleitung für mehrere Firmen / Mandanten geschrieben siehe [hier](<5. Wissenswertes/FAQ/Export mehrere Firmen.md>)
- Anleitung Datev mehrere Rechnungseingangsarten  [hier](<5. Wissenswertes/FAQ/Datev mehrere Rechnungseingangsarten.md>)



## 11.12  - <small>23.01.2025</small> { id="11.12" }

<b><small>Feature</small></b> 

- Beim Export können nun auch mehrere Felder benannt werden die geändert werden soll
- Beim Export kann nun auch der Ordner angegeben werden. Dokumente können so nach verarbeitung in einen definierten Ornder geschoben werden. 
- Experimentell weitere SEPA Pain Formate aufgenommen siehe [hier](<3. Konfiguration/006config_sepaexport.md#unterstutzte-pain-formate>)


<b><small>Verbesserungen</small></b> 

- Wird eine JSON Konfig ohne Lizenznr reinkopiert, wird nochmals nach der Lizenznummer gefragt, statt einfach abgebrochen
- Auch der Basisordner wird nun dynamisch angelegt, wenn nicht auf der Festplatte vorhanden, bisher mit Fehler abgebrochen


<b><small>Docu</small></b> 

- Neue Verwaltungskonfig Vorlage erstellt um schnell Infos aus ecoDMS zu erstellen, siehe [hier](<4. Vorlagen/Verwaltungs Übersicht.md>)
- Anleitung zum exporieren der Listen in Einzeldateien siehe  [hier](<5. Wissenswertes/FAQ/Export in Einzeldateien.md>)
- Anleitung zum exportieren und anschließend verschieben geschrieben siehe [hier](<5. Wissenswertes/FAQ/Export danach in ecoDMS verschieben.md>)
- Anleitung erweitert  zum Status ändern siehe [hier](<5. Wissenswertes/FAQ/Export über Status Steuern.md>)
- Anleitung für komplexe Datumsberechnungen im CSV Header geschrieben siehe [hier](<5. Wissenswertes/FAQ/Datumsberechnugen.md>)

## 11.11 - <small>10.12.2024</small> { id="11.11" }


<b><small>Verbesserungen</small></b> 

- Datev: Export XML Kompatibilität mit Anforderungen der DATEV erweitert.  
- Bug: CSV Rundung auf mehr Nachkommastellen, kürzt mehrere 0en am Ende ggf. weg. 
- Bug: Einzelexport von Dateien konnten keinen dynamnischen Dateipfad verwenden.  


<b><small>Docu</small></b> 

- Nummerformatierung  für CVS Toubleshoot [hier](<5. Wissenswertes/FAQ/Nummerformatierung.md>)


## 11.10   - <small>22.11.2024</small> { id="11.10" }

<b><small>Feature</small></b> 

- Es kann nun gesteuert werden ob die erste, oder letzte Version vom Dokument heruntergeladen wird, abhängig von einem Attribut siehe [hier](<5. Wissenswertes/FAQ/Erste Version herunterladen.md>)
- Datev Export: Exportiert nun die *Roh* Zugpferd bzw. Xrechnungen  für die Datev. Da hier alle Daten von der Datev ausgelesen werden.
- SEPA Export: Das Arkviado Tool schlägt die gängisten Banken nach, wenn keine Bic angegeben ist
- SEPA Export: Weitergehende Prüfung der IBAN auf Richtigkeit. 


<b><small>Verbesserungen</small></b> 

- Bug: Status konnte nicht als ToExport Field verwendet werden
- SEPA Export: IBAN und BIC können nun Leerzeichen enthalten ohne dass es Fehler sind.


<b><small>Docu</small></b> 

- Große Anleitung für E-Rechnung verfasst, siehe:  [Definition](<5. Wissenswertes/FAQ/0. E-Rechnung Definition.md>), [E-Rechnung in ecoDMS](<5. Wissenswertes/FAQ/1. E-Rechnung.md>)
- Anleitung für erste Version herunterladen geschieben, siehe [hier](<5. Wissenswertes/FAQ/Erste Version herunterladen.md>)
- Anleitung für den Datev Export um XRechnungs Optionen erweitert  
- Anleitung für Export der Status gesteuert ist geschrieben, siehe  [hier](<5. Wissenswertes/FAQ/Export über Status Steuern.md>)
- SEPA Doku um dynamischen Verwendungszweck erweitert, siehe [hier](<3. Konfiguration/006config_sepaexport.md>)



## 11.9 Hotfix - <small>09.10.2024</small> { id="11.9" }

<b><small>Verbesserungen</small></b> 

- Bug: @date Funktion mit Datumsfeldern aus ecoDMS haben nicht funktioniert.

<b><small>Docu</small></b> 

- Vorlage: Datev EXTF Format angepasst, dass das Datum in <> steht die Vorlage ist [hier](<4. Vorlagen/Datev EXTF.md>)
  
## 11.9  - <small>09.10.2024</small> { id="11.9" }

<b><small>Feature</small></b> 

- DATEV Export: Rechnungen können über ecoDMS als bezahlt markiert werden.  In der Datev wird auf das Dokument ein Bezahlt Stempel gesetzt. Dazu muss das Feld paidAt konfiguiert werden siehe  [hier](<3. Konfiguration/005config_datevexport.md>)
- DATEV Export: Es können nun auch BIC /swiftCode Werte übergeben werden   [hier](<3. Konfiguration/005config_datevexport.md>)
- Allgemein: Export von Dokumentlisten können nun als viele Einzeldatein ausgegeben werden.  
- Allgemein: Export von den Ordnerschlüssel und Externe Keys im Export [hier](<5. Wissenswertes/FAQ/Externe Ornder Keys verwenden.md>)


<b><small>Verbesserungen</small></b> 

- DATEV Export: IBAN wurde nicht immer übermittelt 
- DATEV Export: Schnittellen Erweitertung auf V.6 
- EcoDMS: Api Tests auf Verbindungen verbessert
- Excel Export: Wird ein doppelter Spaltenname angegeben, wird nun am Ende eine Zahl angehängt um keinen Fehler in Excel zu bekommen


<b><small>Docu</small></b> 

- Neue Vorlage: Excel Rechnungsübersicht: [hier](<4. Vorlagen/Rechungs Übersicht.md>)
- Neue Anleitung für Export mit ecoDMS Ordner Schlüssel / Ordner Keys: [hier](<5. Wissenswertes/FAQ/Externe Ornder Keys verwenden.md>)
- Dokumentation erweitert im Dokumentliste um Metadaten anzuzeigen wie user und ecodmsserver siehe  [hier](<3. Konfiguration/003config_doclist.md>)
  
  
## 11.8  - <small>14.08.2024</small> { id="11.8" }


<b><small>Feature</small></b> 

- Drei neue Funktionen für die Berechtigungsübersicht siehe [hier](<2. Verwendung/001funktionen.md>):
- Benutzer Export
- Ordner Rollen Export
- Ordner Benutzer export
  

<b><small>Verbesserungen</small></b> 

- Ornder, Status, Tyen Ausgabe in formatierten Excel 


## 11.7  - <small>18.07.2024</small> { id="11.7" }


<b><small>Verbesserungen</small></b> 

- Mutifaktor Anmeldung angepasst 
- DATEV Export: Wird kein Rechnungsdatum angegeben oder im falschen Format, wird das Dokument übersprungen und Infromiert.
- Bug: DATEV Export: Info Feld wurde nicht korrekt übergeben
  

## 11.6  - <small>10.07.2024</small> { id="11.6" }

<b><small>Feature</small></b>

- Sepa: Banken export über die EcoDMS Oberfäche ermöglicht

<b><small>Verbesserungen</small></b> 

- Versionsprüfung verbessert
- Bug: Zahlen wurden teilweise nicht in Excel angezeigt 
- Bug: Bei Sepa Export kam es zum Fehler, wenn eine Fehlermeldung erstellt wird
- Bug: Steuerung K hat unter umständen nicht reagiert

<b><small>Docu</small></b> 

- Sepa Doku um das EcoDMS Feld ergänzt


## 11.5  - <small>30.06.2024</small> { id="11.5" }


<b><small>Verbesserungen</small></b> 

- Dateigröße vom Arkviado Tool halbiert: Weniger Platzbedarf und schnellerer Start 
- DATEV Unternehmen Online: Datev löscht ohne Warnung Dokumente bei denen das Zahlungsziel hinter dem Rechnungsdatum liegt: Prüfung eingebaut um ggf. das Zahlungsziel dann automatisch zu entfernen.
- Bug: Bei Sepa Export kam es zu Fehler, wenn in Windows 10 via CMD aufgerufen wurde
- Bug: Zahlen wurden teilweise nicht in Excel angezeigt 
- Bug: Bei Sepa Export kam es zum Fehler, wenn eine Fehlermeldung erstellt wird

## 11.4    - <small>20.06.2024</small> { id="11.4" }


<b><small>Verbesserungen</small></b> 

- Bug: Kommandndozeilen Execute startet nicht korrekt 
    *nur Splashscreen Meldung erscheint* behoben 
- Bug: Konfig legt mehrere Ordner an behoben  
- Bug: Benutzernamen mit Umlauten können sich nicht verbinden behoben
- Bug: *Datev Unternehmen Online* Wenn Dokument Steuer unterschiedlich ist, wird nur das Belegbild übergeben. (Datev löscht sonst ohne Kommentar das Dokument ) behoben
- Bug: *Datev Unternehmen Online* Rechnungsnummer die z.B.  ein ```:``` enthalten, wurden von der Datev abgelehnt. Fehlerhafte Zeichen werden in der Rechnungsnummer ersetzt.

<b><small>Docu</small></b> 

- KB Einträge zur Verbindung angepasst auf neue  -  ``` STRG + K ``` Konfiguration




## 11.3    - <small>11.06.2024</small> { id="11.3" }



<b><small>Feature</small></b> 

- EcoDMS Zugangsdaten über die grafische Oberfläche  einstellen.     
Drücken Sie einfach ```STRG + K``` siehe [hier](<5. Wissenswertes/FAQ/EcoDMS Zugangangsdaten ändern.md>)
- EcoDMS Multifkator Authentifizierung unterstützt

<b><small>Verbesserungen</small></b> 

- Große interne Refactoring 
- Funktionsnamen sind nun Case insensitive    


## 11.2   - <small>23.05.2024</small> { id="11.2" }


<b><small>Feature</small></b> 

- Laufende Aufträge können nun durch User in der Oberfläche abgebrochen werden. 


<b><small>Verbesserungen</small></b> 

- Bug behoben: Ladebalken wird nicht immer angezeigt


<b><small>Docu</small></b> 

- Vorlage für EXTF ergänzt

## 11.1   - <small>14.05.2024</small> { id="11.1" }

:partying_face:  Veröffentlichung der neuen Version :rocket: 


<b><small>Feature</small></b> 

- Export von ecoDMS Dateien in formatierte Excel Berichte
- Oberflächen und Buttons sind über json konfigurierbar. Spezifischer Look für den Endanwender möglich
- Per Kommandozeile aufrufbar, um automatische Workflows zu starten. Damit sind zeitgesteuerte Exporte möglich.
- Möglichkeit Zeitraum Filter ein und auszustellen in allen Optionen
- Möglichkeit Export Spalten anzupassen, umzubenennen hinzuzufügen
- Möglichkeit Export Kopfzeilen hinzuzufügen
- Möglichkeit mehrere Profile für unterschiedliche Berichte und/oder Server zu hinterlegen (benötigt erweiterte Lizenz)
- Exporte können für beliebige FIBU-,ERP-, CRM-Systeme oder Portale konfiguriert werden
- Kopfzeilen können Zusammenfassungen wie min/max oder von bis Datumsangaben wiedergeben
- Standardwerte können hinterlegt werden, wenn keine Werte in ecoDMS vorhanden sind
- Fehler im Datev Export werden nun als *schöne* HTML Tabelle geöffnet

<b><small>Verbesserungen</small></b> 

- Anzeige des Logfiles im Shellfenster kann ausgeblendet werden, Logfile kann über Oberfläche geöffnet werden.
- Prüfung ob ein eingegebenes Datums
- Prüfung der JSON Datei und ggf. Hinweis auf konkreten Fehler
- Bei nicht verbundenen Server, oder fehlerhafter API kommt sofort eine Fehlermeldung.
- Bei Zertifikatsfehler sprechende Fehler hinterlegt
- Sprechende Fehlermeldung wenn Server wenn nicht erreicht ist
- Im Automatik Modus: Programm beendet sich wenn keine Verbindung zum Server aufbaubar ist 

<b><small>Docu</small></b> 

- Einführung Changelog zu Realeaseständen
- Einführung Onlinedokumentation