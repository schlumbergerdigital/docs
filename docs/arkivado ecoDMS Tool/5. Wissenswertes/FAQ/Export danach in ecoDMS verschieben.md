# Nach Export die Dokumente in ecoDMS verschieben

## Problembeschreibung

Der Standard im Arkviado Tool setzt nur einen Haken wenn ein Dokument bearbeitet wurde. 
Soll nun das Dokument zudem in einen anderen Order verschoben werden, kann diese definiert wwerden.

!!! info "Version" 
    Ab der Arkivdo version 11.12 möglich 

## Lösung

Das ```IsExportedField``` steuert was in ecoDMS zurückgeschrieben wird, sobald das Dokument exportiert wird.    
Für den Export wird der Ordner angegeben, unter dem das Dokument abgelegt wird

!!! warning "mehrere Attribute verwenden"
    Es wird dringend empfohlen, sowohl den Haken zu setzen, als auch den Ornder anzugeben.

    Wird nur der Ordner angegeben und das Dokument irgendwann später nochmals in einen anderen Ordner 
    verschoben, würde es nochmlas exportiert werden. 


Passen Sie in der **params.json** (mehr zu der params [hier](<../006technischer Background.md>)) den den Key an.

Der Standard sieht so aus:
``` JSON 
 "IsExportedField": {
        "field": "SEPA Export erfolgt",
        "value": "2"
      },
```

Ändern Sie den Standard zu:

``` JSON 
 "IsExportedField": [
     {
        "field": "SEPA Export erfolgt",
        "value": "2"
      },
    {
        "field": "Ordner",
        "value": "Eingangsrechnungen/verbucht/"
      }   
 ],
```

Achten Sie darauf das der ```IsExportedField``` nun mit ```[``` beginnt und mit ```]``` endet, statt mit ```{ }```

Es wird der Komplette Pfad angegeben. Unter dem  *Eingangsrechnungen * wird es so ein neuen Ordner geben. der *verbucht* heist. 

!!! tip  "Groß und Kleinschreibung beachten"
     Die Groß und Kleinschreibung ist relevant, sowohl bei den Feldern als auch bei den Werten. 
    status ist also nicht gleich Status 

