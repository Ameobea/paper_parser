# Downloads pdfs from arxiv based on a query.

import getopt, sys, pprint, os
import arxiv

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "q:l:o", ["query=", "limit=", "output="])
  except:
    print 'Use syntax: python arxiv-downloader.py -q "network node centrality" -l 50 -o ./input'
    sys.exit(2)

  # Init defaults
  limit = 10
  query = False
  outputDirectory = "./input"

  # Parse arguments
  for opt, arg in opts:
    if opt == "-q":
      query = arg
    elif opt == "-h":
      print 'Use syntax: python arxiv-downloader.py -q "network node centrality" -l 50 -o ./input'
    elif opt == "l":
      limit = arg
    elif opt == "o":
      outputDirectory = arg

  if not(query):
    print 'Use syntax: python arxiv-downloader.py -q "network node centrality" -l 50 -o ./input'
    sys.exit(2)

  if not(os.path.isdir(outputDirectory)):
    print "Given output directory is not a directory."
    sys.exit(2)
  else:
    os.chdir(outputDirectory)

  res = arxiv.query(query, prune=True, start=0, max_results=limit)

  i = 0
  results = []

  # Display titles
  for elem in res:
    for key in elem:
      if key == "title":
        i += 1
        results.append(elem)
        print str(i) + ". " + elem[key] + "\n"

  toDownload = input("Enter the numbers of the papers you want to download separated by commas: \n")

  try:
    iterator = iter(toDownload)
  except TypeError:
    arxiv.download(results[toDownload])
  else:
    for elem in toDownload:
      arxiv.download(results[elem])
    

if __name__ == "__main__":
  main(sys.argv[1:])
