# Kommandozeile 


!!! Warning "Nur für erfahrene Anwender"
    Der folgende Abschnitt richtet sich an erfahrene Anwender. Durch die Automatisierung kann es bei fehlerhafter Konfiguration und Ausführung passieren, dass Exporte nicht korrekt durchgeführt werden.


Das Tool kann auch automatisch via CMD / Powershell ausgeführt werden.
Dies ermöglicht eine zeitgesteuerte Ausführung auf Servern oder Arbeitsplätzen.

## Aufruf
Auf der Befehlszeile wird der gewünschte Befehl als Parameter übergeben.
Achten Sie darauf den Befehl in ```"``` zu schreiben.
Der Aufruf für den DATEV Export lautet dann z.B. 
 
```
arkivado.exe "Datev Export"
```

!!! Warning "Konfiguration anpassen"
    Achten Sie darauf den ```TimeFilter``` unbedingt auf ```false``` zu setzen!
    Sonst werden nur Dokumente mit dem Tagesdatum exportiert.


## Konfiguration anpassen

- Konfigurieren und mit Frontend testen
- in ```params.json```  den ```TimeFilter``` auf ```false```
- Da die Konfiguration im Appdata Verzeichnis des angemeldeten/konfigurierenden User abgespeichert wird, muss die Befehlszeile mit dem gleichen Benutzer aufgerufen werden.

!!! tip "Update"
    Updates werden nicht automatisch installiert. Hier einfach das Gui starten um die Updates durchzuführen