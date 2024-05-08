# Daten in den Turm hochladen


Wie bekomme ich Daten aus Excel oder CSV in den Turm hoch?


## Webupload

Sie können die Dateien einfach hochladen
Der Upload Link lautet:

```
/uploaddata/meine_zu_bearbeitende_tabelle
```
also  z.B.
https://turm.meinserver.arkivado.digital/uploaddata/meine_zu_bearbeitende_tabelle


### Optionale Paramter

Es stehen mehrer Optionale Parameter zur Verfügung:

- workflow: Soll nach Verarbeitung der Daten ein Worlflow ausgeführt werden, kann hier der Name des Workflows angegben werden.
  ``` workflow=Mein Workflow Name```
z.B.
```http://turm.meinserver.arkivado.digital/blaba?workflow=Mein%20Worklfow%20Name```

- create_table: Verindert dass eine neue Tabelle angelegt wird, falls die Tabelle noch nicht vorhanden ist.  
``` create_table=false```
z.B.
```http://turm.meinserver.arkivado.digital/blaba?create_table=false```
Die Tabelle *blabla* würde in so nicht angelegt werden


## Schiff Upload


Die Daten können auch automatisch (und zeitgestuert) hochgeladen werden.
Nutzen Sie hierfür das Schiff.

Zur Benutzung des Schiff die Schiffsdoku lesen. 