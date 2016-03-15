# Various search functions with the purpose of identifying
# and pulling out wanted data from parsed PDFs.

from util import *
import copy

# For all functions, `text` should be an array of lines.
# `Scan` functions perform searches of the text and return
# arrays of likely matches.  

class KeywordSearch:
  # Perform all available scans on the text and returns their results
  # an object like `{testName: [data1, data2], test2Name ...}
  @staticmethod
  def scanAllKeywords(text):
    results = {}
    results["nodes"] = KeywordSearch.nodeCountScan(text)
    results["vertexes"] = KeywordSearch.vertexCountScan(text)
    results["edges"] = KeywordSearch.loopCountScan(text)
    results["loops"] = KeywordSearch.loopCountScan(text)
    results["ratios"] = KeywordSearch.loopCountScan(text)
    results["centralities"] = KeywordSearch.loopCountScan(text)
    anyExist = False
    resultsCopy = copy.deepcopy(results)
    for key, item in results.iteritems():
      if item == []:
        del resultsCopy[key]
    return resultsCopy

  # for each occurance of `term` in `text`, `fun(lineIndex, text)` is run
  # and all results are returned in an array.
  @staticmethod
  def matchIterator(text, term, fun):
    for lineIndex, line in enumerate(text):
      if term.lower().strip(' \t\n\r') in line.lower(): # for every instnace of `term` in `text`,
        fun(lineIndex, text) # apply fun

  # Searches for text like `... there are 234 `term` in total. ...`
  @staticmethod
  def simpleNumericTermSearch(text, term):
    results = []
    fun = lambda lineIndex, text: results.append([lambda: "", lambda: text[lineIndex-1]][lineIndex != 0]() + text[lineIndex] + [lambda: "", lambda: text[lineIndex+1]][lineIndex < len(text)-1]() if number_nearby(term, lineIndex, text, 0) else False)
    KeywordSearch.matchIterator(text, term, fun)
    realResults = []
    for result in results:
      if result != False:
        realResults.append(result.strip(" \t\n\r"))
    return realResults

  # Matches text like `... includes 128,000 nodes in total ...`
  @staticmethod
  def nodeCountScan(text):
    return KeywordSearch.simpleNumericTermSearch(text, "nodes")

  # Matches text like `... up to 5023 vertices. ...`
  @staticmethod
  def vertexCountScan(text):
    return KeywordSearch.simpleNumericTermSearch(text, "vertexes") + KeywordSearch.simpleNumericTermSearch(text, "vertices")

  @staticmethod
  def edgeCountScan(text):
    return KeywordSearch.simpleNumericTermSearch(text, "edges")

  @staticmethod
  def loopCountScan(text):
    return KeywordSearch.simpleNumericTermSearch(text, "loops") + KeywordSearch.simpleNumericTermSearch(text, "multi-edges")

  # Attempts to find any ratios.  TODO tune
  @staticmethod
  def ratioScanner(text):
    return KeywordSearch.simpleNumericTermSearch(text, "ratio")

  # Looks for tablular data formats
  @staticmethod
  def tableScan(text):
    return # TODO

  # Looks for instances of centrality measurements
  @staticmethod
  def centalityScan(text):
    return KeywordSearch.simpleNumericTermSearch(text, "centrality") + KeywordSearch.simpleNumericTermSearch(text, "central")
