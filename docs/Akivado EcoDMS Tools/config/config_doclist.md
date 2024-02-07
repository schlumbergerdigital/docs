## Dokumentenliste-Export

Die Dokumentenliste ist eine Excel- oder CSV-Datei (abhängig vom Wert in ```export_to```), die alle Attribute (Metadaten) des Dokuments enthält. Die Datei selbst wird nicht exportiert. 
Dies eignet sich besonders für Übersichtsberichte. 
Die 1.000-Dokument-Grenze von ecoDMS greift hier nicht. Standardmäßig werden alle Dokumente aufgeführt.

\* = Optional
```
 "Dokumentenliste Export": {
            "Filter": [
                {
                    "classifyAttribut": "docid",
                    "searchOperator": ">",
                    "searchValue": "1"
                }
            ]
        }
```

Opt. | Feld | Beschreibung | Beispielwert
-------|------|--------------|-------------
 | Filter | Der Filter wird immer auf die Dokumente angewendet. Siehe weiter unten für eine ausführliche Beschreibung. | ```[{"classifyAttribut": "docid", "searchOperator": ">", "searchValue": "0"}]```


### Dokumentenfilter
```
     "Dokumenten Export": {
            "Filter": [
                {
                    "classifyAttribut": "docid",
                    "searchOperator": ">",
                    "searchValue": "0"
                }
            ],
```

Es kann ein fester Filter auf den Dokumentenexport gelegt werden. 
Dabei wird das Feld unter ```classifyAttribut``` angegeben, der Vergleich unter ```searchOperator``` und der zu vergleichende Wert bei ```searchValue```.

Sie können mehrere Filterkriterien definieren. 
Der folgende Filter sucht alle Dokumente mit einer ```docid``` größer als ```1000``` und die im Feld ```Name``` den Wert ```Meier``` haben.  
Der Standardfilter gibt alle Dokumente ohne Filter wieder.

```
     "Dokumenten Export": {
            "Filter": [
                {
                    "classifyAttribut": "docid",
                    "searchOperator": ">",
                    "searchValue": "1000"
                },
                {
                    "classifyAttribut": "Name",
                    "searchOperator": "=",
                    "searchValue": "Meier"
                }
            ],
```

Achtung: Bei Häkchenfeldern steht ```"1"``` für kein Häkchen und ```"2"``` für ein gesetztes Häkchen.
