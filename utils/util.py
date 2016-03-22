# Supplemental file for process.py. Contains
# utility functions used to assist in the processing
# of pdfs into text and keyword identification.

import pprint
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.utils import *

def split_pdf(f):
  infile = PdfFileReader(open("input/"+f, 'rb'))
  try:
    for i in xrange(infile.getNumPages()):
     p = infile.getPage(i)
     outfile = PdfFileWriter()
     outfile.addPage(p)
     reali = i+1
     with open('split/'+f.split(".")[0].replace("-","_").replace("+","_")+'+page-%02d.pdf' % reali, 'wb') as f3:
      outfile.write(f3)
  except(PdfReadError): # TODO: fix Object 332 0 not defined. [pdf.py:1600] errors
    pprint.pprint("Error reading PDF " + f)

def convert_pdf(f):
  split = f.split(".")
  command = "/usr/local/bin/pdf2txt.py -o out/" + split[0] + ".txt split/" + f
  os.system(command)

# Checks to see if a number is within 3 word
# on either side of a matched keyword. Will look
# one line up and down but still respects
# the three-word proximity.
def number_nearby(keyword, line_number, text, offset): # TODO: Add support for word numbers like "three"
  # line_number assumes that the first line starts at 1
  # text is an array of strings where each string is a line.
  split = text[line_number+offset].split(" ")
  index = -1
  found_numbers = []
  keyword_index = 0
  for word in split: # set keyword_index and fill found_numbers with indices of all numbers in the line.
    index += 1
    if word.lower() == keyword:
      keyword_index = index
    if  number(word):
      found_numbers.append(index)
  candidate_index = 0
  for candidate in found_numbers: # if a number is near the keyword on another line
    candidate_index += 1
    if offset == 1 and candidate_index < 3:
      return True
    if offset == -1 and candidate_index > len(split)-4:
      return True
    if offset == 0 and abs(candidate_index - keyword_index) < 4:
      return True
  if offset == 0: # if a number is near the keyword on the same line
    if keyword_index < 3 and line_number > 1:
      if  number_nearby(keyword, line_number, text, -1):
        return True
    if keyword_index > len(split)-4 and line_number < len(text)-2:
      if  number_nearby(keyword, line_number, text, 1):
        return True
  return False # if nothing found anywhere

# returns True if a character is on the same line as a given keyword.
def char_nearby(keyword, character, line_number, text):
  for letter in text[line_number]:
    if letter == character:
      return True
  return False

def number(s):
  try:
    float(s)
    return True
  except ValueError:
    return False
