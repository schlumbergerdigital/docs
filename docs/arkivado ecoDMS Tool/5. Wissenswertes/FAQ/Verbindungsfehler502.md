# Verbindungsfehler: 502 Bad Gateway


## Problembeschreibung

- Das Tool startet 
- Beim Klick auf irgendeine Taste kommt eine Fehlermeldung

``` title="Verbindungsfehler im Log"
22024-05-14 11:25:55,691 - CRITICAL - EcoDMS: Keine Verbindung zum ecoDMS Server möglich. Proxy ist erreichbar.
Der ecoDMS API Dienst scheint aus, blockiert oder defekt zu sein!
Proxy meldet Staus: 502 Bad Gateway
Prüfen Sie in den ecoDMS Einstellungen > API ZugriffEcoDMS Sever meldet:
502 Bad Gateway

2024-05-14 11:27:46,162 - CRITICAL -  Ein Fehler bim Verbinden mit ecoDMS ist aufgetreten. Prüfen Sie das Log.
``` 
![Fehlermeldung](img/Verbindungsfehler3.png)


## Erklärung

Das arkivado Tool versucht sich mit ecoDMS zu verbinden und stellt dabei fest, dass die ecoDMS Api nicht erreichbar ist.
Ein (Reverse) Proxy antwortet aber unter der Adresse, kann die Anfrage aber nicht weiter an ecoDMS geben. 


Dies passiert immer dann, wenn der Api Dienst von ecoDMS aus oder defekt ist. 


## Lösung 

Prüfen Sie in ecoDMS ob der Api Dienst an und erreichbar ist. 
Der Fehler liegt in ecoDMS oder an der Webserver konfiguration des Servers, nicht beim Tool. 

siehe auch [Voraussetzungen](<../../1. Einleitung/001voraussetzungen.md>)
