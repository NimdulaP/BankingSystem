#!/bin/bash

# Directory paths
expectedDir="expected_outputs"
outputDir="outputs"

# Initialize counters
totalTests=0
passedTests=0

# Loop through expected output files
for file in $expectedDir/ex_*.txt
do
    # Extracting file name and number
    base=$(basename "$file" .txt) 
    number=${base#ex_} 

    # Display test number
    echo "TEST #$number"
    ((totalTests++))

    # Compare output terminals with expected output terminals
    txtPass=true
    if diff "$outputDir/op_${number}.txt" \
            "$expectedDir/ex_${number}.txt" > /dev/null
    then
    # If the terminals are the same, then the test passed
        echo "Terminal: PASS"
    else
    # Else, the terminals are not the same, meaning the test failed
        echo "Terminal: FAIL"
        # Set txtPass to false if the test failed
        txtPass=false
    fi

    # Compare output transaction files with expected transaction files
    atfPass=true
    if diff "$outputDir/op_${number}.atf" \
            "$expectedDir/ex_${number}.etf" > /dev/null
    then
    # If the transaction files are the same, then the test passed
        echo "Transaction File: PASS"
    else
    # Else, the transaction files are not the same, meaning the test failed
        echo "Transaction File: FAIL"
        # Set atfPass to false if the test failed
        atfPass=false
    fi

    # If both txtPass and atfPass are true, then the whole test passed
    if $txtPass && $atfPass
    then
        # Increase numnber of passed tests by one if the whole test passed
        ((passedTests++))
    fi

    echo ""
done

# Print summary of test results
echo "Passed tests: $passedTests"
echo "Failed tests: $((totalTests - passedTests))"
echo "Total tests:  $totalTests"