
## Konfigurationsdatei

!!! info "Nur On Premice"
    In der Cloud ist dieser Abschnitt nicht nötig

1. **Basis-Konfiguration**
    - Verbindungseinstellungen zum PostgreSQL-Server werden unter `TurmSQL` vorgenommen. Hier müssen die Serveradresse, der Benutzername und das Passwort eingetragen werden. Der Turm legt die Datenbank und den Benutzer an, wenn er im Installationsmodus läuft.
    - Unter `base` muss ein `AuthName` und `AuthPass` für die grafische Oberfläche festgelegt werden.
    - `ServerDomains` *Optional*: Wenn diese Option weggelassen wird, akzeptiert der Turm Verbindungen von überall (empfohlen). Andernfalls können hier Domains eingetragen werden, unter denen der Turm erreichbar ist. Mindestens localhost muss angegeben werden, damit Jobs verarbeitet werden können.
    - `IPWhitelist` *Optional*: Legt die IPs fest, die Anfragen an den Server stellen dürfen. Muss mindestens 127.0.0.1 und die Netzwerk-IP (z.B. 192.168.1.2) enthalten, wenn angegeben. (leer lassen, wenn nichts bekannt ist)
    - `Webroot`: Gibt den Pfad an, unter dem der Turm erreichbar ist. Dies ist besonders wichtig, wenn der Turm hinter einem Reverse Proxy betrieben wird. Wenn nichts angegeben wird, ist der Turm unter der Hauptdomain erreichbar. Soll der Turm beispielsweise unter beispiel.de/smart erreichbar sein, muss im WebRoot "smart" angegeben werden.
    - `LogLevel` *Optional*: Bestimmt, wie detailliert der Turm Logs erstellt. Möglichkeiten sind: `Critical`, `Error`, `Warning`, `Info`, `Debug`.
    - `LogToConsole` *Optional*: Gibt Logs auch auf CMD-Ebene aus.
    - `StartPage` *Optional*: Legt fest, welche Seite beim Laden des Turms angezeigt werden soll. Wenn unter "home" in der `params.json` Buttons definiert sind, werden diese angezeigt. Wenn nichts angegeben wird, wird die Konfigurationsseite angezeigt.

```json
{
    "base": {
        "AuthName": "Benutzername für das Frontend",
        "AuthPass": "Passwort für das Frontend",
        "TurmPort": 8000,
        "ServerDomains": [
            "localhost"
        ],
        "IPWhitelist": [
            "127.0.0.1"
        ],
        "FileBasePath": "C:\\turm_files",
        "WebRoot": "",
        "LogLevel": "INFO",
        "LogToConsole": true,
        "StartPage": "https://<TURM_URL>/upload/pdf?after_upload=smart/1/classify/"
    },
    "TurmSQL": {
        "SQLType": "postgres",
        "SQLServer": "hostname",
        "SQLDatabase": "turm",
        "SQLUsername": "turmadmin",
        "SQLpassword": "2334oijfvgkj",
        "SQLPort": "5432",
        "SQLMaxConncections": 70
    }
}
```