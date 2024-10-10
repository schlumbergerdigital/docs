# Excel Rechnungs übersicht


Um eine schöne Rechnungsübersicht zu bekommen kann folgende Konfigurations Vorlage genommen werden. 

![Rechnungsübersicht](<img/Rechnungsliste Export_endlos.gif>)

## Felder in ecoDMS

Die Namen sind unsere Vorschläge für ecoDMS. Es können auch andere Namen verwendet werden.   
Die Felder müssen dazu lediglich in der JSON angepasst werden.

| Opt. | Feld             | Typ              | Beschreibung                                                                                       |
| ---- | ---------------- | ---------------- | -------------------------------------------------------------------------------------------------- |
|      | Brutto Betrag    | Numerisches Feld | der Brutto Betrag der Rechnung                                                                     |
|      | Netto Betrag       | Numerisches Feld |       | der Netto Betrag der Rechnung                                                             |
|      | Nummer           | Freitext         | die Rechnungsnummer                                                                                |
|      | Belegdatum   | Datumsfeld| das Feld des Rechungsdatums|



## Abschnitt allgemein
```  json  title="Excel Export"
  "dates": [
      "Datum",
      "Belegdatum"
    ],//# (2)!
    "numbers": [
      "Brutto Betrag",
      "Netto Betrag"
    ],//# (1)!
```

1. Alle Zahlen die vorkommen, sowohl wie sie in ecoDMS genannt werden oder wenn sie in einem Spalten Mapping genannt werden 
2. Alle Datumsangaben die vorkommen, sowohl wie sie in ecoDMS genannt werden oder wenn sie in einem Spalten Mapping genannt werden 

## Abschnitt Dokumentlisten Export

Im Arkivado ecoDMS Tool wird der *Dokumentliste Export* verwendet. Es soll eine Excelliste ausgeben werden


```  json  title="EXTF Dokumentlisten Export"
"Dokumentliste Export": {
       "Filter": [
        {
          "classifyAttribut": "Dokumentenart",
          "searchOperator": "=",
          "searchValue": "Rechnungseingang" //# (5)!
        }
      ],
      "PfadListe": "C:\\Daten\\Daten\\ecoDMS Export\\Rechnungsliste.xlsx",  //# (1)!
      "PfadListeReplace": false, //# (2)!
      "DateField": "Belegdatum",//# (3)!
      "TimeFilter": true, //# (4)!
      "export_to": "excel" //# (6)!
      },
      "excel": {
        "do_format": true,
        "table_style": "TableStyleMedium2"  //# (7)!
      },
        ...
```

1. Wohin wird die Datei gelegt
2. Soll die bestehende Datei überschieben werden oder eine weitere Datei angelegt werden ```true``` = überschreiben ```false``` = eine weitere anlegen 
3. Wenn der Time Filter aktiv ist,  wird dieses Feld aus ecoDMS abgefragt. Ist nichts angegeben wird Datum verwendet
4. Gibt an, ob das Datum in der Oberfläche berücksichtigt wird oder nicht. 
5. Filter sodass nur Dokumente von der Dokumentart Rechnungseingang ausgegeben werden. 
6. Muss zwinged excel sein, sonst wird keine Excel Datei erstellt
7. Gibt den Tabellen Stiel aus mögliche Werte [hier](<../3. Konfiguration/008config_formatierung.md#excel-tabellen-formatierung>)

### Abschnitt Header 

In der Spalte Header wird die Kopfzeile des Exportes bestimmt. 



```  json  title="EXTF Header"
    "Header": [
        [
          "Rechnungsuebersicht" //# (1)!
        ],
        [
          "<@date(now,%d.%m.%Y)>" //# (2)!
        ],
        [
          "von Belegdatum",
          "<@min(Belegdatum,%d.%m.%Y)>" //# (3)!
        ],
        [
          "bis Belegdatum",
          "<@max(Belegdatum,%d.%m.%Y)>" //# (3)!
        ]
      ],
    ...

```

1. Die Überschift über der Tabelle
2. Das heutige Datum in Tag Monat Jahr 
3. Das erste Belegdatum in diesem Stapel
4. Das letzte Belegdatum in diesem Stapel




Die Spalten sind nun die konkreten Werte die übergeben werden
```  json  title="EXTF Spalten"
   "Spalten": [
        "<DocID>", 
        {
          "RE-Nummer": "<Nummer>" //# (1)!
        },
        "<Belegdatum>", //# (2)!
        "<Datum>", //# (3)!
        {
          "Lieferant": "<Name>" //# (4)!
        },
        "<Netto Betrag>", //# (5)!
        "<Brutto Betrag>", //# (6)! 
        {
          "Beleglink": "http://localhost:17003/openDoc?openmode=1&docid=<docid>&archive=1&host=<@ecodmsserver()>&port=17001" //# (7)!
        }
   ]
   ...
```

1. Belegnummer
2.  Das Belegdatum, wird nur Datum verwendet, kann die Zeile auch entfernt werden
3.  Das Standard Datum aus ecoDMS
4.  Das Feld Name aus ecoDMS, da der Filter nur Eingangsrechnungen ausgibt, ist es immer ein Lieferant
5.  Das Feld mit dem Nettobetrag
6.  Das Feld mit dem Bruttobetrag
7.  Beleglink: Link auf ecoDMS um direkt aus dem System in das DMS zu springen. Für die einstellung hier: In ecoDMS unter *Einstellungen > Allgemein > Links* auf ```HTTP Hyperlinks verwenden``` stellen

## Abschnitt GUI

Um lediglich einen Knopf im System zu sehen folgende GUI Konfiguration verwenden.


```  json  title="Rechnungs Spalten"
  "gui": {
    "theme": "hell",
    "buttons": [
      {
        "funktion": "Dokument Export",
        "text": "Dokument Export",
        "show": false
      },
      {
        "funktion": "Dokumentliste Export",
        "text": "Dokumentliste",  // # (1)!
        "show": true
      },
      {
        "funktion": "Datev Export",
        "text": "Datev Export",
        "show": false
      },
      {
        "funktion": "SEPA Export",
        "text": "SEPA Export",
        "show": false
      },
      {
        "funktion": "Dokumentliste Export",
        "text": "Liste komplett",
        "show": false
      },
      {
        "funktion": "Ordner Export",
        "text": "Ordner Export",
        "show": false
      },
      {
        "funktion": "Typen Export",
        "text": "Typen Export",
        "show": false
      }
    ]
  }
}

     ...


```

1. Hier den Text für die Endanwender anpassen


## Kopiervorlage

!!!warning 
    Überschreibt bestehende Konfiguration  

1. Kopieren sie den unteren Inhalt die JSON in die Datei
```
%appdata%\arkivado\ecodmstool\params.json
```
1. Starten Sie das Tool 
2. Drücken Sie strg + k um Ihre Zugangsdaten zu ecoDMS einzugeben siehe auch [hier](<../5. Wissenswertes/FAQ/EcoDMS Zugangangsdaten ändern.md>)
3. Starten Sie das Tool neu 
4. Fertig 
   

``` json  title="EXTF Komplett"
{
   {
  "ecodms": {
    "ECODMSurl": "https://MEIN SERVER:8180/api/",
    "ECODMSuser": "MEIN BENUTZERNAME",
    "ECODMSpw": null,
    "ECODMSabort_on_ssl_error": true,
    "export_to": "csv",
    "export_path": "C:\\ecoDMS Daten\\Export_ecoDMS",
    "export_open": true,
    "paths": {
      "Sonstiges": "C:\\Daten\\Daten\\ecoDMS Export\\Sonstiges"
    },
    "dates": [
      "Datum",
      "Belegdatum"
    ],
    "numbers": [
      "Brutto Betrag",
      "Netto Betrag"
    ],
    "datev": {
      "ToExportField": {
        "field": "Datev Export",
        "value": "2"
      },
      "IsExportedField": {
        "field": "DATEV Export erfolgt",
        "value": "2"
      },
      "ExportDate": "Datev Export Datum",
      "DateField": "Belegdatum",
      "TypeField": "Dokumentenart",
      "FileName": [
        "<Datum>",
        "-",
        "<Bemerkung>",
        "-",
        "<DocID>"
      ],
      "RechnungseingangArt": "Rechnungseingang",
      "RechnungausgangArt": "Rechnungausgang",
      "Bemerkung": "Bemerkung",
      "FileAttributeMaxLength": 50,
      "InvoiceNumberField": "Belegnummer",
      "TaxField": "Steuer",
      "DefaultTax": "19.00",
      "SupplierName": "Name",
      "SupplierCity": "Stadt",
      "DueDate": "Zahlungsziel",
      "Info": "Bemerkung",
      "VatID": "USTId",
      "IBAN": "IBAN",
      "Total": "Brutto",
      "ExportPath": "C:\\Datev\\Belegtransfere",
      "ExportArt": 1
    },
    "sepa": {
      "mybanks": {
        "default": {
          "Name": "Max Mustermann",
          "IBAN": "DE12344",
          "BIC": "JE3"
        }
      },
      "ExportPath": "C:\\export\\meineSepaxml.xml",
      "currency": "EUR",
      "schema": "pain.001.003.03",
      "ToExportField": {
        "field": "SEPA Export",
        "value": "2"
      },
      "IsExportedField": {
        "field": "SEPA Export erfolgt",
        "value": "2"
      },
      "Name": "Name",
      "Total": "Brutto",
      "IBAN": "IBAN",
      "BIC": "BIC",
      "DueDate": "Zahlungsziel",
      "Verwendungszweck": "Bemerkung",
      "DateField": "Datum",
      "SetExecutionDateToToday": false,
      "SetValidExecutionDate": true
    },
    "Dokumentliste Export": {
      "Filter": [
        {
          "classifyAttribut": "docid",
          "searchOperator": ">",
          "searchValue": "0"
        },
        {
          "classifyAttribut": "Dokumentenart",
          "searchOperator": "=",
          "searchValue": "Rechnungseingang"
        }
      ],
      "PfadListe": "C:\\Daten\\Daten\\ecoDMS Export\\Rechnungsliste.xlsx",
      "PfadListeReplace": false,
      "DateField": "Belegdatum",
      "TimeFilter": true,
      "Spalten": [
        "<DocID>",
        {
          "RE-Nummer": "<Nummer>"
        },
        "<Belegdatum>",
        "<Datum>",
        {
          "Lieferant": "<Name>"
        },
        "<Netto Betrag>",
        "<Brutto Betrag>",
        {
          "Beleglink": "http://localhost:17003/openDoc?openmode=1&docid=<docid>&archive=1&host=<@ecodmsserver()>&port=17001"
        }
      ],
      "Header": [
        [
          "Rechnungsuebersicht"
        ],
        [
          "<@date(now,%d.%m.%Y)>"
        ],
        [
          "von Belegdatum",
          "<@min(Belegdatum,%d.%m.%Y)>"
        ],
        [
          "bis Belegdatum",
          "<@max(Belegdatum,%d.%m.%Y)>"
        ]
      ],
      "export_to": "excel"
    },
    "excel": {
      "do_format": true,
      "table_style": "TableStyleMedium2"
    },
  },
  "license": "MEINE LIZENZ",
  "gui": {
    "theme": "hell",
    "buttons": [
      {
        "funktion": "Dokument Export",
        "text": "Dokument Export",
        "show": false
      },
      {
        "funktion": "Dokumentliste Export",
        "text": "Dokumentliste",
        "show": true
      },
      {
        "funktion": "Datev Export",
        "text": "Datev Export",
        "show": false
      },
      {
        "funktion": "SEPA Export",
        "text": "SEPA Export",
        "show": false
      },
      {
        "funktion": "Dokumentliste Export",
        "text": "Liste komplett",
        "show": false
      },
      {
        "funktion": "Ordner Export",
        "text": "Ordner Export",
        "show": false
      },
      {
        "funktion": "Typen Export",
        "text": "Typen Export",
        "show": false
      }
    ]
  }
}
```
