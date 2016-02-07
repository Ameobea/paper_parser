# Main file for the parser.  It reads in all the files in
# the input folder and converts all pdfs that it can into
# txt files located in the out directory.  It then returns
# the line numbers of all matched terms in `terms.txt`.
# It then returns the number of times terms were matched
# for each line.

import subprocess
import os
import pprint
from PyPDF2 import PdfFileWriter, PdfFileReader

# Only convert files if the output directory is empty
if len(os.listdir("out")) == 0:
  # Split all pdfs in the input directory into pages
  pprint.pprint("Splitting pdfs into pages...")
  for f in os.listdir("input"):
    infile = PdfFileReader(open("input/"+f, 'rb'))

    for i in xrange(infile.getNumPages()):
      p = infile.getPage(i)
      outfile = PdfFileWriter()
      outfile.addPage(p)
      reali = i+1
      with open('split/'+f.split(".")[0].replace("-","_").replace("+","_")+'+page-%02d.pdf' % reali, 'wb') as f3:
        outfile.write(f3)

  # Process each file in the split directory
  pprint.pprint("converting split pdfs into text...")
  infiles = os.listdir("split")
  for f in infiles:
    split = f.split(".")
    command = "/usr/local/bin/pdf2txt.py -o out/" + split[0] + ".txt split/" + f
    os.system(command)

  # Output processed text files to the out directory
  out_file_names = os.listdir("out")
  with open("terms.txt") as termsfile:
    terms = termsfile.readlines()

out_file_names = os.listdir("out")

with open("terms.txt") as termsfile:
  terms = termsfile.readlines()

# For every line in the converted files, check the number of keywords
# that match and return a score for each line with matched keywords.  
results = []
for file_name in out_file_names:
  results.append([file_name])
  with open("out/" + file_name) as out_file:
    text = out_file.readlines()
    lines = []
    index = 0
    for line in text:
      found = 0
      index += 1
      for term in terms:
        if term.lower().strip(' \t\n\r') in line.lower():
          found += 1
      if found > 0:
        lines.append([index, found])
  results[len(results)-1].append(len(lines))

results = sorted(results, key=lambda x: (x[0].split("+")[0], x[1]), reverse=True)
#pprint.pprint(results)
results_file = open('results.txt','w')
results_file.write("The following is a list of the documents, their pages, and the corresponding score per page.\n")
results_file.write("The higher the score, the more keywords were matched meaning the higher chance there is usful data on that page.\n")

index = -1
for page in results:
  index += 1
  if(index == 0 or (index > 0 and results[index-1][0].split("+")[0] != results[index][0].split("+")[0])):
    results_file.write("\n"+results[index][0].split("+")[0]+":\n")
  results_file.write("Page "+page[0].split("-")[1].split(".")[0]+": "+str(page[1])+"\n")
