rem ## THIS WAS TAKEN/REFERENCED FROM CHAT.GPT.


@echo off
color 9
:menu
cls
echo ---------------------------------------
echo		MAIN MENU OPTIONS
echo ---------------------------------------
echo 		1. SCRIPT ONE
echo		2. SCRIPT TWO
echo		3. SCRIPT THREE
echo		4. EXIT MENU
set /p choice="Enter here (DO NOT USE SPACES)"
rem Process user input
if %choice%=="scriptone" goto scriptONE
if %choice%=="scripttwo" goto scriptTWO
if %choice%=="scriptthree" goto scriptTHREE
if %choice%=="EXIT MENU" goto end
if %choice%==" " echo Invalid choice. Please try again.
pause
goto menu

:scriptONE
type nul>script_one.txt
echo File created.
pause
goto menu

:scriptTWO
type nul>script_two.txt
echo File created.
pause
goto menu

:scriptTHREE
type nul>script_three.txt
echo File created.
pause
goto menu


:end
echo Exiting program...
pause
exit