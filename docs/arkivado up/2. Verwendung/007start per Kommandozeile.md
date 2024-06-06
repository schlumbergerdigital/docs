# Kommandozeile 


Das Tool kann auch automatisch via CMD / Powershell ausgeführt werden.
Dies ermöglicht eine zeitgesteuerte Ausführung auf Servern oder Arbeitsplätzen.
Zudem können mehrere Profile (JSON Konfigurationen) verwendet werden. (Benötigt die Multi Lizenz)

## Intervall Scann

Um z.B. ein Verzeichnis einmal die Stunde zu überprüfen und neue Dateien hochladen wird in der Aufgabenplanung 

```arkviado_up.exe -u ```

hinterlegt. 


## Aufrufe

| Paramert       | Bedeutung                                                                                                                            | Beispiel                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| -s (--scan)     | Scannt nur das Verzeichnis, lädt keine Dateien zu ecoDMS hoch                                                                        | ```arkviado_up.exe -s ``` |
| -u (--upload)   | Scannt das Verzeichnis und lädt alle neuen oder geänderten Dateien hoch (analog zur Oberfläche)                                      | ```arkviado_up.exe -u ``` |
| -t (--transfer) | Lädt nur nicht verarbeitet Dateien zu ecoDMS hoch, ohne nochmals zu scannen. Hilfreich wenn z.B. der Server beim übertragen abbricht | ```arkviado_up.exe -t ``` |
| -w (--watch)    | Überwacht in Echtzeit das Verzeichnis, sobald sich was ändert wird das Dokument hochgeladen.                                         |```arkviado_up.exe -w ``` |
| -n (--number)    | Gibt die Nummer des Profils, dass verwendet werden soll an. kann mit den anderen Parametern verwnedet werden, auch mit Obefläche möglich |```arkviado_up.exe -n 2 ``` |




