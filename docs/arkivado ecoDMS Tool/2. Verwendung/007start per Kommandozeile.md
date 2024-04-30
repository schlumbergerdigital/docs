# Kommandozeile 


Das Tool kann auch automatisch via CMD / Powershell ausgeführt werden.
Dies ermöglicht eine zeitgesteuerte Ausführung auf Servern oder Arbeitsplätzen.
Zudem können mehrere Profile (JSON Konfigurationen) verwendet werden. (Benötigt die Multi Lizenz)

## Automatischer Aufruf
Auf der Befehlszeile wird der gewünschte Befehl als Parameter übergeben.
Achten Sie darauf, den Befehl in ```"``` zu schreiben.
Der Aufruf für den DATEV Export lautet dann z.B. 
 
```
arkivado.exe -f "Datev Export"
```

!!! Warning "Konfiguration anpassen"
    Achten Sie darauf, den ```TimeFilter``` unbedingt auf ```false``` zu setzen!
    Sonst werden nur Dokumente mit dem Tagesdatum exportiert.

Die möglichen Funktionen finden Sie [hier](001funktionen.md)

### Konfiguration anpassen

- Konfigurieren und mit Frontend testen
- in ```params.json```  den ```TimeFilter``` auf ```false```
- Da die Konfiguration im Appdata Verzeichnis des angemeldeten/konfigurierenden User abgespeichert wird, muss die Befehlszeile mit dem gleichen Benutzer aufgerufen werden.

!!!warning "Update"
    Updates werden nicht automatisch installiert. Hier einfach das Gui starten um die Updates durchzuführen


## Mehrere Profile verwenden
Um  andere Profile aufzurufen geben Sie den vollständigen Pfad als Parameter an

!!!warning "Update"
    Es wird hierfür eine Multi Lizenz benötigt
```
arkivado.exe -c "C:\Mein Pfad\dieDatei.json"
```


!!!tip "Enduser Freundlich"
    Verschiedene Profile können verschiedene Farben haben. So können Sie diese besser unterscheiden. 
    Sehen Sie [hier](../config/007config_gui.md)

