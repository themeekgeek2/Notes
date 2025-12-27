@echo off
setlocal

rem move_screenshots script update
rem===============================

cls

set screenshots_locate="C:\Users\korin\OneDrive\Pictures\Screenshots"

set screenshots_destination="C:\Users\korin\Downloads"

set daysold="7"

echo Moving recent screenshots to local downloads...
 
rem ## creates destination if nonexistent
rem======================================
if not exist "%screenshots_destination%" (
	mkdir "%screenshots_destination%"
	if %errorlevel% neq 0 (
		echo ERROR: Could not create destination directory. Exiting...
		goto :eof
	)
)
rem ## :EOF stands for End of File; it's a predefined MS label that exits a subroutine in a batch file right away, before it moves on to the next subroutine.


cd %screenshots_locate%

dir /o-d /tw

rem ## This lists files starting with the most recent date and time.

forfiles /p %screenshots_locate% /m*.* /d %daysold% /c "cmd /c move@path \"%screenshots_destination%\"" 2>nul

echo.

echo Process Complete.

pause




