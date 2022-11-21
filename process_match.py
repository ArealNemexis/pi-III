import requests
from bs4 import BeautifulSoup


url = "/matches/2360162/the-union-vs-oddik-liga-gamers-club-2022-serie-s-cup"


def get_teams_result(soup):
    return soup.select_one("div.team1-gradient.teamsBox.teamName")


def process_match(url):
    page = requests.get('https://www.hltv.org' + url)

    soup = BeautifulSoup(page.text, 'html.parser')

    print(get_teams_result(soup=soup))


process_match(url)