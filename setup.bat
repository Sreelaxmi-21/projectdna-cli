@echo off
setlocal enabledelayedexpansion

REM Create the .github directory
if not exist ".github" (
    mkdir .github
    echo Created .github directory
)

REM Create the copilot-instructions.md file using Python
python create_copilot_instructions.py

if errorlevel 1 (
    echo Error creating file
    exit /b 1
)

echo.
echo Verifying file was created...
if exist ".github\copilot-instructions.md" (
    echo SUCCESS: File created at .github\copilot-instructions.md
    for %%A in (".github\copilot-instructions.md") do echo File size: %%~zA bytes
) else (
    echo ERROR: File was not created
    exit /b 1
)

endlocal
