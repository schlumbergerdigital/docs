
# Workflow Anlegen

## Einen Workflow definieren

In den Workflows kann mit klick auf neuen Workflow ein neuer Workflow angelegt werden.  
![](img/neuer_workflow.png)  

Über den Link kann ein 
```
/workflow/new
```
```
http://localhost:8000/workflow/new
```
![](img/workflow_new.png)  

 
Ein Workflow besteht aus zwei Teilen
- Workflow Kopf: die Rahmenbedingungen des Workflows, wie der Name, ob ein Workflow bei Fehlern abbricht usw.  
- Liste der Todos: Die Aufgaben die es zu Bearbeiten gilt. 


### Workflow Kopf
Der Workflow Kopf enthält mehrere Angaben. 

|Feld     |	Beschreibung                        	| 
|----------|------------------------------------|
|name       |	Der Name des Workflows. Dieser identifiziert den Workflow. Ist angegeben, dass nur ein Workflow gestartet werden darf, wird auf diesen Namen geprüft. |   
|stoponerror   |	 Standardmäßig ja: Der gesamte Workflow wird abgebrochen, wenn in einem Todo ein Fehler auftritt.  |
|unique   |	  Standardmäßig ja: Es darf nur einen Workflow Job mit dem selben Namen aktiv sein |   
|only_change_since_run   |	Es werden nur geänderte Daten verwendet. (Das Änderungsdatum der Daten muss höher als das Startdatum des Workflows sein.) Achtung: Ändern mehrere Worklows eine Quelle komme es zu Fehler wenn der Haken gesetzt ist! |  
|webhook|Gibt an ob der Workflow von außen ohne Anmeldung gestartet werden darf| 

### Todos
Ein Workflow braucht mindesten ein ToDo. Normalerweise aber mindestens 2:
- Ein Abholen von Daten aus den Entity's (oben beschrieben)
- Ein Sync mit einem Mapping  (oben beschrieben)


Ein Todo wird angelegt mit dem Button **Todo hinzufügen**   

![](img/workflow_todo_hinzu.png)  


Jedes Todo hat mehrere Optionen

![](img/worklfow_todo.png)  

Feld     |	Beschreibung                        	| 
|----------|:------------------------------------:|
|type       |	Gibt das HTTP Verb an, für den Turm intern eigentlich immer **POST**  |   
|url   |	die URL die aufgerufen werden soll. für interne turm aufrufe ohne den Pfad zum Server angeben. aus ```http://localhost:8000/espocrm/Accounts/sync/1```   wird ```/espocrm/Accounts/sync/1```  |
|data   |	 Der Body des HTTP Aufrufes -meist leer-|   
|waitfortodo   |	Das Todo wartet bis das vorherige Todo fertig ist, standardmäßig aktiv.  |  


Es können auch Header und Parameter für das Todo übergeben werden:
Hierfür einfach auf  ```Header hinzufügen ``` bzw.  ```Parameter Hinzufügen ```  **klicken**. 

Sowohl Parameter als auch Header setzen sich immer auf einem Key und dem passenden Value zusammen. 


![](img/worflow_toto_parameter.png)  

Ein typischer Anwendungsfall: 
Jeder *Sync* Endpoint hat die Option ```only_new``` dabei werden im Fremdsystem nur Daten geändert die noch nicht gesynct wurden. 
Die Parameter Einstellungen sehen dann so aus:
![](img/parameter.png)  


!!! tip "Pro-Tipp"
    Der *Authorization* Key im Header für interne Aufrufe generiert der Turm automatisch.

!!! tip "Tipp"
     Ein Vorteil wenn Parameter extra angegeben werden: es muss nicht darauf geachtet werden die Daten URL Encoded zu schreiben. Es kann normal geschrieben werden.



[Weiter: Jobs  ](jobs.md){ .md-button }
