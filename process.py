# Main file for the parser.  It reads in all the files in
# the input folder and converts all pdfs that it can into
# txt files located in the out directory.  It then searches
# for all the keywords and applies all the applicable
# keyword filters.  The results of this are then sent to
# the Flask webserver for manual analysis.

import subprocess
import os
import pprint
import json

from utils.util import *
from utils.search import KeywordSearch

# Only convert files if the output directory is empty
outlist = os.listdir("out")
outlist.remove(".gitignore")
if len(outlist) == 0:
  # Split all pdfs in the input directory into pages
  pprint.pprint("Splitting pdfs into pages...")

  infiles = os.listdir("input")
  infiles.remove(".gitignore")
  for f in infiles:
    split_pdf(f)

  # Process each file in the split directory
  pprint.pprint("converting split pdfs into text...")
  infiles = os.listdir("split")
  infiles.remove(".gitignore")
  for f in infiles:
    convert_pdf(f)

# Output processed text files to the out directory
out_file_names = os.listdir("out")
out_file_names.remove(".gitignore")

# For every line in the converted pages, check the number of keywords
# that match and return the matches.
results = []
for file_name in out_file_names:
  with open("out/" + file_name) as out_file:
    text = out_file.readlines()
    scanResults = KeywordSearch.scanAllKeywords(text) # scan each page for advanced keywords
    if(len(scanResults) > 0):
      scanResults["document"] = file_name.split("+")[0]
      scanResults["page"] = file_name.split("-")[1].split(".")[0]
      results.append(scanResults)

results = sorted(results, key=lambda x: (x["document"], x["page"]), reverse=False)

resultsFile = open("web/data/results.json", "w")
resultsFile.write(json.dumps(results))
