#!/usr/bin/python

## basic
import urllib2
from bs4 import BeautifulSoup
target_website = "http://www.realclearpolitics.com/2015/08/27/"
html = urllib2.urlopen(target_website).read()

soup = BeautifulSoup(open(doc.html))
soup.prettify() 
soup.get_text(


## NLP for currated data sources:
import nltk
from nltk.corpus import brown
brown.words()
rom nltk.collocations import *
## bigram measures
bigram_measures = nltk.collocations.BigramAssocMeasures()
dir(bigram_measures)
## trigram reps
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(nltk.corpus.genesis.words('english-web.txt'))
finder.nbest(bigram_measures.pmi, 10)

nltk.corpus.genesis.words('english-web.txt')
len(nltk.corpus.genesis.words('english-web.txt'))
nltk.corpus.genesis.words('english-web.txt')[1:100]


## Moby Dick
from nltk.book import *
text1.concordance("monstrous")


text1.similar("monstrous")
text2.similar("monstrous")
text1.similar("love")
text2.similar("monstrous")
test1.similar("love"))
test2.similar("love"))
test1.similar("wanter"))
test2.similar("water"))

from nltk.book import *

## nlp on website
import urllib2
from bs4 import BeautifulSoup
target_website = "http://www.realclearpolitics.com/2015/08/27/"
html = urllib2.urlopen(target_website).read()

soup = BeautifulSoup(html)
soup.prettify()
soup.get_text() 


## download nltk data/packages
import nltk
import nltk.download()

## grab words from a text corpus
from mltk.corpus import brown
brown.words()

## bigram measurements
from nltk.corpus import brown
brown.words()

$$ bigram association
from nltk.collections import *
bigram_measures = nltk.collocations.BigramAssocMeasures()





