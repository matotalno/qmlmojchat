@echo off
echo === Modern AI Chat - Git Push Script ===
echo.

REM Proveri da li je git instaliran
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo Git nije instaliran! Molimo instalirajte git sa https://git-scm.com/
    pause
    exit /b
)

REM Inicijalizuj git ako ne postoji
if not exist .git (
    echo Inicijalizacija git repozitorijuma...
    git init
    if %errorlevel% neq 0 (
        echo Greška pri inicijalizaciji git-a!
        pause
        exit /b
    )
)

REM Dodaj sve fajlove
echo.
echo Dodavanje fajlova u git...
git add .
if %errorlevel% neq 0 (
    echo Greška pri dodavanju fajlova!
    pause
    exit /b
)

REM Napravi commit
echo.
set /p commit_msg="Unesite commit poruku: "
git commit -m "%commit_msg%"
if %errorlevel% neq 0 (
    echo Greška pri commit-u!
    pause
    exit /b
)

REM Proveri da li postoji remote
git remote -v | findstr "origin" >nul
if %errorlevel% neq 0 (
    echo.
    set /p repo_url="Unesite GitHub repo URL: "
    git remote add origin %repo_url%
)

REM Push na GitHub
echo.
echo Pushing na GitHub...
git push -u origin master
if %errorlevel% neq 0 (
    echo Greška pri push-u! Pokušaj:
    echo 1. git push -u origin main
    echo 2. Proveri da li imaš pristup repozitorijumu
    echo 3. Proveri da li si ulogovan na GitHub
)

echo.
echo === Završeno! ===
pause
