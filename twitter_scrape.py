# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect their twitter feed.
# You'll notice that the tweets are stored in a ordered list <ol></ol>,
# and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and urllib to grab the text contents of the tweets
# located on the twitter page you chose.  The .text attribute will supply the content of a soup object.
# Have fun.  Again, nothing explicit. (15pts)
import urllib.request
from bs4 import BeautifulSoup

url = "https://twitter.com/neiltyson?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(),"html.parser")

print(soup.prettify())
data_list = [x.text.strip() for x in soup.findAll("p",{"class" : "js-tweet-text"})]

print(data_list)