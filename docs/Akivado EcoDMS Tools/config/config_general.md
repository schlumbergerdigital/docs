## Globale Einstellungen

Werte wie Lizenz, ecoDMS Server-Nutzer usw. werden über die Oberfläche konfiguriert, können aber auch bei Bedarf manuell angepasst werden.

```
 "license": "12345",
```

Opt. | Feld | Beschreibung | Beispielwert
-------|------|--------------|-----------------
 | license | Dies ist der Lizenzschlüssel, den Sie erhalten haben. Der Schlüssel wird automatisch konfiguriert. | ```6385c73c550rgrwefg0a11f```

```
    "ecodms": {
        "ECODMSurl": "https://bsp.docarchiv.de:8180/api/",
        "ECODMSuser": "ecodms",
        "ECODMSpw": null,
        "ECODMSabort_on_ssl_error": true,
        "export_to": "excel",
        "export_path": "C:\\ecoDMS Daten\\Export_ecoDMS",
        "export_open": true,
        "paths": {
            "Rechnungseingang": "S:\\Buchhaltung\\Rechnungseingang",
            "Rechnung": "S:\\Buchhaltung\\Rechnungseingang",
            "Rechnungsausgang": "S:\\Buchhaltung\\Rechnungsausgang",
            "Kasse": "S:\\Buchhaltung\\Kasse",
            "Sonstiges": "S:\\Buchhaltung\\Sonstiges",
            "Auswertungen FIBU": "S:\\Buchhaltung\\Auswertungen"
        }
```

\* = Optional

Opt.| Feld | Beschreibung | Beispielwert
-------|------|--------------|-----------------
 | ECODMSurl | Der vollständige Pfad zum ecoDMS Server mit API am Ende. Wird automatisch konfiguriert. | ```https://beispiel.docarchiv.de:8180/api/```
 | ECODMSuser | Der ecoDMS Benutzer. Achten Sie hierbei auf Groß- und Kleinschreibung. Wird automatisch konfiguriert. | ```ecodms```
 | ECODMSpw | Das ecoDMS Passwort wird NICHT hier angegeben, es liegt in der Anmeldeinformationsverwaltung. Der Wert sollte immer null sein. Nur für Testzwecke ein Passwort hier setzen! Andernfalls besteht ein gravierendes Sicherheitsrisiko! | ```null```
 | ECODMSabort_on_ssl_error | Überprüft das Zertifikat des ecoDMS Servers. Bei einem selbstsignierten Zertifikat aus ecoDMS, verwenden Sie ```false```, ansonsten ```true```. | ```true```
\* | export_to | Gibt an, in welchem Format exportiert werden soll. Wenn Sie Excel nutzen, empfehlen wir "excel". Möglichkeiten: ```excel```, ```csv```
\* | export_path | Der Pfad, unter dem die Excel-Dateien abgelegt werden sollen (nicht die Dokumente). Wenn nichts angegeben wird, ist der Pfad: ```%appdata%\\arkivado\\ecodmstool``` | ```C:\\ecoDMS Daten\\Export_ecoDMS```
\* | export_open | Gibt an, ob die erstellte Excel-/CSV-Datei nach dem Export automatisch angezeigt werden soll. Öffnet die Datei mit dem hinterlegten Standardprogramm. | ```true```
 | paths | Gibt an, wohin Dokumente nach Dokumentenart sortiert exportiert werden sollen. Dabei wird die Dokumentenart angegeben, gefolgt vom Pfad auf der Festplatte. Siehe dazu auch den Abschnitt "DATEV konfigurieren". | ```{"Rechnungseingang": "C:\\Datev\\Belegtransfer\\Rechnungseingang", "Rechnungsausgang": "C:\\Datev\\Belegtransfer\\Rechnungsausgang"}```
