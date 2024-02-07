
# Workflows

## Einleitung 

Meisten reicht es nicht aus, nur ein [Mapping](mapping.md) zu definieren. 

Normalerweise:

- wird aus einer *Quelle* ein geänderter Datensatz geholt
- Mit hilfe des Mappings die Daten angepasst, sodass das Zielsystem diese versteht
- und Anschließend dem Zielsystem bereitgestellt  
  
Typischerweise geschieht dies im drei Schritt:

1. Ein Auslöser triggert einen Workflow (Zeitgesteuert, Manuell ausgelöst oder via Hook)
2. Dieser holt die aktuellen Daten aus dem Quell System, indem sich die Daten geändert haben. Dabei werden die Daten im Turm aktualisiert, der Turm prüft selbständig ob die Daten sich *wirklich* geändert haben und gibt die geänderten Daten weiter 
3. Die neuen Daten werden in verschiedenen Drittsysteme gespielt. 

Es handelt sich also um ETL: Extract Transform Load.

Natürlich kann der Turm auch mehrere Quellen und Ziele in einem Workflow bearbeiten. 
z.B. 
- Im CRM die geänderten Adressen holen
- Anschließend im Onlineshop Bestellungen abholen
- Die Bestellungen mit den Adressdaten abgleichen 
- Die neuen Bestellungen ins ERP System spielen

Diese Einzelschritte werden im Turm Todos genannt, ein Workflow ist die Sammlung dieser Todos.
Ein Workflow ist also eine Aufzählung von Todos die hintereinander aufgerufen werden. 



[Weiter: Workflow Ansehen ](workflows_show.md){ .md-button }
