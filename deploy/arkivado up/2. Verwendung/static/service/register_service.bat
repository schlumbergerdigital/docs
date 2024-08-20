::/*<#"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
:: Batch Skript - Registriert den arkivadoUp als Dienst 
:: 				
::  
:: Benötigt: Admin rechte 
::				   			  
::					   
:: Zur Verwendung mit: arkivadoUp und nssm 
:: 
:: Erstellt von:	Max Schwesig	  
:: Version:	 1.0.0
:: Codierung:	UFT-8
:: Stand:	20.08.2024 Max Schwesig		
:: 
:: Copyright (c) 2024 by schlumberger digtial. Alle Rechte vorbehalten.
:: www.schlumberger.digital
::*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""#>*/ 
@echo off
echo "Registiere Arkviado Up"
pushd  %~dp0
nssm install arkivado_up "%cd%\arkivado_up.exe" 
nssm set arkivado_up AppParameters "-w"
nssm set arkivado_up AppDirectory  %cd%\
nssm set arkivado_up DisplayName arkivadoUp - schlumberger digital
nssm set arkivado_up Description Arkivado Up Uploader zu ecoDMS

set /p user="Windows Benutzername benutzername@domain.local: "
set /p pw="Windows Passwort: "


nssm set arkivado_up ObjectName %user% %pw%
net start arkivado_up