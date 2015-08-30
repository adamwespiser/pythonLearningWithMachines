#http://www.nltk.org/book/ch01.html
# Wespise#r


python:  from nltk.book import *
python:  text1
python:  text2


# Search, concordance is every mathcing word plus the surrounding text
python:  text1.concordance("monstrous")

# Search Fuzyy
python:  text1.similar("monstrous")

# Search for common context of a word, describes how different writers associate words:
python:  text2.common_contexts(["monstrous", "very"])

# shows word use through time for a given document
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# token counting
44764

# get the item set of words used in a docoment:
python:  len(set(text3)) 

# count unique words for a while document
python:  len(set(text3)) / len(text3)

#get word frequency
python:  text3.count("smote")
python:  100 * text4.count('a') / len(text4)


# Lex helpers functions
lexical_diversity <- function(text): 
	return len(set(text)) / len(text) 

percentage <- function(count, total): 
	return 100 * count / total

# Frequency stats for document bodies:
python: fdist1 = FreqDist(text1)
python:  fdist1.most_common(50)

# custom queries: How many times do words longer than 7 cgaracters show up?
python:  fdist5 = FreqDist(text5)
python: > sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)


