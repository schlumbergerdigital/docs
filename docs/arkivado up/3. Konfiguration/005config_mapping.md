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


### Pfad / Ordner verwenden

Für Werte aus dem Pfad steht ```<path>``` zur Verfügung.

Um Teile des Pfades zu verwenden, wird dahinter angegeben, welcher Abschnitt verwendet werden soll.

Hat man zum Beispiel bei einer Datei den Pfad:

```text
C:\Ablage\Projekte\12-22NBG-13\Rechnungseingang\VK123445678.pdf
```

| Eingabe           | Bedeutung                         | Ergebnis                                                               |
| ----------------- | --------------------------------- | ---------------------------------------------------------------------- |
| ```<path>     ``` | Der ganze Pfad                    | ````C:\Ablage\Projekte\12-22NBG-13\Rechnungseingang\VK123445678.pdf``` |
| ```<path>[0]  ``` | Der erste "Ordner"/Laufwerksname  | ```C:\```                                                              |
| ```<path>[1]  ``` | Der zweite "Ordner"               | ```Ablage```                                                           |
| ```<path>[3]  ``` | Der dritte "Ordner"               | ```Projekte```                                                         |
| ```<path>[-1] ``` | Der Dateiname (letzter Abschnitt) | ```VK123445678.pdf```                                                  |
| ```<path>[-2] ``` | Der vorletzte Ordner              | ```Rechnungseingang```                                                 |
| ```<path>[-3] ``` | Der vor-vorletzte Ordner          | ```12-22NBG-13```                                                      |

### Dateinamen


Für den Dateinamen inkl. Dateiendung steht ```<file_name>``` zur Verfügung.



Hat man zum Beispiel bei einer Datei die folgendermaßen heißt:

```text
VK123445678.pdf
```

| Eingabe                   | Bedeutung                                                 | Ergebnis               |
| ------------------------- | --------------------------------------------------------- | ---------------------- |
| ```<file_name>     ```    | Der ganze Dateiname                                       | ````VK123445678.pdf``` |
| ```<file_name>[0]  ```    | Das erste Zeichen im Dateiname                            | ```V```                |
| ```<file_name>[0:3]  ```  | Die ersten drei Zeichen im Dateinamen                     | ```VK1```              |
| ```<file_name>[2:]  ```   | lässt die ersten 2 Zeichen weg bis zum Ende               | ```123445678.pdf```    |
| ```<file_name>[2:-4]  ``` | lässt die ersten 2 Zeichen weg, und die letzten 4 Zeichen | ```123445678```        |
| ```<file_name>[2:11]  ``` | Beginnend mit dem dritten Zeichen bis zum 11ten Zeichen   | ```123445678```        |
| ```<file_name>[-1] ```    | Der letzte Buchstabe                                      | ```f```                |
| ```<file_name>[-2] ```    | Die letzten zwei Buchstaben                               | ```df```               |
| ```<file_name>[-3] ```    | Die letzten drei Buchstaben                               | ```pdf```              |
| ```<file_name>[:-4] ```   | Alles bis auf die letzten 4 Buchstaben                    | ```VK123445678```      |



### Splitting im Dateinname

Wird ein Dateinamen durch Trennzeichen geteilt kann dies verwendet werden. Der Befehl heißt split 

```text
AB_123445678_222.pdf
```


| Eingabe                                | Bedeutung                                                                            | Ergebnis        |
| -------------------------------------- | ------------------------------------------------------------------------------------ | --------------- |
| ```str(<file_name>).split('_')[0]  ``` | trennt Dateinamen bei jedem ```_``` und gibt dann den ersten  gefundenen Wert wieder  | ````AB```       |
| ```str(<file_name>).split('_')[1]```   | trennt Dateinamen bei jedem ```_``` und gibt dann den zweiten gefundenen Wert wieder | ```123445678``` |
| ```str(<file_name>).split('_')[2]```   | trennt Dateinamen bei jedem ```_``` und gibt dann den dritten gefundenen Wert wieder | ```222.pdf```   |
| ```str(<file_name>).split('_')[-1]```  | trennt Dateinamen bei jedem ```_``` und gibt dann den letzten gefundenen Wert wieder | ```222.pdf```   |

Wird eine Trennung angegeben die nicht vorhanden ist. 
also z.B. ```str(<file_name>).split('_')[3]```  wird ein leere String zurückgegeben
