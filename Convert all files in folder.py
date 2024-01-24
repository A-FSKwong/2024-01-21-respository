# -*- coding: utf-8 -*-
# importing required modules
try:
    import PyPDF2
except ImportError:
    import os
    os.system('pip install PyPDF2')
    import PyPDF2

def extract_text_from_pdf(pdf_filename, txt_filename):
    # creating a pdf reader object 
    reader = PyPDF2.PdfReader(pdf_filename) 

    # printing number of pages in pdf file 
    print(len(reader.pages)) 

    # extracting text from all pages and saving to txt file
    with open(txt_filename, 'w', encoding='utf-8') as f:  # Open the file with UTF-8 encoding
        for page in reader.pages:
            text = page.extract_text() 
            f.write(text + '\n')

if __name__ == "__main__":
    input_dir = input("Please enter the path to the input directory: ")
    output_dir = input("Please enter the path to the output directory: ")

    # Get a list of all files in the input directory
    files = os.listdir(input_dir)

    # Loop over each file
    for file in files:
        # Construct the full file paths
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, file)

        if not input_file.endswith(".pdf"): #check pdf file
            print(f"No pdf file specified: {input_file}")
        elif not output_file.endswith(".txt"): #check txt file
            print(f"No txt file specified: {output_file}")
        else:
            # Migrating starts here....
            extract_text_from_pdf(input_file, output_file)
