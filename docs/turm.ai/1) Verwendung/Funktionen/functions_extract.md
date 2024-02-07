# Funktionen - Extract
*Stand: Turm Version 14.22.1 - 01.02.2024*

 
## Felder aus einem String lesen 
Oftmals werden in einem Feld mehrere Postionen abgebildet.   
Leicht zu erkennen an ```{}```  oder ```[]``` z.B.; 
```
[{
    "amount": 119.00,
    "taxAmount": 19.00,
    "taxRatePercent": 19,
    "categoryId": "8f8664a8-fd86-11e1-a21f-0800200c9a66"
   },
   {
    "amount": 15.00,
    "taxAmount": 0.00,
    "taxRatePercent": 0,
    "categoryId": "8f8664a8-fd86-11e1-a21f-08004230c9a66"
   }]
```

um nun auf einzelne Werte aus dem Zeichen zuzugreifen, kann der Befehl @extract verwendet werden.

```@extract()```

Soll z.B. in der beren Liste (erkennbar an den ```[]```) aus dem zweiten  Eintrag der Betrag angebgen werden wird folgendes geschrieben:

```
@extract([1]['amount'])
```

### Auslesevorschrift

#### Listen
Listen erkennbar an den ```[]``` können über Zahlenwerte angesprochen werden. 
!!! tip "Zero Index"
    Das zählen geht bei ```0``` los. Der erste Eintrag hat also die Nummer ```0```, der zweite die ```1``` usw. 
Damit man die Nummer Ansprechen kann werden Sie in ```[]``` geschrieben. 

```
@extract([1])
```
würde also in dem Oberen Beispiel den kompletten zweiten Eintrag wiederdegeben. Als Ergebnis hätte man dann:
```

   {
    "amount": 15.00,
    "taxAmount": 0.00,
    "taxRatePercent": 0,
    "categoryId": "8f8664a8-fd86-11e1-a21f-08004230c9a66"
   }
```

#### Key Value / Hasmap / Dictonaries

Der zweite Part enthält einen Key und einen Wert dazu. 
Die Werte bekomtm an indem man die Key übergibt. 
Auch hier wird der gewünschte Wert in ```[]``` angegeben und zusätzlich mit ```'``` eingefasst also gibt :
```
['amount']
```
bei dem oberen Dictionary den Wert aus. 

#### Kombinieren

Die Vorschriften können beliebig kombiniert werden. 

Um das Erste Beispiel korrekt abzufragen. also den amount aus dem zweiten Eintrag wiederzugeben folgendes schreiben:


```
@extract([1]['amount'])
```
An den Eckigen Klammern erkennt man, dass die Abfrage auf die zweite Ebenen Tief geht.
Als erstes wird der *zweite* (```[1]``` ) Eintrag der Liste ausgesucht und dann der Key *amount* ```['amount']``` aus dem Dictionary.  