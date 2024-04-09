# Comandozeile

!!! Warning "Profi Bereich"
    folgender Abschnitt richtet sich an IT Profis.


Das Tool kann auch automatisch via CMD / Poweshell ausgeführt werden. 
z.B. um Zeitgesteuert Dokumente zu exportieren. 

## Aufruf
in der CMD wird der gewünschte Befehl als Parameter übergeben. 
Achten Sie darauf den Befehl in ```"``` zu schreiben.
Der Aufruf für den Datev Export lautet dann z.B. 
 
```
arkivado_datev_sepa.exe "Datev Export"
```

!!! Warning "Konfig anpassen"
    Achten Sie darauf die den ```TimeFilter``` umbedingt auf ```false``` zu setzen!
    Es werden sonst nicht alle Dokumente exportiert sondern nur die von heute!


## Konfiugration anpassen

- Einmal mit Frontend konfigurieren und testen
- in ```params.json```  den ```TimeFilter``` auf ```false```
- die CMD muss mit dem selben Benutzer aufgerufen werden, unter dem der User konfiguriert wurde

!!! tip "Update"
    Updates werden nicht automatisch installiert. Hier einfach das Gui starten um die Updates durchzuführen