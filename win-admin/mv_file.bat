:@echo off
:cls

:set "dow=c:\users\korin\downloads"
:set "docs=c:\users\korin\documents"
:set "pic"=C:\Users\korin\OneDrive\Pictures"
:set "mus=C:\Users\korin\OneDrive\Music"
:set "vid=c:\users\korin\onedrive\videos"

:cd %dow%
:findstr /f /a:green /i /m /s "*.png"
:if not exist "*.png* cd %docs% 

rem ISSUES INCLUDED:
rem  Syntax error with line 6 (variable called '"pic"' with quotes instead of just 'pic'
rem  Findstr is only designed to search for text INSIDE files and LIST them. Findstr cannot move files.
rem   Syntax error with line 12 (missing a quote for '.png*'. Inefficient to use if exist/if not exist with wildcards as it's more prone to errors.
rem  In line 12, the 'cd' command only moves the focus to the Documents folder and stops without repeating the search logic.
rem  Script is incomplete.
