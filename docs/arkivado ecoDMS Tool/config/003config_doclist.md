# Dokumentenliste-Export

Die Dokumentenliste ist eine Excel- oder CSV-Datei (abhängig vom Wert in ```export_to```), die alle Attribute (Metadaten) des Dokuments enthält. Die Datei selbst wird nicht exportiert. 
Dies eignet sich besonders für Übersichtsberichte. 
Die 1.000-Dokument-Grenze von ecoDMS greift hier nicht. Standardmäßig werden alle Dokumente aufgeführt.

```
 "Dokumentenliste Export": {
            "Filter": [
                {
                    "classifyAttribut": "docid",
                    "searchOperator": ">",
                    "searchValue": "1"
                }
            ],
            "TimeFilter": true,
            "Spalten": [
                "<DocID>",
                "Mein Attribut",
                 {"Kreditor":"<Name>"},
                 {"Mandant": "15"}
            ]
        }
```

\* = Optional


| Opt. | Feld       | Beschreibung                                                                                               | Beispielwert                                                                     |
| ---- | ---------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
|      | Filter     | Der Filter wird immer auf die Dokumente angewendet. Siehe weiter unten für eine ausführliche Beschreibung. | ```[{"classifyAttribut": "docid", "searchOperator": ">", "searchValue": "0"}]``` |
| *    | TimeFilter | Gibt an ob das Datums Auswahlfeld berücksichtigt werden soll oder nicht.  ist der Wert True muss das Datums im Zeitraum liegen.                                 | ```true```                                                                       |
| *    | Spalten    | Welche Spalten ausgegeben werden sollen und wie diese heißen                                                                         | ```"Spalten": [ "<DocID>", {"Kreditor":"<Name>"}  ]```                           |




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


### Feldausgabe begrenzen / umbenennen

Über den Eintrag Spalten kann bestimmt werden welche Spalten im Excel / CSV ausgegeben werden.
Zudem kann bestimmt werden wie diese heißen soll.  
```
            "Spalten": [
                "<DocID>",
                "Mein Attribut",
                 {"Kreditor":"<Name>"},
                 {"Mandant": "15"}
            ]
```
Spalten ist eine Liste. Die die Attribute von ecoDMS enthält. 
Dabei kann einfach nur die Spalte wie sie in der ecoDMS Oberfläche angegeben ist, zwischen ```<>```reingeschrieben werden.


!!!tip "Protipp"
    Das Tool übernimmt vollautomatisch die Übersetzung für dynamische Attribute

Wird also ```"<DocID>"``` in die JSON geschrieben, wird nur die Docid aus ecoDMS zurückgegeben. Die Spalte heißt dann auch *DocID* in der CSV.

Alternativ kann auch ein andere Überschrift für das Attribut übergeben werden. Dafür  wird erst die neue Überschrift ```"Kreditor"``` und dann der Attributsname aus ecoDMS genannt ```"<Name>"```.

Im Beispiel wird aus dem EcoDMS Attribut *Name* in der CSV *Kreditor* ```{"Name":"Kreditor"}```. Die Reinfolge der CSV/ Excel bildet sich wie in der JSON ab.