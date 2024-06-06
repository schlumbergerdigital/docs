# Kommandozeile 

Das Tool kann auch automatisch via CMD / Powershell ausgeführt werden. Dies ermöglicht eine zeitgesteuerte Ausführung auf Servern oder Arbeitsplätzen. Zudem können mehrere Profile (JSON Konfigurationen) verwendet werden. (Benötigt die Multi Lizenz)

## Intervall Scann

Um z.B. ein Verzeichnis einmal die Stunde zu überprüfen und neue Dateien hochladen wird in der Aufgabenplanung 

```arkviado_up.exe -u ```

hinterlegt. 

## Kommandzeilen Parameter

| Parameter       | Bedeutung                                                                                                                            | Beispiel                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| -s (--scan)     | Scannt nur das Verzeichnis, lädt keine Dateien zu ecoDMS hoch                                                                        | ```arkviado_up.exe -s ``` |
| -u (--upload)   | Scannt das Verzeichnis und lädt alle neuen oder geänderten Dateien hoch (analog zur Oberfläche)                                      | ```arkviado_up.exe -u ``` |
| -t (--transfer) | Lädt nur nicht verarbeitete Dateien zu ecoDMS hoch, ohne nochmals zu scannen. Hilfreich wenn z.B. der Server beim Übertragen abbricht | ```arkviado_up.exe -t ``` |
| -w (--watch)    | Überwacht in Echtzeit das Verzeichnis, sobald sich etwas ändert wird das Dokument hochgeladen.                                         |```arkviado_up.exe -w ``` |
| -n (--number)   | Gibt die Nummer des Profils an, das verwendet werden soll. Kann mit den anderen Parametern verwendet werden, auch mit Oberfläche möglich |```arkviado_up.exe -n 2 ``` |
