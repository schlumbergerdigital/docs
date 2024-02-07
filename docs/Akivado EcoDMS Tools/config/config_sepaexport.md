## SEPA-Exportkonfiguration

Der SEPA-Export erzeugt eine XML-Datei, die die Überweisungsdaten enthält. Dafür müssen diverse Informationen hinterlegt werden.

```
     "sepa": {
            "mybanks": {
                "default": {
                    "Name": "Meine Firma",
                    "IBAN": "DE12344",
                    "BIC": "JE3"
                }
```

## Eigene Bankinformationen
Das SEPA-Tool kann mehrere Banken verwalten. Es muss jedoch mindestens eine Bank unter `mybanks` -> `default` hinterlegt sein. Wenn mehrere Banken hinterlegt sind und keine Auswahl in EcoDMS getroffen wird, wird die `default`-Bank verwendet. Für weitere Banken wird der Name der Bank, wie er in EcoDMS im Auswahlmenü steht, eingetragen. Zum Beispiel, wenn es in EcoDMS das Auswahlmenü „Bank“ mit den Werten `Commerzbank`, `Deutsche Bank` und `Sparkasse` gibt und `Sparkasse` der Standard für Überweisungen sein sollte, sieht die JSON-Konfiguration wie folgt aus:

```
     "sepa": {
            "mybanks": {
                "default": {
                    "Name": "Meine Firma",
                    "IBAN": "DE12344",
                    "BIC": "Sparkassenbic"
                },
                "Commerzbank": {
                    "Name": "Meine Firma Holding",
                    "IBAN": "DE23455466",
                    "BIC": "Commerzbic"
                },
                "Deutsche Bank": {
                    "Name": "Meine Firma KG",
                    "IBAN": "DE32467544",
                    "BIC": "Deutschebankbic"
                },
```

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
            "Verwendungszweck": "Bemerkung"
        },
```

Opt. | Feld | Beschreibung | Beispielwert
-----|------|--------------|-------------
     | mybanks -> default -> Name | Der Name Ihres Kontos | `Meier GmbH`
     | mybanks -> default -> IBAN | Die IBAN Ihres Bankkontos | `DE12345667`
     | mybanks -> default -> BIC | Die BIC Ihres Bankkontos | `GERXDG`
     | ExportPath | Der vollständige Pfad zur SEPA XML-Datei, überschreibt bestehende XML | `C:\\export\\meineSepaxml.xml`
     | currency | Die Währungseinheit, in der die Beträge überwiesen werden. Standard: EUR | `EUR`
     | schema | Das XML-Schema der Überweisung. Möglich sind: `pain.001.001.03`, `pain.001.003.03`, `pain.008.001.02`, `pain.008.002.02`, `pain.008.003.02` | `pain.001.003.03`
     | ToExportField -> field | Der Name des Felds in EcoDMS, das geprüft wird. Z. B. ein extra Feld "Sepa Export" oder das Statusfeld | `Sepa Export`
     | ToExportField -> value | Der Wert, den das Feld haben muss, damit es zum Export ausgewählt wird. Bei Häkchenfeldern: `1` = Kein Haken, `2` = Haken | `"2"`
     | Name | Der Name des Felds in EcoDMS, das den Lieferantennamen enthält | `Name`
     | Total | Der Name des Felds in EcoDMS, das den Überweisungsbetrag enthält | `Total`
     | Iban | Der Name des Felds in EcoDMS, das die IBAN enthält | `IBAN`
     | BIC | Der Name des Felds in EcoDMS, das die BIC enthält | `BIC`
     | DueDate | Der Name des Felds, das das Ausführungsdatum enthält | `Zahlungsziel`
     | Verwendungszweck | Der Name des Felds in EcoDMS, das den Verwendungszweck für die Überweisung enthält | `Verwendungszweck`
