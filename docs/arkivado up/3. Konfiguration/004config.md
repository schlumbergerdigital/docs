# Konfigurieren


Um das Tool verwenden zu können, müssen Sie Ihre ecoDMS Zugangsdaten eintragen. 
klicken Sie dafür auf Konfigrueren. 

![Konfig](<../3. Konfiguration/img/Konfig.png>)



| Feld                                      | Bedeutung                                                                                                                                                                                                                                                                                      | Beispiel                                |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Pfad                                      | Der Pfad, der überwacht werden soll. Es werden auch alle Unterordner einbezogen.                                                                                                                                                                                                               | C:\Ablage                               |
| ecoDMS URL                                | Der vollständige URL zur API von ecoDMS.                                                                                                                                                                                                                                                       | https://dms.bsp.docarchivdemo.net/api/  |
| Zertifikatsprüfung                        | Prüft, ob das Zertifikat des Webservers gültig ist. Wird ein lokales ecoDMS verwendet, kann der Haken entfernt werden, es wird jedoch dringend davon abgeraten.                                                                                                                                | ja                                      |
| Maximale Uploadgröße in KB:               | Die Größe die eine Datei maximal haben darf. Das ist Abhängig von den Einstellungen im ecoDMS Server. Mehr Infos dazu [hier](https://confluence.applord-gruppe.eu/api/upload-groesse) |
| Benutzername                              | Der Benutzername in ecoDMS, mit dem sich angemeldet wird.                                                                                                                                                                                                                                      | ecodms                                  |
| Passwort                                  | Das Passwort von ecoDMS, mit dem sich angemeldet wird.                                                                                                                                                                                                                                         |
| API Schlüssel (MFA)                       | Der Token von ecoDMS, wenn die Multifaktor-Authentifizierung aktiv ist, ansonsten leer lassen.                                                                                                                                                                                                 | areigeuoghrSERgauihdtobujvtsdopitbastd= |
| Geänderte Dateien als Version importieren | Wird eine Datei verändert, wird die Version hochgeladen. Wird der Haken entfernt, werden die Dateien in ecoDMS nicht aktualisiert.                                                                                                                                                             | Ja                                      |
| Lizenz                                    | Die Lizenznummer vom Arkivado Up Tool.                                                                                                                                                                                                                                                         | 123456789abcdef                         |


Nachdem die Basisinformationen hinterlegt wurden, muss nun noch das Mapping eingestellt werden:

[Mapping Einstellungen](005config_mapping.md){ .md-button }


Zum Schluss können sie optional eine Auschluss Liste definieren, sodass nur "sinnvolle" Dokumente in ecoDMS abgelegt werden:

[Datei Endungen Whitelist](006config_whitelist.md){ .md-button }



## Profi Konfigurationen

!!! warning "IT Profi Bereich"
    Der folgende Abschnitt ist für Profis da

in der JSON Datei sind noch mehr Optionen die gesetzt werden können


| Feld               | Bedeutung                                                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| watch_startup_scan | Führt noch einen Vollscann durch bevor die Ornderüberwachung startet. Stadnard True.                                                                   |
| watch_redo         | Kann angegeben werden, dass alle X Tage nochmals ein Vollscann durchgeführt werden soll.                                                               |
| max_upload_size    | Die Maximale Dateigröße pro Dokumente in KB                                                                                                            |
| import_versions    | Standard True: Zur bestehende Dateien werden neue Versionen angelegt. Standard true.                                                                   |
| redo_all           | Alle bisherigen Daten Nochmal bearbeiten                                                                                                               |
| delete_if_done     | Wenn verarbeitet wurde, wird die Datei gelöscht, ACHTUNG: wird der selbe Name nochmals vergeben, wird eine neue Version, kein neues Dokument angelegt. |
| db_path            | Der Pfad zur Datenbank                                                                                                                                 |