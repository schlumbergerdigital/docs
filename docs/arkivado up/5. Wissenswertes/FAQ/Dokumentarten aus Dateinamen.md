# Dokumentarten bestimmen am Dateinamen


## Problembeschreibung

Oftmals wird im Dateinamen der Dokumententyp angegeben. Manchmal auch am Ende des Dateinamens. 
Eine Weitere Schwierigkeit kann sein, dass dabei auch unterschiedliche Bezeichnungen verwendet wurden.

z.B. ist ```213234-RE.pdf``` und ```345-213234kdeRechnung.pdf``` jeweils vomm Typ *Rechnung*


## Erklärung

in dem Beispiel sind mehrere Herausforderungen enthalten:

1. Die Länge des Dokumentes ist variabel. Ein  *splitting* nach starren Regeln funktioniert nicht
2. Der Typ steht am Ende des Dateinamnes 
3. Der Typ ist nicht einheitlich vergeben

Um richtige Werte zu bekommen, wird eine verschachteltet *IF* Abfrage verwendet. Die Anlayse wird auf das Ende des Strings angewendet. 




## Lösung 


Der Befehl unterscheidert zwischen

- Rechnungsausgang
- Angebot
- Gutschrift
- Auftragsbestätigung
  
Alle Andere Dokumente werden als 

- nicht zugeordnet

abgelegt.

Folgender String ist die *fertig* Lösung. Die einzelnen Elemente werden unten erklärt.

```python title="Fertige Syntax" 
'Rechnungsausgang' if str(<file_name>)[:-4].lower().endswith(('rg','rechnung','wartungsrechnung','schlussrechnung'))  else 'angebot' if str(<file_name>)[:-4].lower().endswith(('an','angebot'))  else 'gutschrift' if str(<file_name>)[:-4].lower().endswith(('gutschri', 'gutschrift','gs')) else 'Auftragsbestätigung' if str(<file_name>)[:-4].lower().endswith(('ausbestä','auftragsbestätigung','au')) else 'nicht zugeordnet'
```

zunächst der erste Abschitt
```python title="Rechnungsausgang" 
'Rechnungsausgang' if str(<file_name>)[:-4].lower().endswith(('rg','rechnung','wartungsrechnung','schlussrechnung')) else
```

Es wird *Rechnungsausgang* ausgegeben wenn die Bedingung erfüllt ist. die Bedingung (if) kommt nach dem if.
also

```python title="If" 
if str(<file_name>)[:-4].lower().endswith(('rg','rechnung','wartungsrechnung','schlussrechnung')) 
```
in der if Bedingung werden mehrere Dinge durchgeführt:

 - Es wird auf den Dateinamen  referenziert mit: ```<file_name>``` 
 - Die letzten 4 Zeichen des Dateinamens werden entfernt ```[:-4]``` (also wird aus z.B.*213234-RE.pdf* *213234-RE*)
 - Der ganze Dateiname wird für die Prüfung in kleinbuchstaben verwandelt. Es ist also egal ob das Dokument   *213234-RE.pdf* oder *213234-re.pdf* heißt 
 - Zum Schluss wird geprüft ob der Dateinamen entweder mit *rg* oder mit *rechnung* oder mit *wartungsrechnung* oder mit *schlussrechnung* aufhört. ist dem so, wird der Wert vor dem *if* ausgeben wenn nicht kommt die nächste prüfung hinter dem *else* 

es können bilibig viele verschachtelungen vorgenommen werden. 

