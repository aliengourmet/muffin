# -*- coding: utf-8 -*-
"""prescription-parser.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iM_bwQG539HiaJF_XvLDHxy6nM5866YZ

### Data Input
Upload file with text.
"""

from google.colab import files
uploaded = files.upload()

"""### Install Pre-requisites
- tesseract linux binary
- pytesseract
"""

!sudo apt install tesseract-ocr -y

!pip install pytesseract

"""### OCR"""

import pytesseract
from PIL import Image
file_content = pytesseract.image_to_string(Image.open('test1.jpg'))

"""### Post-processing to Excel"""

# Run this cell only once
from collections import OrderedDict
if 'final_prescriptions' not in locals():
  final_prescriptions = OrderedDict()

def parse_prescription(file_content):
  file_content_str = [elem.strip() for elem in file_content.split('\n')]
  prescription_row = {}
  for elem in map(str,file_content_str):
    if ':' in elem:
      key, val = elem.split(':')
      prescription_row[key] = val
  return prescription_row

# file_content = open('out.txt.txt', 'rb').readlines()
prescription_row=parse_prescription(file_content)

final_prescriptions[len(final_prescriptions)] = prescription_row

import pandas as pd
df = pd.DataFrame.from_dict(final_prescriptions, orient="index")
df.to_excel("prescriptions_dict.xlsx", 'Sheet1', index=False)

files.download("prescriptions_dict.xlsx")