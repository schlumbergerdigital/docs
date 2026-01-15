# Datumsangaben in Pfaden 


## Problembeschreibung

Sie wollen ein Datumsfeld als Dateiname verwenden. Sie müssen aber ein bestimmtes Format haben. Also z.B. TT.MM.JJJJ (26.01.2026)

## Lösung

Prüfen Sie ob der Name des Datumsfelds auch in den *dates* vorkommt.
Siehe  [hier](<../../3. Konfiguration/002config_general.md>).


Nun kann mit dem Befehl ```<@date(<FELDNAME>,FORMAT)>``` der Name angegeben werden.

 Für die Erklärung vom Befehl 
[siehe dazu hier](<../../3. Konfiguration/003config_doclist.md>)



 
``` JSON title="Konfiguration Datum im Dateinamen"
    "FileName": [
        "<@date(<Belegdatum>,%d-%m-%Y)>",
        "_",
        "<DocID>",
        "_",
        "<Bemerkung>"
      ],
```

führt z.B. zu ```26-01-2026_1234567_Zum Vorgang Müller.pdf```

