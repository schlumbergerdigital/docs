# Zertifikatsfehler im Logfile


## Problembeschreibung

- Das Tool startet 
- Beim Klick auf eine Taste steht im Log ein Fehler

``` title="Zertifikatsfehler im Log"
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain 
```
- Es passiert sonst nichts

## Erklärung

Das Arkivado Tool versucht sich mit ecoDMS zu verbinden, stellt dabei fest, dass die Verbindung nicht mit einem gültigen Zertifikat versehen ist. 

Dies gehschieht immer dann wenn Sie in ecoDMS *Vom System selbst siginiertes Zertifikat verwenden* ausgewählt haben
![selbstsiginirtes Zertifikat in ecoDMS](<img/ecoDMS selbstsiginiertes Zertifikat.png>)


## Lösung 

Deaktiveren Sie die Zertifikatsprüfung in der config Datei.

```  json  title="EXTF Dokumentlisten Export"
    "ecodms": {
        "ECODMSurl": "https://dmsentwicklung.docarchivdemo.net:8180/api/",
        "ECODMSuser": "ecodms",
        "ECODMSpw": null,
        "ECODMSabort_on_ssl_error": false,  //# (1)!
        "export_to": "excel",
        "export_path": "C:\\ecoDMS Daten\\Export_ecoDMS",
        "export_open": true,
        "DateField":"Belegdatum",
...
```

1. ändern Sie den Wert von ```true``` auf ```false```


!!! danger "Nur lokal"
    Die Änderung sollten höchsten bei lokale Installationen durchgeührt werden, in Cloud/Web Umgebungen defintiv nicht!

siehe auch: [hier](<../3. Konfiguration/002config_general.md>)