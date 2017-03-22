'''
Web Scraping Example #2
NBA Player Stats
'''

import urllib.request
from bs4 import BeautifulSoup

url = "http://www.nba.com/celtics/stats"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

my_table = soup.find("table", {"class" : "player-stats"}) # target a specific table
print(my_table.prettify())


rows = my_table.findAll("tr") # tr is table row

player_stat_list = []


player_names = []
for row in rows:
    try:
        name = row.find("span", {"class" : "playerName"})
        player_names.append(name.text.strip())
    except:
        pass


print(player_names)

for row in rows:
    row_data = []
    cells = row.findAll("td") # td is table data
    for cell in cells:
        row_data.append(cell.text.strip())
    player_stat_list.append(row_data)

player_stat_list = player_stat_list[1:]
print(player_stat_list)