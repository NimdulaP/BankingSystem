@echo off
setlocal enabledelayedexpansion

REM Create output folder if it doesn't exist
if not exist output mkdir output

REM Loop through each input file
for %%f in (inputs\*.txt) do (

    echo Running test with %%f

    REM Clear old transaction files
    if exist daily_transactions rmdir /s /q daily_transactions
    mkdir daily_transactions

    REM Run program with redirected input and save terminal log
    python main.py < %%f > output\%%~nf_terminal.txt

    REM Copy transaction file to output folder
    for %%t in (daily_transactions\*.txt) do (
        copy %%t output\%%~nf_transactions.txt > nul
    )

    echo Finished %%f
)

echo All tests complete.
pause