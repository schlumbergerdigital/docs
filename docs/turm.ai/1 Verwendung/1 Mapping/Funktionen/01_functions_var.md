# Variablen
![](../../../img/mapping.png)
## Variablen
In der zweiten Modulspalte kann der Output modifiziert werden.

Es ist möglich, auf Werte aus dem Mapping zuzugreifen. Sowohl feste Werte als auch dynamische Werte können verwendet werden. Zum Beispiel kann in die sekundäre Modulspalte Folgendes geschrieben werden:   
```
www.{data['webseite']}.de  
```

Durch diesen Befehl wird der Wert aus der Spalte *webseite* genommen, und *www.* wird davor sowie *.de* dahinter gesetzt.

Variablen und Befehle werden in  ```{}``` eingeschlossen, und die Werte der zu bearbeitenden Spalte befinden sich im *data*-Dictionary.

Um also das Feld "email" aufzurufen, muss in der Modulspalte Folgendes stehen:

```
{data['email']}
```

!!! tip "Tipp"
    Der Name des Feldes wird in der dritten Spalte definiert. Die dritte Spalte muss also – irgendwo – einen Eintrag enthalten, der *email* heißt (siehe auch den Eintrag zu @no@).

!!! tip "Pro-Tipp"
    Innerhalb von ```{}``` steht die gesamte Bandbreite der Python-Bibliotheken für **f-Strings** zur Verfügung.


## Escape-Zeichen und Sonderzeichen

Um das Zeichen ```{```  zu schreiben, ohne dass es als Befehl interpretiert wird, muss es doppelt eingegeben werden:

```
 {{
```

Das Gleiche gilt für das Zeichen `}`. Es muss ebenfalls doppelt eingegeben werden, um es ohne Befehlsauslösung zu schreiben:

```
 }}
```

Um einen Zeilenumbruch zu erzeugen, verwenden Sie:

```
@newline@
```

!!! warning "Verbotenes Zeichen"
    Verwenden Sie niemals ein `\` innerhalb von `{}`.  
Wenn Sie beispielsweise einen Windows-Pfad über das Mapping zusammensetzen möchten, schreiben Sie:
    ```
    {data['pfad']}\{data['filename']}
    ```
    Das `\` befindet sich außerhalb der Klammern!
    Ein fehlerhafter Befehl wäre:  
    FALSCH:
    ```
    {data['pfad']}+'\'+{data['filename']}
    ```

Um ein `@` im Mod-Text zu schreiben, verwenden Sie bitte `@@`.  
Zum Beispiel, wenn die E-Mail-Adresse `max@beispiel.de` immer erscheinen soll, geben Sie ein:

```
max@@beispiel.de
```

## Felder nicht im Zielsystem übertragen
Um ein Feld zum Mapping zur Verfügung zu stellen, weil es in einem anderem Feld benötigt wird, ohne das es am ende im Fremdsystem auftauchen soll, schreiben Sie im hinteren Mod Feld 
```
 @no@
```
