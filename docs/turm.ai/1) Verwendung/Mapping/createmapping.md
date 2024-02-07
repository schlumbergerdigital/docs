# Mapping / Einen Link anlegen

Ein Link verbindet den Turm mit einem Fremdsystem. Dabei sollen die Daten modifiziert werden. Dies geschieht mittels Mapping, welches definiert, welche Informationen wohin übertragen werden sollen.

Beispiel: Das Feld *Notiz* aus dem CRM enthält Informationen, die im DMS unter *Beschreibung* sichtbar sein sollen. Dies ermöglicht die Datenübertragung von einer Webapp zur anderen.

Jede Entität aus jedem Modul entspricht einer Tabelle im Turm. Um Entitäten zu verknüpfen, muss ein neuer *Link* angelegt werden.

Hier sehen Sie, wie ein neuer Link angelegt wird:

![](img/new_link.png)

Der URL zum Erstellen eines neuen Links lautet:```/link```
also z.B.
```
http://localhost:8000/link
```

 [Weiter: Mapping konfigurieren](mapping.md){ .md-button }