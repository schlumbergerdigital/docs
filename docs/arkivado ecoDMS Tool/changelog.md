# Changelog

Alle Aktualisierungen des Arkivado ecoDMS Tools 


## 11.20 - <small>23.01.2026</small> { id="11.20" }

<b><small>Verbesserungen</small></b> 

- Bei einigen Windowsversionen wurden die Dialoge nicht angezeigt
- Es wurde ein Fehler angezeigt, wenn in der Gui Konfiguration "show" fehlte. 
  

## 11.19 - <small>23.01.2026</small> { id="11.19" }

<b><small>Feature</small></b> 


- SEPA / Datev Export: Experimentelles Feature: ```AfterFailedValues``` Im Fehlerfall kann nun nach ecoDMS zurückgeschrieben werden. siehe [hier](<5. Wissenswertes/FAQ/Fehlerbehandlung.md>)
- SEPA: Es wird nun im Fehlerfall ein HTML Protokoll erstellt, dass die ganzen fehlerhaften Belege auflistet.



<b><small>Verbesserungen</small></b> 

- SEPA Export kann fehlschlagen bei bestimmten BIC Konstellationen
- EcoDMS Schnittstelle hat kleineren Memory Footprint bei sehr großen Dokumenten
- Messageboxen wurden nicht angezeigt. 
- SEPA Banking Schemata aktualisiert

<b><small>Docu</small></b> 

- Anleitung für  ```AfterFailedValues```  geschrieben [hier](<5. Wissenswertes/FAQ/Fehlerbehandlung.md>)
- SEPA Erklärung um ```AfterFailedValues```  erweitert  [hier](<3. Konfiguration/006config_sepaexport.md>)
- DATEV Erklärung um ```AfterFailedValues```  erweitert  [hier](<3. Konfiguration/005config_datevexport.md>)
- 
## 11.18 - <small>15.01.2026</small> { id="11.18" }

<b><small>Feature</small></b> 


- Dokumentexport: Nun möglich als Dateinamen dynamische Datumsangaben in Namen zu hinterlegen. Es können sowohl Dynamische Datumsangaben als auch formatierte Datumsangaben aus ecoDMS exportiert werden. [siehe hier](<5. Wissenswertes/FAQ/Datumsformatierung im Pfad.md>)  
- SEPA Export: Schon innerhalb des Arkivado Tools wird eine Logikprüfung der IBAN und BIC durchgeführt ob die Zahlen formal korrekt sind. Leerstellen usw. werden nun automatisch behandelt.

<b><small>Verbesserungen</small></b> 

- Retry Logik wenn Server überlastet ist z.B. wenn keine Antwort vom Server kommt intelligent implementiert  
- Umformatieren der Berechtigung wenn z.B. ein User beim Lesen und beim Schreiben stand. Dies war früher in ecoDMS erlaubt, führt nun aber zu Fehlern.  
- Umstellung auf HTTPX 
  

## 11.17 - <small>04.11.2025</small> { id="11.17" }

<b><small>Feature</small></b> 


 - Neuer Parameter eingeführt: ```AfterSuccessValues```. Hier können nach dem Export Klassifizierungen geändert werden, z. B. in einen anderen Ordner verschieben oder einen Status ändern.
 - Es können nun mehrere Bedingungen im ```IsExportedField``` hinterlegt werden. 
 - Das ecoDMS Modul erkennt automatisch die ecoDMS Version und erweitert seine Funktionalitäten, wenn unterstützt. 
 - Updatefilter-Zeiträume können, wenn von ecoDMS unterstützt, auch zeitlich fein (nicht nur tagesgenau) durchsucht werden.

<b><small>Verbesserungen</small></b> 

 - Verbesserte Logmeldungen.
 - Async Config Loader.
 - Prüfung auf plausible API-URL. 
 - Wenn kein Status gefunden oder übergeben wurde, wird ein Standardwert (1) gesetzt, da ohne Status kein Dokument angelegt wird.
 - Wenn keine Dokumentart gesetzt ist, wird "Nicht zugeordnet" (0) verwendet, da ohne Dokumentart kein Dokument angelegt wird.
 - Dokumentenberechtigung: Wenn ein Benutzer / eine Gruppe sowohl in Klassifizieren als auch in Lesen auftaucht, wird er/sie bei Lesen entfernt, da es sonst ab 25.02 zu Fehlern kommen kann.
 - Dokumentenberechtigung: Es konnte dazu kommen, dass die Berechtigung nicht geschrieben wurde. 

## 11.16 - <small>28.05.2025</small> { id="11.16" }

<b><small>Verbesserungen</small></b> 

 - Verbesserte Logmeldungen.
 - Zeigt nun Frontend-Fehler an, wenn Attribute in ecoDMS fehlen. Bisher wurde angezeigt "Nichts zum Exportieren gefunden".  
 - DATEV Export: Fehler ```set_default_tax_on_tax_error``` kann in gewissen Konfigurationen auftreten, wenn keine Rechnungsnummer übergeben wird. 
 - Bug beim automatischen Programmaufruf "cannot schedule new future" behoben.


## 11.15 - <small>23.05.2025</small> { id="11.15" }


<b><small>Feature</small></b> 

- Komplettes Umschreiben der HTTP Engine auf Async Calls.
- DATEV Kassenbelege als Kassenbeleg zu exportieren.
- Der Fehlerbericht enthält einen Link zum Dokument (bisher nur interner HTML-Link unterstützt).
- Bei Steuerprüfung im Fehlerfall auf Standard setzen: ```set_default_tax_on_tax_error``` siehe [hier](<3. Konfiguration/005config_datevexport.md>).

  
<b><small>Verbesserungen</small></b> 

- DATEV Export ab Stufe 2 unterstützt nun Sach- und Personenkonten.
- DATEV Export ab Stufe 2 unterstützt nun auch den Buchungscode.
- DATEV Steuerprüfung von negativen Werten in Gutschriften wird nun korrekt durchgeführt. 
- Verbesserter Umgang mit nicht existierenden Status / Typen. 
 

<b><small>Docu</small></b> 

- Funktionen ergänzt, siehe [hier](<2. Verwendung/001funktionen.md>)
- Artikel für Klassifizierung verfasst, siehe [hier](<3. Konfiguration/007config_klassifizierung.md>)
- Artikel für Berechtigungen geschrieben, siehe [hier](<5. Wissenswertes/FAQ/Berechtigungen setzen.md>)


## 11.14  - <small>17.03.2025</small> { id="11.14" }


<b><small>Feature</small></b> 

- Es ist nun möglich, Filter zu erstellen und ohne Export Attribute zu ändern. Z. B. Dokumente anhand von Filtern in Ordner zu verschieben. Siehe [hier](<3. Konfiguration/007config_klassifizierung.md>).
- Es ist nun möglich, Berechtigungen zu setzen oder unverändert zu lassen. Siehe [hier](<5. Wissenswertes/FAQ/Berechtigungen setzen.md>).

  
<b><small>Verbesserungen</small></b> 

- Mit ```STRG + J ``` kann nun die aktuelle JSON-Datei im Standard-Editor geöffnet werden. 
- SEPA Export kann nun auch mit Filtern versehen werden.
- DATEV: Mehr Logging. 
- SEPA: Fehlender Rechnungsbetrag führt dazu, dass die Buchung übersprungen wird. 
- DATEV: Rechnungsdatumsparser verbessert, wenn das Feld kein Datumsfeld ist. 
- Intern: Verwendet nun Python 3.13.
- Intern: Refactoring für großes Async Update.
 

<b><small>Docu</small></b> 

- Funktionen ergänzt, siehe [hier](<2. Verwendung/001funktionen.md>)
- Artikel für Klassifizierung verfasst, siehe [hier](<3. Konfiguration/007config_klassifizierung.md>)
- Artikel für Berechtigungen geschrieben, siehe [hier](<5. Wissenswertes/FAQ/Berechtigungen setzen.md>)


## 11.13  - <small>12.02.2025</small> { id="11.13" }


<b><small>Verbesserungen</small></b> 

- Bug DATEV: Absturz, wenn kein Belegdatum geschickt wird.
- Verbesserung ecoDMS: Beim Zurückschreiben keine NULL-Werte, da dies in neuer Version nicht mehr gestattet ist.
- Verbesserung DATEV: Meldung, wenn kein Datum hinterlegt ist.
- Verbesserung: Meldung, wenn in der Konfiguration DATEV gestartet wird, ohne dass Einträge vorhanden sind.
- Verbesserung: Ordnerverarbeitung intern verbessert.


<b><small>Docu</small></b> 


- DATEV EXTF Anleitung: Header angepasst, siehe [hier](<4. Vorlagen/Datev EXTF.md>)
- Anleitung für mehrere Firmen / Mandanten geschrieben, siehe [hier](<5. Wissenswertes/FAQ/Export mehrere Firmen.md>)
- Anleitung DATEV mehrere Rechnungseingangsarten, siehe [hier](<5. Wissenswertes/FAQ/Datev mehrere Rechnungseingangsarten.md>)



## 11.12  - <small>23.01.2025</small> { id="11.12" }

<b><small>Feature</small></b> 

- Beim Export können nun auch mehrere Felder benannt werden, die geändert werden sollen.
- Beim Export kann nun auch der Ordner angegeben werden. Dokumente können so nach Verarbeitung in einen definierten Ordner geschoben werden. 
- Experimentell weitere SEPA Pain-Formate aufgenommen, siehe [hier](<3. Konfiguration/006config_sepaexport.md#unterstützte-pain-formate>).


<b><small>Verbesserungen</small></b> 

- Wird eine JSON-Konfiguration ohne Lizenznummer eingefügt, wird nochmals nach der Lizenznummer gefragt, statt einfach abzubrechen.
- Auch der Basisordner wird nun dynamisch angelegt, wenn nicht auf der Festplatte vorhanden (bisher mit Fehler abgebrochen).


<b><small>Docu</small></b> 

- Neue Verwaltungskonfig-Vorlage erstellt, um schnell Infos aus ecoDMS zu erstellen, siehe [hier](<4. Vorlagen/Verwaltungs Übersicht.md>).
- Anleitung zum Exportieren der Listen in Einzeldateien, siehe  [hier](<5. Wissenswertes/FAQ/Export in Einzeldateien.md>).
- Anleitung zum Exportieren und anschließenden Verschieben geschrieben, siehe [hier](<5. Wissenswertes/FAQ/Export danach in ecoDMS verschieben.md>).
- Anleitung erweitert zum Status ändern, siehe [hier](<5. Wissenswertes/FAQ/Export über Status Steuern.md>).
- Anleitung für komplexe Datumsberechnungen im CSV-Header geschrieben, siehe [hier](<5. Wissenswertes/FAQ/Datumsberechnungen.md>).

## 11.11 - <small>10.12.2024</small> { id="11.11" }


<b><small>Verbesserungen</small></b> 

- DATEV: Export-XML Kompatibilität mit Anforderungen der DATEV erweitert.  
- Bug: CSV-Rundung auf mehr Nachkommastellen kürzt mehrere Nullen am Ende ggf. weg. 
- Bug: Einzelexport von Dateien konnte keinen dynamischen Dateipfad verwenden.  


<b><small>Docu</small></b> 

- Nummerformatierung für CSV Troubleshoot, siehe [hier](<5. Wissenswertes/FAQ/Nummerformatierung.md>)


## 11.10   - <small>22.11.2024</small> { id="11.10" }

<b><small>Feature</small></b> 

- Es kann nun gesteuert werden, ob die erste oder letzte Version vom Dokument heruntergeladen wird, abhängig von einem Attribut. Siehe [hier](<5. Wissenswertes/FAQ/Erste Version herunterladen.md>).
- DATEV Export: Exportiert nun die "Roh"-ZUGFeRD bzw. XRechnungen für die DATEV, da hier alle Daten ausgelesen werden.
- SEPA Export: Das Arkivado Tool schlägt die gängigsten Banken nach, wenn keine BIC angegeben ist.
- SEPA Export: Weitergehende Prüfung der IBAN auf Richtigkeit. 


<b><small>Verbesserungen</small></b> 

- Bug: Status konnte nicht als ```ToExport``` Feld verwendet werden.
- SEPA Export: IBAN und BIC können nun Leerzeichen enthalten, ohne dass dies Fehler sind.


<b><small>Docu</small></b> 

- Große Anleitung für E-Rechnung verfasst, siehe:  [Definition](<5. Wissenswertes/FAQ/0. E-Rechnung Definition.md>), [E-Rechnung in ecoDMS](<5. Wissenswertes/FAQ/1. E-Rechnung.md>).
- Anleitung für "Erste Version herunterladen" geschrieben, siehe [hier](<5. Wissenswertes/FAQ/Erste Version herunterladen.md>).
- Anleitung für den DATEV Export um XRechnungs-Optionen erweitert.  
- Anleitung für Export, der statusgesteuert ist, geschrieben, siehe  [hier](<5. Wissenswertes/FAQ/Export über Status Steuern.md>).
- SEPA Doku um dynamischen Verwendungszweck erweitert, siehe [hier](<3. Konfiguration/006config_sepaexport.md>).



## 11.9 Hotfix - <small>09.10.2024</small> { id="11.9" }

<b><small>Verbesserungen</small></b> 

- Bug: ```@date``` Funktion mit Datumsfeldern aus ecoDMS hat nicht funktioniert.

<b><small>Docu</small></b> 

- Vorlage: DATEV EXTF Format angepasst, sodass das Datum in <> steht. Die Vorlage ist [hier](<4. Vorlagen/Datev EXTF.md>).
  
## 11.9  - <small>09.10.2024</small> { id="11.9" }

<b><small>Feature</small></b> 

- DATEV Export: Rechnungen können über ecoDMS als bezahlt markiert werden. In der DATEV wird auf das Dokument ein Bezahlt-Stempel gesetzt. Dazu muss das Feld ```paidAt``` konfiguriert werden, siehe  [hier](<3. Konfiguration/005config_datevexport.md>).
- DATEV Export: Es können nun auch BIC / swiftCode Werte übergeben werden, siehe  [hier](<3. Konfiguration/005config_datevexport.md>).
- Allgemein: Export von Dokumentlisten kann nun als viele Einzeldateien ausgegeben werden.  
- Allgemein: Export der Ordnerschlüssel und externen Keys im Export, siehe [hier](<5. Wissenswertes/FAQ/Externe Ordner Keys verwenden.md>).


<b><small>Verbesserungen</small></b> 

- DATEV Export: IBAN wurde nicht immer übermittelt. 
- DATEV Export: Schnittstellen-Erweiterung auf v6. 
- ecoDMS: API-Tests auf Verbindungen verbessert.
- Excel Export: Wird ein doppelter Spaltenname angegeben, wird nun am Ende eine Zahl angehängt, um keinen Fehler in Excel zu bekommen.


<b><small>Docu</small></b> 

- Neue Vorlage: Excel Rechnungsübersicht: [hier](<4. Vorlagen/Rechungs Übersicht.md>).
- Neue Anleitung für Export mit ecoDMS Ordner-Schlüssel / Ordner Keys: [hier](<5. Wissenswertes/FAQ/Externe Ordner Keys verwenden.md>).
- Dokumentation erweitert in der Dokumentliste, um Metadaten wie User und ecoDMS Server anzuzeigen, siehe  [hier](<3. Konfiguration/003config_doclist.md>).
  
  
## 11.8  - <small>14.08.2024</small> { id="11.8" }


<b><small>Feature</small></b> 

- Drei neue Funktionen für die Berechtigungsübersicht, siehe [hier](<2. Verwendung/001funktionen.md>):
- Benutzer Export
- Ordner Rollen Export
- Ordner Benutzer Export
  

<b><small>Verbesserungen</small></b> 

- Ordner-, Status-, Typen-Ausgabe in formatierter Excel.


## 11.7  - <small>18.07.2024</small> { id="11.7" }


<b><small>Verbesserungen</small></b> 

- Multifaktor-Anmeldung angepasst. 
- DATEV Export: Wird kein Rechnungsdatum angegeben oder im falschen Format, wird das Dokument übersprungen und informiert.
- Bug: DATEV Export: Info-Feld wurde nicht korrekt übergeben.
  

## 11.6  - <small>10.07.2024</small> { id="11.6" }

<b><small>Feature</small></b>

- SEPA: Bankenexport über die ecoDMS Oberfläche ermöglicht.

<b><small>Verbesserungen</small></b> 

- Versionsprüfung verbessert
- Bug: Zahlen wurden teilweise nicht in Excel angezeigt. 
- Bug: Bei SEPA Export kam es zu einem Fehler, wenn eine Fehlermeldung erstellt wurde.
- Bug: Steuerung K hat unter Umständen nicht reagiert.

<b><small>Docu</small></b> 

- SEPA Doku um das ecoDMS Feld ergänzt.


## 11.5  - <small>30.06.2024</small> { id="11.5" }


<b><small>Verbesserungen</small></b> 

- Dateigröße vom Arkivado Tool halbiert: Weniger Platzbedarf und schnellerer Start. 
- DATEV Unternehmen Online: DATEV löscht ohne Warnung Dokumente, deren Zahlungsziel hinter dem Rechnungsdatum liegt: Prüfung eingebaut, um ggf. das Zahlungsziel automatisch zu entfernen.
- Bug: Bei SEPA Export kam es zu einem Fehler, wenn in Windows 10 via CMD aufgerufen wurde.
- Bug: Zahlen wurden teilweise nicht in Excel angezeigt. 
- Bug: Bei SEPA Export kam es zu einem Fehler, wenn eine Fehlermeldung erstellt wurde.

## 11.4    - <small>20.06.2024</small> { id="11.4" }


<b><small>Verbesserungen</small></b> 

- Bug: Kommandozeilen-Execute startet nicht korrekt – nur Splashscreen Meldung erscheint – behoben. 
- Bug: Konfiguration legt mehrere Ordner an – behoben.  
- Bug: Benutzernamen mit Umlauten können sich nicht verbinden – behoben.
- Bug: *DATEV Unternehmen Online* Wenn Dokumentsteuer unterschiedlich ist, wird nur das Belegbild übergeben (DATEV löscht sonst ohne Kommentar das Dokument) – behoben.
- Bug: *DATEV Unternehmen Online* Rechnungsnummern, die z. B. ein ```:``` enthalten, wurden von der DATEV abgelehnt. Fehlerhafte Zeichen werden in der Rechnungsnummer ersetzt – behoben.

<b><small>Docu</small></b> 

- KB Einträge zur Verbindung angepasst auf neue ```STRG + K``` Konfiguration.




## 11.3    - <small>11.06.2024</small> { id="11.3" }



<b><small>Feature</small></b> 

- ecoDMS Zugangsdaten über die grafische Oberfläche einstellen.     
Drücken Sie einfach ```STRG + K``` siehe [hier](<5. Wissenswertes/FAQ/EcoDMS Zugangsdaten ändern.md>).
- ecoDMS Multifaktor-Authentifizierung unterstützt.

<b><small>Verbesserungen</small></b> 

- Großes internes Refactoring. 
- Funktionsnamen sind nun Case-insensitive.    


## 11.2   - <small>23.05.2024</small> { id="11.2" }


<b><small>Feature</small></b> 

- Laufende Aufträge können nun durch Benutzer in der Oberfläche abgebrochen werden. 


<b><small>Verbesserungen</small></b> 

- Bug behoben: Ladebalken wird nicht immer angezeigt.


<b><small>Docu</small></b> 

- Vorlage für EXTF ergänzt.

## 11.1   - <small>14.05.2024</small> { id="11.1" }

:partying_face: Veröffentlichung der neuen Version :rocket: 


<b><small>Feature</small></b> 

- Export von ecoDMS Dateien in formatierte Excel-Berichte.
- Oberflächen und Buttons sind über JSON konfigurierbar. Spezifischer Look für den Endanwender möglich.
- Per Kommandozeile aufrufbar, um automatische Workflows zu starten. Damit sind zeitgesteuerte Exporte möglich.
- Möglichkeit, Zeitraum-Filter ein- und auszuschalten in allen Optionen.
- Möglichkeit, Export-Spalten anzupassen, umzubenennen, hinzuzufügen.
- Möglichkeit, Export-Kopfzeilen hinzuzufügen.
- Möglichkeit, mehrere Profile für unterschiedliche Berichte und/oder Server zu hinterlegen (benötigt erweiterte Lizenz).
- Exporte können für beliebige FIBU-, ERP-, CRM-Systeme oder Portale konfiguriert werden.
- Kopfzeilen können Zusammenfassungen wie min/max oder von-bis Datumsangaben wiedergeben.
- Standardwerte können hinterlegt werden, wenn keine Werte in ecoDMS vorhanden sind.
- Fehler im DATEV Export werden nun als *schöne* HTML Tabelle geöffnet.

<b><small>Verbesserungen</small></b> 

- Anzeige des Logfiles im Shellfenster kann ausgeblendet werden, Logfile kann über Oberfläche geöffnet werden.
- Prüfung, ob ein eingegebenes Datum gültig ist.
- Prüfung der JSON-Datei und ggf. Hinweis auf konkreten Fehler.
- Bei nicht verbundenem Server oder fehlerhafter API kommt sofort eine Fehlermeldung.
- Bei Zertifikatsfehlern sprechende Fehler hinterlegt.
- Sprechende Fehlermeldung, wenn Server nicht erreicht ist.
- Im Automatik-Modus: Programm beendet sich, wenn keine Verbindung zum Server aufbaubar ist. 

<b><small>Docu</small></b> 

- Einführung Changelog zu Releaseständen.
- Einführung Online-Dokumentation.