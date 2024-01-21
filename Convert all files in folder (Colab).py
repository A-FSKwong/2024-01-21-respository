!pip install opencc-python-reimplemented

from opencc import OpenCC
cc = OpenCC('s2t')  # convert from Simplified Chinese to Traditional Chinese
# can also set conversion by calling set_conversion
# cc.set_conversion('s2tw')

from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

import os

input_dir = '/content/drive/My Drive/史传部S'
output_dir = '/content/drive/My Drive/史傳部T'

# Get a list of all files in the input directory
files = os.listdir(input_dir)

# Loop over each file
for file in files:
    # Construct the full file paths
    input_file = os.path.join(input_dir, file)
    output_file = os.path.join(output_dir, file)

    # Run the opencc command on the file
    !python -m opencc -c s2t -i "{input_file}" -o "{output_file}"