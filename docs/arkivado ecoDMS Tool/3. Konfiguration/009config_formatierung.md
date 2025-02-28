
# Formatierung Excel/CSV

**Änderungen sind im Bereich "Dokumentliste Export" anzufügen.**

## Excel
``` JSON title="Konfiguration der Excel Exportdatei:"
 "excel":{
            "do_format": false,
            "table_style": "TableStyleMedium1",
            "date_style": "DD.MM.YYYY",
            "number_style": "#,##0.00"
        },
```
Für den Export in Excel Format kann die Tabelle automatisch formatiert werden.

\* = Optional

| Optional | Feld         | Beschreibung                                                                                      | Beispielwert            |
| -------- | ------------ | ------------------------------------------------------------------------------------------------- | ----------------------- |
| *        | do_format    | Wird es auf false gesetzt, wird die Formatierung deaktiviert. Standardmäßig ist die Formatierung an | ```false``              |
| *        | table_style  | Wie die Tabelle formatiert werden soll. Standard ist: ```TableStyleMedium6```                     | ```TableStyleLight10``` |
| *        | date_style   | Gibt an, wie ein Datum formatiert werden soll. Standard ist: Tag Monat Jahr                       | ```DD.MM.YYYY```        |
| *        | number_style | Gibt an, wie eine Zahl  formatiert werden soll. Standard ist: 10,22                               | ```#,##0.00```          |


### Excel Tabellen Formatierung
| Option             | Vorschau                                          |
| ------------------ | ------------------------------------------------- |
| TableStyleLight1   | ![TableStyleLight1](img/TableStyleLight1.png)     |
| TableStyleLight2   | ![TableStyleLight2](img/TableStyleLight2.png)     |
| TableStyleLight3   | ![TableStyleLight3](img/TableStyleLight3.png)     |
| TableStyleLight4   | ![TableStyleLight4](img/TableStyleLight4.png)     |
| TableStyleLight5   | ![TableStyleLight5](img/TableStyleLight5.png)     |
| TableStyleLight6   | ![TableStyleLight6](img/TableStyleLight6.png)     |
| TableStyleLight7   | ![TableStyleLight7](img/TableStyleLight7.png)     |
| TableStyleLight8   | ![TableStyleLight8](img/TableStyleLight8.png)     |
| TableStyleLight9   | ![TableStyleLight9](img/TableStyleLight9.png)     |
| TableStyleLight10  | ![TableStyleLight10](img/TableStyleLight10.png)   |
| TableStyleLight11  | ![TableStyleLight11](img/TableStyleLight11.png)   |
| TableStyleLight12  | ![TableStyleLight12](img/TableStyleLight12.png)   |
| TableStyleLight13  | ![TableStyleLight13](img/TableStyleLight13.png)   |
| TableStyleLight14  | ![TableStyleLight14](img/TableStyleLight14.png)   |
| TableStyleLight15  | ![TableStyleLight15](img/TableStyleLight15.png)   |
| TableStyleLight16  | ![TableStyleLight16](img/TableStyleLight16.png)   |
| TableStyleLight17  | ![TableStyleLight17](img/TableStyleLight17.png)   |
| TableStyleLight18  | ![TableStyleLight18](img/TableStyleLight18.png)   |
| TableStyleLight19  | ![TableStyleLight19](img/TableStyleLight19.png)   |
| TableStyleLight20  | ![TableStyleLight20](img/TableStyleLight20.png)   |
| TableStyleLight21  | ![TableStyleLight21](img/TableStyleLight21.png)   |
| TableStyleMedium1  | ![TableStyleMedium1](img/TableStyleMedium1.png)   |
| TableStyleMedium2  | ![TableStyleMedium2](img/TableStyleMedium2.png)   |
| TableStyleMedium3  | ![TableStyleMedium3](img/TableStyleMedium3.png)   |
| TableStyleMedium4  | ![TableStyleMedium4](img/TableStyleMedium4.png)   |
| TableStyleMedium5  | ![TableStyleMedium5](img/TableStyleMedium5.png)   |
| TableStyleMedium6  | ![TableStyleMedium6](img/TableStyleMedium6.png)   |
| TableStyleMedium7  | ![TableStyleMedium7](img/TableStyleMedium7.png)   |
| TableStyleMedium8  | ![TableStyleMedium8](img/TableStyleMedium8.png)   |
| TableStyleMedium9  | ![TableStyleMedium9](img/TableStyleMedium9.png)   |
| TableStyleMedium10 | ![TableStyleMedium10](img/TableStyleMedium10.png) |
| TableStyleMedium11 | ![TableStyleMedium11](img/TableStyleMedium11.png) |
| TableStyleMedium12 | ![TableStyleMedium12](img/TableStyleMedium12.png) |
| TableStyleMedium13 | ![TableStyleMedium13](img/TableStyleMedium13.png) |
| TableStyleMedium14 | ![TableStyleMedium14](img/TableStyleMedium14.png) |
| TableStyleMedium15 | ![TableStyleMedium15](img/TableStyleMedium15.png) |
| TableStyleMedium16 | ![TableStyleMedium16](img/TableStyleMedium16.png) |
| TableStyleMedium17 | ![TableStyleMedium17](img/TableStyleMedium17.png) |
| TableStyleMedium18 | ![TableStyleMedium18](img/TableStyleMedium18.png) |
| TableStyleMedium19 | ![TableStyleMedium19](img/TableStyleMedium19.png) |
| TableStyleMedium20 | ![TableStyleMedium20](img/TableStyleMedium20.png) |
| TableStyleMedium21 | ![TableStyleMedium21](img/TableStyleMedium21.png) |
| TableStyleMedium22 | ![TableStyleMedium22](img/TableStyleMedium22.png) |
| TableStyleMedium23 | ![TableStyleMedium23](img/TableStyleMedium23.png) |
| TableStyleMedium24 | ![TableStyleMedium24](img/TableStyleMedium24.png) |
| TableStyleMedium25 | ![TableStyleMedium25](img/TableStyleMedium25.png) |
| TableStyleMedium26 | ![TableStyleMedium26](img/TableStyleMedium26.png) |
| TableStyleMedium27 | ![TableStyleMedium27](img/TableStyleMedium27.png) |
| TableStyleMedium28 | ![TableStyleMedium28](img/TableStyleMedium28.png) |
| TableStyleDark1    | ![TableStyleDark1](img/TableStyleDark1.png)       |
| TableStyleDark2    | ![TableStyleDark2](img/TableStyleDark2.png)       |
| TableStyleDark3    | ![TableStyleDark3](img/TableStyleDark3.png)       |
| TableStyleDark4    | ![TableStyleDark4](img/TableStyleDark4.png)       |
| TableStyleDark5    | ![TableStyleDark5](img/TableStyleDark5.png)       |
| TableStyleDark6    | ![TableStyleDark6](img/TableStyleDark6.png)       |
| TableStyleDark7    | ![TableStyleDark7](img/TableStyleDark7.png)       |
| TableStyleDark8    | ![TableStyleDark8](img/TableStyleDark8.png)       |
| TableStyleDark9    | ![TableStyleDark9](img/TableStyleDark9.png)       |
| TableStyleDark10   | ![TableStyleDark10](img/TableStyleDark10.png)     |
| TableStyleDark11   | ![TableStyleDark11](img/TableStyleDark11.png)     |

## CSV
``` JSON title="Konfiguration der csv Exportdatei:"
 "csv":{
            "newline": "\r\n",
            "encoding": "iso-8859-1",
            "seperator": ";",
            "quotechar": "\"",
            "quote":"minimal",
            "number_round":2,
            "number_format":","

        },
```

Wird ein CSV Export ausgeführt, kann hier das Aussehen der CSV bestimmt werden. 

\* = Optional

| Optional | Feld          | Beschreibung                                                                                                                                                                                                               | Beispielwert     |
| -------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| *        | newline       | Welches Zeichen am Ende stehen soll. Windows erwartet ```\r\n``` linux und Mac brauchen nur ```\n```   Standard ist:    ```\r\n```                                                                                         | ```\n```         |
| *        | encoding      | In welchem Zeichensatz die Daten gespeichert werden. Standard ist ```UTF-8``` und ist allgemein empfohlen.  Datev erwartet das alte Windows Format:  ```iso-8859-1```                                                         | ```iso-8859-1``` |
| *        | seperator     | Mit welchem Zeichen werden die Spalten getrennt? Standard ist ```,```                                                                                                                                                      | ```;```          |
| *        | quotechar     | Wie werden Spalten umschlossen, die Sonderzeichen wie z.B. einen Separator enthalten?  Standard ist ein doppeltes Anführungszeichen ```"```  Achtung in JSON Format müssen Sie das Zeichen mit einem ```\``` davor schreiben | ```\"```         |
| *        | quote         | Was soll alles umschlossen werden? die Liste der Werte weiter unten.                                                                                                                                                       |                  |
| *        | number_round  | Auf wieviele Stellen nach dem Komma soll gerundet werden? (Es wird buchhalterisch gerundet)                                                                                                                                | ```2```          |
| *        | number_format | Wie wird das Dezimaltrennzeichen dargestellt. Im Standard : ```.``` für Deutschland typisch: ```,```                                                                                                                       | ```,```          |


### CSV Quote Style


- ```minimal``` : Standardmodus: Felder werden nur dann in Anführungszeichen gesetzt (gequotet), wenn es unbedingt nötig ist - also wenn sie Kommas, Anführungszeichen oder Zeilenumbrüche enthalten. Dieser Modus versucht, die Verwendung von Anführungszeichen auf das notwendige Minimum zu beschränken.
- ```alles```: Alle Felder werden in Anführungszeichen gesetzt, unabhängig davon, ob sie spezielle Zeichen enthalten oder nicht. Dies kann hilfreich sein, um sicherzustellen, dass die Struktur der CSV-Daten eindeutig ist, reduziert jedoch eventuell die Lesbarkeit der Datei.
- ```zeichen```: Hier werden alle nicht-numerischen Felder in Anführungszeichen gesetzt. Numerische Felder werden ohne Anführungszeichen geschrieben. Dieser Modus kann nützlich sein, wenn Sie sicherstellen möchten, dass numerische Werte leicht als solche erkannt und verarbeitet werden können, während Textfelder klar als Text markiert sind.
- ```none```: In diesem Modus werden keine Felder in Anführungszeichen gesetzt. Dies bedeutet, dass Sie selbst sicherstellen müssen, dass Ihre Daten keine Kommas oder andere spezielle Zeichen enthalten, die normalerweise das Einfügen von Anführungszeichen erfordern würden. Dies kann zu Problemen führen, wenn solche Zeichen unbeabsichtigt in den Daten vorkommen, da die CSV-Struktur dadurch gebrochen werden kann.

