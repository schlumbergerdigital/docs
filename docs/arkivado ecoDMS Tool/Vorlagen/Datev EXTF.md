# Datev EXTF Export


Im Datev Buchunstapel Export müssen diverse Felder angegeben und einfügt werden.
Die Beschreibung des Formats finden Sie [hier](https://developer.datev.de/datev/platform/de/dtvf/formate/buchungsstapel){:target="_blank"}
## Exportart

Im Arkivado ecoDMS Tool wird der *Dokumentliste Export* verwendet. Das EXTF Format kennt keine Übergabe von Dokumenten. 
Es werden nur die Metadaten aus ecoDMS übergben. 




## Header 

Der Header einer 


```  json  title="EXTF Header"
"Header":[
                [
                "EXTF",
                "700",
                "21",
                "Buchungsstapel",
                "13",
                "<@date(now,%Y%m%d%H%M%S000)>",
                "",
                "RE",
                "",
                "<@user()>", //# (1)!
                "", 
                "123456",//# (2)!
                "1", //# (3)!,
                "<date(now,%Y)>0101", //# (4)!,
                "<@min(Belegdatum)>",
                "<@max(Belegdatum)>",
                "Rechnungsspapel vom <@date(now,%Y-%m-%d%)>",
                "AE",
                "1",
                "0",
                "0", //# (5)!,
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

1.  Hier wird der ecoMDS User als Export User angegegeben. Es kann auch ein biliger starrer Name eingetragen werden.
2.  Ihre Beraternummer
3.  Ihre Manantennummer 
4.  Der Beginn des Wirtschaftsjahres = Standardmäßig der 01.01.DIESE JAHRES
5.  Ob der Stapel gleich festgeschieben wird oder nicht. 0 = keine Festschreibung 1 = Festschreibung
6.  


Die Spalten sind nun die 
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