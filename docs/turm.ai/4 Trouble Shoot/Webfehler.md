# Weboberfläche


## Invalid host header

### Fehlerbeschreibung 
Es wird kein Frontend angezeigt nur ein Fehler
``` Invalid host header XXXXXX ``` 

Die Fehler treten aus, wenn der Domainname unter dem der Turm erreichbar ist nicht in der der params.json steht. 
    

### Lösung 
Tragen Sie in der params.json unter ServerDomains die passende Domain ein. 
``` 
"ServerDomains": [
                    "localhost",
                    "MEINESERVERDOMAIN",
                ],
```

siehe auch : 
**[Konfigurationsdatei](base_configuration.md)**
