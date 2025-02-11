# Datums Berechnung

Es können im Arkivado Tool auch aufwendige Bedingungen hinterlegt werden.

!!! tip "Profi Anleitung" 
    Diese Anleitung richtet sich an IT Profis!
    Holen Sie sich im Zweifel Support von Ihrem Systemhaus. 

## Problembeschreibung

- Ein Header in einer CSV soll abhängig vom Belegdatum und dem heutigen Datum ein Datum ausgeben
- Das Datum soll heute sein, wenn kein Datum übergeben
- Das Datum soll auf dem auf den 31.12. dieses Jahres fallen, wenn das Belegdatum *nicht* diesem Jahr entspricht
- Das Datum soll das Belegdatum sein, wenn das Jahr des Beleges dem diesem Jahr entspricht.


## Lösung 

Die Berechnung funtkionier natürlich nur, wenn es nur 1 Beleg gibt. 

Daher muss pro Beleg eine Datei ausgegeben werden

``` JSON title="Konfiguration der csv Exportdatei:"
      "MultiFiles" : true
```

Die eigentliche Berechnung wird im Header hinterlegt 

``` JSON title="Konfiguration der csv Exportdatei:"
   "Header": [
        [
          "{datetime.now().strftime('%Y%m%d') if str(data['Belegdatum']) == ''  else str(data['Belegdatum'].year)+'1231' if data['Belegdatum'].year != datetime.now().year else  data['Belegdatum'].strftime('%Y%m%d')}"
        ]
       
      ]
```

### Erläuterung


- Spalten die in ```{ }``` stehen, werden berrechnet. 


#### Heute Wenn kein Datum angegeben


Der Erste Teil ist das heutige Datum, wenn nicht übergben wurde
  
``` python title="Heute Wenn kein Datum"
datetime.now().strftime('%Y%m%d') if str(data['Belegdatum']) == '' 
```


``` python title="Heutiges Datum"
datetime.now().strftime('%Y%m%d') 
```

gibt den heuten Tag im Format YYYYMMDD aus. 

``` python title="Eingränzen auf leeres Belegdatum"
if str(data['Belegdatum']) == '' 
```

schränkt die Ausgabe ein, nur wenn das ecoDMS Attribut *Belegdatum* leer ist, wird das heutige Datum ausgegebn.

``` python title="Auf das Belegdatum zugreifen"
data['Belegdatum']
```

spricht das Attribut von ecoDMS  mit dem Name *Belegdatum* an. 


#### 31.12 Wenn Belegdatum von anderem Jahr 


``` python title="31.12. vom Belegdatum"
else str(data['Belegdatum'].year)+'1231' 
```

gibt an, dass wenn ein Belegdatum vorhanden ist, gib das Jahr des Belegdatums aus und setze es auf den 31.12. also für ein Dokument von 15.02.2016 wäre es 20161231 

``` python title="Nur das Jahr von einem Datum"
data['Belegdatum'].year
```

Gibt nur das Jahr eines Datums zurück. Möglich ist auch .month .day

!!! warning "Leere Datumsangaben davor abfrangen"
  Mit dem ```if str(data['Belegdatum']) == ''``` sorgen wir dafür dass defintiv ein echtes Datum im Attribut angegeben ist. 

 
#### 31.12 Wenn Belegdatum von anderem Jahr 
Die Ausgabe vom 31.12. wird ebenfalls eingegränzt: 
Nur wenn das Jahr des Belgdatums nicht mit dem aktuellen Jahr des Server entspricht. 

``` python title="Prüft ob Beleg Jahr gleich dieses Jahr"
  if data['Belegdatum'].year != datetime.now().year
```

``` python title="Das heute Jahr"
datetime.now().year
``` 

datetime.now() gibt heute zurück. 


## Normalfall: Ausgbabe des Belegdatums 

zum schluss noch der *normalfall*, Ausgabe des Belegdatums im Format YYYMMDD.

``` python title="Prüft ob Beleg Jahr gleich dieses Jahr"
 else  data['Belegdatum'].strftime('%Y%m%d')
``` 

