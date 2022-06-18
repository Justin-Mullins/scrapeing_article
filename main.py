'''

Scrape article

This ask the user for a url and then shows the article text, summary and title

'''
# Using this library to scrape text from artcles on the web.
from newspaper import Article
import nltk # For natural language processsing

nltk.download('punkt') 

url = input("Enter Url: ")

article = Article(url, language='en')

article.download()
article.parse() # Parse article
article.nlp()  # Perform natural language processoring

#To extract title
print("Article's Title:")
print(article.title)
print("")
 
#To extract text
print("Article's Text:")
print(article.text)
print("")
 
#To extract summary
print("Article's Summary:")
print(article.summary)
print("")