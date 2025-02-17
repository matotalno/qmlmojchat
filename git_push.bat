@echo off
echo === Modern AI Chat Git Push Script ===
echo.

REM Proveri da li postoji .git folder
if not exist .git (
    echo Inicijalizacija git repozitorijuma...
    git init
)

REM Dodaj sve fajlove
echo Dodavanje fajlova...
git add .

REM Napravi commit
set /p commit_msg="Unesite commit poruku: "
git commit -m "%commit_msg%"

REM Ako remote nije podešen, traži URL
git remote -v > nul 2>&1
if %errorlevel% neq 0 (
    set /p repo_url="Unesite GitHub repo URL: "
    git remote add origin %repo_url%
)

REM Push na GitHub
echo Pushing na GitHub...
git push -u origin master

echo.
echo === Završeno! ===
pause
