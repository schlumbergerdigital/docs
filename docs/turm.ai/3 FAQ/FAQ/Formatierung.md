# Cast Type


oftmals ist es wichtig die Datentypen im Turm in einen anderen Datentyp umzuwandeln. 
Vor allem wenn der Werte filtern will. Siehe [hier](Filtern.md)

| Beispiel                                     | Bedeutung                                                    | Ergebnis              |
| -------------------------------------------- | ------------------------------------------------------------ | --------------------- |
| ```'2022-09-02'::date ```                    | Gibt den Ihnalt als Datum wieder                             | ```2022-09-02```      |
| ```'2022-09-02'::date + INTERVAL '1 DAY' ``` | Gibt den Ihnalt als Datum wieder und addiert einen Tag drauf | ```2022-09-03```      |
| ```'2022-01-01 23:30+10'::timestamp ```      | Gibt den Ihnalt als Datum mit Zeitangabe wieder              | '2022-01-01 00:00+10' |
| ```'2022-01-01 23:30+10'::time ```           | Gibt den Ihnalt als Zeitangabe wieder                        | ```23:30```           |
| ```'1.23'::real ```                          | Gibt den Inhalt als Komma Zahl (float) wieder.               | ```1.23```            |
| ```'1.23'::bigint ```                        | Gibt den Inhalt als Ganz Zahl (integer) wieder.              | ```1```               |
