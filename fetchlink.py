import re 
import linkGrabber

links=linkGrabber.Links('https://www.google.com/search?client=firefox-b-d&q=king')
gb=links.find(limit=4,duplicates=False,pretty=True)
print(gb)