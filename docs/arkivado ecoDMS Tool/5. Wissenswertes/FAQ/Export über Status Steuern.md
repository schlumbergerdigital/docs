# Export über status Steuern


## Problembeschreibung

Ein Workflow wird über den Status gesteuert. In diesen Status Workflow soll das Arkivado ecoDMS Tool eingebunden werden. 
z.B.  Wenn eine Rechnung freigeben wird, soll diese via SEPA gezahlt werden 

## Lösung

Wenn Sie mit dem Status arbeiten wollen, muss bei *value*  der Name des Statuswertes stehen. 

Nehmen wir an, Sie haben in ecoDMS folgende Statusangaben konfiguriert: 

- nicht bearbeitet
- zu zahlen
- angewiesen


dann müssen Sie in der Konfiguration den die beiden Statusangaben hinterlegen:

Der Status der den Prozess auslöst. Hier: ```zu zahlen``` 
Den Status den das Dokument bekommt, wenn der Export ausgeführt wurde. Hier:  ```erledigt```

``` JSON 
 "ToExportField": {
                "field": "Status",
                "value": "zu zahlen"
            },
 "IsExportedField": {
                "field": "Status",
                "value": "erledigt"
            },
```


!!! warning "unterschiedliche Status"
    Wichtig ist, dass Sie unterschiedliche Status nehmen!
    Wird zweimal der gleiche Status angegeben, haben Sie eine Dauerschleife produziert.
    Der Datensatz würde dann immer wieder exportiert werden.  


!!! tip  "Groß und Kleinschreibung beachten"
     Die Groß und Kleinschreibung ist relevant, sowohl bei den Feldern als auch bei den Werten. 
    status ist also nicht gleich Status 

