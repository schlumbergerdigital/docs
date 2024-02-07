# Funktionen
*Stand: Turm Version 14.22.1 - 01.02.2024*

## Bedingungen "Wenn-Dann" im Befehl
    
Es ist möglich, Bedingungen zu definieren:

```
{ <meinWert> if (<DieseBedingungmusspassen>) else <ersatzWert> }
```

| Feld                        | Bedeutung                                                         | Beispiel                      |
| --------------------------- | ----------------------------------------------------------------- | ----------------------------- |
| <meinWert\>                  | Gibt den Wert an, der ausgegeben werden soll, wenn die Bedingung zutrifft. | ```data['email']``` |
| <DieseBedingungmusspassen\>  | Diese Bedingung wird geprüft. Wenn sie *True* ist, wird *<meinWert>* ausgegeben. | ```len(data['email']) > 0``` |
| <ersatzWert\>                | Wird ausgegeben, wenn die Bedingung *False* ist, also nicht zutrifft. | ```'xx@xx.de'``` |

Der folgende Befehl ersetzt leere E-Mail-Adressen durch '*xx@xx.de*':

```
{ data['email'] if (data['email'] is not None and len(data['email']) > 0) else 'xx@xx.de' }
```


## Feste Vorschriften für feste Werte Case

Um einen Wert durch einen anderen zu ersetzen, kann der Befehl @case() verwendet werden.  
Dabei wird der angegebene Wert durch einen anderen festgelegten Wert ersetzt.  
Der zweite Parameter wird verwendet, wenn kein passender Wert gefunden wird. Dieser Standardparameter ist optional. Wird er nicht angegeben, bleibt der ursprüngliche Wert erhalten. 
Die "Tabelle" der Ersatzwerte wird in ```{ }``` notiert. 

```
@case({'<wert1>': '<ersatzwert1>','<wert2>': '<ersatzwert2>'}, '<WertWennKeinErsatzwertvorhanden>' )
```


| Feld                        | Bedeutung                                                         | Beispiel                      |
| --------------------------- | ----------------------------------------------------------------- | ----------------------------- |
| `<wert1>`                  | Gibt den ersten möglichen Wert aus dem Quellsystem an. | `29682885` |
| `<ersatzwert1>`  | Ist der Wert, der ins Zielsystem übergeben werden soll.  | `600fee2e544461c8b` |
| `<WertWennKeinErsatzwertVorhanden>` | Wird verwendet, wenn keiner der Bedingungen entspricht. | `'0000000000'` |





```
@case({ 
  'Dieser Text wird ersetzt' : 'durch diesen Text' 
 ,'29682885' : '600fee2e544461c8b' 
 ,'29682886' : '6026692a3ee487761' 
 ,'29682890' : '605afe85afaef48b8'
 ,'29682907' : '608a89e4157de1714'
},'Hier der Standard Text wenn keines der Oberen passt')
```
