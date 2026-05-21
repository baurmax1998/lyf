# lyf

Statische Website für GitHub Pages.

## Lokal ansehen

Öffne `index.html` im Browser.

## Als GitHub-Repository veröffentlichen

```bash
cd /Users/ba22036/Documents/lyf
git init -b main
git add .
git commit -m "Initial commit"
```

Danach auf GitHub ein leeres Repo `lyf` anlegen und verbinden:

```bash
git remote add origin git@github.com:<DEIN-USERNAME>/lyf.git
git push -u origin main
```

## GitHub Pages aktivieren

Auf GitHub:
1. Repository öffnen
2. **Settings** → **Pages**
3. **Deploy from a branch** wählen
4. Branch **main** und Folder **/(root)** wählen
5. Speichern

Danach ist die Website unter der GitHub-Pages-URL erreichbar.
