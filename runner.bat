SET mypath=%~dp0
SET realpath=%mypath:~0,-1%

cd %realpath%

set arg1 = %1
set arg2 = %2
set arg3 = %3
set arg4 = %4

CALL venv\Scripts\activate.bat

python main.py %arg1% %arg2% %arg3% %arg4% %*
