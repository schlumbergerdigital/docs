# Export in Einzeldateien


## Problembeschreibung
Bei dem CSV/Excel Export soll pro Dokument eine Datei ausgegeben werden.   
Im Standard wird eine Liste mit allen Dokumenten erstellt. 





## Lösung 

Die nötigen Änderungen werden in der Konfigurationsdatei vorgenommen. 

### Wo zu ändern

Um dem Arkivado Tool zu sagen, dass pro ecoDMS Dokument eine Datei erstellt werden soll, muss die Konfigurationsdatei ```params.json```  angepasst werden. Mehr infos [hier](<../006technischer Background.md>).

Je nachdem welche Exportart benötigt, werden die Einstellungen unter folgenden Keys geändert:

-  *Dokumenten Export* wird verwendet um Metadaten und auch das Dokument selbst zu exportiern
-  *Dokumentenliste Export* wird verwendet um *nur* Metadaten zu exportiern

Mehr zu den Funktionen [hier](<../../2. Verwendung/001funktionen.md>).



### Was zu ändern

Setzen  Sie (ggf. legen Sie Ihn neu an) die Key unter dem benötigten Export verfahren:

-  ```MultiFiles``` auf  ```true``` 
-  ```Pfad``` mit dem vollständingen Ablage Pfad inkl Variablen für die Metadaten.
  
!!! warning "Variablen im Dateinamen verwenden"
    Sie können nicht nur einen *starren* Dateinamen vergeben, da Sie ja mehrere Dateien anlegen wollen.    
     Vergeben Sie keine Variablen, überschreiben sich die Metadaten Dateien.     
     Für den dynamischen Dateinamen lesen Sie hier [hier](<../../3. Konfiguration/003config_doclist.md#dateinamen-dynamisch-angeben>). 


## Beispiel




``` JSON title="Teilkonfig für mehrere Dateien"

"Dokumentliste Export": {
    "MultiFiles" : true,
    "Pfad" : "C:\\pfad\\zur\\ablage\\{data['docid']}_{datum(%Y-%m-%d)}_{uid()}.csv",

...
```

Mit dieser Konfiguration wird pro ecoDMS Dokument eine CSV Datei erstellt. Diese wird dann unter dem Pfad:

```
C:\pfad\zur\ablage\
```

und dem Dateinamen (bei DocID 12542 am 31.01.2025 exportiert):
```
12542_2025-01-31_abc32431fdfd3223454.csv
```
abgelegt.
