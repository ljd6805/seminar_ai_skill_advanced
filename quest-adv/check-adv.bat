@echo off
chcp 65001 >nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0check-adv.ps1" %*
echo.
echo  (이 창은 결과 확인을 위해 열려 있습니다)
pause
