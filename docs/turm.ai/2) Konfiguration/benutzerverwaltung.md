# Benutzerverwaltung anlegen

!!! info "Nur On Premise"
    In der Cloud ist dieser Abschnitt nicht nötig
## Einleitung

Der Turm kann sowohl mit als auch ohne Benutzerverwaltung betrieben werden. Ohne Benutzerverwaltung existiert nur der Benutzer, der in der `params.json` angegeben ist. Ohne Benutzerverwaltung:

- Können keine automatischen Jobs ausgeführt werden.
- Gibt es keine Unterscheidung zwischen Admin und Endanwendern.

## Eine Benutzerverwaltung anlegen

!!! warning "One Time Job"
    Dieser Schritt ist nur einmalig erforderlich.

Durch das Aktivieren der Benutzerverwaltung wird das initiale Passwort in der `params.json` ungültig. Um die Benutzerverwaltung zu installieren, besuche:


```
https://<TURM_URL>/docs#/turm/Erstellt_Benutzerverwaltung_im_Turm_config_user_verwaltung_create_post
```

Klicke auf *Try it Out* und dann auf *Execute*.  
Die Verwaltung ist nun installiert.

!!! danger "admin anlegen"
    Erst einen Admin Account anlegen, ansonsten ist man ausgesperrt

## Benutzer anlegen

Um einen Benutzer im Turm anlegen zu können, muss die Benutzerverwaltung aktiv sein.

Siehe hierzu die Anleitung in der Installationsanleitung unter *Benutzerverwaltung anlegen*.  

Zum Benutzer anlegen muss man Admin sein.

Bei allen Links das `<TURM_URL>` durch den Kundenserver ersetzen.



```
https://<TURM_URL>/docs#/turm/Erstellt_Neuen_Benutzer_im_Turm_config_user_create_post

```


| Feld     | Beschreibung                         | Hinweis  |
|----------|--------------------------------------|----------|
| User     | Ist der Username für den Turmnutzer  | Der Benutzername entfernt automatisch Leerzeichen, Doppelpunkte und Punkte. Zudem wird alles in Kleinbuchstaben abgespeichert. (z.B. John = john) |
| Password | Das Passwort für den Benutzer        | Das Passwort wird in der Datenbank bcrypt-gehasht und mit Salt (Stand: 19.10.21) abgespeichert. |
| Admin    | Gibt an, ob der User auf die Turm-Adminoberfläche zugreifen darf. | |
