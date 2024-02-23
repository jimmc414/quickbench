# Benchmarking Tool for IO, CPU, and Memory

This Python script benchmarks the performance of IO (Input/Output), CPU (Central Processing Unit), and memory operations on a computer system. It specifically generates a large file and copies this file to measure the system's performance across these critical components. The process not only tests disk IO but also gives insights into CPU and memory efficiency, providing a comprehensive score for system comparison.

## Features

- **File Generation**: Utilizes `os.urandom` to generate a large file, testing disk IO and indirectly measuring CPU and memory performance through the handling and temporary storage of data.
- **File Copy**: Copies the generated file to test file system performance, further stressing disk IO and showcasing read/write capabilities.
- **Performance Measurement**: Measures the time taken for file generation and copying, calculates throughput, offering a holistic view of system performance.

## Technical Details

- **CPU Testing**: While primarily testing IO, the script indirectly measures CPU performance through the execution of `os.urandom` for data generation and the overall management of IO operations.
- **Memory Testing**: The script tests memory by allocating and managing space for the temporary storage of the data before it is written to disk, although this is not its primary focus.
- **IO Testing**: The core of the benchmarking, testing the disk's ability to write and read large files efficiently, providing clear metrics on IO performance.

## Requirements

- Python 3.x

## Usage

1. Clone or download the program to your local system.
2. Open a terminal or command prompt.
3. Navigate to the program directory.
4. Execute the program with Python:

```bash
python benchmark_tool.py


![image](https://github.com/jimmc414/quickbench/assets/6346529/9792b10d-f5a9-48d4-90a2-cc9ffc12d1d2)

