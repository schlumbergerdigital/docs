# Export Liste Dokumente

Die Dokumentenliste ist eine Excel- oder CSV-Datei (abhängig vom Eintrag in ```export_to```), die alle Attribute (Metadaten) des Dokuments enthält. Das Dokument selbst wird nicht exportiert. 
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
            "Pfad" :"C:\\eco_liste\\meineDatei.xlsx",
            "PfadListeReplace": false,
            "TimeFilter": true,
            "DateField" :"Belegdatum",
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


| Opt. | Feld             | Beschreibung                                                                                                                                                     | Beispielwert                                                                           |
| ---- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
|      | Filter           | Der Filter wird immer auf die Dokumente angewendet. Siehe weiter unten für eine ausführliche Beschreibung.                                                       | ```[{"classifyAttribut": "docid", "searchOperator": ">", "searchValue": "0"}]```       |
| *    | Pfad        | Der Ablagepfad der Exportdatei (Excel/CSV)<br>Ohne Angabe wird dass Appdata Verzeichnis verwendet<br>Achtung wg JSON-Format immer doppeltes  ```\\``` verwenden. | ```C:\\eco_liste\\meineDatei.xlsx```                                                   |
| *    | PfadListeReplace | Gibt an, ob die Datei überschrieben werden soll oder vorhandene hochgezählt werden sollen. true = löscht die bestehende Datei.                                  | ```false```                                                                            |
| *    | TimeFilter       | Gibt an, ob das Auswahlfeld Datum berücksichtigt werden soll.<br>Bei "true" muss das Datum im Zeitraum liegen.                                                   | ```true```                                                                             |
| *    | DateField        | Das Feld, das bestimmt welches Datum genommen wird, wenn der Datumsfilter verwendet wird, wenn leer Datum                                                        | ```Belegdatum ```                                                                      |
| *    | Spalten          | Konfiguration der Datenspalten inkl. Benennung der Spaltentitel                                                                                                  | ```"Spalten": [ "<DocID>", {"Kreditor":"<Name>"}  ]```                                 |
| *    | IsExportedField  | arkviado Tool setzt den Wert automatisch in ecoDMS (z.B. Haken für "ist exportiert".                                                                             | ``` IsExportedField": {"field": "StB exportiert","value": "2"}```                      |
| *    | MultiFiles       |  Wird dies auf True gesetzt, wird pro Dokument ein  Datensatz erzeugt und der Name des Dokumentes Dyamisch generiert. Formatierung des Names [hier](#dateinamen-dynamisch-angeben)                                           | ``` false``                      |
| *    | Header           | Definition eines Headers oder Überschrift über den Datenzeilen werden.                                                                                           | ```["Zeile 1 Spalte 1","Zeile 1 Spalte 2"], ["Zeile 2 Spalte 1","Zeile 2 Spalte 2"]``` |
| *    | export_to        | Gibt an, in welchem Format das Dokument abweichend vom Standard erstellt werden soll. Mögliche Formate:  [hier](../Verwendung/001funktionen.md)                  | ```csv```                                                                              |




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

Über den Eintrag Spalten kann bestimmt werden, welche Spalten im Excel oder CSV-Format ausgegeben werden.
Zudem kann bestimmt werden, wie diese benannt werden sollen.  
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

Alternativ kann auch ein andere Überschrift für die Spalte übergeben werden. Dafür  wird der neue Spaltenname ```"Kreditor"``` und dann der Klassifizierungsname  aus ecoDMS aufgeführt ```"<Name>"```.

Im Beispiel wird aus dem ecoDMS Attribut *Name* in der CSV *Kreditor* ```{"Name":"Kreditor"}```. Die Reihenfolge der CSV/ Excel bildet sich wie in der JSON ab.

ecoDMS nennt in der RestAPI die Felder der Klassifizierung (Oberfläche ecoDMS) Attribute. Daher kann es in der Doku zu Doppelungen kommen 😊.


### Standardwerte setzen

- Wenn immer ein Wert gesetzt werden soll: einfach den Wert reinschreiben im Beispiel oben die *15* beim Mandant.    
- Wenn ein Wert von ecoDMS genommen werden soll, wird der Name des Attributs in ```<>``` geschrieben. 
- Soll ein standard Wert verwendet werden, wenn in ecoDMS nichts steht kann ```@default``` verwendet werden. 

``` JSON title="Standard Werte"
<@default(ecoDMS Quelle,ersatzwert)>
```


``` JSON title="Standard Werte Beispiel"
<@default(<Steuerschluessel>,9)>
```
In dem Beispiel wird der das Feld ```Steuerschluessel``` aus ecoDMS genommen.
Liefert ecoDMS keinen Wert zurück, wird der Wert *9* genommen.


### Felder formatieren mit Datum 

Die Felder  können auch mit Datumsangaben versehen werden. 
als Wert für die Spalte wird die Funktion
``` JSON title="Konfiguration Header mit dynamischem Datum"
<@date(quelle,format)>
```

```JSON title="Beispiel Belgedatum  31.12.2024"
<@date(<Belegdatum>,%d.%m.%Y)>
```
verwendet. 

| Opt. | Feld   | Beschreibung                                                                                                                                                                                                          | Beispielwert   |
| ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
|      | quelle | Welches Datum soll abgedruckt werden? Mögliche Werte sind: ```from_time``` (das *Von Datum* aus der Oberfläche), ```to_time```  ( das *Bis Datum* aus der Oberfläche), ```now``` (Jetzt) oder Datumsfelder aus ecoDMS | ```now```      |
| *    | format | Wie das Format im Zielsystem aussehen muss. Die möglichen Werte sind unten aufgeführt. Wird nichts angegeben, wird das Format dd.mm.yyyy (31.12.2024) verwendet.                                                      | ```%Y.%m.%d``` |


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


### Felder formatieren mit dynamischem Datum 

``` JSON title="Beispiel heute 2024-12-31 23:01:05"
<@date(now,%Y-%m-%d %H:%M:%S)>
```

Mögliche dynamische Datumsangaben sind:

die dynamischen werte werden **nicht** in <> geschrieben
- now = jetzt
- from_time = das *Von Datum* aus der Oberfläche
- to_time = das *Bis Datum* aus der Oberfläche


### Felder mit Standardwert belegen wenn Feld leer ist.

``` JSON title="Beispiel heute 2024-12-31 23:01:05"
<@date(<@default(<Belegdatum>,now)>,%d.%m,%Y)>
```
Die Formel nimmt das Belegdatum und formatiert es zu TT.MM.YYYY (31.12.2024). Ist das Feld des Belegdatums leer, wird das heutige Datum ausgegeben. 



### Ordner Zusatzdaten ausgeben

In ecoDMS können zusätzlich zu dem Ordnerpfad auch die zusatz Daten wie Schlagwörter und Externe Keys ausgegegen werden.

Dazu gibt es folgende Befehle:

``` JSON title="Externe Key vom Ordner ausgeben"
<@folder(external_key)>
```

gibt den externenen Schlüssel des direkten Ordners aus 

``` JSON title="Externe Key vom HauptOrdner ausgeben"
<@mainfolder(external_key)>
```
gibt den externenen Schlüssel des Hauptordners aus

``` JSON title="Buzzwords vom Ordner ausgeben"
<@folder(buzzwords)>
```

gibt den die Schlagwörter des direkten Ordners aus 

``` JSON title="Buzzwords vom HauptOrdner ausgeben"
<@mainfolder(buzzwords)>
```

gibt den die Schlagwörter des Haupt Ordners aus 


### Zusatzinformationen ausgeben

Um den Servernamen des ecoDMS Servers auszugben: 
``` JSON title="EcoDMS Server"
<@ecodmsserver()>
```

Um den  ecoDMS Benutzer auszugeben: 
``` JSON title="ecoDMS Benutzer"
<@user()>
```

### Header 

Für  eine oder mehrere Kopfzeilen eingefügt folgendes schreiben
In der JSON den  ``` Header``` eintragen.
Dies ist z.B. bei einem DATEV Export notwendig oder kann als Überschrift für Auswertungen in Excel genutzt werden. 

``` JSON title="Konfiguration Header Exportdatei"
   "Header": [
                ["Zeile 1 Spalte 1","Zeile 1 Spalte 2"],
                ["Zeile 2 Spalte 1","Zeile 2 Spalte 2"],
                [],
                ["Zeile 4 Spalte 1","Zeile 4 Spalte 2"],
            ]
```

Dabei stellt eine Liste (alles zwischen den inneren  ```[ ]```) eine Zeile dar. 
Innerhalb der Zeile können beliebig viele Spalten eingefügt werden, diese werden mit ```,``` getrennt und in ```"``` geschrieben. 

Das Tool fügt die Kopfdaten dann in CSV oder Excel ein. 
In dem Beipsiel oben werden also 4 Zeilen a 2 Spalten geschrieben. 


Die Kopfzeile kann auch das Minimum und das Maximum einer Spalte ausgeben.
Dies ist sinnvoll wenn man z.B. den höchsten Betrag im Export wissen will. 

### Header mit Minimum

Das Minimum gibt den niedrigsten Wert bzw. das älteste Datum einer Spalte wieder.  


``` JSON title="Konfiguration Header mit Minimum"
<@min(quelle,format)>
```
``` JSON title="Beispiel"
<@min(Brutto Betrag)>
```


| Opt. | Feld   | Beschreibung                                                                          | Beispielwert        |
| ---- | ------ | ------------------------------------------------------------------------------------- | ------------------- |
|      | quelle | Welche Spalte aus den Daten genommen werden soll. Die Spalte muss im Export vorkommen | ```Brutto Betrag``` |
| *    | format | In welchem Format das Minimum zurückgegeben werden soll. Vor allem für Datumsangaben  | ```%d.%m.%Y```      |


### Header mit Maximum

Das Maximum gibt den höchsten Wert bzw. das jüngste Datum einer Spalte wieder.  

``` JSON title="Konfiguration Header mit Maxmimum"
<@max(quelle,format)>
```
``` JSON title="Beispiel"
<@max(Brutto Betrag)>
```
verwendet. 

| Opt. | Feld   | Beschreibung                                                                          | Beispielwert        |
| ---- | ------ | ------------------------------------------------------------------------------------- | ------------------- |
|      | quelle | Welche Spalte aus den Daten genommen werden soll. Die Spalte muss im Export vorkommen | ```Brutto Betrag``` |
| *    | format | In welchem Format das Minimum zurückgegeben werden soll. Vor allem für Datumsangaben  | ```%d.%m.%Y```      |

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
    In dem Beispiel sind in der ersten Zeile "Von" und Datumsangabe in einer Spalte, 
    die zweite Zeile enthält zwei Spalten, daher das Trennzeichen ";".
    Abhängig davon, welches Format das Zielsystem erwartet.


### Dateinamen dynamisch angeben

Der Dateipfad kann mit dynamischen Werten erstellt werden.    
Dabei wird der Ordnerpfad unter der ```Pfad``` angepasst:

```
C:\pfad\{data['name']}-{datum(%Y-%m-%d)}-blabla-{uid()}-(mutsche){datum(%d)}.csv
``` 

wird zu:
```
C:\pfad\Müller-2024-01-08-blabla-{1235gwedtbws4334}-(mutsche)08.csv
```

Angaben in {} können dabei dynamsich verwendet werden. 

es stehen alle Attribute von ecoDMS und noch zwei weitere Funktion zur Verfügung:  

- ```datum(FORMAT)``` : Für das aktuelle Datum 
- ```uid()```: Für eine Unique ID 



Alle Metadaten aus dem aktuellen Datensatz können mit:
```
{data['NAME DES FELDES']}
```
ausgegeben werden.

Damit die  Docid im Pfad auftaucht schreibt man


```
{data['docid']}
```

