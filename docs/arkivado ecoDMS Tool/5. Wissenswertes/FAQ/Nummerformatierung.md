# Zahlen Formatierung fehlt 


## Problembeschreibung

Es wurden eine Zahlen Formatierung  wie [hier](<../../3. Konfiguration/008config_formatierung.md>) beschrieben vorgenommen. 
Die Zahlen werden aber nicht formatiert. 

## Lösung

Prüfen Sie ob der Name des Zahlenfelds auch in den *numbers* vorkommt.
Siehe  [hier](<../../3. Konfiguration/002config_general.md>).

Dabei ist entschieden, wie das Feld am *Ende* heißt. Wenn Sie also die Spalte am Ende *Netto* heißt, muss auch *Netto* in den Numbers stehen.


``` JSON title="Konfiguration Spalten"

 "Spalten": [
        {"Netto" :"<Netto Betrag>"}
      ],
```


Numbers können auch Felder benannt werden die nicht in ecoDMS existeren.

``` JSON title="Konfiguration numbers"
   "numbers": [
      "Netto Betrag",
      "Netto"
    ],
```
