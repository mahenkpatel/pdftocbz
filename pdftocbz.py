import os
import glob
import shutil
import time
from pdf2image import convert_from_path, convert_from_bytes

list_of_files = glob.glob("*.pdf")

for pdf_file in list_of_files:
    pdf_file_without_extension = pdf_file[:-4]
    print("Extracting " + pdf_file)
    os.mkdir(pdf_file_without_extension)
    images = convert_from_path(pdf_file, output_folder=pdf_file_without_extension, fmt='jpg', output_file=pdf_file_without_extension)
    print("creating archive " + pdf_file_without_extension + ".cbz")
    shutil.make_archive(pdf_file_without_extension, 'zip', pdf_file_without_extension)
    os.rename(str(pdf_file_without_extension)+'.zip', str(pdf_file_without_extension)+'.cbz')
