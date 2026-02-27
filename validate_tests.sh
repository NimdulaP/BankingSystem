#!/bin/bash

expected_dir="expected_outputs"
output_dir="outputs"

total_tests=0
passed_tests=0

for file in $expected_dir/ex_*.txt
do
    base=$(basename "$file" .txt)   # ex_01
    number=${base#ex_}              # 01

    echo "Checking outputs of test $number"
    ((total_tests++))

    txt_pass=true
    if diff "$output_dir/op_${number}.txt" \
            "$expected_dir/ex_${number}.txt" > /dev/null
    then
        echo "  TXT: PASS"
    else
        echo "  TXT: FAIL"
        txt_pass=false
    fi

    atf_pass=true
    if diff "$output_dir/op_${number}.atf" \
            "$expected_dir/ex_${number}.etf" > /dev/null
    then
        echo "  ATF: PASS"
    else
        echo "  ATF: FAIL"
        atf_pass=false
    fi

    if $txt_pass && $atf_pass
    then
        ((passed_tests++))
    fi

    echo ""
done

echo "=============================="
echo "Total tests:  $total_tests"
echo "Passed tests: $passed_tests"
echo "Failed tests: $((total_tests - passed_tests))"

# #!/bin/bash

# expected_dir="expected_outputs"
# output_dir="outputs"

# for file in $expected_dir/ex_*.txt
# do
#     base=$(basename "$file" .txt)   # ex_01
#     number=${base#ex_}              # 01

#     echo "Checking outputs of test $number"

#     # Compare txt output
#     diff "$output_dir/op_${number}.txt" \
#          "$expected_dir/ex_${number}.txt"

#     # Compare transaction file (.atf vs .etf)
#     diff "$output_dir/op_${number}.atf" \
#          "$expected_dir/ex_${number}.etf"

#     echo ""
# done