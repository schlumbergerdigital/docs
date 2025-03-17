# Berechtigungen setzen 


## Problembeschreibung

Normalerweise wird die Berrechtigung von Dokumenten beim schreiben auf alle bearbeiten gesetzt wird. 
Die Dokument-Berechtigung erhalten bleiben, muss die Konfiguration anpassen. 

## Lösung

Bei allen Optionen bei denen Workflow bezogen felder geändert werden können, also bei Funktionen die ```ToExportField``` anbieten:

``` JSON title="Konfiguration Spalten"

  "ToExportField": {
        "field": "Datev Export",
        "value": "2"
    },
    "IsExportedField": {
        "field": "DATEV Export erfolgt",
        "value": "2"
    },
```


ist es möglich die Berechtigungen zu setzen oder diese zu erhalten.
Wird nichts angegeben, wird die Berrechtigung für alle Klassifizierbar gesetzt.


Um  die ```edit_roles``` und ```read_roles``` des Dokumentes so zu lassen wie sie davor gesetzt waren, setzen Sie die Werte auf  ```keep```

``` JSON title="Berechtigung erhalten"
   "edit_roles": "keep",
   "read_roles":"keep",
   "ToExportField": {
        "field": "Datev Export",
        "value": "2"
    },
    "IsExportedField": {
        "field": "DATEV Export erfolgt",
        "value": "2"
    },
```


Um Dokumente die Berrechtiung zu ändern, schreiben Sie die Gruppen in einer Liste zusammen.
!!! warning "Nicht änderbar"
  Achten Sie darauf den Users selbst in die edit Gruppe aufzunehnem, sonst verlieren Sie selbst den Zugriff daruf 


``` JSON title="Berrechtigung expiziet setzen"
   "edit_roles": ["ecodms","r_maxMueller"],
   "read_roles":["buchaltung","controlling"],
   "ToExportField": {
        "field": "Datev Export",
        "value": "2"
    },
    "IsExportedField": {
        "field": "DATEV Export erfolgt",
        "value": "2"
    },
```