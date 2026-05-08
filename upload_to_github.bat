@echo off
chcp 65001 >nul
title GitHub Upload - literature_review Skill

echo.
echo ==============================================
echo   Literature Review Skill — GitHub Upload
echo ==============================================
echo.

:: Check git
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Git is not installed.
    echo Please install Git from: https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

:: Check if already a git repo
if exist ".git" (
    echo [OK] Git repository already initialized.
    goto :ask_push
)

:: Initialize
echo [1/3] Initializing git repository...
git init
if %errorlevel% neq 0 (
    echo [ERROR] Failed to initialize git.
    pause
    exit /b 1
)

:: Add all files
echo [2/3] Adding files...
git add README.md SKILL.md CHANGELOG.md LICENSE .gitignore examples/ references/
if %errorlevel% neq 0 (
    echo [ERROR] Failed to add files.
    pause
    exit /b 1
)

:: Commit
echo [2/3] Committing...
git commit -m "v1.1.0: Strict sequential execution protocol + completion gates + dogfooding case study"
if %errorlevel% neq 0 (
    echo [ERROR] Failed to commit. Check if files exist.
    pause
    exit /b 1
)

:ask_push
echo.
echo [3/3] Ready to push to GitHub.
echo.
set /p REPO_URL="Enter your GitHub repo URL (e.g. https://github.com/YOURNAME/literature-review-skill.git): "

if "%REPO_URL%"=="" (
    echo No URL entered. Skipping push.
    echo You can push later with:
    echo   git remote add origin YOUR_URL
    echo   git push -u origin main
    pause
    exit /b 0
)

git remote add origin %REPO_URL% 2>nul
if %errorlevel% neq 0 (
    echo Remote 'origin' already exists. Updating URL...
    git remote set-url origin %REPO_URL%
)

git branch -M main
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ==============================================
    echo   SUCCESS! Files uploaded to GitHub.
    echo ==============================================
) else (
    echo.
    echo [ERROR] Push failed. Check:
    echo   1. Your internet connection
    echo   2. The GitHub URL is correct
    echo   3. You have permission to push to this repo
    echo   4. The repo exists and is empty
)

echo.
pause
