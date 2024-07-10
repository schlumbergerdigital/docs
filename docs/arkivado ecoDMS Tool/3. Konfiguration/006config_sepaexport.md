# Export SEPA
Der SEPA-Export erzeugt eine XML-Datei, die die Überweisungsdaten enthält. Dafür müssen diverse Informationen hinterlegt werden.
## SEPA-Exportkonfiguration


``` json title="Abschnitt Firmenangaben"
     "sepa": {
            "mybanks": {
                "default": {
                    "Name": "Meine Firma",
                    "IBAN": "DE12344",
                    "BIC": "JE3"
                }
```

## Eigene Bankinformationen
Das SEPA-Tool kann mehrere Banken verwalten. Es muss jedoch mindestens eine Bank unter `mybanks` -> `default` hinterlegt sein. Wenn mehrere Banken hinterlegt sind und keine Auswahl in ecoDMS getroffen wird, wird die `default`-Bank verwendet. Für weitere Banken wird der Name der Bank, wie er in ecoDMS im Auswahlmenü steht, eingetragen. Zum Beispiel, wenn es in ecoDMS das Auswahlmenü „Bank“ mit den Werten `Commerzbank`, `Deutsche Bank` und `Sparkasse` gibt und `Sparkasse` der Standard für Überweisungen sein sollte, sieht die JSON-Konfiguration wie folgt aus:

``` json title="Abschnitt Banken"
     "sepa": {
            "mybanks": {
                "default": { //# (1)!
                    "Name": "Meine Firma",
                    "IBAN": "DE12344",
                    "BIC": "Sparkassenbic"
                },
                "Commerzbank": { //# (2)!
                    "Name": "Meine Firma Holding",
                    "IBAN": "DE23455466",
                    "BIC": "Commerzbic"
                },
                "Deutsche Bank": {
                    "Name": "Meine Firma KG",
                    "IBAN": "DE32467544",
                    "BIC": "Deutschebankbic"
                },
            },
            "EcoDMSBankingField" : "Hier Der Feldname aus ecodms"  //# (3)!
```

1. Die Standardbank, wird immer genommen wenn nichts ausgwählt ist
2. Eine Beispielbank. Im EcoDMS Feld muss bei dem Auswahlfeld  ```EcoDMSBankingField``` der Wert *Commerzbank* stehen.
3. Hier wird angegeben welches Feld


## Schema-Beschreibung des XML

- `pain.001` = SEPA-Überweisung
- `pain.008` = SEPA-Lastschrift

Welches Format letztendlich verwendet wird, hängt vom Verwendungszweck und der Unterstützung durch die Bank ab.

## Feldbeschreibung

```
     "sepa": {
            "mybanks": {
                "default": {
                    "Name": "Meine Firma",
                    "IBAN": "DE12344",
                    "BIC": "JE3"
                }
            },
            "ExportPath": "C:\\export\\meineSepaxml.xml",
            "currency": "EUR",
            "schema": "pain.001.003.03",
            "ToExportField": {
                "field": "Sepa Export",
                "value": "2"
            },
            "IsExportedField": {
                "field": "Sepa Export erfolgt",
                "value": "2"
            },
            "Name": "Name",
            "Total": "Brutto",
            "Iban": "IBAN",
            "BIC": "BIC",
            "DueDate": "Zahlungsziel",
            "Verwendungszweck": "Bemerkung",
            "EcoDMSBankingField": false
        },
```

| Opt. | Feld                       | Beschreibung                                                                                                                                                      | Beispielwert                   |
| ---- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
|      | mybanks -> default -> Name | Der Name Ihres Kontos                                                                                                                                             | `Meier GmbH`                   |
|      | mybanks -> default -> IBAN | Die IBAN Ihres Bankkontos                                                                                                                                         | `DE12345667`                   |
|      | mybanks -> default -> BIC  | Die BIC Ihres Bankkontos                                                                                                                                          | `GERXDG`                       |
|      | ExportPath                 | Der vollständige Pfad zur SEPA XML-Datei, überschreibt bestehende XML                                                                                             | `C:\\export\\meineSepaxml.xml` |
|      | currency                   | Die Währungseinheit, in der die Beträge überwiesen werden. Standard: EUR                                                                                          | `EUR`                          |
|      | schema                     | Das XML-Schema der Überweisung. Möglich sind: `pain.001.001.03`, `pain.001.003.03`, `pain.008.001.02`, `pain.008.002.02`, `pain.008.003.02`                       | `pain.001.003.03`              |
|      | ToExportField -> field     | Der Name des Felds in ecoDMS, das geprüft wird. Z. B. ein extra Feld "Sepa Export" oder das Statusfeld                                                            | `Sepa Export`                  |
|      | ToExportField -> value     | Der Wert, den das Feld haben muss, damit es zum Export ausgewählt wird. Bei Häkchenfeldern: `1` = Kein Haken, `2` = Haken                                         | `"2"`                          |
|      | Name                       | Der Name des Felds in ecoDMS, das den Lieferantennamen enthält                                                                                                    | `Name`                         |
|      | Total                      | Der Name des Felds in ecoDMS, das den Überweisungsbetrag enthält                                                                                                  | `Total`                        |
|      | Iban                       | Der Name des Felds in ecoDMS, das die IBAN enthält                                                                                                                | `IBAN`                         |
|      | BIC                        | Der Name des Felds in ecoDMS, das die BIC enthält                                                                                                                 | `BIC`                          |
|      | DueDate                    | Der Name des Felds, das das Ausführungsdatum enthält                                                                                                              | `Zahlungsziel`                 |
|      | Verwendungszweck           | Der Name des Felds in ecoDMS, das den Verwendungszweck für die Überweisung enthält                                                                                | `Verwendungszweck`             |
| *    | EcoDMSBankingField         | Hier wird bestimmt welches Auswahlfeld in ecoDMS zur Auswahl steht. Wenn nur eine Bank genommen wird, kann es auch weggelassen oder auf  `false` gesetzt  werden. | `Verwendungszweck`             |
