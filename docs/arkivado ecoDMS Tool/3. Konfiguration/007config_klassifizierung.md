# Klassifizierung

!!! info "Version"
    mindestens Version 11.14 nötig


Klassifizierung wird vor allem in Mehrstufigen Workflows verwendet. 
Z.B. wird ein [SEPA Export](006config_sepaexport.md) durchgeführt, und alle bearbeitetn Dokumente anschliesend verschoben. 

Nun bleiben Dokumente die Eingezogen werden, also nicht unter den SEPA Export fallen liegen. 
Hierfür kann die Klassifizierung verwendet werden.
Dieser wird dann Entweder via Button oder in einem Skript ausgeführt.

## Klassifizierung konfiguration


``` json title="Klassifizierung ändern"
       "Klassifizierung": {
      "Filter": [
        {
          "classifyAttribut": "Status",
          "searchOperator": "=",
          "searchValue": "Erledigt"
        },
        {
          "classifyAttribut": "Zahlweise",
          "searchOperator": "=",
          "searchValue": "SEPA Lastschrift"
        },
        {
          "classifyAttribut": "Ordner",
          "searchOperator": "!=",
          "searchValue": "Rechnungseingang/archiv/"
        },
        {
          "classifyAttribut": "SEPA Export erfolgt",
          "searchOperator": "!=",
          "searchValue": "2"
        }
      ],
      "IsExportedField": [
        {
          "field": "SEPA Export erfolgt",
          "value": "2"
        },
        {
          "field": "Ordner",
          "value": "Rechnungseingang/archiv/"
        }
      ],
      "TimeFilter":false,
      "DateField":"Datum"
    },
```

\* = Optional


| Opt. | Feld             | Beschreibung                                                                                                                                                     | Beispielwert                                                                           |
| ---- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
|      | Filter           | Der Filter wird immer auf die Dokumente angewendet. Siehe  [hier](007config_klassifizierung.md#dokumentenfilter) für eine ausführliche Beschreibung.                                                       | ```[{"classifyAttribut": "docid", "searchOperator": ">", "searchValue": "0"}]```       |
|      | IsExportedField  | Das oder die Felder die das Arkviado Tool ändern soll. Auch Ordner möglich                                                                            | ``` IsExportedField": {"field": "StB exportiert","value": "2"}```                      |
| *    | TimeFilter       | Gibt an, ob das Auswahlfeld Datum berücksichtigt werden soll.<br>Bei "true" muss das Datum im Zeitraum liegen.  Standard ist false                                                 | ```true```                                                                             |
| *    | DateField        | Das Feld, das bestimmt welches Datum genommen wird, wenn der Datumsfilter verwendet wird, wenn leer Datum                                                        | ```Belegdatum 


!!! warning "TimeFilter nur mit Oberfäche"
    Diese sind nur mit Oberfläche sinnvoll, bitte bei automatischen Skripts (via cmd siehe [ hier](<../2. Verwendung/007start per Kommandozeile.md>) ) NICHT verwenden!

!!! warning "Ordner muss vorhanden sein"
  Wenn Sie Filter auf Ordner definieren sollten diese bereits in ecoDMS vorhanden sein.     

## Button hinterlegen

Damit der User die Funktion ausführen kann, benötigt er noch einen Button. 
Diesen können Sie konfigurieren. Für ausführliche Infos siehe [hier](008config_gui.md)

``` json title="Button im Gui"
 "gui": {
        "theme":"hell",
        "buttons": [
            {
                "funktion": "Klassifizierung",
                "text": "Lastschrift Archivieren",
                "show": true
            },
``` 