#!/bin/bash

# Folder containing daily transaction files
dir="daily_transactions"

# Find the highest existing daily_transactions_{num}.txt number
last_num=$(ls $dir/daily_transactions_*.txt 2>/dev/null | \
    sed -E 's/.*_([0-9]+)\.txt/\1/' | sort -n | tail -1)

# If none exist, start from 0
if [ -z "$last_num" ]; then
    last_num=0
fi

counter=$((last_num + 1))

for file in inputs/*.txt
do
    name=$(basename "$file" .txt)

    echo "Running test $name"

    grep -v '^#' "$file" | python3 main.py currentaccounts.txt \
        > "outputs/$name.txt"

    # Move the newly created daily_transactions file
    mv "$dir/daily_transactions_${counter}.txt" "outputs/$name.atf"

    counter=$((counter + 1))
done