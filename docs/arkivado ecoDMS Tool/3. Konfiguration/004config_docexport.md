# Export Dokumente

!!!Tip "Filter, Überschriften usw."
    Die Filtermechanismen, Header, Formateinstellungen usw., beschrieben in der Dokumentenliste, können auch unter Dokument Export verwendet werden. Weitere Informationen finden Sie [hier](003config_doclist.md).

## Dokumentexport

Der Dokumentexport speichert die Dokumente aus ecoDMS auf der Festplatte und erstellt zudem eine Excel- oder CSV-Datei (abhängig vom Wert in ``export_to```), die alle Attribute/Klassifizierungen (Metadaten) des Dokuments enthält. Die 1.000-Dokument-Grenze von ecoDMS greift nicht; standardmäßig werden alle Dokumente exportiert.
``` JSON title="Dokumentexport"
"Dokument Export": {
            "TimeFilter": false,
            "DateField": "Belegdatum",
            "Filter": [
                {
                    "classifyAttribut": "docid",
                    "searchOperator": ">",
                    "searchValue": "0"
                }
            ],
            "Pfad": "C:\\ecodms_script\\Export",
            "FileName": [
                "<Datum>",
                "-",
                "<DocID>",
                "-",
                "<Bemerkung>"
            ],
            "Spalten": [
                "<DocID>",
                "Mein Attribut",
                 {"Kreditor":"<Name>"},
                 {"Mandant": "15"}
            ]
            "FileAttributeMaxLength": 50
        }
```

\* = Optional


!!!warning "Filter, Überschriften usw."
    Einstellungen die schon einmal im Dokumentenlisten Export beschrieben wurden, werden nicht nochmals geschrieben. Die Einstellungen stehen  [hier](003config_doclist.md).


| Opt. | Feld                   | Beschreibung                                                                                                                                                                                                                                                                                                    | Beispielwert                                                                        |
| ---- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| *    | TimeFilter | Gibt an, ob das Datum Auswahlfeld berücksichtigt werden soll oder nicht.  Ist der Wert True muss das Datum im Zeitraum liegen.                                 | ```false```                                                                       |
| *    | DateField        | Das Feld, das bestimmt welches Datum genommen wird, wenn der Datumsfilter verwendet wird, wenn leer Datum                                                        | ```Belegdatum ```                                                                      |

|      | Filter                 | Der Filter wird immer auf die Dokumente angewendet. Siehe weiter oben.                                                                                                                                                                                                                                          | ```[ { "classifyAttribute": "docid", "searchOperator": ">", "searchValue": "0"}]``` |
|      | Pfad                   | Wohin die Dokumente auf der Festplatte exportiert werden sollen. Bei Pfadangaben in JSON wird ein "\\" immer mit "\\\\" geschrieben.                                                                                                                                                                            | ```C:\\ecoDMS Daten\\Export```                                                      |
|      | FileName               | Der Name, den die Exportdatei haben soll. In ```< >``` geschrieben, greift auf ecoDMS-Felder zu. Ohne ```< >``` wird fester Text verwendet. **Dringend**: Bitte immer die ```<DocID>``` mit angeben, damit Dateinamen eindeutig sind. Aus dem Beispiel rechts würde z.B. **2022-11-23-Rechnung Baum-3421.pdf**. | ```["<Belegdatum>","-","<Bemerkung>","-",<DocID>"]```                               |
|      | FileAttributeMaxLength | Die maximale Länge, die ein ```< >``` Attribut im Dateinamen haben darf.                                                                                                                                                                                                                                        | ```50```                                                                            |
| *    | Spalten    | Welche Spalten ausgegeben werden sollen und wie diese heißen. Ausführliche Beschreibung [hier](003config_doclist.md)                                                                          | ```"Spalten": [ "<DocID>", {"Kreditor":"<Name>"}  ]```                           |
