# Zertifikatsfehler


## Problembeschreibung

- Das Tool startet 
- Beim Klick auf eine Taste kommt eine Fehlermeldung

``` title="Zertifikatsfehler im Log"
CRITICAL - Konnte ecoDMS Verbindung nicht starten: Zertifikatsfehler vom Server https://beispiel.docarchivdemo.net:8181/api/
Fehler verursacht durch selbstsigniertes Zertifikat in ecoDMS.
Tipp: Setzen Sie ECODMSabort_on_ssl_error auf false.
Siehe auch docs.arkivado.digital
![Fehlermeldung](<img/arkivado Fehlermeldung.png>)



## Erklärung

Das Arkivado Tool versucht sich mit ecoDMS zu verbinden und stellt dabei fest, dass die Verbindung nicht mit einem gültigen Zertifikat versehen ist. 

Dies passiert immer dann, wenn Sie in ecoDMS *Vom System selbst siginiertes Zertifikat verwenden* ausgewählt haben
![Selbstsigniertes Zertifikat in ecoDMS](<img/ecoDMS selbstsiginiertes Zertifikat.png>)


## Lösung 

Deaktivieren Sie die Zertifikatsprüfung in der Konfigurationsdatei (params.json).

```  json  title="EXTF Dokumentlisten Export"
    "ecodms": {
        "ECODMSurl": "https://beispiel.docarchivdemo.net:8180/api/",
        "ECODMSuser": "ecodms",
        "ECODMSpw": null,
        "ECODMSabort_on_ssl_error": false,  //# (1)!
        "export_to": "excel",
        "export_path": "C:\\ecoDMS Daten\\Export_ecoDMS",
        "export_open": true,
        "DateField":"Belegdatum",
...
```

1. Ändern Sie den Wert von ```true``` auf ```false```


!!! danger "Nur lokal"
        Die Änderung sollte höchstens bei lokalen Installationen durchgeführt werden, in Cloud/Web-Umgebungen definitiv nicht!


siehe auch: [Generelle Einstellungen](<../3. Konfiguration/002config_general.md>)