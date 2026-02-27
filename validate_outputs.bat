@echo off
setlocal enabledelayedexpansion

REM Configuration
set expected_dir=expected_outputs
set output_dir=outputs

set total_tests=0
set passed_tests=0

REM Loop through all expected txt files
for %%f in (%expected_dir%\ex_*.txt) do (

    REM Get base name (ex_01)
    set "fullpath=%%f"
    set "basename=%%~nf"
    set "number=!basename:~3!"  REM strip 'ex_' prefix

    echo Checking outputs of test !number!
    set /a total_tests+=1

    REM Check terminal output (.txt)
    set "txt_pass=true"
    fc /b "%output_dir%\op_!number!.txt" "%expected_dir%\ex_!number!.txt" >nul 2>&1
    if errorlevel 1 (
        echo   TERMINAL: FAIL
        set "txt_pass=false"
    ) else (
        echo   TERMINAL: PASS
    )

    REM Check transaction files (.atf vs .etf)
    set "atf_pass=true"
    fc /b "%output_dir%\op_!number!.atf" "%expected_dir%\ex_!number!.etf" >nul 2>&1
    if errorlevel 1 (
        echo   TRANSACTION FILE: FAIL
        set "atf_pass=false"
    ) else (
        echo   TRANSACTION FILE: PASS
    )

    REM Increment passed_tests if both passed
    if "!txt_pass!"=="true" if "!atf_pass!"=="true" (
        set /a passed_tests+=1
    )

    echo.
)
REM Summary
set /a failed_tests=total_tests-passed_tests
echo Total tests:  !total_tests!
echo Passed tests: !passed_tests!
echo Failed tests: !failed_tests!