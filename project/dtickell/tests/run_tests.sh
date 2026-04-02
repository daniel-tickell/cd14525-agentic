#!/bin/bash
# run_tests.sh - Runs all Python tests in the tests/ directory and saves output to .txt files.

# path for venv
PYTHON_CMD="/home/dtickell/myvenv/bin/python3"

echo "Starting tests..."

for test_file in *.py; do
    [ -e "$test_file" ] || continue
    
    base_name="${test_file%.py}"
    output_file="${base_name}.txt"
    
    echo "Processing $test_file -> $output_file"
    "$PYTHON_CMD" "$test_file" > "$output_file" 2>&1
done

echo "Done! Test results have been saved as .txt files in the '$TESTS_DIR' folder."
