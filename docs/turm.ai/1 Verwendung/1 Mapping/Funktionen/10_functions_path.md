# Dateinamen

## Dateinamen: Aus einem String den Dateinamen extrahieren

Der Turm kann aus `turm_file_ids` und Pfadangaben einen Dateinamen extrahieren.

![filename](../../../img/filename.png)

Um Regex anzuwenden, wird `@filename` verwendet.

```
@filename()
```

Der Befehl kommt in die zweite Modspalte. Kann kein Dateiname berechnet werden, wird `None` zurückgegeben.

So wird aus `turm_file_12346` -> `jahresbericht.pdf`.
