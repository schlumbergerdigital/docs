# Export DATEV

## Einleitung

Das arkivado ecoDMS Tool ist für die Datenübertragun an die DATEV gedacht.
Dabei übergibt das Tool die Daten an den DATEV Belegtransfer.
Zu einem späteren Zeitpunkt ist eine direkte Anbindung an DATEV Unternehmen Online geplant ohne den Belegtransfer zu nutzen.

Download unter [Belegtransfer](https://www.datev.de/web/de/service-und-support/software-bereitstellung/download-bereich/betriebliches-rechnungswesen/belegtransfer/?stat_Mparam=int_url_datev_belegtransfer)


### Belegtransfer konfigurieren
- Das Exporttool exportiert Daten in die für den Belegtransfer vorgesehenen Ordner. 

- Diese müssen in DATEV Belegtransfer entsprechend konfiguriert werden.  
Details dazu finden Sie in der DATEV-Hilfe:  [hier](https://apps.datev.de/help-center/documents/1020025  )



- In DATEV Unternehmen Online sollte durch den Steuerberater die Belegbearbeitung von "Standard" auf "Erweitert" umgestellt werden. Obwohl der Import auch im Standardmodus funktioniert, werden Fehler gemeldet und das Hochladen mehrerer Steuersätze ist nicht möglich. Wenn eine Umstellung auf "Erweitert" nicht möglich ist, wählen Sie die Exportart 2 (siehe unten).
Die Umstellung ist Stand 4/2024 kostenfrei bzw. es entstehen keine Mehrkosten.

Sobald die Ordner im Belegtransfer angelegt und eingerichtet sind, kann das Exporttool konfiguriert werden.

!!! tip "Nur bei veraltetem Belegtranfer"
    Es ist wichtig, dass die Ordner für  Ausgangs- und Eingangsrechnungen aktiviert sind, indem der Schieberegler auf "aktiv" gesetzt wird. Weitere Informationen finden Sie in der DATEV-Hilfe:  [hier](https://apps.datev.de/help-center/documents/1023377)

### DATEV Exportarten

Die DATEV-Schnittstelle kann in verschiedenen Konfigurationsstufen genutzt werden, abhängig vom Einsatzzweck und der Kompatibilität. Höhere Stufen beinhalten die Funktionen der unteren Stufen:

1. **PDF-Export:** Dokumente werden als PDF in einem Verzeichnis gespeichert und in ecoDMS als exportiert markiert.
2. **XML-Export:** Zusätzlich werden Rechnungsdaten als XML generiert und in einer ZIP-Datei zusammengefasst. Daten wie Rechnungsnummer, Betrag, Lieferantenname usw. werden aus EcoDMS übernommen.
3. **Erweiterter XML-Export:** Neben den Kopfdaten werden Buchungssätze (Aufteilung der Steuer) übergeben. Dies erfordert die erweiterte Bearbeitungsform in DATEV.

Alle DATEV-Felder befinden sich unterhalb von ```ecodms```

### Exportordner angeben
``` JSON title="Konfiguration bzw. Zuweisung der Exportordner"
"ecodms": {
    "paths": {
        "Rechnungseingang": "C:\\Datev\\Belegtransfer\\Rechnungseingang",
        "Gutschrift": "C:\\Datev\\Belegtransfer\\Rechnungseingang",
        "Rechnungsausgang": "C:\\Datev\\Belegtransfer\\Rechnungsausgang",
        "Gutschrift Lieferant": "C:\\Datev\\Belegtransfer\\Rechnungsausgang",
        "Kasse": "C:\\Datev\\Belegtransfer\\Kasse",
        "Sonstiges": "C:\\Datev\\Belegtransfer\\Sonstiges",
        "Auswertungen FIBU": "C:\\Datev\\Belegtransfer\\Auswertungen"
    }
```
Unter ```paths``` geben Sie für Ihre Dokumentenarten jeweils den Pfad an, in welchen die Dokumente abgelegt werden. Die Pfade entsprechen dem jeweiligen Pfad im DATEV Belegtransfer.
<br>Die Zuordnung erfolgt immer in der Form ```"Dokumentart": "Pfad"```.
<br>**Bei Pfadangaben in JSON wird ein ```\``` (Backslash) immer doppelt ```\\``` angegeben.**
<br>Im obigen Beispiel sind sechs Dokumentarten und fünf unterschiedliche Pfade benannt: Mehrere Dokumentarten können so für die Übergabe zusammengefasst werden.
<br><br>
**Alle Dokumentarten, die nicht zugeordnet werden können werden an das Verzeichnis "Sonstiges" übergeben. Im obigen Beispiel der vorletzte Eintrag.**
<br>

### DATEV-Felder konfigurieren

Das Exporttool speichert nicht nur PDFs in den Ordnern, sondern überträgt auch Buchhaltungsdaten wie Betrag, Steuer usw. für Rechnungseingänge und -ausgänge. Hierfür wird eine ZIP-Datei für die Dokumente erstellt (die Dokumente befinden sich anschließend nicht mehr in den oben beschriebenen Pfaden). Um dies zu ermöglichen, müssen die folgenden Einstellungen in der JSON-Datei vorgenommen werden.

```JSON title="Konfiguration DATEV Export"
"Datev": {
    "ToExportField": {
        "field": "Datev Export",
        "value": "2"
    },
    "IsExportedField": {
        "field": "DATEV Export erfolgt",
        "value": "2"
    },
    "ExportDate": "Datev Export Datum",
    "DateField": "Belegdatum",
    "InvoiceNumberField": "Belegnummer",
    "TaxField": "Steuer",
    "SupplierName": "Name",
    "SupplierCity": "Stadt",
    "DueDate": "Zahlungsziel",
    "Info": "Bemerkung",
    "VatID": "USTId",
    "Iban": "Iban",
    "Total": "Brutto",
    "TypeField": "Dokumentenart",
    "FileName": [
        "<Kostenstelle>",
        "-",
        "<Projektnummer>",
        "-",
        "<Bemerkung>",
        "-",
        "<DocID>"
    ],
    "FileAttributeMaxLength": 50,
    "ExportPath": "C:\\Datev\\Belegtransfer",
    "ExportArt": 3,
    "TimeFilter":false
}
```
* Optional

| Opt. | Feld                          | Beschreibung                                                                                                                                   | Beispielwert             |
|------|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
|      | ToExportField -> field        | Name des Felds in EcoDMS, das geprüft wird. Z.B. ein extra Feld "Datev Export" oder das Statusfeld                                             | ```Datev Export``` |
|      | ToExportField -> value        | Wert, den das Feld haben muss, damit es zum Export ausgewählt wird. Bei Häkchenfeldern: ```"1"``` = kein Haken, ```"2"``` = Haken | ```"2"```          |
|      | IsExportedField -> field      | Name des Felds in EcoDMS, das befüllt wird, sobald das Dokument heruntergeladen wurde. Ein extra Feld "DATEV Export erfolgt" oder das Statusfeld  | ```DATEV Export erfolgt``` |
|      | IsExportedField -> value      | Wert, den das Feld haben muss, damit es zum Export ausgewählt wird. Bei Häkchenfeldern: ```"1"``` = kein Haken, ```"2"``` = Haken | ```"2"```          |
|      | ExportDate                    | Name des Felds in EcoDMS, wird mit dem Datum des Exports befüllt                                                                                | ```Datum```         |
|      | DateField                     | Name des Felds in EcoDMS, in dem das Belegdatum steht                                                                                           | ```Belegdatum```    |
|      | InvoiceNumberField            | Name des Felds in EcoDMS, in dem die Rechnungsnummer steht                                                                                      | ```Belegnummer```   |
|      | TaxField                      | Name des Felds in EcoDMS, in dem die Steuer steht. Format: ```<Steuersatz1>: <Wert1> | <Steuersatz2>: <Wert2>```                              | ```Steuer```        |
| *    | DefaultTax                    | Wenn ein Standardsteuersatz hinterlegt wird, wird das TaxField als reiner Wert übernommen und immer der angegebene Steuersatz verwendet        | ```19.00```         |
|      | Total                         | Name des Felds in EcoDMS, in dem der Bruttobetrag steht                                                                                         | ```Brutto Betrag``` |
|      | TypeField                     | Feld, das bestimmt, welche Art ein Dokument hat. Eigentlich immer: ```docart```                                                   | ```docart```        |
|      | RechnungseingangArt           | Name der Dokumentenart, die Dokumente als Eingangsrechnung klassifiziert. Standard: "Rechnungseingang"                                          | ```Rechnungseingang``` |
|      | RechnungausgangArt            | Name der Dokumentenart, die Dokumente als Ausgangsrechnung klassifiziert. Standard: "Rechnungsausgang"                                           | ```Rechnungausgang```  |
|      | FileName                      | Name, den die Exportdatei haben soll. In ```< >``` geschrieben greift auf EcoDMS Felder zu. Ohne ```< >``` wird fester Text verwendet.           | ```["<Belegdatum>","-","<Bemerkung>","-",<DocID>"]``` |
|      | FileAttributeMaxLength        | Maximallänge eines Felds im Dateinamen. Wird der Wert überschritten, wird mit ```...``` angehängt und gekürzt.                     | ```50```            |
|      | SupplierName                  | Name des Felds in EcoDMS, in dem der Lieferantenname steht                                                                                      | ```Name```          |
| *    | SupplierCity                  | Name des Felds in EcoDMS, in dem die Stadt des Lieferanten steht                                                                                | ```Stadt```         |
| *    | DueDate                       | Name des Felds in EcoDMS, in dem das Zahlungsziel steht                                                                                         | ```Zahlungsziel```  |
| *    | VatID                         | Name des Felds in EcoDMS, in dem die Umsatzsteuer-ID des Lieferanten steht                                                                      | ```USTId```         |
| *    | Iban                          | Name des Felds in EcoDMS, in dem die IBAN des Lieferanten steht                                                                                 | ```Iban```          |
|      | ExportPath                    | Pfad zum Belegtransfer-Ablage. Diese wird im Belegtransfer definiert. Bei der Pfadangabe wird ein ```\``` immer mit ```\\``` geschrieben.      | ```C:\\Datev\\Belegtransfer``` |
| *    | TimeFilter                    | Ob von bis berücksichtigt werden soll oder nicht. Wenn ```false``` wird nur  ```ToExportField ``` und  ```IsExportedField ``` berücksichtigt. |  ```false ```|

