# Funktionen

Folgendes kann das arkivado Tool

- Dokumentliste Export
- Dokument Export
- DATEV Export
- SEPA Export
- Ordner Export
- Typen Export
- Status Export
- Benutzer Export
- Ordner Rollen Export
- Ordner Benutzer Export
- Klassifikation 
- Konfigurieren

## Dokumentliste Export
Hiermit kann eine ```csv``` oder ```Excel``` Liste erstellt werden. 

Dabei kann der Export in ecoDMS markieren, was bereits exportiert wurde. 

Typischerweise werden damit folgende Szenarien abgedeckt:

- Eine Liste von Protokollen erstellen
- Ein DATEV Export in Ext Format also ohne Dokumente
- Export für diverse ERP Systeme die nur aufs DMS verweisen ohne Dokumente

[hier mehr](<../3. Konfiguration/003config_doclist.md>){ .md-button }
  


## Dokument Export
Der Dokument Export macht alles wie der  ```Dokumentliste Export``` und zusätzlich werden die Dokumente exportiert

Typischerweise werden damit folgende Szenarien abgedeckt:

- Übergabe an andere Systeme wie Buchhaltung
- Portale
- Steuerberatung usw.

[hier mehr](<../3. Konfiguration/004config_docexport.md>){ .md-button }


## DATEV Export
Der DATEV Export geht auch für andere Systeme die eine Importschnittstelle besitzen. 

Export im modernen **DATEV XML Format**, bei dem sowohl die Dokumente, als auch die Metadaten übergeben werden.

- Dabei werden bereits exportierte Dokumente in ecoDMS als exportiert markiert. 
- Zudem werden noch mehr Felder aufbereitet und eine Logikprüfung durchgeführt z.B. passen Steuern mit dem Rechnungsbetrag zusammen.
- Eignet sich v.a. für DATEV Unternehmen Online  + Turm Rechnungseingangs KI

[hier mehr](<../3. Konfiguration/005config_datevexport.md>){ .md-button }


## SEPA Export 

Erstellt aus den Metadaten in ecoDMS eine SEPA XML Überweisungsdatei.

[hier mehr](<../3. Konfiguration/006config_sepaexport.md>){ .md-button }

## Ordner Export 

Erstellt eine ```csv``` oder ```Excel``` Datei mit den in ecoDMS angelegten Ordnern 


## Typen Export
Erstellt eine ```csv``` oder ```Excel``` Datei mit den in ecoDMS angelegten Dokument Typen

## Status Export 
Erstellt eine ```csv``` oder ```Excel``` Datei mit den in ecoDMS angelegten Statusarten z.B. erledigt. 

## Benutzer Export
Erstellt eine Excel Tabelle mit Rollen und Benutzern. So erhält man einen Überblick welche Benutzer gibt es und in welchen Rollen sind sie. 

## Ordner Rollen Export
Erstellt eine Excel Tabelle in der aufgeführt wird, welche Rolle auf welchen Ordner zugriff hat.

## Ordner Benutzer Export
Erstellt eine Excel Tabelle ähnlich wie die *Ordner Rollen Export* Liste, nur dass es auf die einzelnen Benutzer runtergebrochen wirs. 

## Klassifizierung

Ohne etwas zu Exportieren kann das arkivado Tool nun die Attribute von Dokumenten ändern. 
Die Funktionalität entspricht wie in ecoDMS eeinem Filter setzen und dann Massenklassifizierung durchführen. 

[hier mehr](<../3. Konfiguration/007config_klassifizierung.md>){ .md-button } 

## Konfigurieren
Die Einstellungsmaske für die ecoDMS Zugangsdaten. (Keine weitere  Einstellungen)
Kann auch mit ``` STRG + K ``` aufgerufen werden.

[hier mehr](<../5. Wissenswertes/FAQ/EcoDMS Zugangangsdaten ändern.md>){ .md-button }