# Main file for the parser.  It reads in all the files in
# the input folder and converts all pdfs that it can into
# txt files located in the out directory.  It then returns
# the line numbers of all matched terms in `terms.txt`.
# It then returns the number of times terms were matched
# for each line.

import subprocess
import os
import pprint

infiles = os.listdir("input")
for f in infiles:
  split = f.split(".")
  command = "/usr/local/bin/pdf2txt.py -o out/" + split[0] + ".txt input/" + f
  os.system(command)

outfiles = os.listdir("out")
with open("terms.txt") as termsfile:
  terms = termsfile.readlines()

results = []
for f in outfiles:
  results.append(f)
  lines = []
  with open("out/" + f) as f:
    text = f.readlines()
    lines = []
    index = 0
    for line in text:
      found = 0
      index += 1
      for term in terms:
        if term.lower().strip(' \t\n\r') + " " in line.lower():
          found += 1
      if found > 0:
        lines.append([index, found])
  results.append(lines)
pprint.pprint(results)
