menu_test.bat

rem ## Creates a separate menu with options to call another batch script.

cmd /k 

set scriptONE="c:\users\Korin\onedrive\documents\tech_stuff\my-projects\script_ONE.bat"

prompt "SELECT AN OPTION: %scriptONE%"

rem ## NOTE: For now, there will only be one option to open only one script.

if %scriptONE% EXIST start %scriptONE%

