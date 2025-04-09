@echo off
chcp 65001 >nul
@title KLTOOL - by kltzqu / kltz4074
@color 2



echo.       
echo.
echo		welcome👋🏻
echo 	добро пожаловать👋🏻
echo. 		
echo      	 (1) start tool



set /p input="⠀⠀⠀⠀⠀⠀⠀⠀>>"

if "%input%"=="1" (
    python files\main.py
)
pause
