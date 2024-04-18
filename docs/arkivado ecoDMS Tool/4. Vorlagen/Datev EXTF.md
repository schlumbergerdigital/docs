# Datev EXTF Export


Im Datev Buchunstapel Export müssen diverse Felder angegeben und einfügt werden.
Die Beschreibung des Formats finden Sie [hier](https://developer.datev.de/datev/platform/de/dtvf/formate/buchungsstapel){:target="_blank"}


## Abschnitt CSV

Die CSV Optionen geben an in welchem Format die Datev Daten geliefert werden.
Die Einstellungen können so übernommen werden 

```  json  title="EXTF cvs Einstellungen"
"csv": {
            "newline": "\r\n",
            "encoding": "ISO-8859-1",
            "seperator": ";",
            "quotechar": "\"",
            "quote": "minimal",
            "number_round":2,
            "number_format":","
        },

```

## Abschnitt Dokumentlisten Export

Im Arkivado ecoDMS Tool wird der *Dokumentliste Export* verwendet. Das EXTF Format kennt keine Übergabe von Dokumenten. 
Es werden nur die Metadaten aus ecoDMS übergben. 


```  json  title="EXTF Dokumentlisten Export"
"Dokumentliste Export": {
        "export_to": "csv",
        "PfadListe": "C:\\eco_liste\\EXTF_Buchungsstapel.csv", //# (1)!
        "PfadListeReplace": false, //# (2)!
        "numbers": [ //# (3)!
            "Brutto Betrag",
            "Umsatz (ohne Soll/Haben-Kz)"
        ],
        "dates": [ //# (4)!
            "Belegdatum"
        ],
        "ToExportField": {
            "field": "StB Export",  //# (5)!
                "value": "2"
            },
        "IsExportedField": {
            "field": "StB exportiert", //# (6)!
                "value": "2"
            },
        "TimeFilter": false, //# (7)!
        "DateField": "Belegdatum", //# (8)!

        ...
```

1. Wohin wird die Datei gelegt
2. Soll die bestehende Datei überschieben werden oder eine weitere Datei angelegt werden ```true``` = überschreiben ```false``` = eine weitere anlegen 
3. Alle Zahlen die vorkommen, sowohl wie Sie in ecoDMS genannt werden oder wenn Sie in einem Spalten Mapping genannt werden 
4. Alle Datumsangaben die vorkommen, sowohl wie Sie in ecoDMS genannt werden oder wenn Sie in einem Spalten Mapping genannt werden 
5. Der Name der Spalte die angibgt das das Dokument zu bearbeiten ist
6. Der Name der Spalte die angibgt, dass das Dokumente bereits bearbeit worden ist. 
7. Gibt an ob das Datum in der Oberfläche berücksichtigt wird oder nicht. Wichtig: für automatische Exports IMMER false!
8. Wenn der Time Filter aktiv ist  wird dieses Feld abgefragt. Ist nichts angegeben wird Datum verwendet

### Abschnitt Header 

in der Spalte Header wird die Kopfzeile des Exportes bestimmt. 



```  json  title="EXTF Header"
"Header":[
                [
                "EXTF",
                "700",
                "21",
                "Buchungsstapel",
                "13",
                "<@date(now,%Y%m%d%H%M%S)>000",
                "",
                "RE",
                "",
                "<@user()>", //# (1)!
                "", 
                "123456",//# (2)!
                "1", //# (3)!,
                "<date(now,%Y)>0101", //# (4)!,
                "<@min(Belegdatum,%Y%m%d)>",
                "<@max(Belegdatum,%Y%m%d)>",
                "Rechnungsspapel vom <@date(now,%Y-%m-%d%)>",
                "AE",
                "1",
                "0",
                "1", //# (5)!,
                "EUR",
                "",
                "",
                "",
                "",
                "",
                ""
            ]
]
```

1.  Hier wird der ecoMDS User als exportierender User übergeben. Es kann auch ein beliebiger fester Name eingetragen werden.
2.  Ihre Beraternummer
3.  Ihre Mandantennummer 
4.  Der Beginn des Wirtschaftsjahres = Standardmäßig der 01.01.DIESE JAHRES
5.  Ob der Stapel gleich festgeschrieben wird oder nicht. 0 = keine Festschreibung 1 = Festschreibung



Die Spalten sind nun die konkreten Werte die übergeben werden
```  json  title="EXTF Spalten"
"Spalten": [
     {"Umsatz (ohne Soll/Haben-Kz)": "<Brutto Betrag>"} //# (1)!
    ,{"Soll/Haben-Kennzeichen": "S"}
    ,{"WKZ Umsatz": "EUR"}
    ,{"Kurs": ""}
    ,{"Basis-Umsatz": ""}
    ,{"WKZ Basis-Umsatz": ""}
    ,{"Konto": "1234" } //# (2)!
    ,{"Gegenkonto (ohne BU-Schl\u00FCssel)": ""} //# (3)!
    ,{"BU-Schl\u00FCssel": ""} //# (4)!
    ,{"Belegdatum": "<@date(Belegdatum,%d%m)>"} //# (5)!
    ,{"Belegfeld 1": "<Nummer>"} //# (6)!
    ,{"Belegfeld 2": ""}
    ,{"Skonto": ""}
    ,{"Buchungstext": ""} //# (7)!
    ,{"Postensperre": ""}
    ,{"Diverse Adressnummer": ""}
    ,{"Gesch\u00E4ftspartnerbank": ""}
    ,{"Sachverhalt": ""}
    ,{"Zinssperre": ""}
    ,{"Beleglink": "http://localhost:17003/openDoc?openmode=1&docid=<docid>&archive=1&host=<@ecodmsserver()>&port=17001"} //# (8)!
    ,{"Beleginfo - Art 1": ""}
    ,{"Beleginfo - Inhalt 1": ""}
    ,{"Beleginfo - Art 2": ""}
    ,{"Beleginfo - Inhalt 2": ""}
    ,{"Beleginfo - Art 3": ""}
    ,{"Beleginfo - Inhalt 3": ""}
    ,{"Beleginfo - Art 4": ""}
    ,{"Beleginfo - Inhalt 4": ""}
    ,{"Beleginfo - Art 5": ""}
    ,{"Beleginfo - Inhalt 5": ""}
    ,{"Beleginfo - Art 6": ""}
    ,{"Beleginfo - Inhalt 6": ""}
    ,{"Beleginfo - Art 7": ""}
    ,{"Beleginfo - Inhalt 7": ""}
    ,{"Beleginfo - Art 8": ""}
    ,{"Beleginfo - Inhalt 8": ""}
    ,{"KOST1 - Kostenstelle": ""}
    ,{"KOST2 - Kostenstelle": ""}
    ,{"Kost-Menge": ""}
    ,{"EU-Land u. UStID (Bestimmung)": ""}
    ,{"EU-Steuersatz (Bestimmung)": ""}
    ,{"Abw. Versteuerungsart": ""}
    ,{"Sachverhalt L+L": ""}
    ,{"Funktionserg\u00E4nzung L+L": ""}
    ,{"BU 49 Hauptfunktionstyp": ""}
    ,{"BU 49 Hauptfunktionsnummer": ""}
    ,{"BU 49 Funktionserg\u00E4nzung": ""}
    ,{"Zusatzinformation - Art 1": ""}
    ,{"Zusatzinformation- Inhalt 1": ""}
    ,{"Zusatzinformation - Art 2": ""}
    ,{"Zusatzinformation- Inhalt 2": ""}
    ,{"Zusatzinformation - Art 3": ""}
    ,{"Zusatzinformation- Inhalt 3": ""}
    ,{"Zusatzinformation - Art 4": ""}
    ,{"Zusatzinformation- Inhalt 4": ""}
    ,{"Zusatzinformation - Art 5": ""}
    ,{"Zusatzinformation- Inhalt 5": ""}
    ,{"Zusatzinformation - Art 6": ""}
    ,{"Zusatzinformation- Inhalt 6": ""}
    ,{"Zusatzinformation - Art 7": ""}
    ,{"Zusatzinformation- Inhalt 7": ""}
    ,{"Zusatzinformation - Art 8": ""}
    ,{"Zusatzinformation- Inhalt 8": ""}
    ,{"Zusatzinformation - Art 9": ""}
    ,{"Zusatzinformation- Inhalt 9": ""}
    ,{"Zusatzinformation - Art 10": ""}
    ,{"Zusatzinformation- Inhalt 10": ""}
    ,{"Zusatzinformation - Art 11": ""}
    ,{"Zusatzinformation- Inhalt 11": ""}
    ,{"Zusatzinformation - Art 12": ""}
    ,{"Zusatzinformation- Inhalt 12": ""}
    ,{"Zusatzinformation - Art 13": ""}
    ,{"Zusatzinformation- Inhalt 13": ""}
    ,{"Zusatzinformation - Art 14": ""}
    ,{"Zusatzinformation- Inhalt 14": ""}
    ,{"Zusatzinformation - Art 15": ""}
    ,{"Zusatzinformation- Inhalt 15": ""}
    ,{"Zusatzinformation - Art 16": ""}
    ,{"Zusatzinformation- Inhalt 16": ""}
    ,{"Zusatzinformation - Art 17": ""}
    ,{"Zusatzinformation- Inhalt 17": ""}
    ,{"Zusatzinformation - Art 18": ""}
    ,{"Zusatzinformation- Inhalt 18": ""}
    ,{"Zusatzinformation - Art 19": ""}
    ,{"Zusatzinformation- Inhalt 19": ""}
    ,{"Zusatzinformation - Art 20": ""}
    ,{"Zusatzinformation- Inhalt 20": ""}
    ,{"St\u00FCck": ""}
    ,{"Gewicht": ""}
    ,{"Zahlweise": ""}
    ,{"Forderungsart": ""}
    ,{"Veranlagungsjahr": ""}
    ,{"Zugeordnete F\u00E4lligkeit": ""}
    ,{"Skontotyp": ""}
    ,{"Auftragsnummer": ""}
    ,{"Buchungstyp (Anzahlungen)": ""}
    ,{"USt-Schl\u00FCssel (Anzahlungen)": ""}
    ,{"EU-Land (Anzahlungen)": ""}
    ,{"Sachverhalt L+L (Anzahlungen)": ""}
    ,{"EU-Steuersatz (Anzahlungen)": ""}
    ,{"Erl\u00F6skonto (Anzahlungen)": ""}
    ,{"Herkunft-Kz": ""}
    ,{"Buchungs GUID": ""}
    ,{"KOST-Datum": ""}
    ,{"SEPA-Mandatsreferenz": ""}
    ,{"Skontosperre": ""}
    ,{"Gesellschaftername": ""}
    ,{"Beteiligtennummer": ""}
    ,{"Identifikationsnummer": ""}
    ,{"Zeichnernummer": ""}
    ,{"Postensperre bis": ""}
    ,{"Bezeichnung SoBil-Sachverhalt": ""}
    ,{"Kennzeichen SoBil-Buchung": ""}
    ,{"Festschreibung": "1"} //# (9)!
    ,{"Leistungsdatum": ""}
    ,{"Datum Zuord. Steuerperiode": ""}
    ,{"F\u00E4lligkeit": ""}
    ,{"Generalumkehr (GU)": ""}
    ,{"Steuersatz": ""}
    ,{"Land": ""}
    ,{"Abrechnungsreferenz": ""}
    ,{"BVV-Position": ""}
    ,{"EU-Land u. UStID (Ursprung)": ""}
    ,{"EU-Steuersatz (Ursprung)": ""}
    ,{"Abw. Skontokonto": ""}
    ,{"Besteuerungsart Leistender": ""}
]
```

1. Das Feld mit dem Bruttobetrag
2. Das Sach- oder Personenkonto auf das gebucht werden soll. Entweder ein EcoDMS Feld oder Sammelkonto
3. Das Konto gegen das gebucht werden soll. Entweder ein EcoDMS Feld oder Sammelkonto
4. Buchungs Schlüssel der Datev siehe hier: [Datev Buchungsschlüssel](https://apps.datev.de/help-center/documents/1002086){:target="_blank"}
5. Das Belegdatum darf nur Tag und Monat enthalten 
6. Belegnummer
7. Der Buchungstext in der Datev
8. Beleglink: Link auf ecoDMS um direkt aus dem System in das DMS zu springen. Für die einstellung hier: In ecoDMS unter *Einstellungen > Allgemein > Links* auf ```HTTP Hyperlinks verwenden``` stellen
9. Ob der Datensatz festgeschreiben werden soll



## Abschnitt GUI

um lediglich einen Knopf im System zu sehen folgende GUI koniguration verwenden.


```  json  title="EXTF Spalten"

"buttons": [
         {
             "funktion": "Dokument Export",
             "text": "Dokument Export",
             "show": false
         },
         {
             "funktion": "Dokumentliste Export",
             "text": "Buchungsstapel Export", // # (1)!
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

```

1. Hier den Text für die Endanwender anpassen


## Kopiervorlage
``` json  title="EXTF Komplett"
{
    "ecodms": {
        "ECODMSurl": "https://meinserver.docarchivdemo.net:8180/api/",
        "ECODMSuser": "MEIN BENUTZERNAME",
        "ECODMSpw": null,
        "ECODMSabort_on_ssl_error": true,
        "export_to": "csv",
        "export_path": "C:\\ecoDMS Daten\\Export_ecoDMS",
        "export_open": false,
        "paths": {
            "Sonstiges": "C:\\ecoDMS Daten\\Export_ecoDMS\\DATEV\\Sonstige",
        },
        "csv": {
            "newline": "\r\n",
            "encoding": " ISO-8859-1",
            "seperator": ";",
            "quotechar": "\"",
            "quote": "minimal",
            "number_round":2,
            "number_format":","
        },
        "Dokumentliste Export": {
            "TimeFilter": false,
            "export_to": "csv",
            "PfadListe": "C:\\ecoDMS Daten\\Export_ecoDMS\\EXTF_Buchungsstapel.csv",
            "PfadListeReplace": true,
            "numbers": [
                "Brutto Betrag",
                "Umsatz (ohne Soll/Haben-Kz)"
            ],
            "dates": [
                "Belegdatum",
                "Datum"
            ],
            "Header":[
                        [
                        "EXTF",
                        "700",
                        "21",
                        "Buchungsstapel",
                        "13",
                        "<@date(now,%Y%m%d%H%M%S)>000",
                        "",
                        "RE",
                        "",
                        "<@user()>", 
                        "", 
                        "123456",
                        "1", 
                        "<date(now,%Y)>0101", 
                        "<@min(Belegdatum,%Y%m%d)>",
                        "<@max(Belegdatum,%Y%m%d)>",
                        "Rechnungsspapel vom <@date(now,%Y-%m-%d%)>",
                        "AE",
                        "1",
                        "0",
                        "1", 
                        "EUR",
                        "",
                        "",
                        "",
                        "",
                        "",
                        ""
                       ]
            ],
        "Spalten": [
             {"Umsatz (ohne Soll/Haben-Kz)": "<Brutto Betrag>"} 
            ,{"Soll/Haben-Kennzeichen": "S"}
            ,{"WKZ Umsatz": "EUR"}
            ,{"Kurs": ""}
            ,{"Basis-Umsatz": ""}
            ,{"WKZ Basis-Umsatz": ""}
            ,{"Konto": "1234" } 
            ,{"Gegenkonto (ohne BU-Schl\u00FCssel)": ""} 
            ,{"BU-Schl\u00FCssel": ""} 
            ,{"Belegdatum": "<@date(Belegdatum,%d%m)>"} 
            ,{"Belegfeld 1": "<Nummer>"} 
            ,{"Belegfeld 2": ""}
            ,{"Skonto": ""}
            ,{"Buchungstext": ""} 
            ,{"Postensperre": ""}
            ,{"Diverse Adressnummer": ""}
            ,{"Gesch\u00E4ftspartnerbank": ""}
            ,{"Sachverhalt": ""}
            ,{"Zinssperre": ""}
            ,{"Beleglink": "http://localhost:17003/openDoc?openmode=1&docid=<docid>&archive=1&host=<@ecodmsserver()>&port=17001"} 
            ,{"Beleginfo - Art 1": ""}
            ,{"Beleginfo - Inhalt 1": ""}
            ,{"Beleginfo - Art 2": ""}
            ,{"Beleginfo - Inhalt 2": ""}
            ,{"Beleginfo - Art 3": ""}
            ,{"Beleginfo - Inhalt 3": ""}
            ,{"Beleginfo - Art 4": ""}
            ,{"Beleginfo - Inhalt 4": ""}
            ,{"Beleginfo - Art 5": ""}
            ,{"Beleginfo - Inhalt 5": ""}
            ,{"Beleginfo - Art 6": ""}
            ,{"Beleginfo - Inhalt 6": ""}
            ,{"Beleginfo - Art 7": ""}
            ,{"Beleginfo - Inhalt 7": ""}
            ,{"Beleginfo - Art 8": ""}
            ,{"Beleginfo - Inhalt 8": ""}
            ,{"KOST1 - Kostenstelle": ""}
            ,{"KOST2 - Kostenstelle": ""}
            ,{"Kost-Menge": ""}
            ,{"EU-Land u. UStID (Bestimmung)": ""}
            ,{"EU-Steuersatz (Bestimmung)": ""}
            ,{"Abw. Versteuerungsart": ""}
            ,{"Sachverhalt L+L": ""}
            ,{"Funktionserg\u00E4nzung L+L": ""}
            ,{"BU 49 Hauptfunktionstyp": ""}
            ,{"BU 49 Hauptfunktionsnummer": ""}
            ,{"BU 49 Funktionserg\u00E4nzung": ""}
            ,{"Zusatzinformation - Art 1": ""}
            ,{"Zusatzinformation- Inhalt 1": ""}
            ,{"Zusatzinformation - Art 2": ""}
            ,{"Zusatzinformation- Inhalt 2": ""}
            ,{"Zusatzinformation - Art 3": ""}
            ,{"Zusatzinformation- Inhalt 3": ""}
            ,{"Zusatzinformation - Art 4": ""}
            ,{"Zusatzinformation- Inhalt 4": ""}
            ,{"Zusatzinformation - Art 5": ""}
            ,{"Zusatzinformation- Inhalt 5": ""}
            ,{"Zusatzinformation - Art 6": ""}
            ,{"Zusatzinformation- Inhalt 6": ""}
            ,{"Zusatzinformation - Art 7": ""}
            ,{"Zusatzinformation- Inhalt 7": ""}
            ,{"Zusatzinformation - Art 8": ""}
            ,{"Zusatzinformation- Inhalt 8": ""}
            ,{"Zusatzinformation - Art 9": ""}
            ,{"Zusatzinformation- Inhalt 9": ""}
            ,{"Zusatzinformation - Art 10": ""}
            ,{"Zusatzinformation- Inhalt 10": ""}
            ,{"Zusatzinformation - Art 11": ""}
            ,{"Zusatzinformation- Inhalt 11": ""}
            ,{"Zusatzinformation - Art 12": ""}
            ,{"Zusatzinformation- Inhalt 12": ""}
            ,{"Zusatzinformation - Art 13": ""}
            ,{"Zusatzinformation- Inhalt 13": ""}
            ,{"Zusatzinformation - Art 14": ""}
            ,{"Zusatzinformation- Inhalt 14": ""}
            ,{"Zusatzinformation - Art 15": ""}
            ,{"Zusatzinformation- Inhalt 15": ""}
            ,{"Zusatzinformation - Art 16": ""}
            ,{"Zusatzinformation- Inhalt 16": ""}
            ,{"Zusatzinformation - Art 17": ""}
            ,{"Zusatzinformation- Inhalt 17": ""}
            ,{"Zusatzinformation - Art 18": ""}
            ,{"Zusatzinformation- Inhalt 18": ""}
            ,{"Zusatzinformation - Art 19": ""}
            ,{"Zusatzinformation- Inhalt 19": ""}
            ,{"Zusatzinformation - Art 20": ""}
            ,{"Zusatzinformation- Inhalt 20": ""}
            ,{"St\u00FCck": ""}
            ,{"Gewicht": ""}
            ,{"Zahlweise": ""}
            ,{"Forderungsart": ""}
            ,{"Veranlagungsjahr": ""}
            ,{"Zugeordnete F\u00E4lligkeit": ""}
            ,{"Skontotyp": ""}
            ,{"Auftragsnummer": ""}
            ,{"Buchungstyp (Anzahlungen)": ""}
            ,{"USt-Schl\u00FCssel (Anzahlungen)": ""}
            ,{"EU-Land (Anzahlungen)": ""}
            ,{"Sachverhalt L+L (Anzahlungen)": ""}
            ,{"EU-Steuersatz (Anzahlungen)": ""}
            ,{"Erl\u00F6skonto (Anzahlungen)": ""}
            ,{"Herkunft-Kz": ""}
            ,{"Buchungs GUID": ""}
            ,{"KOST-Datum": ""}
            ,{"SEPA-Mandatsreferenz": ""}
            ,{"Skontosperre": ""}
            ,{"Gesellschaftername": ""}
            ,{"Beteiligtennummer": ""}
            ,{"Identifikationsnummer": ""}
            ,{"Zeichnernummer": ""}
            ,{"Postensperre bis": ""}
            ,{"Bezeichnung SoBil-Sachverhalt": ""}
            ,{"Kennzeichen SoBil-Buchung": ""}
            ,{"Festschreibung": "1"} 
            ,{"Leistungsdatum": ""}
            ,{"Datum Zuord. Steuerperiode": ""}
            ,{"F\u00E4lligkeit": ""}
            ,{"Generalumkehr (GU)": ""}
            ,{"Steuersatz": ""}
            ,{"Land": ""}
            ,{"Abrechnungsreferenz": ""}
            ,{"BVV-Position": ""}
            ,{"EU-Land u. UStID (Ursprung)": ""}
            ,{"EU-Steuersatz (Ursprung)": ""}
            ,{"Abw. Skontokonto": ""}
            ,{"Besteuerungsart Leistender": ""}
        ],
       
        }
    },
    "gui": {
        "theme": "einhorn",
        "buttons": [
         {
             "funktion": "Dokument Export",
             "text": "Dokument Export",
             "show": false
         },
         {
             "funktion": "Dokumentliste Export",
             "text": "Buchungsstapel Export", 
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
    },
    "license": "MEINE LIZENZ"
}
```
