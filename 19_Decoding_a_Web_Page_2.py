## Using the requests and BeautifulSoup Python libraries, print to the screen the
## full text of the article on this website.
## http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
## The article is long so it is split up bbetween 4 pages. Your task is to print
## out the text to the screen so that you can read the full article without
## having to click any buttons. This will just print the full text of the article
## to the screen. It won't be easy to read.

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
soup = BeautifulSoup(r.text,'html.parser')

## kills all script and style elements
for script in soup(['script', 'style']):
    script.extract()    ## rip it out
## get text
text = soup.get_text()

## break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
## break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
## drop blank lines
text = '\n'.join(elem for elem in chunks if elem)

print(text)



