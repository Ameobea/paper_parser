# Paper Parser
#### Casey Primozic

## Overview

### Description
Takes scientific or research papers as input.  Given a set of keywords or other identiers, it then searches them for sections of interest.  These areas of interest are then outputted for the user.  

Modules include a pdf reader for pdf-based papers and may also includea web parser in the future for papers located online.  

### Process
Given input pdfs in the input directory, it first splits them into individual pdfs by page.  Then it converts each of the split pages into text.  Once they have been split, it then converts them into text and runs the scoring function.  Once scores have been determined for each of the pages for each of the input documents, it returns a file (results.txt) which contains a report of the pages with the highest scores and thus the highest liklihood of containing useful data.

### PDF Parser
Converts a text-based PDF into plaintext words that can be searched.  Should take a regular pdf as input and process it automatically.

### Keyword Analysis
Keywords are identified that point to useful data from the bot.  They are then found within the parsed text from the pdfs and applied to filters.  These filters can do things such as only accept keywords that are near a number, or only return if the keyword occurs at the beginning or the end of a sentence.

### Manual Review
Once the keywords have been located and filtered, the results are parsed into JSON files and sent off to a Flask webserver.  They are then dumped into tables with check boxes for users to classify as useful or not useful.  At this point, it is also possible for data to be inserted into a database or recorded externally.

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

#### Flask
This is used to create the webserver that hosts the split pdfs, parsed text, and manual review modules.  In order to install it, follow the process on this page: http://flask.pocoo.org/docs/0.10/installation/

It boils down to the following:

`pip install Flask`
