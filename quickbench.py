import os
import shutil
import time

def generate_large_file(file_size, file_path='large_test_file.bin'):
    """
    Generate a large file for testing purposes and measure the time taken.
    
    :param file_size: Size of the file to generate in MB
    :param file_path: Path where the file will be generated
    :return: Time taken to generate the file
    """
    start_time = time.time()
    print(f"Generating a {file_size} MB file for testing...")
    with open(file_path, 'wb') as f:
        f.write(os.urandom(file_size * 1024 * 1024))  # Generate random data
    end_time = time.time()
    return end_time - start_time

def copy_file_and_measure_performance(source_path, destination_path='test_copy.bin'):
    """
    Copy a file and measure the performance of the operation.
    
    :param source_path: Path of the source file
    :param destination_path: Path where the file will be copied
    :return: Time taken to copy the file, size of the file
    """
    start_time = time.time()
    shutil.copy2(source_path, destination_path)
    end_time = time.time()
    file_size = os.path.getsize(source_path)
    return end_time - start_time, file_size

if __name__ == "__main__":
    file_size_mb = int(input("Enter the file size for the test in MB: "))
    
    # Generate the large file and measure the time taken
    file_generation_time = generate_large_file(file_size_mb)
    print("\n--- File Generation Results ---")
    print(f"File Size:        {file_size_mb:>5} MB")
    print(f"Generation Time:  {file_generation_time:>5.2f} seconds\n")
    
    # Copy the file and measure performance
    print("--- File Copy Performance ---")
    copy_time, file_size_bytes = copy_file_and_measure_performance('large_test_file.bin')
    print(f"Copy Time:        {copy_time:>5.2f} seconds")
    print(f"File Size:        {file_size_bytes / (1024 * 1024):>5.2f} MB")
    
    # Calculate and display throughput
    average_throughput = file_size_bytes / copy_time
    print(f"Average Throughput:{average_throughput / (1024 * 1024):>5.2f} MB/s\n")
    
    # Cleanup generated and copied files
    print("--- Cleanup ---")
    os.remove('large_test_file.bin')
    os.remove('test_copy.bin')
    print("Temporary files removed.\n")
