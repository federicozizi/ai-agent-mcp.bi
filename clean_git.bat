@echo off
echo 🧹 Pulizia Git in corso...

git rm -r --cached . -f
git add .
git commit -m "Pulizia: rimossi dal tracking Git i file presenti nel .gitignore"

echo ✅ Fatto! Il repository ora rispetta il .gitignore
pause
