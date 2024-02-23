# Benchmarking Tool for IO, CPU, and Memory

This Python program is designed to benchmark the performance of IO, CPU, and memory operations on your system. It generates a large file, copies this file, and measures the performance of these operations.

## Features

- **File Generation**: Generates a large file to test disk IO.
- **File Copy**: Copies the generated file to test file system performance.
- **Performance Measurement**: Measures the time taken for file generation and copying, calculates throughput.

## Requirements

- Python 3.x

## Usage

1. Clone or download the program to your local system.
2. Open a terminal or command prompt.
3. Navigate to the program directory.
4. Run the program with Python:

```bash
python benchmark_tool.py
```


# Benchmarking Tool for IO, CPU, and Memory

This Python program is designed to benchmark the performance of IO, CPU, and memory operations on your system. It generates a large file, copies this file, and measures the performance of these operations.

## Features

- **File Generation**: Generates a large file to test disk IO.
- **File Copy**: Copies the generated file to test file system performance.
- **Performance Measurement**: Measures the time taken for file generation and copying, calculates throughput.

## Requirements

- Python 3.x

## Usage

1. Clone or download the program to your local system.
2. Open a terminal or command prompt.
3. Navigate to the program directory.
4. Run the program with Python:

```bash
python benchmark_tool.py
```
Follow the on-screen instructions to enter the desired file size for the test in MB.
## Output
The program will output the time taken to generate and copy the file, the size of the files, and the average throughput during the copy operation.
After the benchmark, it cleans up the generated files.
## Example

Enter the file size for the test in MB: 100

--- File Generation Results ---
File Size:         100 MB
Generation Time:  2.34 seconds

--- File Copy Performance ---
Copy Time:        0.56 seconds
File Size:        100.00 MB
Average Throughput:178.57 MB/s

--- Cleanup ---
Temporary files removed.
