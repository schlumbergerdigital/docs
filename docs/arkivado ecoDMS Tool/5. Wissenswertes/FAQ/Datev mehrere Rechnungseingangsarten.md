
# DATEV: mehrere Rechnungseingangsarten

## Problembeschreibung

Sie haben mehrere Dokumentarten, die alle dem Rechnungseingang entsprechen.  
Nehmen wir an, wir haben zwei Eingangsrechnungsarten:

- Rechnungseingang
- Rechnungen

zudem haben wir 2 Ausgangsrechnungsarten:

- Rechnungsausang
- Teil-Rechnungen

## Lösung

Dies ist möglich: Sie können mehrere Dokumentarten zusammenfassen.

### Konfigurieren

Allgemein finden Sie [hier](../../3. Konfiguration/005config_datevexport.md) alle Optionen des DATEV-Exports beschrieben.

Sie müssen die Dokumentarten an zwei Orten hinterlegen:

#### Exportordner angeben

Unter `paths` werden die Dokumentarten sowie der Zielordner, in dem die Datei abgelegt wird, angegeben.  
Der Pfad kann auch derselbe sein.

``` JSON title="Konfiguration bzw. Zuweisung der Exportordner"
{
  "ecodms": {
    "paths": {
      "Rechnungseingang": "C:\\Datev\\Belegtransfer\\Rechnungseingang",
      "Rechnungen": "C:\\Datev\\Belegtransfer\\Rechnungseingang",
      "Rechnungsausang": "C:\\Datev\\Belegtransfer\\Rechnungsausgang",
      "Teil-Rechnungen": "C:\\Datev\\Belegtransfer\\Rechnungsausgang",
      "Sonstiges": "C:\\Daten\\lexoffice upload"
    }
  }
}
```

#### Rechnungsxml Klassifikation 

Zudem muss für den XML-Export noch angegeben werden, dass es sich um eine Eingangsrechnung handelt.

Hierfür wird der Schlüssel *RechnungseingangArt* bzw. *RechnungausgangArt* angepasst. Er wird um eckige Klammern ```[ ]``` erweitert, und die Dokumentarten werden aufgelistet.

``` JSON title="RechnungseingangArt erweitern"
{
  "datev": {
    "RechnungseingangArt": ["Rechnungseingang", "Rechnungen"]
  }
}
```


``` JSON title="RechnungausgangArt erweitern"
{
  "datev": {
    "RechnungausgangArt": ["Rechnungsausang", "Teil-Rechnungen"]
  }
}
```
