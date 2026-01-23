# Fehlerbehandlung 

!!! warning "Experimentell"
    Diese Funktion ist neu, und noch experimentell Stand: Version 11.19


!!! info "Module"
    Diese Funktion ist nur nutzbar in:

    - SEPA
    - DATEV 


## Problembeschreibung

- Ein Dokument kann nicht exportiert werden, oder es fehlen wichtige Informationen 
- Nun kann das Arkivado tool diese Meldung zurück an ecoDMS geben. 


## Erklärung

- Mit der Einstellung kann der Fehler zurück an ecoDMS gemeldet werden. Die Funktion nennt sich: ```AfterFailedValues```



## Lösung 

Fügen Sie in der ```param.json``` (siehe [hier](<../006technischer Background.md>)) unter dem entsprechenden Punkt ein:

``` "JSON" title="AfterFailedValues"
   "AfterFailedValues" : 
      [   
        {
          "field": "Status",
          "value": "Fehler"
        }
      ]
``` 

Beim Fehlerfall wird der Status des 
betroffenen Dokumentes auf ```Fehler``` gesetzt.

!!! info "Status ecoDMS"
    Im Standard ecoDMS gibt es keinen Status Fehler, dieser muss in ecoDMS angelegt werden


Es können auch mehrere Attribute gesetzt werden. 

``` "JSON" title="AfterFailedValues"
   "AfterFailedValues" : 
      [   
        {
          "field": "Status",
          "value": "Fehler"
        },
        {
        "field": "SEPA Export erledigt",
        "value" : "1"
        }
      ]
``` 
Hier würde der Haken wieder entfernt werden, sodass das Tool im nächsten Durchlauf wieder versucht. 



Es kann auf die Fehlermeldung nach ecoDMS zurückgeschrieben werden

``` "JSON" title="AfterFailedValues"
   "AfterFailedValues" : 
      [   
        {
          "field": "Status",
          "value": "Fehler"
        },
        {
        "field": "Fehlermeldung",
        "value" : "<error>"
        }
      ]
``` 

Nun wird die Meldung vom Arkivado Tool in das ecoDMS Feld *Fehlermeldung* geschrieben

!!! info "Fehlermeldung ecoDMS"
    Im Standard ecoDMS gibt es kein Feld Fehlermeldung, dieser muss in ecoDMS angelegt werden
