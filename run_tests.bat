@echo off
setlocal enabledelayedexpansion

REM Create outputs folder if it doesn't exist
if not exist outputs mkdir outputs

REM Loop through each input file
for %%f in (inputs\in*.txt) do (

    echo Running test with %%f

    REM Extract the number 
    set name=%%~nf
    set number=!name:~2!

    REM Clear old transaction files
    if exist daily_transactions rmdir /s /q daily_transactions
    mkdir daily_transactions

    REM Run program and save terminal outputs
    REM Skip the first line of the input file (comment line)
    more +1 "%%f" | python main.py currentaccounts.txt > "outputs\op!number!.txt"

    REM Copy generated transaction file
    for %%t in (daily_transactions\*.txt) do (
        copy %%t "outputs\op!number!.atf" > nul
    )
)