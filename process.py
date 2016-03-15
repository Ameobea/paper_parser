# Main file for the parser.  It reads in all the files in
# the input folder and converts all pdfs that it can into
# txt files located in the out directory.  It then returns
# the line numbers of all matched terms in `terms.txt`.
# It then returns the number of times terms were matched
# for each line.

import subprocess
import os
import pprint

from utils.util import *
from utils.search import KeywordSearch

# Only convert files if the output directory is empty
if len(os.listdir("out")) == 0:
  # Split all pdfs in the input directory into pages
  pprint.pprint("Splitting pdfs into pages...")
  for f in os.listdir("input"):
    split_pdf(f)
  # Process each file in the split directory
  pprint.pprint("converting split pdfs into text...")
  infiles = os.listdir("split")
  for f in infiles:
    convert_pdf(f)

  # Output processed text files to the out directory
  out_file_names = os.listdir("out")

out_file_names = os.listdir("out")

# For every line in the converted files, check the number of keywords
# that match and return a score for each line with matched keywords.  

results = []

for file_name in out_file_names:
  # numbers.append([file_name])
  with open("out/" + file_name) as out_file:
    text = out_file.readlines()
    scanResults = KeywordSearch.scanAllKeywords(text) # scan each page for advanced keywords
    if(len(scanResults) > 0):
      scanResults["document"] = file_name.split("+")[0]
      scanResults["page"] = file_name.split("-")[1].split(".")[0]
      results.append(scanResults)

results = sorted(results, key=lambda x: (x["document"], x["page"]), reverse=False)
pprint.pprint(results)
