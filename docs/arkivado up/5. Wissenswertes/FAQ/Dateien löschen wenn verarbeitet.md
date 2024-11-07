# Dokumente löschen wenn hochgeladen


## Problembeschreibung

Wenn man ein Archiv nach ecoDMS "verschieben" will, sodass lokal nichts mehr liegen.


## Erklärung

Hierfür kann in der Konfiguration *delete_if_done* gesetzt werden, dadurch werden die lokale Dokumente auf der Festplatte endgültig gelöscht, sobald sie hochgeladen wurden. 

!!! warning
    Wichtig ist dabei, dass die Logik der revisionierung weiterhin aktiv ist! Das heißt wird ein neue Datei mit dem selben Namen abgelegt, wird eine neue Version des Dokuments angelegt. NICHT ein neues Dokument!


## Lösung 

In der params.json Konfiguration wird ein neuer Eintrag gesetzt bei:
```json title="Fertige Syntax" 
{
  "arkivado_up": {
    "delete_if_done": true

  }
}

```
| JSON Key        | Bedeutung                        | Beispiel        |
| --------------- | -------------------------------- | --------------- |
| ```delete_if_done``` | Bei ```true``` wird das Dokument unwiederuflich lokal gelöscht. Wenn nicht vorhanden oder false, bleibt das Dokument liegen | ```true``` |
