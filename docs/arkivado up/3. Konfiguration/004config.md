# Konfigurieren


Um das Tool verwenden zu können, müssen Sie Ihre ecoDMS Zugangsdaten eintragen. 
klicken Sie dafür auf Konfigrueren. 

![Konfig](<../3. Konfiguration/img/Konfig.png>)



| Feld                                      | Bedeutung                                                                                                                                                | Beispiel                                |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Pfad                                      | DDer Pfad, der überwacht werden soll. Es werden auch alle Unterordner einbezogen.                                                                      | C:\Ablage                               |
| ecoDMS URL                            | Der vollständige URL zur API von ecoDMS.                                                                                                         | https://dms.bsp.docarchivdemo.net/api/  |
| Zertifikatsprüfung                        | Prüft, ob das Zertifikat des Webservers gültig ist. Wird ein lokales ecoDMS verwendet, kann der Haken entfernt werden, es wird jedoch dringend davon abgeraten. | ja                                      |
| Benutzername                              | Der Benutzername in ecoDMS, mit dem sich angemeldet wird.                                                                                             | ecodms                                  |
| Passwort                                  | Das Passwort von ecoDMS, mit dem sich angemeldet wird.                                                                                          |
| API Schlüssel (MFA)                       | Der Token von ecoDMS, wenn die Multifaktor-Authentifizierung aktiv ist, ansonsten leer lassen.                                               | areigeuoghrSERgauihdtobujvtsdopitbastd= |
|Geänderte Dateien als Version importieren | Wird eine Datei verändert, wird die Version hochgeladen. Wird der Haken entfernt, werden die Dateien in ecoDMS nicht aktualisiert.                           | Ja                                      |
| Lizenz                                    | Die Lizenznummer vom Arkivado Up Tool.                                                                                                                   | 123456789abcdef                         |


Nachdem die Basisinformationen hinterlegt wurden, muss nun noch das Mapping eingestellt werden:

[Mapping Einstellungen](005config_mapping.md){ .md-button }


Zum Schluss können sie optional eine Auschluss Liste definieren, sodass nur "sinnvolle" Dokumente in ecoDMS abgelegt werden:

[Datei Endungen Whitelist](006config_whitelist){ .md-button }
