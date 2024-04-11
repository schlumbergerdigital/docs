# Konfiguration Oberfläche


Sie können das Design des Tools anpassen. Buttons können definiert, angepasst oder ausgeblendet werden. 
Wird nichts angegeben, werden alle Buttons angezeigt und der Standardtext des Buttons angezeigt.


## Themes 

Das Tool kann in vier verschiedenen Farben dargestellt werden.
Es stehen folgende Designs zur Verfügung:

### Theme: schwarz (standard)
Keine weitere Konfiguration notwendig.    

![hell](img/default.png)
```
  "theme":"schwarz"
```  

### Theme: hell
Für das helle Design in der JSON ```gui``` ->   ```theme ``` auf ```hell``` stellen.   

![hell](img/hell.png)
```
  "theme":"hell"
```  
### Theme: blau
Für das helle Design in der JSON ```gui``` ->   ```theme ``` auf ```blau``` stellen.   

![hell](img/blau.png)
```
  "theme":"blau"
``` 
### Theme: einhorn
Für das helle Design in der JSON ```gui``` ->   ```theme ``` auf ```einhorn``` stellen.   

![hell](img/einhorn.png)
```
  "theme":"einhorn"
``` 
## GUI Config
``` json title="GUI Einstellungen"
   "gui": {
        "theme":"hell",
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



## Button 
Unter dem Key ```gui``` -> ```buttons``` werden die Buttons konfiguiert. 
Es stehen insgesamt 7 Slots für Buttons zur Verfügung.
Die Buttons sind frei definierbar.

```json title="Abschnitt buttons"
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

!!! Warning "Spaltenbreite"
    Die Breite der Buttons ist fix. Beachten Sie dies bei der Länge der Texte. 

\* = Optional

| Opt. | Feld | Beschreibung                                                                                          | Beispielwert                                  |
| ---- | ---- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| *    | funktion | Der Name der Funktion die ausgeführt werden soll. Der Name muss einer der Funktionen entsprechen                | ```Dokument Export``` |
| *    | text | Der neue Text, der auf dem Button angezeigt wird.                | ```hallo ``` |
| *    | show | Gibt an ob der Button angezeigt werden soll. true/false | ```false```                                  |


!!! tip "Gruppieren"
    Die Buttons können auch ausgeblendet werden. Wird z.B. der dritte Slot ausgeblendet, entsteht eine Gruppierung. 