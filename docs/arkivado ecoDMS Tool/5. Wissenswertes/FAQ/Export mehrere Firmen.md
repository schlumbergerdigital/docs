# Export mehrerer Firmen

## Problembeschreibung

Sie haben mehrere Firmen bzw. Mandanten und möchten pro Mandant exportieren.

## Lösung

Dies ist möglich: Sie können das Arkivado-Tool mit verschiedenen Profilen starten.  
Dabei entspricht ein Profil einer Firma.

### Profile verwenden

Ein Profil ist eine JSON-Konfigurationsdatei.  
Allgemeine Informationen zu JSON finden Sie [hier](<../006technischer Background.md>).

Das Laden eines anderen Profils wird über einen Parameter gesteuert.  
Allgemeine Informationen zu den Parametern finden Sie [hier](<../../2. Verwendung/007start per Kommandozeile.md#mehrere-profile-verwenden>).

Für den Endanwender können Sie die verschiedenen Profilaufrufe folgendermaßen realisieren:

- **Verknüpfungen**: Keine CMD nötig, Icon ist schöner. Allerdings anfälliger für Fehler, wenn kopiert usw.
- **Batch-Dateien**: Robuster, aber es öffnet sich kurz ein Konsolenfenster (CMD). Kein Icon; zudem müssen die erforderlichen Rechte für die CMD vorhanden sein.

### Profile einrichten

Zunächst erstellen Sie eine passende *params.json*, die als Ausgangspunkt dienen soll.

1. Erstellen Sie einen Ordner, in dem sich die Arkivado.exe befindet.
2. Kopieren Sie die *params.json* aus dem AppData-Verzeichnis in Ihr Arbeitsverzeichnis.
3. Geben Sie der kopierten *params.json* einen neuen Namen, z. B. *erste_Firma_Rechnungs_Export.json*.
4. Passen Sie die *params.json* so an, dass nur Daten der ersten Firma exportiert werden (mithilfe von Filtern).
5. Ändern Sie die Farbe der Oberfläche, damit die Endanwender sofort erkennen, um welche Firma es sich handelt (siehe [hier](<../../3. Konfiguration/007config_gui.md>)).

!!!warning "Profil Filter implementieren"
    wie genau Sie den Firmen Filter bauen, hängt von Ihrem ecoDMS ab, das ist NICHT Teil dieser Anleitung!

Anschließend erstellen Sie entweder eine *Verknüpfung* oder legen eine *Batch-Datei* an.

-----------------------

#### Batch-Datei erstellen

- Legen Sie eine leere Datei mit der Endung *.bat* an.
- Nennen Sie diese z. B. „erste_Firma_Rechnungs_Export.bat“.
- Schreiben Sie folgenden Text in die Datei (ersetzen Sie ggf. *erste_Firma_Rechnungs_Export.json* durch den Namen Ihrer JSON-Datei):

```batch
@echo off
pushd %~dp0
start "" /min "%~dp0arkivado.exe" -c "%~dp0erste_Firma_Rechnungs_Export.json"
exit
```

- Mit einem Klick auf die .bat-Datei wird nun Arkivado mit dem Profil *erste_Firma_Rechnungs_Export.json* gestartet.

-----------------------

#### Verknüpfung erstellen

Alternativ zur *.bat-Datei* können Sie auch eine *Verknüpfung* erstellen:

- Klicken Sie mit der rechten Maustaste auf die Arkivado.exe, ziehen Sie sie an eine freie Stelle und wählen Sie „Verknüpfung erstellen“.
  
  ![Eine Verknüpfung erstellen](<img/Verknüpfung Erstellen.png>)

- Benennen Sie die Verknüpfung mit einem aussagekräftigen Namen, z. B. *erste Firma Rechnungs Export*.
- Öffnen Sie per Rechtsklick die *Eigenschaften* der Verknüpfung.
  
  ![Eigenschaften der Verknüpfung](img/Eigenschaften_Verknüpfung.png)
  
- Ergänzen Sie im Feld „Ziel“ den Parameteraufruf.  
  Der Parameter lautet:

```
-c "IHR JSON NAME HIER"
```

  ![Parameter ergänzen](<img/Parameter Ergänzen.png>)

  Das vollständige Ziel lautet beispielsweise:

```
C:\bsp\arkivado.exe -c "erste_Firma_Rechnungs_Export.json"
```

- Klicken Sie auf OK. Die Verknüpfung ist nun fertig.

Wird die Verknüpfung gestartet, wird das entsprechende Profil geöffnet.

Verfahren Sie so für alle Firmen.

### Vollautomatischer Export mehrerer Firmen

Sie können auch einen vollautomatischen Export durchführen.  
Fassen Sie dazu die verschiedenen Aufrufe in einer großen Batch-Datei zusammen und ergänzen Sie den Aufruf um die jeweilige Funktion.

Wenn der *DATEV Export* (alle Funktionen [hier](<../../2. Verwendung/001funktionen.md>)) genutzt wird, lautet der Aufruf für drei Profile beispielsweise:

```batch
@echo off
pushd %~dp0
start "" /min "%~dp0arkivado.exe" -c "%~dp0erste_Firma_Rechnungs_Export.json" -f "Datev Export"
start "" /min "%~dp0arkivado.exe" -c "%~dp0zweite_Firma_Rechnungs_Export.json" -f "Datev Export"
start "" /min "%~dp0arkivado.exe" -c "%~dp0dritte_Firma_Rechnungs_Export.json" -f "Datev Export"
exit
```
