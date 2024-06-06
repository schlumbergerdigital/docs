# Konfigurieren


Um das Tool verwenden zu können, müssen Sie Ihre ecoDMS Zugangsdaten eintragen. 
klicken Sie dafür auf Konfigrueren. 

![Konfig](<../3. Konfiguration/img/Konfig.png>)



| Feld                                      | Bedeutung                                                                                                                                                | Beispiel                                |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Pfad                                      | Der Pfad den es zu Überwachen gilt. Es werden auch alle Unteronrder mit einbezogen                                                                        | C:\Ablage                               |
| ecoMDS URL                                | Die vollständige URL Angabe zumr API von ecoDMS.                                                                                                          | https://dms.bsp.docarchivdemo.net/api/  |
| Zertifikatsprüfung                        | Prüft ob das Zertifkat des Webservers gültig ist. Wird ein lokales ecoDMS verwendet kann der Haken entfert werden, es wird aber dringend davon abgeraten. | ja                                      |
| Benutzername                              | Der Bentutzername in ecoDMS mit dem sich angemeldet wird.                                                                                                 | ecodms                                  |
| Passwort                                  | Das Passwort von ecoDMS mit dem sich angemeldet wird.                                                                                                     |
| API Schlüssel (MFA)                       | Der Token von ecoDMS, wenn multifaktor authentifizierung aktiv ist, ansonsten leer lassen                                                                 | areigeuoghrSERgauihdtobujvtsdopitbastd= |
| Geänderte Dateien als Version importieren | Wird eine Datei verändert, wird die Version hochgeladen. Wird der Haken entfernt, werden die Datei in ecoDMS nicht aktuallisert                           | Ja                                      |
| Lizenz                                    | Die Lizenznummer vom Arkivado Up tool                                                                                                                     | 123456789abcdef                         |


Nachdem die Basis Informantionen hinterlegt wurden, muss nun noch das Mapping eingestellt werden:

[Mapping Einstellungen](005config_mapping.md){ .md-button }