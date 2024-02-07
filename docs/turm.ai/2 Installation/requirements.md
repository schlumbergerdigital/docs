# Systemvoraussetzungen

!!! info "Nur On Premise"
    In der Cloud ist dieser Abschnitt nicht nötig
    
## Hardware

### Speicherplatz
- 2 GB für Programme
- Zusätzlicher Speicher für Datenbank und Dateien, stark abhängig von der Nutzung
- Empfohlener Mindestspeicherplatz: 30 GB
- Anbindung an SSD oder schneller empfohlen

### CPU
- Stark von der Nutzung abhängig (Mehr ist besser)
- Mindestens 2 Kerne, wobei die Kernanzahl entscheidend für die Anzahl der Prozesse ist, die gleichzeitig abgearbeitet werden können:
  - 1 Kern = ca. 5 Hintergrundjobs + 1 Kern für die Turm-Oberfläche und Verwaltung

### Arbeitsspeicher
- Stark von der Nutzung abhängig (Mehr ist besser)
- Mindestens 1 GB für den Turm einplanen
- Empfohlen: Mindestens 4 GB

## Software

### Betriebssystem (OS)
- Windows 10 / Windows 2012 oder höher
- Ubuntu 18.04 (20.04 empfohlen) oder höher

### Datenbank
- Postgresql 10 (neueste Version empfohlen) oder höher

### Python
- 3.10 (neueste Version empfohlen) oder höher
- Mit Pip (wird automatisch installiert)
- Mit FastAPI mindestens Version 0.100.0 (neueste Version empfohlen) (wird automatisch installiert)
- Mit Uvicorn (wird automatisch installiert)

### Reverse Proxy
- Nginx empfohlen
- Kompatibel mit allen Reverse Proxys
- Wird benötigt für HTTPS
