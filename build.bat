@echo off
cd /d "%~dp0"
pyinstaller "URBISRateCalculator.spec"
pause