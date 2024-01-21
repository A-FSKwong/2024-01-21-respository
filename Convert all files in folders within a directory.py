pip install opencc-python-reimplemented

import os
from opencc import OpenCC

cc = OpenCC('s2t')  # convert from Simplified Chinese to Traditional Chinese

input_dir = 'C:/Simplified'
output_dir = 'C:/Traditional'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Walk through all files in the input directory, including subdirectories
for dirpath, dirnames, filenames in os.walk(input_dir):
    for filename in filenames:
        input_file = os.path.join(dirpath, filename)
        
        # Construct the output file path
        output_file = os.path.join(output_dir, os.path.relpath(input_file, input_dir))
        
        # Create the output file's directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Run the opencc command on the file
        python -m opencc -c s2t -i "{input_file}" -o "{output_file}"
