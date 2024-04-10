# GUI


Im Tool können Button ausgeblendet werden oder deren Text geändert werden. 
Wird nichts angegeben, werden die Button angezeigt und der Standard Text des Buttons angezeigt.


## GUI Config
```
   "gui": {
        "buttons": [
            {
                "funktion": "Dokument Export",
                "text": "Dokument Export",
                "show": true
            },
            {
                "funktion": "Dokumentliste Export",
                "text": "Dokumentliste",
                "show": true
            },
            {
                "funktion": "Datev Export",
                "text": "Datev Export",
                "show": true
            },
            {
                "funktion": "SEPA Export",
                "text": "SEPA Export",
                "show": true
            },
            {
                "funktion": "Dokumentliste Export",
                "text": "Liste komplett",
                "show": true
            },
            {
                "funktion": "Ordner Export",
                "text": "Ordner Export",
                "show": true
            },
            {
                "funktion": "Typen Export",
                "text": "Typen Export",
                "show": true
            }
        ]
    }
```
Unter dem Key ```gui``` -> ```buttons``` werden die Knöpfe konfiguiert. 
Der Key entspricht dem Standard Text des Buttons in der Oberfläche. 

!!! Warning "Spaltenbreite"
    die Button Breite ist fix. Bitte halten Sie den Text knapp, damit er komplett angezeigt wird. 


\* = Optional

| Opt. | Feld | Beschreibung                                                                                          | Beispielwert                                  |
| ---- | ---- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| *    | funktion | Der Name der Funktion die ausgeführt werden soll. Der Name muss einer der Funktionen entsprechen                | ```Dokument Export``` |
| *    | text | Der neue Text, der auf dem Button angezeigt wird.                | ```hallo ``` |
| *    | show | Gibt an ob der Button angezeigt werden soll. Wenn nicht, muss show auf false gesetzt werden | ```false```                                  |


!!! tip "Gruppieren"
    Die Button können auch ausgeblendet werden. Wird z.B. der dritte Slot ausgeblendet, entsteht eine Gruppierung. 