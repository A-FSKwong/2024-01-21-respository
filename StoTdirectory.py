import subprocess
import os
import sys

# Install the opencc module
subprocess.check_call([sys.executable, "-m", "pip", "install", "opencc-python-reimplemented"])

from opencc import OpenCC

cc = OpenCC('s2t')  # convert from Simplified Chinese to Traditional Chinese

# Ask for the input and output directories
input_dir = input("Please enter the path of the input (Simplified) directory: ")
output_dir = input("Please enter the path of the output (Traditional) directory: ")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Initialize a counter for the number of files converted
num_files_converted = 0

# Walk through all files in the input directory, including subdirectories
for dirpath, dirnames, filenames in os.walk(input_dir):
    for filename in filenames:
        input_file = os.path.join(dirpath, filename)
        
        # Construct the output file path
        output_file = os.path.join(output_dir, os.path.relpath(input_file, input_dir))
        
        # Create the output file's directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Run the opencc command on the file
        subprocess.check_call([sys.executable, "-m", "opencc", "-c", "s2t", "-i", input_file, "-o", output_file])
        
        # Increment the counter
        num_files_converted += 1
        
        # Print the number of files converted so far, updating the same line each time
        print(f"\rTotal files converted: {num_files_converted}", end="")

print("\nAll Done.")


"""
### Conversions 轉換

* `hk2s`: Traditional Chinese (Hong Kong standard) to Simplified Chinese

* `s2hk`: Simplified Chinese to Traditional Chinese (Hong Kong standard)

* `s2t`: Simplified Chinese to Traditional Chinese

* `s2tw`: Simplified Chinese to Traditional Chinese (Taiwan standard)

* `s2twp`: Simplified Chinese to Traditional Chinese (Taiwan standard, with phrases)

* `t2hk`: Traditional Chinese to Traditional Chinese (Hong Kong standard)

* `t2s`: Traditional Chinese to Simplified Chinese

* `t2tw`: Traditional Chinese to Traditional Chinese (Taiwan standard)

* `tw2s`: Traditional Chinese (Taiwan standard) to Simplified Chinese

* `tw2sp`: Traditional Chinese (Taiwan standard) to Simplified Chinese (with phrases)
"""
