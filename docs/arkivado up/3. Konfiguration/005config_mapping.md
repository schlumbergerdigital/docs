# Mapping


Beim Mapping wird angegeben Welche Felder (Attribute) in ecoDMS befüllt werden. 
Dabei kann der Dateipfad verwendet werden um die Attribute zu befüllen. 


![Mappping](img/Mapping.png)!


Links stehen die Attribute aus ecoDMS und Rechts wird angegeben was eingetragen werden soll.

Dabei ist Text der eingetragen wird, wird einfach übetragen. z.B. Bei Status steht ```Erledigt``` so werden alle Dokumente mit dem Status *Erledigt* abgespeichert. 

Order Angaben können Unterordner Angaben enthalten der Unteronder wird dabei mit ```/``` getrennt. 
In dem Beispiel werden alle Dokumente unter dem Ordner *Projekte* abgelegt.


## Dynamische Werte

Es kann auch abhängig vom Pfad Werte Übergeben werden.
Dabei werden Dynamische Werte immer in ```<>``` geschrieben.  

Für Werte aus dem Pfad steht ```<path>``` zur Verfügung.

Um Teile des Pfades zu Verwenden, wird dahinter angegeben, welche Abschnitt verwendet werden soll. 

Hat man z.B. bei einer Datei den Pfad:


```C:\Ablage\Projekte\12-22NBG-13\Rechnungseingang\VK123445678.pdf```



| Eingabe    | Bedeutung                          | Ergebnis                                                               |
| ---------- | ---------------------------------- | ---------------------------------------------------------------------- |
| ```<path>     ```| Der Ganze Pfad                     | ````C:\Ablage\Projekte\12-22NBG-13\Rechnungseingang\VK123445678.pdf``` |
| ```<path>[0]  ```| Der erste "Ordner"/Laufwerksname                 | ```C:\```                                                              |
| ```<path>[1]  ```| Der zweite "Ordner"                | ```Ablage```                                                           |
| ```<path>[3]  ```| Der dritte "Ordner"                | ```Projekte```                                                         |
| ```<path>[-1] ```| Der Dateiname (letzter Abgschnitt) | ```VK123445678.pdf```                                                  |
| ```<path>[-2] ```| Der vorletzte Ordner               | ```Rechnungseingang```                                                 |
| ```<path>[-3] ```| Der vor-vorletzte Ordner           | ```12-22NBG-13```                                                      |