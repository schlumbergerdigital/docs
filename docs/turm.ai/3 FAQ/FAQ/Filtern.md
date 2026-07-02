# Filtern

Sollen in eine andere App nur bestimmte Daten hochgeladen werden, können diese gefiltert werden. 
Es gibt drei Hauptkomponenten zum Filter:
- only_new
- filter
- filter_internal


## only_new

only_new hat zwei Bedeutungen: 

- Beim Einlesen der Daten vom einem Quell system bedeutet only_new: gib alle Daten zurrück die sich seit dem letzen abfragen hinzugekommen sind, oder sich verändert haben. 

- Beim übertragen an ein Ziel System heißt only_new alle Datensätze die noch nicht hochgesynct wurden. Also noch nicht angelegt wurden

## filter

Die Hauptkomnponente zum eingrenzen der Daten. 
Hier kann im SQL Dialekt gefiltert werden. 

Dabei wir der Name der Spalte mit ```"``` geschreiben und der Wert der abgefragt wird mit ```'```

soll z.B. nur Datensätze genommen werden, bei dem  True im syncFolder steht. 

```
"syncFolder" = 'True'
```

| Operatoren | Bedeutung                                                                             | Beispiel                                            |
| ---------- | ------------------------------------------------------------------------------------- | --------------------------------------------------- |
| =          | gleich der Wert muss exact der Angabe ensprechen                                      | ``` "syncFolder" = 'True' ```                       |
| !=         | ungleich der Wert muss exact der Angabe ensprechen                                    | ``` "syncFolder" != 'True' ```                      |
| LIKE       | Um Angaben zu machen wie. *Beginnt mit*, *endet mit*. Dabei wird ``` % ``` angegeben. | alle Namen mit Mei suchen ```"name" LIKE 'Mei%'```  |
| iLIKE      | wie ```LIKE``` nur dass groß und Kleinschreibung nicht beachtet wird                  | alle Namen mit Mei suchen ```"name" iLIKE 'Mei%'``` |
|SIMILAR TO '([0-9]\|A)%'; | Regex Suche im Vergleich. z.B. Um alle Daten finden die mit einer Zahl oder dem Buchstaben A anfangen| ``` SIMILAR TO "salesnumber" SIMILAR TO'([0-9]|A)%' ``` |
| <          | Kleiner als. Achtung hier muss das Format mit angegeben werden  wie eine Anggabe zu interpretieren (Zahl, Datum) ist  Siehe [hier](Formatierung.md)       |  ```"umsatz"::numeric < 1000.00 ``` |
| >         | Größer als. Achtung hier muss das Format mit angegeben werden  wie eine Anggabe zu interpretieren (Zahl, Datum) is  Siehe [hier](Formatierung.md)       |  ```"umsatz"::numeric > 1000.00``` |


