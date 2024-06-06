# Technischer Background

## Updates
Das arkivado Tool ist ein einzelnes ausführbares Softwarepaket (exe Datei), welches ohne Installation auskommt.
Bei einem Update wird einfach die bestehende Datei ausgetauscht.

Wir unterstützen Windows 10 und 11 bzw. die entsprechenden Serverbetriebssystem ab Version 2016.

## Konfiguration
Die Konfiguration wird in einer JSON Datei abgelegt.

Diese ist im Verzeichnis ```C:\Users\<Username>>\AppData\Roaming\arkivado\arkivado_up``` 
abgelegt.
Sie können das Verzeichnis auch im Dateiexplorer mit ```%appdata%```  aufrufen.
Diese JSON Datei ist unbedingt im *UTF8* Format abzuspeichern.
Vorsicht mit älteren Editoren unter Windows 10 oder 11. Diese speichern und öffnen die Datei nicht im korrekten Format.    

Siehe auch den Bereich [UTF8](<008utf8.md>) in dieser Dokumentation.


## Passwort Speicher
Das Passwort für die Anmeldung wird unter
```"Systemsteuerung\Benutzerkonten\Anmeldeinformationsverwaltung"``` gespeichert und kann dort bei Bedarf gelöscht oder geändert werden.

Das arkivado Tool kann auch per Kommandozeile mit einer angegebenen Konfiguration gestartet werden.
Damit können bei Bedarf auch zeitgesteuerte Aufgaben auf einem Server durchgeführt werden.
