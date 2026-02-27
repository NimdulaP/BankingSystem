#!/bin/bash

for file in inputs/*.txt
do
    name=$(basename "$file" .txt)

    echo "Running test $name"

    grep -v '^#' "$file" | python3 main.py currentaccounts.txt \
        > "outputs/$name.txt"

    mv transout.txt "outputs/$name.atf"
done