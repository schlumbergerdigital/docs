# Datenbank Fehler


## InsufficientPrivilege

### Fehlerbeschreibung 
Das Frontend bei klick auf eine Tabelle, link oder VIEW erscheint 
``` Internal Server Error ``` 

Im Logfile vom Turm wird folgender *CRITICAL* Fehler vermerkt:
 ```PSQL: SQL Query fehlerhaft, breche AKTION AB! Fehler: InsufficientPrivilege - permission denied for ```

Die Fehler treten aus, wenn die Tabellen o.ä. nicht vom Turm erstellt wurden. 
    

### Lösung 
Dem User mit dem der Turm auf die Tabelle zugreift fehlen die Rechte.
Melden Sie sich in der Datenbank mit dem User an, mit dem Sie die Tabelle erstellt haben und geben Sie alle rechte dem Turm Datenbenbankuser. Im Standard ```turmadmin```

zb. für die Tabelle oder view ```meinetabelle``` folgendes ausführen: 

``` GRANT ALL PRIVILEGES ON TABLE meinetabelle TO turmadmin ```
