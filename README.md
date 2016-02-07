# Paper Parser
#### Casey Primozic

## Overview

### Description
Takes scientific or research papers as input.  Given a set of keywords or other identiers, it then searches them for sections of interest.  These areas of interest are then outputted for the user.  
Modules include a pdf reader for pdf-based papers and a web parser for papers located online.  

### Process
Given input pdfs in the input directory, it first splits them into individual pdfs by page.  Then it converts each of the split pages into text.  Once they have been split, it then converts them into text and runs the scoring function.  Once scores have been determined for each of the pages for each of the input documents, it returns a file (results.txt) which contains a report of the pages with the highest scores and thus the highest liklihood of containing useful data.

### PDF Parser
Converts a text-based PDF into plaintext words that can be searched.  Should take a regular pdf as input and process it automatically.

### Text Analysis
Attempts to identify areas of interest in the text.  These areas are identified using one or more of the following methods:

#### Keyword Matching
Simply searches the text for matches from a list of words or phrases.  Can assign a score to pages/sub-pages based on the amount or quality of matches.  

#### Similarity Indexer
Given a sample text or texts, attempts to find areas of a paper that are similar to another.  Can be run using one or multiple reference texts which will return a similarity score.  

## Setup and Execution

### Installation
This program requires python; developed and tested using python 2.7.6

To install, simply run the command `git clone https://github.com/Ameobea/paper_parser.git` and then navigate to paper_parser directory that is created.

### Execution
To run the processing script, fill the input directoy with pdfs to be processed.  Then edit the `terms.txt` file and add, one per line, keywords that you'd like the tool to search for.  Then, run the `run.sh` script and the files will automatically be processed.  This will automatically clear the old data out of the `out` and `split` directories.  You can view the results in `results.txt`.

If you would like to re-run the scoring section of the program without re-splitting and processing the input data, run the command `python process.py` which will only run the scoring section of the process, allowing you to change the keywords in `terms.txt` without having to re-process all the input documents.

#### Dependencies
##### PDFMiner
The pdfminer suite is used to process the journal PDFs and convert them into plaintext which can be analyzed and processed for keywords and identifying areas of interest.  

PDFMiner can be downloaded from here: https://github.com/euske/pdfminer

In the project's root directory, run the command `git clone https://github.com/euske/pdfminer.git pdfminer` to clone it to the correct directory.  Then navigate to the pdfminer directory and run the command `python install.py` to build the package and install it.  See the PDFMiner reference on github for more information.  

##### PyPDF2
This utility is useful for its ability to split pdfs into individual pages.  This allows each page to be converted and processed individually giving us the ability to assign pages scores based on the number and quality of keywords matched.  

It can be downloaded from here: https://pypi.python.org/pypi/PyPDF2/1.25.1

To install it, navigate to the extracted folder and run the command "python setup.py install" which will install the utility on the machine.  
