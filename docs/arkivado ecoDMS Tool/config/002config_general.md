# Globale Einstellungen


## ecoDMS Verbindung 
Die Einstellungen werden im Frontend abgefragt. Im Allgemeinen muss hier nichts eingestellt werden.
 
``` JSON title="ecoDMS Verbindungseinstellungen"
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
        },
     
```

\* = Optional

| Opt. | Feld                     | Beschreibung                                                                                                                                                                                                                        | Beispielwert                                                                                                                               |
| ---- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| *    | ECODMSurl                | Der vollständige Pfad zum ecoDMS Server mit API am Ende. Wird automatisch konfiguriert.                                                                                                                                             | ```https://beispiel.docarchiv.de:8180/api/```                                                                                              |
| *    | ECODMSuser               | Der ecoDMS Benutzer. Achten Sie hierbei auf Groß- und Kleinschreibung. Wird automatisch konfiguriert.                                                                                                                               | ```ecodms```                                                                                                                               |
| *    | ECODMSpw                 | Das ecoDMS Passwort wird NICHT hier angegeben, es liegt in der Anmeldeinformationsverwaltung. Der Wert sollte immer null sein. Nur für Testzwecke ein Passwort hier setzen! Andernfalls besteht ein gravierendes Sicherheitsrisiko! | ```null```                                                                                                                                 |
| *    | ECODMSabort_on_ssl_error | Überprüft das Zertifikat des ecoDMS Servers. Bei einem selbstsignierten Zertifikat aus ecoDMS, verwenden Sie ```false```, ansonsten ```true```.                                                                                     | ```true```                                                                                                                                 |
| *    | export_to                | Gibt an, in welchem Format exportiert werden soll. Wenn Sie Excel nutzen, empfehlen wir "excel". Möglichkeiten: ```excel```, ```csv```                                                                                              |
| *    | export_path              | Der Pfad, unter dem die Excel-Dateien abgelegt werden sollen (nicht die Dokumente). Wenn nichts angegeben wird, ist der Pfad: ```%appdata%\\arkivado\\ecodmstool```                                                                 | ```C:\\ecoDMS Daten\\Export_ecoDMS```                                                                                                      |
| *    | export_open              | Gibt an, ob die erstellte Excel-/CSV-Datei nach dem Export automatisch angezeigt werden soll. Öffnet die Datei mit dem hinterlegten Standardprogramm.                                                                               | ```true```                                                                                                                                 |
|      | paths                    | Gibt an, wohin Dokumente nach Dokumentenart sortiert exportiert werden sollen. Dabei wird die Dokumentenart angegeben, gefolgt vom Pfad auf der Festplatte. Siehe dazu auch den Abschnitt "DATEV konfigurieren".                    | ```{"Rechnungseingang": "C:\\Datev\\Belegtransfer\\Rechnungseingang", "Rechnungsausgang": "C:\\Datev\\Belegtransfer\\Rechnungsausgang"}``` |


## CSV
``` JSON title="Konfiguration der csv Exportdatei:"
 "csv":{
            "newline": "\r\n",
            "encoding": "iso-8859-1",
            "seperator": ";",
            "quotechar": "\"",
            "quote":"minimal"

        },
```

Wird ein CSV Export ausgeführt kann hier das Aussehen der CSV bestimmt werden. 

\* = Optional

| Optional | Feld        | Beschreibung                                                                                                                                                                                                               | Beispielwert                                                                                                                               |
| ---- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| *    | newline     | Welches Zeichen am Ende stehen soll. Windows erwartet ```\r\n``` linux und Mac brauchen nur ```\n```   Standard ist:    ```\r\n```                                                                                         | ```\n```                                                                                                                                   |
| *    | encoding    | In Welchem Zeichnsatz die Daten gespeichert werden Standard ist ```UTF-8``` und ist allgemin empfohlen.  Datev erwartet das alte Windows Format:  ```iso-8859-1```                                                         | ```iso-8859-1```                                                                                                                           |
| *    | seperator   | mit Welchem Zeichen werden die Spalten getrennt, Standard ist ```,```                                                                                                                                                      | ```;```                                                                                                                                    |
| *    | quotechar   | Wie werden Spalten umschlossen die Sonderzeichen wie z.B. einen Separator enthalten  Standard ist ein doppeltes Anführungszeichen ```"```  Achtung in JSON Format müssen Sie das Zeichen mit einem ```\``` davor schreiben | ```\"```                                                                                                                                   |
| *    | quote   | Was soll alles umschlossen werden? die Liste der Werte weiter unten.| 


### CSV Quote Style


- ```minimal``` : Standardmodus: Felder werden nur dann in Anführungszeichen gesetzt (gequotet), wenn es unbedingt nötig ist - also wenn sie Kommas, Anführungszeichen oder Zeilenumbrüche enthalten. Dieser Modus versucht, die Verwendung von Anführungszeichen auf das notwendige Minimum zu beschränken.
- ```alles```: Alle Felder werden in Anführungszeichen gesetzt, unabhängig davon, ob sie spezielle Zeichen enthalten oder nicht. Dies kann hilfreich sein, um sicherzustellen, dass die Struktur der CSV-Daten eindeutig ist, reduziert jedoch eventuell die Lesbarkeit der Datei.
- ```zeichen```: Hier werden alle nicht -numerischen Felder in Anführungszeichen gesetzt. Numerische Felder werden ohne Anführungszeichen geschrieben. Dieser Modus kann nützlich sein, wenn Sie sicherstellen möchten, dass numerische Werte leicht als solche erkannt und verarbeitet werden können, während Textfelder klar als Text markiert sind.
- ```none```: In diesem Modus werden keine Felder in Anführungszeichen gesetzt. Dies bedeutet, dass Sie selbst sicherstellen müssen, dass Ihre Daten keine Kommas oder andere spezielle Zeichen enthalten, die normalerweise das Einfügen von Anführungszeichen erfordern würden. Dies kann zu Problemen führen, wenn solche Zeichen unbeabsichtigt in den Daten vorkommen, da die CSV-Struktur dadurch gebrochen werden kann.


## Lizenz
Werte wie Lizenz, ecoDMS Server-Nutzer usw. werden beim ersten Start über die Oberfläche konfiguriert.   
Diese können bei Bedarf in der Konfigurationsdatei angepasst werden.

``` title="Lizenzeintrag:"
 "license": "12345",
```

| Opt. | Feld    | Beschreibung                                                                                       | Beispielwert                  |
| ---- | ------- | -------------------------------------------------------------------------------------------------- | ----------------------------- |
| *    | license | Dies ist der Lizenzschlüssel, den Sie erhalten haben. Der Schlüssel wird automatisch konfiguriert. | ```6385c73c550rgrwefg0a11f``` |
