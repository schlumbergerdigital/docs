# Download: Erste Version vom Dokument herunterladen 


## Problembeschreibung
Standarmäßig wird immer die neuste Version von ecoDMS heruntergeladen. 
Manchmal soll aber die erste Version genommen werden. 
z.B. bei X-Rechnungen wird die XML (erste Version) benötigt, nicht die neuste (PDF Darstellung)



## Lösung
Damit abänig von einem ecoDMS Feld die Daten geändert werden, wird im passenden Abschnitt *version* hinzugefügt. 

über die Konfiguration kann gesteuert werden, welche Version unter welcher Bedingung exportiert wird. 

```JSON title="versionierung"
      "version" :{
          "field": "REformat", //# (1)!
          "value": "XRE" //# (2)!
      }, 

```

1. in EcoDMS wird das Feld reformat ausgelesen
2. Das Feld *refomat* muss den Wert "XRE" haben, dann wird die erste und nicht die neuste Version von dem Dokument ausgegeben.  


### Immer erste Version

```JSON title="versionierung"
      "version" :{
          "field": "<*>", 
          "value": "" 
      }, 

```

Wird ```<*>``` im field geschrieben, wird **immer** die erste Version genommen


