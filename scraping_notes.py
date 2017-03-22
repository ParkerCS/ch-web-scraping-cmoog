'''
my_list = [7,7,3,3,5,5,9,0,3,8]
new_list = [x for x in my_list if x > 5]
'''


#print(new_list)

import matplotlib.pyplot as plt
import numpy as np


#THE UGLY SIDE OF SCRAPING

import urllib.request
from bs4 import BeautifulSoup
url = "https://www.google.com/finance/historical?q=NASDAQ%3AAAPL&ei=bx3SWJnvAsfDjAGq1p_YCw"

#CLEANING UP AROUND THE EDGES ON WEB SCRAPING
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(),"lxml")
#UGGHGHHGHG
# If it's broke, try lxml
# heals the self closing tag problem amongst other problems

#print(soup.prettify())

# THESE LISTS AND FOR LOOPS ARE ANNOYING!!!
# SYNTACTIC SUGAR TO THE RESCUE >>>> COMPREHENSION LIST
# my_new_list = [x(returned) for x(input) in list(input) if(condition)]
rows = [x for x in soup.findAll("table")[3].findAll("tr")]

#print(rows)
headers = rows[0].findAll("th")
headers = [x.text.strip() for x in headers]
print(headers)

data = rows[1:]
#data = [x. for x in rows]
data = [x.findAll("td") for x in data]
print(data)

for i in range(len(data)):
    data[i] = [x.text.strip() for x in data[i]]

print(data)

dates = [x[0] for x in data]
closings = [float(x[-2]) for x in data]
print(closings)
plt.figure(tight_layout=True)
plt.plot(np.arange(len(closings)), closings)
plt.xticks(np.arange(len(closings)), dates, rotation=90)
plt.show()





