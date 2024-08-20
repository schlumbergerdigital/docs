# Start ohne Bilschirm


## Problembeschreibung

- Das Tool startet 
- Es kommt der Ladebilschirm 
- Nichts weiter passiertt 

``` title="Startfehler im Log"
2024-08-20 13:01:31,532 - WARNING - Das Programm läuft bereits, es kann nur einmal gestartet werden.
Beende nun diese Insantz
``` 

## Erklärung

Das arkivado up prüft ob das Programm bereits läuft. Ist bereits ein Arkviado Up gesartet wird nicht noch einmal gestartet


## Lösung 

- Beenden Sie den Dienst (wenn als Dienst konfiguriert ist)
- Beenden Sie mit dem Taskmanager alle *akrivado.exe*
- Starten Sie das Programm nochmals