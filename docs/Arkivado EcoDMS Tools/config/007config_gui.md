# Gui


Im Tool können Button ausgeblendet werden oder deren Text geändert werden. 
Wird nichts angegeben, werden die Button angezeigt und der Standard Text des Buttons angezeigt. 

## Gui Config
Die Einstellungen werden im Frontend abgefragt. Im Allgemeinen muss hier nichts eingestellt werden.
 
```
    "gui": {
        "buttons": {
            "Dokument Export": {
                "text": "alle meine Dokumente",
                "show": true
            },
            "SEPA Export": {
                "text": "mehr Geld",
                "show": true
            },
            "Datev Export": {
                "text": "mehr Steuerberater",
                "show": true
            }
            
        }
    },
```
Unter dem Key ```gui``` -> ```buttons``` werden die Knöpfe konfiguiert. 
Der Key entspricht dem Standard Text des Buttons in der Oberfläche. 

!!! Warning "Spaltenbreite"
    die Button Breite ist fix. Bitte halten Sie den Text knapp, damit er komplett angezeigt wird. 


\* = Optional

| Opt. | Feld | Beschreibung                                                                                          | Beispielwert                                  |
| ---- | ---- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| *    | text | Der neue Text, der auf dem Button angezeigt wird.                | ```hallo ``` |
| *    | show | Gibt an ob der Button angezeigt werden soll. Wenn nicht, muss show auf false gesetzt werden | ```false```                                  |

