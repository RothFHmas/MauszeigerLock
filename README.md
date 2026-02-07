# MauszeigerLock 🖱️🔒

**MauszeigerLock** ist ein kleines Windows-Tool, das den Mauszeiger auf den Monitor begrenzt, auf dem das Programm gestartet wird.  
Sobald das Fenster geschlossen wird, ist der Mauszeiger wieder vollständig „frei“ und kann sich über alle Bildschirme bewegen.

---

## Funktionen

- Sperrt den Mauszeiger automatisch auf den aktuellen Monitor  
- Freigabe der Maus beim Schließen des Fensters oder durch einen Klick auf den Freigabe-Button  
- ESC-Taste kann ebenfalls zum Freigeben verwendet werden  
- Einfaches, übersichtliches GUI-Fenster  
- Klickbarer Link zum GitHub-Profil des Entwicklers  

---

## Technische Details

- Programmiert für **Windows** – läuft nur auf Windows-Systemen  
- Nutzt die Python-Bibliothek [`screeninfo`](https://pypi.org/project/screeninfo/), um Monitorinformationen zu ermitteln  
- Das Icon für die Desktop-Anwendung wurde **KI-generiert**  
- Die fertige `.exe` liegt im Ordner `dist`  

---

## Installation & Nutzung

1.Repository klonen oder herunterladen:
   ```bash
   git clone https://github.com/RothFHmas/MauszeigerLock.git
   ```
2.Python-Abhängigkeiten installieren:
   ```bash
   pip install screeninfo pywin32
   ```
3.Das Skript direkt ausführen (für Entwickler):
   ```python
   python src/MauszeigerLock.py
   ```
4.Alternativ die ```.exe``` aus ```dist``` starten – kein Python erforderlich

## EXE selbst generieren

Falls du die .exe selbst erstellen möchtest, kannst du folgenden Befehl verwenden:
```bash
pyinstaller --onefile --windowed --icon=Bilder/Ai_image.ico src/MauszeigerLock.py
```

⚡ Hinweis: Der Pfad zum Icon (Bilder/Ai_image.ico) muss korrekt sein.
Die fertige .exe findest du danach im dist-Ordner.

## Lizenz & Sicherheit

- Dieses Programm ist 100% frei und lizenzfrei, kann von jedem genutzt, verändert und weitergegeben werden

- Enthält keine Malware, Spyware oder versteckten Funktionen – volle Sicherheit für den Nutzer

Entwickler

[RothFHmas](https://github.com/RothFHmas) auf GitHub