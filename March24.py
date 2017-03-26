import urllib.request
from bs4 import BeautifulSoup

url = "http://www.theus50.com/fastfacts/population.php"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

data_list = [[y.text.strip() for y in x.findAll("td")] for x in soup.find("table",{"class" : "table"}).findAll("tr")]

population = [int(x[2].replace(",","")) for x in data_list[1:]]
print(population)

state_list = [x[1] for x in data_list[1:]]
print(state_list)