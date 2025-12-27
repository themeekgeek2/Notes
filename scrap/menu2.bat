menu2.bat

rem ## THIS WAS TAKEN/REFERENCED FROM CHAT.GPT.

set scriptONE=type nul>script_one.txt

set scriptTWO=type nul>script_two.txt

set scriptTHREE=type nul>script_three.txt


@echo off
:menu
cls
echo ---------------------------------------
echo		MAIN MENU OPTIONS
echo ---------------------------------------
echo 		1. SCRIPT ONE
echo		2. SCRIPT TWO
echo		3. SCRIPT THREE
echo		4. EXIT MENU
set /p choice="ENTER HERE: "
rem Process user input
if %choice%=="SCRIPT ONE" goto %scriptONE%
if %choice%=="SCRIPT TWO" goto %scriptTWO%
if %choice%=="SCRIPT THREE" goto %scriptTHREE%
if %choice%=="EXIT MENU" goto end
echo Invalid choice. Please try again.
pause
goto menu

:end
echo Exiting program...
pause
exit