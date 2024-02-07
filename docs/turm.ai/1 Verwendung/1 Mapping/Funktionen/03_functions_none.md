#  Empty / None 
*Stand: Turm Version 14.22.1 - 01.02.2024*
![](../../../img/mapping.png)

# Ersetzen von None, Null oder leeren Werten

Werte, die `None` sind, können ersetzt werden.   
Achtung: Dies gilt nicht für Booleans (True/False). In diesem Fall muss eine If-Bedingung verwendet werden, siehe unten. 
Das Schlüsselwort dafür lautet `or`.

```
Wert or AlternativWert
```

Wenn fehlende Werte durch einen Standardwert ersetzt werden sollen, kann Folgendes verwendet werden:

```
{str(data['kdnr'] or 'Keine Kundennummer')}
```

In diesem Fall wird der Wert aus dem Feld `kdnr` genommen, es sei denn, er ist nicht gesetzt also *None*; dann wird ein  String *Keine Kundennummer* übergeben.
