@echo off
setlocal enabledelayedexpansion

REM Configuration
set expectedDir=expected_outputs
set outputDir=outputs

set totalTests=0
set passedTests=0

REM Loop through all expected txt files
for %%f in (%expectedDir%\ex_*.txt) do (

    REM Get base name (ex_01)
    set "fullpath=%%f"
    set "basename=%%~nf"
    REM strip 'ex_' prefix
    set "number=!basename:~3!" 

    echo Checking outputs of test !number!
    set /a totalTests+=1

    REM Check terminal output (.txt)
    set "txt_pass=true"
    fc /b "%outputDir%\op_!number!.txt" "%expectedDir%\ex_!number!.txt" >nul 2>&1
    if errorlevel 1 (
        echo   TERMINAL: FAIL
        set "txt_pass=false"
    ) else (
        echo   TERMINAL: PASS
    )

    REM Check transaction files (.atf vs .etf)
    set "atf_pass=true"
    fc /b "%outputDir%\op_!number!.atf" "%expectedDir%\ex_!number!.etf" >nul 2>&1
    if errorlevel 1 (
        echo   TRANSACTION FILE: FAIL
        set "atf_pass=false"
    ) else (
        echo   TRANSACTION FILE: PASS
    )

    REM Increment passedTests if both passed
    if "!txt_pass!"=="true" if "!atf_pass!"=="true" (
        set /a passedTests+=1
    )

    echo.
)
REM Summary
set /a failedTests=totalTests-passedTests
echo Total tests:  !totalTests!
echo Passed tests: !passedTests!
echo Failed tests: !failedTests!