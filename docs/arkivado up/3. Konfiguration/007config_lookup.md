# Metadaten-Lookup für Fremdsysteme

!!!warning  
    Dieser Abschnitt ist für IT-Profis /Programmierer gedacht, nicht für normale Anwender geeignet!

## Allgemein

Es kann notwendig sein, zu dem eigentlichen Dokument Zusatzinformationen aus anderen Systemen an ecoDMS mit zu übergeben. Dafür ist der *Lookup* gedacht.

Ein Lookup kann zum Beispiel in einem SQL Server, einer JSON-Datei oder einer Excel-Datei Daten nachschlagen und diese zusätzlich zu dem Dokument an ecoDMS übergeben.

Typische Anwendungsfälle sind:

- Ein Ordner enthält die Kundennummer, aber in ecoDMS soll der Namen des Kunden als Attribut geschieben werden. Dazu wird die Kundennummer aus dem Ordner in der Adress Tabelle des Fremdsystems nachgeschlagen und schlussendlich der Kundenname in ecoDMS gespeichert.
- Ein Programm exportiert zusätzlich zur PDF-Datei noch eine JSON-Datei mit Buchungsdaten die den Status des Dokumentes beschreiben, diese  sollen mit in ecoDMS als Attribut importiert werden sollen.

Das lookup System ist expiziert Modular aufgebaut und kann leicht erweitert werden. 

Aktuell werden folgende Lookup-Arten unterstützt:

- **json**: Importiert eine oder mehrere JSON-Dateien aus einem angegebenen Pfad.
- **mssql**: Importiert Daten aus einem Microsoft SQL Server via ODBC.

## Aufbau

Prinzipiell funktioniert ein Lookup wie folgt:

1. In dem [Mapping Attributen](005config_mapping.md) ist ein Lookup für ein Attribut definiert, z.B. `<@lookup(adressen.firstname)>`. Dies weist Arkivado an, die Spalte `firstname` aus der Tabelle `adressen` zu verwenden.
![lookup im Mapping](<img/Lookup in Mapping.png>)

1. in der Konfigurationsdatei `params.json` [mehr infos hier](<../5. Wissenswertes/006technischer Background.md>) wird im Unterpunkt `lookup` definiert welche Systeme abgefragt werden.
2. Beim import Start werden dann alle lookup Quellen aktualisiert und stehen zum Nachschlagen bereit.
3. Den Abschnitt `join` im Lookup gibt an, welcher Teil des Pfades / Dateinamen als Bindeglied genommen werden sollen.
4. Über Aliase können die Teile des Pfades oder Dateinamen definiert werden, die zum Joinen verwendet werden.

Falls Sie hilfe benötigen:  [Kontakt](https://www.schlumberger.digital/#Kontaktformular_Startseite)


hier eine "fertige" Konfigurationsdatei: 
![Fertige Konfig](<img/Konfig Mit Lookup.png>)

Die Einzelnen Einträge werden nun im Detail erklärt

### Lookup

Die Konfigurationsdatei `params.json` muss um den Punkt `lookup` erweitert werden.

```json title="Beispiel Konfiguration" 
{
"lookup": [
      {"type": "json",
       "source": "C:\\test\\json",
       "tablename":"adressen",
       "attributes" : [
        {"name": ["person","nachname"]},
        {"firstname": ["person","vorname"]},
        {"ordner": ["person","ordner"]}
       ],
       "join" : [{"source":"kundennummer","comparison" :"=","destination":"ordner"}]
      }
]
}
```

Es können beliebig viele Lookups konfiguriert werden.

Ein Lookup besteht immer aus folgenden Punkten:

| JSON Key         | Bedeutung                                                                                                                                                                                                  | Beispiel                                |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| ```type```       | Der Lookup-Typ, der durchgeführt werden soll, z.B. mssql oder json                                                                                                                                         | ```json```                              |
| ```source```     | Die Quelle der Daten. Bei JSON ist dies der Pfad, bei SQL die Abfrage                                                                                                                                      | ```C:\\test\\json```                    |
| ```tablename```  | Der interne Tabellenname in der Arkivado Up-Datenbank. Dieser muss eindeutig sein und wird mit dem Befehl @lookup referenziert                                                                             | ```adressen```                          |
| ```attributes``` | Gibt an, wie die Attribute in der Arkivado Up-Datenbank gespeichert werden. Das Attribut heißt in der Arkivado-Datenbank `name` und kommt aus dem Unterschlüssel `person -> nachname` in der JSON          | ```[{"name": ["person","nachname"]}]``` |
| ```join```       | Gibt an, wie die Daten zwischen der Datei und den Lookup-Daten verbunden werden sollen. Dabei ist  ```source ``` das Feld im Pfad bzw. Dateinamen und  ```destination ``` der Name in der Metadatentabelle |                                         | ```[{"source":"ordner","comparison" :"=","destination":"ordner"}] ``` |


### Alias

Damit ein JOIN funktionieren kann, wird oftmals ein Teil des Pfades benötigt, um darauf zu joinen.

Beispielsweise lautet der gesamte Pfad zu einer Datei:

```text title="MS SQL Konfiguration" 
  C:\Ablage\Doku\1234\Rechnung.pdf

```

mit ```<path> ``` kann auf den gesamten Pfad zugegriffen werden.
Die Kundennummer steckt im letzen Orndername und lautet *1234*. 
Damit der Join funktioniert, muss definiert werden, dass nicht der gesamte Pfad genommen wird, sondern nur der Teil des Pfades. Die Sytax dafür entspricht der, des Mappings siehe [hier](005config_mapping.md).

In der JSON wird das Alias so angebeben:

```json title="Alias Konfiguration" 
   "alias": {
      "kundennummer" : "<path>[-2]"
    },

```
Konktet heißt dass, im *join* und auch in den *attributes* der Teil des Pfades (letzter Ordnername) mit ```<kundennummer>``` verwendet werden kann. 

Der Name des Alias wird am Anfang angegeben, gefolgt von der Abbildungsvorschrift, wie im [Mapping](005config_mapping.md).

!!!tipp  "Technischer Hinweis"
    Ein Alias wird in der Arkivado-Datenbank als zusätzliche Spalte angelegt und ermöglicht so einen JOIN.

### JSON-spezifisch

- Die Angabe bei *source* kann entweder ein Ordner sein, in dem alle JSON-Dateien durchsucht werden, oder eine spezifische einzelne Datei.
- Bei den Attributen wird im zweiten Teil der "Pfad" zur Information angegeben.

Sieht die JSON-Datei beispielsweise so aus:

```json title="Beispiel JSON" 
"person": {
    "nachname": "Müller",
    "vorname": "Max",
    "ordner": "Geschäftsleitung"
}

```

kann auf die Schlüssel mit folgender Syntax zugegriffen werden:

```python title="Personen-Info" 
[
        {"name": ["person","nachname"]},
        {"firstname": ["person","vorname"]},
        {"ordner": ["person","ordner"]}
]
    
```

### MS SQL-spezifisch

Zusätzlich zur allgemeinen Konfiguration wird ein SQL-spezifischer Teil benötigt, um Servername, Datenbankname und Benutzername anzugeben.

!!!warning  
    Es wird DRINGEND empfohlen, mit einer Windows-Authentifizierung zu arbeiten! (SQLUseWindowsAuth = true)


```json title="MS SQL Konfiguration" 
  "mssql": {
    "SQLServer": "localhost",
    "SQLDatabase": "test",
    "SQLUsername": "domain\\benutzername",
    "SQLpassword": "MeinTollesPasswort",
    "SQLUseWindowsAuth": true,
    "SQLPort": "1433"
},

```

| JSON Key                | Bedeutung                                                                                                                                                             | Beispiel                   |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| ```SQLServer```         | Hostname oder IP des SQL Servers                                                                                                                                      | ```localhost```            |
| ```SQLDatabase```       | Der Datenbankname innerhalb des SQL Servers                                                                                                                           | ```test```                 |
| ```SQLUsername```       | Der Usernamen mit dem die Authenifizierung stattfindet, achtung: ```\\```  [JSON schreibweise beachten](<../5. Wissenswertes/008utf8.md#sonderzeichen-und-umlaute>) ! | ```domain\\benutzername``` |
| ```SQLpassword```       | Das SQL Server Passwort, es wird empfohlen die Windows Authenifizierung zu verwenden:  ```SQLUseWindowsAuth ``` damit hier kein Passwort im Klartext steht!           | ```MeinTollesPasswort```   |
| ```SQLUseWindowsAuth``` | bei true wird die Windows Anmledung verwendet. Das Passwort wird dann ignoriert                                                                                       | ```true```                 |
| ```SQLPort```           | Der Port unter dem der SQL Server erreichbar ist, standard: 1433                                                                                                      | ```1433 ```                |