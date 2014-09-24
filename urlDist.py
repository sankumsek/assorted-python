import urllib.request
import re

class Sitegram:
    def __init__(self, url):
        self.hist = {}
        text = urllib.request.urlopen(url).read().decode('UTF-8')
        number = re.findall("[A-Za-z]+", text)
        # Use re.findall() to get the words from text
        for n in number:
            if n not in self.hist:
                self.hist[n] = 1
            else:
                self.hist[n] += 1
        # Then count them up in self.hist

    def countOf(self, word):
        if number in self.hist:
            return self.hist[n]
        else:
            return 0
        # Check for the word; if present, return count;
        # if absent, return zero
        

class SearchData:
    def __init__(self):
        self.sites = {}

    def addSite(self, url):
        self.sites[url] = Sitegram(url)

    def rankedPages(self, term):
        pass
        # Your code here
