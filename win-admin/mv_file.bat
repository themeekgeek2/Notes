@echo off
cls

set "dow=c:\users\korin\downloads"
set "docs=c:\users\korin\documents"
set "pic"=C:\Users\korin\OneDrive\Pictures"
set "mus=C:\Users\korin\OneDrive\Music"
set "vid=c:\users\korin\onedrive\videos"

cd %dow%
findstr /f /a:green /i /m /s "*.png"
if not exist "*.png* cd %docs% 
