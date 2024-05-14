# Verbindungsfehler: API nicht erreichbar


## Problembeschreibung

- Das Tool startet 
- Beim Klick auf irgendeine Taste kommt eine Fehlermeldung

``` title="Zertifikatsfehler im Log"
2024-05-14 10:33:51,421 - CRITICAL - EcoDMS: Keine Verbindung zu "https://dmsentwicklung.docarchivdemo.net:8181/api/" möglich. Der API Dienst scheint aus, blockiert oder defekt zu sein! 
Prüfen Sie in den ecoDMS Einstellungen > API Zugriff
HTTPSConnectionPool(host='dmsentwicklung.docarchivdemo.net', port=8181): Max retries exceeded with url: /api/connect/1 (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x000002087993B310>: Failed to establish a new connection: [WinError 10061] Es konnte keine Verbindung hergestellt werden, da der Zielcomputer die Verbindung verweigerte'))
2024-05-14 10:34:40,877 - CRITICAL -  Ein Fehler bim Verbinden mit ecoDMS ist aufgetreten. Prüfen Sie das Log.
``` 
![Fehlermeldung](img/Verbindungsfehler2.png)


## Erklärung

Das arkivado Tool versucht sich mit ecoDMS zu verbinden und stellt dabei fest, dass der API Server von ecoDMS nicht erreichbar ist.


Dies passiert immer dann, wenn der Api Dienst von ecoDMS aus oder defekt ist. 


## Lösung 

Prüfen Sie in ecoDMS ob der Api Dienst an und erreichbar ist. 
Der Fehler liegt in ecoDMS nicht beim Tool. 

siehe auch [Voraussetzungen](<../../1. Einleitung/001voraussetzungen.md>)