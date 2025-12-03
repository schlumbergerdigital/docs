# Changelog

alle Aktualisierungen vom arkivado up

## 1.5.0  - <small>01.12.2025</small> { id="1.5.0" }

<b><small>Feature</small></b> 

- Die Möglichkeit Filter als Parameter zu übergeben. Damit können z.B. Teile nachklassifiziert werden. 
  

<b><small>Verbesserungen</small></b> 

- Besserer Umgang mit sehr vielen Ordnern. Die ecoDMS Api gibt dann öfters Fehler aus, was dazu geführt hat, dass Ornder doppelt angelegt wurden. 
- Switch auf HTTPX Modul im Async Request.

## 1.4.2   - <small>25.09.2025</small> { id="1.4.2" }

<b><small>Verbesserungen</small></b> 

- Monitoring fehlertolleranter geschrieben
- Fehlerbehebung: Ohne Mapping kann nun auch hochgeladen werden
- EcoDMS resilenter: Wenn kein Status angegeben ist wird standard gesetzt. 


## 1.4.1   - <small>13.08.2025</small> { id="1.4.1" }


<b><small>Verbesserungen</small></b> 

- Diverse kleine Bugs behoben v.a. bei instabilen Verbindungen

## 1.4.0   - <small>23.05.2025</small> { id="1.4.0" }

<b><small>Feature</small></b> 

- Klassifizierungsattribute können nun nachgeholt werden. z.B. bei falschem Erstimport siehe [hier](<2. Verwendung/007start per Kommandozeile.md>)
  
<b><small>Verbesserungen</small></b> 

- Bug behoben, bei dem nicht kassifziert wurde, wenn ein nicht existienter Status oder Dokumentenart angegeben war. 


## 1.3.1   - <small>21.05.2025</small> { id="1.3.1" }

<b><small>Feature</small></b> 

- Bei Ornderüberwachung kann nun ein Timer eingestellt werden der im X Tagen wieder ein vollscann durchführt. siehe [hier](<3. Konfiguration/004config.md>)
- Es kann nun eingestellt werden ob ein Vollscann vor der Ordnerüberachung durchgeführt wird. siehe [hier](<3. Konfiguration/004config.md>)
- Experimentell: Oberfläche die belibige Profile als Dienste einrichtet.  siehe [hier](<2. Verwendung/008start als Dienst.md>)
- Maximale Dateigröße kann nun angegeben werden. 

<b><small>Verbesserungen</small></b> 

- Komplett auf Async Http umgestellt
- Leere Dokumente werden übersprungen

  

## 1.2.2   - <small>14.03.2025</small> { id="1.2.2" }


<b><small>Verbesserungen</small></b> 

- Mehrere Profile können nun als Dienst laufen
- Bug: Wite List greift nicht bei mehren Profilen
  

## 1.2.1   - <small>13.03.2025</small> { id="1.2.1" }


<b><small>Verbesserungen</small></b> 

- MS SQL: Parst nun die Werte vom SQL Server. 
- Intern: Upgrade auf Python 3.13
- EcoDMS: Diverse verbesserungen und vorbereitung auf große Async Umstellung 
- Bug: Fehler behoben, bei dem bei mehreren Profilen (mittels -c ) Einstellungen im Konfigmenü ggf. überschreiben wurden
  
<b><small>Docu</small></b> 

- Artikel erweitert: Ausgabe von Dateinamen ohne Dateiendung siehe  [hier](<3. Konfiguration/005config_mapping.md>)
  
  

## 1.2.0   - <small>08.11.2024</small> { id="1.2.0" }

<b><small>Feature</small></b> 

- Arkviado UP kann nun in Fremdsystemen Daten nachschlagen siehe [hier](<3. Konfiguration/007config_lookup.md>)
- Arkviado UP kann jetzt mit mehreren Profilen für verschiede Ordner arbeiten. Dabei kann mit dem Parameter  -c einfach eine andere JSON Konfiguration angegeben werden siehe [hier](<2. Verwendung/007start per Kommandozeile.md>)
- Arkivado UP kann nun Dokumente nach erfolgreichem Verarbeiten auf der Festplatte löschen, siehe [hier](<5. Wissenswertes/FAQ/Dateien löschen wenn verarbeitet.md>)


<b><small>Verbesserungen</small></b> 

- Bisher wurde wenn Arkviado UP als Dienst läuft und jemand das Programm nochmals starten wollte keine Fehlermeldung ausgegeben, nun wird der User informiert, dass erst der Dienst gestoppt werden muss.
- Anpassung: Wenn mit -c aufgerufen wird, findet keine Prüfung statt ob das Tool schon läuft
  
<b><small>Docu</small></b> 

- Artikel zu: Dokumentarten aus Dateinamen bestimmen geschrieben, siehe [hier](<5. Wissenswertes/FAQ/Dokumentarten aus Dateinamen.md>)
- Arkikel zum Lookup geschieben siehe [hier](<3. Konfiguration/007config_lookup.md>)
- Artikel zum Löschen geschrieben siehe [hier](<5. Wissenswertes/FAQ/Dateien löschen wenn verarbeitet.md>)

  

## 1.1.1   - <small>22.08.2024</small> { id="1.1.1 " }

<b><small>Verbesserungen</small></b> 

- 0 KB Dateien werden nicht mehr zu ecoDMS hochgeladen, da es sonst zu Abstürtzen in der ecoDMS API kommen kann. 


<b><small>Docu</small></b> 

- Artikel zu: Dokumente nachholen geschrieben siehe [hier](<5. Wissenswertes/FAQ/Dokumente Nachholen.md>)
  


## 1.1.0   - <small>20.08.2024</small> { id="1.1.0 " }


<b><small>Feature</small></b> 

- Programm kann nun als Windowsdienst laufen, siehe [hier](<2. Verwendung/008start als Dienst.md>)


<b><small>Verbesserungen</small></b> 

- Bug: Start vom Programm schlägt manchmal fehl wenn Appvezeichnis fehlt


<b><small>Docu</small></b> 

- Artikel zu: Oberfläche startet nicht siehe [hier](<5. Wissenswertes/FAQ/Start_ohne_bilschirm.md>)
- Artikel Mapping erweitert: Um Case erweitert siehe [hier](<3. Konfiguration/005config_mapping.md>)



## 1.0.1   - <small>18.07.2024</small> { id="1.0.1 " }

<b><small>Verbesserungen</small></b> 

- Mutifaktor Anmeldung angepasst 

## 1.0.0   - <small>03.07.2024</small> { id="1.0.0 " }

:partying_face:  Veröffentlichung von der  Version 1.0.0  :rocket:



<b><small>Verbesserungen</small></b> 

- Verbesserung: Deutlich kleinere Exe Größe ist halbiert: Kleiner, schneller 
- Verbesserung: Info wenn Lizenz nicht aktiviert ist in der Oberfläche
- Bug: ecoDMS User mit Umlauten konnten sich nicht anmelden
- Bug: Bei Fehler im Kommandozielen Modus wurd der Job ggf. nicht beendet


##  0.8.0   - <small>14.06.2024</small> { id="0.8.0" }


<b><small>Feature</small></b> 

- Dateinamen kann angesprochen werden
- Dateinamen können gesplittet werden z.B. bei _ siehe: [Splitting](<3. Konfiguration/005config_mapping.md#splitting-im-dateinname>)
- Bedingungen *If Then* Vergleiche können verwendet werden siehe: [Bedingungen](<3. Konfiguration/005config_mapping.md#bedingungen-if-then-else>)

<b><small>Docu</small></b> 

- Mapping part um Splitting und If erweitert

##  0.7.1   - <small>07.06.2024</small> { id="0.7.1" }

:partying_face: Erste BETA Veröffentlichung :rocket: 


<b><small>Feature</small></b> 

- Watchdog implementiert 
- Whiteliste für Dateien programmiert
- Mapping für ecoDMS Attribute programmiert
- Oberfläche geschrieben
- File und Oberfläche mit Logging versehen
- Hashing der Dateien paralleliert 
- Kommandozeilen Optionen hinzugefügt
- Automatische Anlage der Internen DB 
- EcoDMS Schnittstelle impementiert
- Folder Scann geschrieben
  


<b><small>Docu</small></b> 

- Einführung Changelog zu Realeaseständen
- Einführung Onlinedokumentation