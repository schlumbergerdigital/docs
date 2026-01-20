# Kommandozeile 

Das Tool kann auch automatisch via CMD / Powershell ausgeführt werden. Dies ermöglicht eine zeitgesteuerte Ausführung auf Servern oder Arbeitsplätzen. Zudem können mehrere Profile (JSON Konfigurationen) verwendet werden. (Benötigt die Multi Lizenz)

## Intervall Scan

Um z.B. ein Verzeichnis einmal die Stunde zu überprüfen und neue Dateien hochzuladen wird in der Aufgabenplanung 

```arkivado_up.exe -u ```

hinterlegt. 

## Kommandozeilen-Parameter

| Parameter       | Bedeutung                                                                                                                            | Beispiel                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| -s (--scan)     | Scannt nur das Verzeichnis, lädt keine Dateien zu ecoDMS hoch                                                                        | ```arkviado_up.exe -s ``` |
| -u (--upload)   | Scannt das Verzeichnis und lädt alle neuen oder geänderten Dateien hoch (analog zur Oberfläche)                                      | ```arkviado_up.exe -u ``` |
| -t (--transfer) | Lädt nur nicht verarbeitete Dateien zu ecoDMS hoch, ohne nochmals zu scannen. Hilfreich wenn z.B. der Server beim Übertragen abbricht | ```arkviado_up.exe -t ``` |
| -w (--watch)    | Überwacht in Echtzeit das Verzeichnis, sobald sich etwas ändert wird das Dokument hochgeladen.                                         |```arkviado_up.exe -w ``` |
| -c (--config)   | Gibt den Pfad zu einer anderen JSON-Datei an. So können unterschiedliche Ordner synchronisiert werden |```arkivado_up.exe -c "C:\mein\pfad\params.json" ``` |
| -m (--modify)   | Ändert bestehende Klassifizierungsattribute in ecoDMS. Dies ist praktisch, wenn beim Erstimport falsch importiert wurde.||
| -f (--filter)  | Es kann ein SQLite Filter-String übergeben werden z.B. Praktisch wenn nur ein Teil aktualisiert werden soll. z.B. alle Dokumente über der docid 1000 ändern würde der Filter so lauten  |```-f "cast(docid AS INTEGER) > 1000 "``` | 
