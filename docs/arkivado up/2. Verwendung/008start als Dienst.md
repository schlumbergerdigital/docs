# Windowsdienst 

## Einleitung

Das Tool kann auch als Dienst aktivert werden. Dabei wird der Ornder in Echtzeit überwacht und Änderungen sofort hochgeschoben.
Wichtig ist dabei, dass der Dienst unter dem User läuft,unter dem er konfiguriert wurde. 
Der Dienst kann nicht als Systemdienst laufen. 

Wir empfehlen einen eigenen lokalen Benutzer anzulegen. 




!!! Waring "Für folgende Aktionen werden Administrationsrechte Benötigt "

## Installer

!!! Tip "Experimentelle Installer Oberfläche"

- Laden Sie den Installer [download](https://turm.lizenz.arkivado.digital/lizer/download/up_service_register)
in das *selbe Verzeichnis* herunter in dem das Arkviado Up liegt. 



![Service Konfigurieren](<img/Service Registerer.jpg>)

- Geben den Windows Benutzer ein, unter dem das Arkivado Up Tool laufen soll. Wenn Sie einen 
- Geben Sie das zugehörige Passwort ein. 
- Wählen Sie die JSON aus die Sie konfiguriert haben. Wird nur eine verwendet, liegt diese unter APP Data. 
- Klicken Sie auf Service registierern und starten um den Dienst einzustellen 

## Benötigte Dateien

Damit Arkviado_up als Dienst laufen kann, werden noch zwei weitere Dateien benötigt:

- [nssm](static/service/nssm.exe){:download="nssm.exe"}
- [register_service.bat](static/service/register_service.bat){:download="register_service.bat"}

Laden Sie diese herunter und legen sie ins selbe Verzeichniss wie die *arkivado_up.exe*.


## Dienst konfiguriere

- Starten Sie die Batchdatei *register_service.bat* als Administrator
- Geben Sie nun den Benutzernamen und Passwort des Windows Benutzer ein, unter dem das Arkivado Up Tool registiert ist.  