## Use the BeautifulSoup and requests Python packages to print out a list of all
## the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests                         #libraries, require previous installation

url = 'https://www.nytimes.com/'        ## these two lines access the NY times
r = requests.get(url)                   ## homepage
soup = BeautifulSoup(r.text,"html.parser")            ## reads the page
                            ## have to use html.parser for 0 errors



## find and loop through all elements on page with class name story-heading
for story_heading in soup.find_all(class_="story-heading"):
    #for the story headings that are links, print out text
    #format
    #for others takes contents out
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())

