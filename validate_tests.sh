#!/bin/bash

expected_dir="expected_outputs"
output_dir="outputs"

total_tests=0
passed_tests=0

for file in $expected_dir/ex_*.txt
do
    base=$(basename "$file" .txt) 
    number=${base#ex_} 

    echo "TEST #$number"
    ((total_tests++))

    txt_pass=true
    if diff "$output_dir/op_${number}.txt" \
            "$expected_dir/ex_${number}.txt" > /dev/null
    then
        echo "Terminal: PASS"
    else
        echo "Terminal: FAIL"
        txt_pass=false
    fi

    atf_pass=true
    if diff "$output_dir/op_${number}.atf" \
            "$expected_dir/ex_${number}.etf" > /dev/null
    then
        echo "Transaction File: PASS"
    else
        echo "Transaction File: FAIL"
        atf_pass=false
    fi

    if $txt_pass && $atf_pass
    then
        ((passed_tests++))
    fi

    echo ""
done

echo "Passed tests: $passed_tests"
echo "Failed tests: $((total_tests - passed_tests))"
echo "Total tests:  $total_tests"