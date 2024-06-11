# Changelog

alle Aktuallisierungen vom arkivado ecoDMS Tool 

## 11.3    - <small>11.06.2024</small> { id="11.2" }



<b><small>Feature</small></b> 

- EcoDMS Zugangesdaten  über die grafische Oberfläche  einstellen. Drücken Sie einfach ```STRG + K``` 
- EcoDMS Multifkator Authentifizierung unterstützt

<b><small>Verbesserungen</small></b> 

- Große interne Refactoring 
- Funktionsnamen sind nun Case insensitive    


## 11.2   - <small>23.05.2024</small> { id="11.2" }


<b><small>Feature</small></b> 

- Laufende Aufträge können nun durch User in der Oberfläche abgebrochen werden. 


<b><small>Verbesserungen</small></b> 

- Bug behoben: Ladebalken wird nicht immer angezeigt


<b><small>Docu</small></b> 

- Vorlage für EXTF ergänzt

## 11.1   - <small>14.05.2024</small> { id="11.1" }

:partying_face:  Veröffentlichung der neuen Version :rocket: 


<b><small>Feature</small></b> 

- Export von ecoDMS Dateien im formatierten Exelberichten
- Oberflächen und Buttons sind über json konfigurierbar. Spezifischer Look für den Endanwender möglich
- Per Kommandozeile aufrufbar um automatische Workflows zu starten. Damit sind zeitgesteuerte Exporte möglich.
- Möglichkeit Zeitraum Filter ein und auszustellen in allen Optionen
- Möglichkeit Export Spalten anzupassen, umzubenennen hinzuzufügen
- Möglichkeit Export Kopfzeilen hinzuzufügen
- Möglichkeit mehrere Profile für unterschiedliche Berichte und/oder Server zu hinterlegen (benötigt erweiterte Lizenz)
- Exporte können für beliebige FIBU-,ERP-, CRM-Systeme oder Portale konfiguriert werden
- Kopfzeilen können Zusammenfassungen wie min/max oder von bis Datumsangaben wiedergeben
- Standardwerte können hinterlegt werden, wenn keine Werte in ecoDMS vorhanden sind
- Fehler im Datev Export werden nun als *schöne* HTML Tabelle geöffnet

<b><small>Verbesserungen</small></b> 

- Anzeige des Logfiles im Shellfenster kann ausgeblendet werden, Logfile kann über Oberfläche geöffnet werden.
- Prüfung ob ein eingegebenes Datums
- Prüfung der JSON Datei und ggf. Hinweis auf konkreten Fehler
- Bei nicht verbundenen Server, oder fehlerhafter API kommt sofort eine Fehlermeldung.
- Bei Zertifikatsfehler sprechende Fehler hinterlegt
- Sprechende Fehlermeldung wenn Server wenn nicht erreicht ist
- Im Automatik Modus: Programm beendet sich wenn keine Verbindung zum Server aufbaubar ist 

<b><small>Docu</small></b> 

- Einführung Changelog zu Realeaseständen
- Einführung Onlinedokumentation