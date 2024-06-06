# Mapping

Beim Mapping wird angegeben, welche Felder (Attribute) in ecoDMS befüllt werden.
Dabei kann der Dateipfad verwendet werden, um die Attribute zu befüllen.

![Mapping](img/Mapping.png)

Links stehen die Attribute aus ecoDMS und rechts wird angegeben, was eingetragen werden soll.

Dabei wird Text, der eingetragen wird, einfach übertragen. Zum Beispiel: Bei Status steht ```Erledigt```, so werden alle Dokumente mit dem Status *Erledigt* abgespeichert.

Ordnerangaben können Unterordner enthalten, der Unterordner wird dabei mit ```/``` getrennt.
In dem Beispiel werden alle Dokumente unter dem Ordner *Projekte* abgelegt.

## Dynamische Werte

Es können auch abhängig vom Pfad Werte übergeben werden.
Dabei werden dynamische Werte immer in ```<>``` geschrieben.

Für Werte aus dem Pfad steht ```<path>``` zur Verfügung.

Um Teile des Pfades zu verwenden, wird dahinter angegeben, welcher Abschnitt verwendet werden soll.

Hat man zum Beispiel bei einer Datei den Pfad:

```text
C:\Ablage\Projekte\12-22NBG-13\Rechnungseingang\VK123445678.pdf
```

| Eingabe    | Bedeutung                          | Ergebnis                                                               |
| ---------- | ---------------------------------- | ---------------------------------------------------------------------- |
| ```<path>     ```| Der ganze Pfad                   | ````C:\Ablage\Projekte\12-22NBG-13\Rechnungseingang\VK123445678.pdf``` |
| ```<path>[0]  ```| Der erste "Ordner"/Laufwerksname                | ```C:\```                                                              |
| ```<path>[1]  ```| Der zweite "Ordner"                | ```Ablage```                                                           |
| ```<path>[3]  ```| Der dritte "Ordner"                | ```Projekte```                                                         |
| ```<path>[-1] ```| Der Dateiname (letzter Abschnitt) | ```VK123445678.pdf```                                                  |
| ```<path>[-2] ```| Der vorletzte Ordner               | ```Rechnungseingang```                                                 |
| ```<path>[-3] ```| Der vor-vorletzte Ordner          | ```12-22NBG-13```                                                      |