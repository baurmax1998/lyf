# Haushalts- und Selfcare-Plan – 4 Wochen

## Ziel
Dieser Plan verteilt **deine Aufgaben** über einen Monat mit **4 Wochen**, damit nicht alles gleichzeitig anfällt.

Wichtig:
- Es sind **nur deine Aufgaben** enthalten
- Keine zusätzlichen Aufgaben von deinem Partner
- Der Plan soll **leicht wiederholbar** sein
- Zusätzlich bekommst du sinnvolle **Cron-Muster / Wiederholungen**

---

# 1. Aufgaben sortiert nach Rhythmus

## Täglich / fast täglich
Diese Aufgaben brauchen keinen festen Wochentag, sondern eher einen festen Trigger.

- **Creatin nehmen**
- **Duschen**
- **Aufräumen**
- **Müll einsammeln**

## Mehrmals pro Woche
- **Spüli einräumen**
- **Spüli ausräumen**
- **Bio Müll**
- **Rest Müll**
- **Gelber Sack**
- **Wäsche aufhängen**
- **Wäsche einräumen**

## Wöchentlich
- **Flaschen runterbringen**
- **Getränke kaufen**

## Alle 2 Wochen
- **Bett beziehen**
- **Bart rasieren**
- **Mani und Pedi**

## Etwa monatlich
- **Haare schneiden**
- **Nasenhaare schneiden**

---

# 2. Gute Trigger statt nur feste Uhrzeiten

Manche Aufgaben funktionieren besser mit Ereignissen als mit Kalendereinträgen.

## Event-Trigger
- **Creatin nehmen** → direkt **nach dem Frühstück** oder **nach dem Training**
- **Duschen** → nach Training oder morgens nach dem Aufstehen
- **Spüli ausräumen** → **morgens nach dem Kaffee**
- **Spüli einräumen** → **abends nach dem Essen**
- **Müll einsammeln** → **bevor du die Wohnung verlässt** oder **abends 5 Minuten Reset**
- **Aufräumen** → **jeden Abend 10 Minuten**
- **Wäsche einräumen** → **direkt nachdem die Wäsche trocken ist**
- **Flaschen runterbringen** → **wenn du sowieso das Haus verlässt**
- **Getränke kaufen** → **direkt nach dem Flaschenwegbringen**

---

# 3. Empfohlene Wiederholungsmuster / Cron-Ideen

Hinweis: Cron ist nur ein Muster. Für manche Aufgaben sind **Event-Trigger** besser als Uhrzeiten.

## Täglich
### Creatin nehmen
- **Pattern:** täglich
- **Cron-Idee:** `0 8 * * *`
- besser: nach Frühstück

### Abendlicher Reset: Aufräumen + Müll einsammeln
- **Pattern:** täglich abends, 10 Minuten
- **Cron-Idee:** `0 20 * * *`

### Duschen
- kein hartes Cron-Muster nötig
- eher: **nach Training** oder **morgens bei Bedarf**

---

## Mehrmals pro Woche
### Spüli ausräumen
- **Pattern:** Mo, Mi, Fr, So morgens
- **Cron-Idee:** `0 9 * * 1,3,5,0`

### Spüli einräumen
- **Pattern:** täglich oder mindestens Di, Do, Sa abends
- **Cron-Idee:** `30 20 * * 2,4,6`

### Bio Müll
- **Pattern:** 2x pro Woche
- Empfehlung: **Mittwoch + Sonntag**
- **Cron-Idee:** `0 19 * * 3,0`

### Rest Müll
- **Pattern:** 1x pro Woche
- Empfehlung: **Freitag**
- **Cron-Idee:** `0 19 * * 5`

### Gelber Sack
- **Pattern:** 1x pro Woche prüfen, nur bei Bedarf rausbringen
- Empfehlung: **Samstag**
- **Cron-Idee:** `0 11 * * 6`

### Wäsche aufhängen
- **Pattern:** 2x pro Woche
- Empfehlung: **Mittwoch + Samstag**
- **Cron-Idee:** `0 18 * * 3,6`

### Wäsche einräumen
- **Pattern:** 2x pro Woche, 1 Tag nach Wäsche
- Empfehlung: **Donnerstag + Sonntag**
- **Cron-Idee:** `0 19 * * 4,0`

---

## Wöchentlich
### Flaschen runterbringen
- **Pattern:** 1x pro Woche
- Empfehlung: **Samstag vormittag**
- **Cron-Idee:** `0 11 * * 6`

### Getränke kaufen
- **Pattern:** 1x pro Woche
- Empfehlung: **direkt nach Flaschen runterbringen**
- **Cron-Idee:** `0 12 * * 6`

---

## Alle 2 Wochen
### Bett beziehen
- **Pattern:** jede 2. Woche
- Empfehlung: **Sonntag**
- z. B. Woche 1 und Woche 3

### Bart rasieren
- **Pattern:** alle 2 Wochen
- Empfehlung: **Sonntagabend**
- z. B. Woche 2 und Woche 4

### Mani und Pedi
- **Pattern:** alle 2 Wochen
- Empfehlung: **Sonntagabend**
- z. B. Woche 1 und Woche 3

---

## Monatlich
### Haare schneiden
- **Pattern:** 1x pro Monat
- Empfehlung: **Woche 4 Samstag oder Sonntag**

### Nasenhaare schneiden
- **Pattern:** 1x pro Monat
- Empfehlung: **zusammen mit Haare schneiden** oder Bartpflege

---

# 4. Monatsverteilung über 4 Wochen

## Woche 1
### Täglich
- Creatin nehmen
- Duschen nach Bedarf / nach Training
- 10 min Aufräumen
- Müll einsammeln

### Montag
- Spüli ausräumen

### Dienstag
- Spüli einräumen

### Mittwoch
- Bio Müll
- Wäsche aufhängen
- Spüli ausräumen

### Donnerstag
- Wäsche einräumen
- Spüli einräumen

### Freitag
- Rest Müll
- Spüli ausräumen

### Samstag
- Gelber Sack prüfen / rausbringen falls nötig
- Flaschen runterbringen
- Getränke kaufen
- Wäsche aufhängen
- Spüli einräumen

### Sonntag
- Bio Müll
- Wäsche einräumen
- **Bett beziehen**
- **Mani und Pedi**
- Spüli ausräumen

---

## Woche 2
### Täglich
- Creatin nehmen
- Duschen nach Bedarf / nach Training
- 10 min Aufräumen
- Müll einsammeln

### Montag
- Spüli ausräumen

### Dienstag
- Spüli einräumen

### Mittwoch
- Bio Müll
- Wäsche aufhängen
- Spüli ausräumen

### Donnerstag
- Wäsche einräumen
- Spüli einräumen

### Freitag
- Rest Müll
- Spüli ausräumen

### Samstag
- Gelber Sack prüfen / rausbringen falls nötig
- Flaschen runterbringen
- Getränke kaufen
- Wäsche aufhängen
- Spüli einräumen

### Sonntag
- Bio Müll
- Wäsche einräumen
- **Bart rasieren**
- Spüli ausräumen

---

## Woche 3
### Täglich
- Creatin nehmen
- Duschen nach Bedarf / nach Training
- 10 min Aufräumen
- Müll einsammeln

### Montag
- Spüli ausräumen

### Dienstag
- Spüli einräumen

### Mittwoch
- Bio Müll
- Wäsche aufhängen
- Spüli ausräumen

### Donnerstag
- Wäsche einräumen
- Spüli einräumen

### Freitag
- Rest Müll
- Spüli ausräumen

### Samstag
- Gelber Sack prüfen / rausbringen falls nötig
- Flaschen runterbringen
- Getränke kaufen
- Wäsche aufhängen
- Spüli einräumen

### Sonntag
- Bio Müll
- Wäsche einräumen
- **Bett beziehen**
- **Mani und Pedi**
- Spüli ausräumen

---

## Woche 4
### Täglich
- Creatin nehmen
- Duschen nach Bedarf / nach Training
- 10 min Aufräumen
- Müll einsammeln

### Montag
- Spüli ausräumen

### Dienstag
- Spüli einräumen

### Mittwoch
- Bio Müll
- Wäsche aufhängen
- Spüli ausräumen

### Donnerstag
- Wäsche einräumen
- Spüli einräumen

### Freitag
- Rest Müll
- Spüli ausräumen

### Samstag
- Gelber Sack prüfen / rausbringen falls nötig
- Flaschen runterbringen
- Getränke kaufen
- Wäsche aufhängen
- **Haare schneiden**
- **Nasenhaare schneiden**
- Spüli einräumen

### Sonntag
- Bio Müll
- Wäsche einräumen
- **Bart rasieren**
- Spüli ausräumen

---

# 5. Kompakte Wochenregeln

## Jeden Tag
- **Creatin nach Frühstück**
- **10 min Aufräumen am Abend**
- **Müll einsammeln als Mini-Reset**
- **Duschen nach Bedarf / nach Training**

## Jede Woche
- **Mittwoch + Sonntag:** Bio Müll
- **Freitag:** Rest Müll
- **Samstag:** Gelber Sack prüfen, Flaschen runterbringen, Getränke kaufen
- **Mittwoch + Samstag:** Wäsche aufhängen
- **Donnerstag + Sonntag:** Wäsche einräumen
- **Mo + Mi + Fr + So:** Spüli ausräumen
- **Di + Do + Sa:** Spüli einräumen

## Alle 2 Wochen
- **Woche 1 + 3:** Bett beziehen, Mani und Pedi
- **Woche 2 + 4:** Bart rasieren

## Einmal im Monat
- **Woche 4:** Haare schneiden + Nasenhaare schneiden

---

# 6. Einfache Umsetzung im Alltag

## Gute Bündelungen
Diese Aufgaben lassen sich gut koppeln:

### Samstag-Block
- Flaschen runterbringen
- Getränke kaufen
- Gelber Sack prüfen

### Sonntag-Reset
- Bio Müll
- Wäsche einräumen
- Bett beziehen oder Pflegeaufgabe

### Abend-Reset
- Spüli einräumen
- Müll einsammeln
- 10 min Aufräumen

### Morgen-Reset
- Spüli ausräumen
- Creatin nehmen

---

# 7. Einfachste Version als Reminder-System

## Täglich
- morgens: **Creatin + ggf. Spüli ausräumen**
- abends: **Aufräumen + Müll einsammeln + ggf. Spüli einräumen**

## Mittwoch
- **Bio Müll + Wäsche aufhängen**

## Freitag
- **Rest Müll**

## Samstag
- **Flaschen + Getränke + Gelber Sack Check + Wäsche aufhängen**

## Sonntag
- **Bio Müll + Wäsche einräumen + 2-wöchige Pflege-/Bett-Aufgabe**

---

# 8. Empfehlung
Am praktischsten ist wahrscheinlich diese Mischung:
- **feste Wochentage** für Müll, Wäsche, Flaschen, Getränke
- **Event-Trigger** für Creatin, Duschen, Spüli und Aufräumen
- **Sonntags-Reset** für Bett / Pflege / Monatsaufgaben

Wenn du willst, kann ich dir als Nächstes noch:
1. daraus eine **saubere Checklisten-Version** bauen  
2. einen **Markdown-Wochenplan zum Abhaken** machen  
3. die Aufgaben in **Kalender-/Reminder-Format** mit kurzen Titeln umwandeln.