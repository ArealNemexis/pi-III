from datetime import date
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

enum_month = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def get_date(raw_title: str):
    _, _, month, day, year = raw_title.split()
    day = ''.join(l for l in day if l.isdigit())

    return date(day=int(day), month=int(enum_month[month.lower()]), year=int(year))


url = 'https://www.hltv.org/results?offset='
offsets = [0]
offsets.extend(list(range(100, 2600, 100)))


for offset in offsets:
    page = requests.get(f"{url}{offset}")

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')

    itens = soup.select('.result-con a',)

    for item in itens:
        print(item['href'])