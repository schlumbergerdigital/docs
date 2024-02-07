# Konfigurationsdatei `params.json`

Alle Einstellungen des Arkivado Ecodms-Tools (außer dem Passwort) sind in einer Konfigurationsdatei auf dem lokalen Rechner gespeichert. Hier werden die Felder, Filter usw. definiert.

!!! Warning "UTF-8-Encoding"
    Die `params.json` muss zwingend in UTF-8 kodiert sein! Weitere Informationen finden Sie [hier](../Einleitung/utf8.md).

## Speicherorte

- Die Konfigurationsdatei `params.json` ist eine JSON-Datei in UTF-8-Kodierung.
- Sie befindet sich im Verzeichnis `%appdata%\arkivado\ecodmstool`.

- Das Passwort für ecoDMS ist nicht in der JSON-Datei enthalten. Es ist in der Anmeldeinformationsverwaltung von Windows gespeichert:
  `Systemsteuerung\Benutzerkonten\Anmeldeinformationsverwaltung`
- Die Lizenzdatei `license.lic` befindet sich ebenfalls im AppData-Verzeichnis. Diese Datei wird in der Regel beim Start aktualisiert und kann im Fehlerfall einfach gelöscht werden.
- Alle weiteren Pfade, z.B. für den Export, werden innerhalb der `params.json` definiert.

## Aufbau der JSON

1. Allgemeine Einstellungen [hier](config_general.md)
2. Dokumentenliste [hier](config_doclist.md)
3. Dokumentenexport [hier](config_docexport.md)
4. DATEV-Export [hier](config_datevexport.md)
5. SEPA-Export [hier](config_sepaexport.md)

[Weiter: Allgemeine Einstellungen](config_general.md){ .md-button }
