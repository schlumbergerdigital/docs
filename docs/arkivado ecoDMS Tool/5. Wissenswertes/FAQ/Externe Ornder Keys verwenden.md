# ecDMS Ordner: Schlagwörter/key


## Problembeschreibung

- nicht nur der Odner sondern auch der Schlüssel oder Schlagwort soll ausgegeben werden


## Lösung 

In der Konfiguration können Sie mit den funktionen @folder, @mainfolder arbeiten. sieh [hier](<../../3. Konfiguration/003config_doclist.md#ordner-zusatzdaten-ausgeben>)

Damit die Werte eine saubere Überschrift bekommen empfehlen wir in der Konfiguration den Namen zu vergeben.
``` JSON title="Konfiguration der csv Exportdatei:"
  "Dokumentliste Export": {
      "TimeFilter": false,
      "Filter": [
        {
          "classifyAttribut": "docid",
          "searchOperator": ">",
          "searchValue": "0"
        }
      ],
      "Spalten": [
        "<DocID>",
        "<Hauptordner>",
        "<Ordner>",
         {"Ordner Keys":"<@folder(external_key)>"},
         {"Haupt Ordner Key": "<@mainfolder(external_key)>"},
         {"Ordner Schlagwort": "<@folder(buzzwords)>"},
         {"Haupt Ordner Schlagwort": "<@mainfolder(buzzwords)>"}
    ]
     
    }
```

## Beispiel

Angenommen alle Dokumente liegen im Ornder *Unterornder* dieser liegt unter dem Hauptornder: *Hauptordner*
wird nun ein Export mit der Spalten konfiguration von oben ausgeführt sieht das ergebnis so aus:
![Excel Export mit Schlüsselworten](<img/Excel Export Schlüssel.png>)