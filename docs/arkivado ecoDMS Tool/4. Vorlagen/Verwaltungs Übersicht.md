# Verwaltungsübersicht


Für Administratoren und  Verwaltung ist es wichtig einen Übergblick über ecoDMS zu behalten.

Typische Fragen sind hier: 

- Welche Person auf einen Ornder in ecoDMS Zugriff hat
- Welche Gruppe ist einem Ornder zugeorndet
- Weche Benutzer sind in ecoDMS angelegt
- Welche Ornder, Status, Dokumentenarten sind in ecoDMS angelegt

mit dem Tool können diese Listen mit einem Klick oder zeitgesteuert exportiert werden. 

![Ordnerberechtigungs Export](<img/Ornder Berechtigungs Export.png>)

![Verwaltungs Übersicht](<img/Admin Oberfläche.png>)



## Funktionen

- **Benutzer Export** : Erstellt eine Excel Tabelle mit Rollen und Benutzern. So erhält man einen Überblick welche Benutzer gibt es und in welchen Rollen sind sie. 
- **Ordner Export**:  Erstellt eine Excel Tabelle mit allen Orndern die in ecoDMS angelegt sind. 
- **Ordner Zugr. Rollen**: Erstellt eine Excel Tabelle in der aufgeführt wird, welche Benutzerrolle auf welchen Ordner Zugriff hat.
- **Ordner Zugr. Benutzer**: Wie bei den Rollen, nur werden die Rollen runtergebrochen auf die einzelnen Nutzern. Man sieht hier also welcher Benutzer auf welchen Ornder zugriff hat. 
- **Status Export**: Erstellt eine Excel Tabelle mit allen Statusarten die in ecoDMS angelegt sind. 
- **Typen Export**: Erstellt eine Excel Tabelle mit allen Dokument Typen die in ecoDMS angelegt sind. 




## Konfigurieren / Erste Verwendung


1. Laden Sie sich die Zip Datei herunter [Admin Konfig Export](<static/adminkonfig/Admin Konfig Export.zip>){:download="Admin Konfig Export.zip"}
2. Exportieren Sie die 2 Dateien ```adminkonfig.json``` und ```Admin Konfig Export.bat``` in das Verzeichnis, indem das Arkviado Tool liegt (falls noch nicht heruntergaladen dann [hier](https://lizenz.arkivado.digital/lizer/download/Arkivado_Ecodms_Tools)). 
3. Starten Sie die ```Admin Konfig Export.bat```
4. Sie bekommen eine Meldung, dass keine Lizenz hinterlegt ist
5. Geben Sie Ihren Lizenzschlüssel ein
6. Die Lizenz wird aktivert und in in Ihre ```adminkonfig.json```  geschrieben. Das Programm wird beendet-
7. Starten Sie die ```Admin Konfig Export.bat``` erneut
8. Klicken auf Konfigurieren
9. Geben Sie den API Pfad zu ecoDMS ein siehe [hier](<../1. Einleitung/001voraussetzungen.md>) mehr dazu 
10. Geben Sie einen Admin User und dessen Passwort ein.
11. Klicken Sie auf Speichern
12. Sie können nun die Berichte Erstellen

## Kopiervorlage

Zur Dokumentation der Konfigs hier noch einmal die beiden Dokumenete aus der ZIP zum kopieren. 

``` json  title="adminkonfig.json"
 {
  "ecodms": {
    "ECODMSurl": "https://hiermeineAPIAdresse/api/",
    "ECODMSuser": "ecodms",
    "ECODMSpw": null,
    "ECODMSabort_on_ssl_error": true,
    "export_to": "excel",
    "export_path": "C:\\ecoDMS Daten\\Export_ecoDMS",
    "export_open": true,
    "paths": {
      "Sonstiges": "C:\\Daten\\Daten\\ecoDMS Export\\Sonstiges"
    },
    "excel": {
      "do_format": true,
      "table_style": "TableStyleMedium2"
    },
    "ECODMStoken": ""
  },
  "gui": {
    "theme": "blau",
    "buttons": [
      {
        "funktion": "Benutzer Export",
        "text": "Benutzer Export",
        "show": true
      },
      {
        "funktion": "Ordner Export",
        "text": "Ordner Export",
        "show": true
      },
      {
        "funktion": "Ordner Rollen Export",
        "text": "Ordner Zugr. Rollen",
        "show": true
      },
      {
        "funktion": "Ordner Benutzer Export",
        "text": "Ordner Zugr. Benutzer",
        "show": true
      },
      {
        "funktion": "Status Export",
        "text": "Status Export",
        "show": true
      },
      {
        "funktion": "Typen Export",
        "text": "Typen Export",
        "show": true
      },
      {
        "funktion": "Konfigurieren",
        "text": "Konfigurieren",
        "show": true
      }
    ]
  },
  "license": ""
}
```


``` bat  title="Admin Konfig Export.bat"
cd %~dp0
"%~dp0arkivado.exe" -c "%~dp0adminkonfig.json"
```