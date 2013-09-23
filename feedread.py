import feedparser
from flask import Flask

app = Flask(__name__)


#hard code RSS feed URL into code
gov_rss_url = "http://www.civilservice.gov.uk/feed"


#grab feed data
var = feedparser.parse(gov_rss_url)

gov_links = []
def FeedDisplay():
	#loop through all entries in feed 
	for x in range(0, len(var.entries)):
	
		#collate web URLs for pages to variable
		gov_links.append(var.entries[x].link)

	return gov_links

if __name__ == "__main__":
    app.run()
