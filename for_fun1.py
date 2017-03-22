from bs4 import BeautifulSoup
import urllib.request
from operator import itemgetter

url= 'http://www.cbssports.com/collegebasketball/ncaa-tournament/brackets/viewable_men'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")


print(soup.prettify())


# Find the tags which hold the name and seeds
my_teams = soup.findAll("span",{"class" : "name"})
my_seeds = soup.findAll("span", {"class" : "seed"})

team_list = []
seed_list = []

# Add teams to team_list
for team in my_teams:
    print(team.text)
    if len(team.text) > 0:
        team_list.append([team.text])
# Add seeds to the team_list
i = 0
for seed in my_seeds:
    print(seed.text)
    if len(seed.text) > 0:
        team_list[i].append(int(seed.text))
        i += 1

team_list.sort(key=itemgetter(1))

print(team_list)
