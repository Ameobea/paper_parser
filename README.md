# Paper Parser
#### Casey Primozic

## Overview

### Description
Takes scientific or research papers as input.  Given a set of keywords or other identiers, it then searches them for sections of interest.  These areas of interest are then outputted for the user.  
Modules include a pdf reader for pdf-based papers and a web parser for papers located online.  

### PDF Parser
Converts a text-based PDF into plaintext words that can be searched.  Should take a regular pdf as input and process it automatically.

### Web Scraper
Given a page, list of pages, crawl pattern, reads or downloads all pages listed for further processing or scraping.  

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

#### Dependencies
The pdfminer suite is used to process the journal PDFs and convert them into plaintext which can be analyzed and processed for keywords and identifying areas of interest.  

PDFMiner can be downloaded from here: https://github.com/euske/pdfminer

In the project's root directory, run the command `git clone https://github.com/euske/pdfminer.git pdfminer` to clone it to the correct directory.  Then navigate to the pdfminer directory and run the command `python install.py` to build the package and install it.  See the PDFMiner reference on github for more information.  
