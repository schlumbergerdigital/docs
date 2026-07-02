# Liste nachschlagen und ersetzen (maplist)

## Mapping: Elementweises Nachschlagen einer Liste `@maplist`

Manchmal steht in einer Quellspalte nicht ein einzelner Wert, sondern eine ganze Liste als String, z.B.:

```
['Nürnberg','München','Würzburg']
```

Mit `@maplist` wird jeder Eintrag dieser Liste einzeln in einer Referenztabelle nachgeschlagen und durch den dort hinterlegten Wert ersetzt. Das Ergebnis wird wieder als Liste – **in unveränderter Reihenfolge** – ausgegeben.

```
 @maplist(referenztabelle, schluesselspalte, zielspalte, <Optional WHERE>)
```

| Name             | Bedeutung                                                                                                          | Beispiel          |
|------------------|--------------------------------------------------------------------------------------------------------------------|-------------------|
| referenztabelle  | Der Name der Nachschlagetabelle im Turm.                                                                            | `ref_staedte`     |
| schluesselspalte | Die Spalte in der Referenztabelle, deren Wert mit den Listeneinträgen verglichen wird.                             | `quelle_name`     |
| zielspalte       | Die Spalte in der Referenztabelle, deren Wert stattdessen ausgegeben werden soll.                                  | `ziel_name`       |
| Optional WHERE   | Ein zusätzlicher Filter auf die Referenztabelle (z.B. nur aktive Einträge berücksichtigen).                        | `aktiv = '1'`     |

!!! warning "In der ersten Modifikationsspalte"
    Der Befehl muss in der ersten Modifikationsspalte eingegeben werden.

### Beispiel

In der Quelle steht in der Spalte `staedte` der Wert `['Giessen','München','Würzburg']`.
In der Referenztabelle `ref_staedte` gibt es die Zuordnung:

| quelle_name | ziel_name |
|-------------|-----------|
| Giessen     | GI        |
| München     | M         |
| Würzburg    | WÜ        |

Das Mapping:

| at_quelle | at_quelle_mod                              | ziel_tabelle | ziel_tabelle_mod |
|-----------|--------------------------------------------|--------------|------------------|
| staedte   | @maplist(ref_staedte, quelle_name, ziel_name) | staedte   |                  |

ergibt im Ziel die Liste:

```
['GI','M','WÜ']
```

### Nicht gefundene Werte

Wird für einen Listeneintrag **kein** passender Wert in der Referenztabelle gefunden, bleibt der **Originalwert** erhalten. Aus `['Giessen','Berlin']` würde – wenn `Berlin` nicht in der Referenztabelle steht – `['GI','Berlin']`.

### Optional WHERE

Die Referenztabelle kann zusätzlich gefiltert werden. Hat die Referenztabelle z.B. eine Aktiv-Spalte und sollen nur aktive Einträge berücksichtigt werden:

```
 @maplist(ref_staedte, quelle_name, ziel_name, aktiv = '1')
```

**und**-Verknüpfungen werden mit `and` geschrieben, **oder**-Verknüpfungen mit `or`.

### Performance

Intern wird die Liste mit einem einzigen SQL-Statement verarbeitet (`LEFT JOIN LATERAL` mit `unnest ... WITH ORDINALITY` und `array_agg`). Pro Listeneintrag erfolgt ein indizierter Lookup in der Referenztabelle.

!!! tip "Index setzen"
    Für eine performante Verarbeitung sollte auf der **Schlüsselspalte** der Referenztabelle ein Index liegen.
