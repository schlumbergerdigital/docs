# Dokumenten Export

!!! tip "Filter"
    Die Filtermechanismen, beschrieben in der Dokumentenliste, greifen ebenso hier. Weitere Informationen finden Sie [hier](003config_doclist.md).

## Dokumentexport

Der Dokumentexport speichert die Dokumente aus ecoDMS auf der Festplatte und erstellt zudem eine Excel- oder CSV-Datei (abhängig vom Wert in ```export_to```), die alle Attribute (Metadaten) des Dokuments enthält. Die 1.000-Dokument-Grenze von ecoDMS greift nicht; standardmäßig werden alle Dokumente aufgeführt.

| Opt. | Feld                | Beschreibung | Beispielwert |
|------|---------------------|--------------|--------------|
|      | Filter              | Der Filter wird immer auf die Dokumente angewendet. Siehe weiter oben. | ```[ { "classifyAttribute": "docid", "searchOperator": ">", "searchValue": "0"}]``` |
|      | Pfad                | Wohin die Dokumente auf der Festplatte exportiert werden sollen. Bei Pfadangaben in JSON wird ein "\\" immer mit "\\\\" geschrieben. | ```C:\\ecoDMS Daten\\Export``` |
|      | FileName            | Der Name, den die Exportdatei haben soll. In ```< >``` geschrieben, greift auf ecoDMS-Felder zu. Ohne ```< >``` wird fester Text verwendet. **Dringend**: Bitte immer die ```<DocID>``` mit angeben, damit Dateinamen eindeutig sind. Aus dem Beispiel rechts würde z.B. **2022-11-23-Rechnung Baum-3421.pdf**. | ```["<Belegdatum>","-","<Bemerkung>","-",<DocID>"]``` |
|      | FileAttributeMaxLength | Die maximale Länge, die ein ```< >``` Attribut im Dateinamen haben darf. | ```50``` |
