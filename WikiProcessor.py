import nltk  ##Installs Natural Language Processor
import urllib.request   ##Url Requester
import matplotlib   ##Allows us to Plot Properly
from bs4 import BeautifulSoup   ##Beautiful Soup to simplify html
from nltk.corpus import stopwords   ##Gets rid of 'a' 'the' etc

"""
Takes in the link and applies it to a variable link
which will be used to interpret wiki article
"""
link = input("Enter Wikipedia Link : ")

'''
Requests the url before reading through it
Then uses beautiful soup to simplify the html
'''
response = urllib.request.urlopen(link)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text(strip=True)

'''
Sections off each word into individual tokens 
within an array we could use 
'''
tokens = [t for t in text.split()]

'''
Uses english stopwords such as 'the' 'a' 'for' 
and creates a new array that doesnt contain the stopwords
'''
sr = stopwords.words('english')
clean_tokens = tokens[:]

for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

'''
Applies a value to the key given for how frequent the 
given word is found within our array 
'''
freq = nltk.FreqDist(clean_tokens)

for key, val in freq.items():
    print(str(key) + ':' + str(val))

'''
Creates a plot with our first 20 words
within the array and orders them by 
the frequency in which they are found 
'''
freq.plot(20, cumulative=False)


