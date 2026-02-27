#!/bin/bash

# Folder containing daily transaction files
dir="daily_transactions"

# Find the highest existing daily_transactions file number
lastNum=$(ls $dir/daily_transactions_*.txt 2>/dev/null | \
    sed -E 's/.*_([0-9]+)\.txt/\1/' | sort -n | tail -1)

# If none exist, start from 0
if [ -z "$lastNum" ]; then
    lastNum=0
fi

# Increment the counter for the next daily_transactions file
counter=$((lastNum + 1))

# Remove all existing files in outputs directory before running tests
rm -f outputs/*

# Loop through each input file and and running the program
for file in inputs/in*.txt
do
    # Extracting file name, number and creating output file name
    base=$(basename "$file" .txt)
    number=${base:3}
    name="op_$number"

    # Print the test number being run
    echo "Running Test #$number"

    # Run the program with the current input file, while ignoring comment lines, and save the output
    grep -v '^#' "$file" | python3 main.py currentaccounts.txt \
> "outputs/${name}.txt"

    # Move the daily_transactions file to the outputs directory
    mv "$dir/daily_transactions_${counter}.txt" \
       "outputs/${name}.atf"
done