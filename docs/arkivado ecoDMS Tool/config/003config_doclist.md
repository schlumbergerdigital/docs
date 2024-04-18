# Export Liste Dokumente

Die Dokumentenliste ist eine Excel- oder CSV-Datei (abhängig vom Eintrag in ```export_to```), die alle Attribute (Metadaten) des Dokuments enthält. Da Dokument selbst wird nicht exportiert. 
Dies eignet sich für Listen und Auswertungen aller Art. Denkbar sind Rechnungslisten, Übersicht über Dokumente z.B. Führerscheinkopien, Führungszeugnisse, Dokumente mit Ablaufdatum usw..
Die 1.000-Dokument-Grenze von ecoDMS greift hier nicht. Standardmäßig werden alle Dokumente exportiert, abhängig vom hinterlegten Filter.

``` JSON title="Konfiguration Dokumentlistenexport:"
 "Dokumentenliste Export": {
            "Filter": [
                {
                    "classifyAttribut": "docid",
                    "searchOperator": ">",
                    "searchValue": "1"
                }
            ],
            "PfadListe" :"C:\\eco_liste\\meineDatei.xlsx",
            "PfadListeReplace": false,
            "TimeFilter": true,
            "Spalten": [
                "<DocID>",
                "Mein Attribut",
                 {"Kreditor":"<Name>"},
                 {"Mandant": "15"}
            ],
            "Header": [
                ["Zeile 1 Spalte 1","Zeile 1 Spalte 2"],
                ["Zeile 2 Spalte 1","Zeile 2 Spalte 2"]
            ],
            "export_to":"excel"
        }
```

\* = Optional


| Opt. | Feld             | Beschreibung                                                                                                                                             | Beispielwert                                                                           |
| ---- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
|      | Filter           | Der Filter wird immer auf die Dokumente angewendet. Siehe weiter unten für eine ausführliche Beschreibung.                                               | ```[{"classifyAttribut": "docid", "searchOperator": ">", "searchValue": "0"}]```       |
| *    | PfadListe        | Der Ablagepfad der Exportdatei (Excel/CSV)<br>Ohne Angabe wird dass Appdata verzeichnis verwendet<br>Achtung wg JSON-Format immer doppeltes Backslash verwenden. | ```C:\\eco_liste\\meineDatei.xlsx```                                                   |
| *    | PfadListeReplace | Gibt an ob die Datei überschrieben werden soll oder Vorhandene hochgezählt werden sollen. true = löscht die bestehende Datei.| ```false```                                                                            |
| *    | TimeFilter       | Gibt an ob das Auswahlfeld Datum berücksichtigt werden soll<br>Bei "true" muss das Datums im Zeitraum liegen.                          | ```true```                                                                             |
| *    | Spalten          |Konfiguration der Datenspalten inkl. Benennung der Spaltentitel   | ```"Spalten": [ "<DocID>", {"Kreditor":"<Name>"}  ]```                                 |
| *    | IsExportedField  | arkviado Tool setzt den Wert automatisch in ecoDMS (z.B. Haken für "ist exportiert" | ``` IsExportedField": {"field": "StB exportiert","value": "2"}```                      |
| *    | Header           | Definition eines Headers oder Überschrift über den Datenzeilen werden.  | ```["Zeile 1 Spalte 1","Zeile 1 Spalte 2"], ["Zeile 2 Spalte 1","Zeile 2 Spalte 2"]``` |
| *    | export_to        | Gibt an in welchem Format das Dokument abweichend vom Standard erstellt werden soll. Mögliche Formate:  [hier](../Verwendung/001funktionen.md)           | ```csv```                                                                              |




### Dokumentenfilter
``` JSON title="Konfiguration Filterbedingungen"
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

``` JSON title="Beispielfilter"
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

Über den Eintrag Spalten kann bestimmt werden welche Spalten im Excel oder CSV-Format ausgegeben werden.
Zudem kann bestimmt werden wie diese benannt werden sollen.  
``` JSON title="Konfiguration Spaltennamen"
            "Spalten": [
                "<DocID>",
                "Mein Attribut",
                 {"Kreditor":"<Name>"},
                 {"Mandant": "15"}
            ]
```
Spalten entsprechen den Klassifizierungsfeldern aus ecoDMS, die exportiert werden sollen.
Dabei kann einfach nur die Spalte, wie sie in der ecoDMS Oberfläche angegeben ist, zwischen ```<>```benannt werden.


Wird zum Beispiel ```"<DocID>"``` in die JSON geschrieben, wird nur die Docid aus ecoDMS zurückgegeben. Die Spalte heißt dann auch *DocID* in der CSV.

Alternativ kann auch ein andere Überschrift für die Spalte übergeben werden. Dafür  wird der neu Spaltenname ```"Kreditor"``` und dann der Klassifizierungsname  aus ecoDMS aufgeführt ```"<Name>"```.

Im Beispiel wird aus dem ecoDMS Attribut *Name* in der CSV *Kreditor* ```{"Name":"Kreditor"}```. Die Reinfolge der CSV/ Excel bildet sich wie in der JSON ab.

ecoDMS nennt in der RestAPI die Felder der Klassifizierung (Oberfläche ecoDMS) Attribute. Daher kann es in der Doku zu Doppelungen kommen 😊.


### Header 

Soll eine oder mehrere Kopfzeilen einefügt werden, kann dies Ebenfalls realisiert werden.
Hierfür muss in der JSON der folgende Eintrag um einen Header in der Exportdatei voranzustellen.
Dies ist z.B. bei einem DATEV Export notwendig oder kann als Überschrift für Auswertungen in Excel genutzt werden. 

``` JSON title="Konfiguration Header Exportdatei"
   "Header": [
                ["Zeile 1 Spalte 1","Zeile 1 Spalte 2"],
                ["Zeile 2 Spalte 1","Zeile 2 Spalte 2"],
                [],
                ["Zeile 4 Spalte 1","Zeile 4 Spalte 2"],
            ]
```

Dabei stellt eine Liste eine Zeile dar. 
Innerhalb der Zeile können beliebig viele Spalten eingefügt werden. 
Das Tool fügt die Kopfdaten ein. 


### Header mit Minimum


Die Kopfzeile kann auch mit Minumum und Maximum einer Spalte ausgeben. 
als Wert für die Spalte wird die Funktion
``` JSON title="Konfiguration Header mit Minimum"
<@min(quelle,format)>
```
``` JSON title="Beispiel"
<@min(Brutto Betrag)>
```
verwendet. 

| Opt. | Feld   | Beschreibung                                                                                                                                                                            | Beispielwert   |
| ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
|      | quelle | Welche Spalte aus den Daten genommen werden soll. Die Spalte muss im Export vorkommen  | ```Brutto Betrag```      |
| *    | format | In welchem Format das Minimum zurückgegeben werden soll. Vor allem für Datumsangaben | ```%d.%m.%Y```   |


### Header mit Maximum


Die Kopfzeile kann auch mit Maximum einer Spalte ausgeben. 
als Wert für die Spalte wird die Funktion
``` JSON title="Konfiguration Header mit Maxmimum"
<@max(quelle,format)>
```
``` JSON title="Beispiel"
<@max(Brutto Betrag)>
```
verwendet. 

| Opt. | Feld   | Beschreibung                                                                                                                                                                            | Beispielwert   |
| ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
|      | quelle | Welche Spalte aus den Daten genommen werden soll. Die Spalte muss im Export vorkommen  | ```Brutto Betrag```      |
| *    | format | In welchem Format das Minimum zurückgegeben werden soll. Vor allem für Datumsangaben | ```%d.%m.%Y```   |


### Header mit dynamischen Datum 

Die Kopfzeile kann auch mit Datumsangaben versehen werden. 
als Wert für die Spalte wird die Funktion
``` JSON title="Konfiguration Header mit dynamischem Datum"
<@date(quelle,format)>
```
``` JSON title="Beispiel"
<@date(now,%Y-%m-%d %H:%M:%S)>
```
verwendet. 

| Opt. | Feld   | Beschreibung                                                                                                                                                                            | Beispielwert   |
| ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
|      | quelle | Welches Datum soll abgedurckt werden? Mögliche Wert sind: ```from_time``` (das *Von Datum* aus der Oberfläche), ```to_time```  ( das *Bis Datum* aus der Oberfläche), ```now``` (Jetzt) | ```now```      |
| *    | format | wie Das Format im Zielsystem aussehen muss. Die Möglichen werte sind unten aufgeführt. Wird nichts angegeben wird das Format dd.mm.yyyy (31.12.2024) verwendet.                         | ```%Y.%m.%d``` |


#### Werte fürs Datumsformat
- `%Y` = Jahr mit Jahrhundert, z.B.: 2023
- `%m` = Monat mit führender Null, z.B.: 01 oder 12
- `%d` = Tag mit führender Null, z.B.: 01 oder 31
- `%H` = Stunde (24-Stunden-Format) mit führender Null, z.B.: 01 bis 23
- `%M` = Minute mit führender Null, z.B.: 01 oder 59
- `%S` = Sekunde mit führender Null, z.B.: 01 oder 59
- `%f` = Millisekunde mit führenden Nullen, z.B.: 000001 bis 999999
- `%z` = Zeitzonen-Offset zur UTC ±HHMM[SS[.ffffff]], z.B.: +0200 (Deutsche Sommerzeit)
- `%y` = Jahr ohne Jahrhundert, z.B.: 23
- `%-m` = Monat ohne führende Null, z.B.: 1 oder 12
- `%-d` = Tag ohne führende Null, z.B.: 1 oder 31
- `%-H` = Stunde (24-Stunden-Format) ohne führende Null, z.B.: 1 bis 23
- `%-M` = Minute ohne führende Null, z.B.: 1 oder 59
- `%-S` = Sekunde ohne führende Null, z.B.: 1 oder 59

#### Beispiel
``` JSON title="Konfigurationseintrag mit dynamischem Datum"
   "Header": [
                ["Von <@date(from_time,%Y-%m-%d)>"],
                ["Bis","<@date(to_time,%Y.%m.%d)>"],
                ["Jetzt","<@date(now,%Y-%m-%d %H:%M:%S)>"],
                ["heute","<@date(now)>"],
                ["von Belegdatum","<@min(Belegdatum,%d.%m.%Y)>"],
                ["bis Belegdatum","<@max(Belegdatum,%d.%m.%Y)>"],
                ["min Betrag","<@min(Brutto Betrag)>"],
                ["max Betrag","<@max(Brutto Betrag)>"]
            ]
```

Aus dem Beispiel wird in der CSV der folgende Eintrag den Daten vorangestellt.:
```
Von 2024-04-10
Bis;2024.04.10
Jetzt;2024-04-10 15:40:38
heute;10.04.2024
von Belegdatum;01.01.2023
bis Belegdatum;17.04.2024
min Betrag;197,78
max Betrag;522

```
!!! tip "Spalten beachten"
    In dem Beispiel sind in der ersten Zeile "Von" und Datumsangabe in einer Spalte 
    die zweite Zeile enthält zwei Spalten, daher das Trennzeichen ";".
    Abhängig davon, welches Format das Zielsystem erwartet.

