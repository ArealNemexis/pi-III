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

    results = soup.find_all(class_='results-sublist')

    column_names = ["team1", "team2", "result1",
                    "result2", "date_of_match", "reference"]
    print(results[0])
    for l in results:
        df = pd.DataFrame(columns=column_names)
        title = l.find_all(class_='standard-headline')[0].text
        date_of_day = get_date(title)
        matches = l.find_all(class_='result-con')
        print()
        print(f"matches of {date_of_day}")
        for match in matches:
            link_of_match = match.find_all('a', href=True)[0]['href']
            team_1 = match.find_all('div', class_="team1")[
                0].find_all('div', class_="team")[0].text
            team_2 = match.find_all('div', class_="team2")[
                0].find_all('div', class_="team")[0].text
            team_1_result, team_2_result = map(lambda x: x.text, match.find_all(
                'td', class_="result-score")[0].find_all('span'))

            df.loc[len(df.index)] = [team_1, team_2, team_1_result,
                                    team_2_result, str(date_of_day), link_of_match]

        filename = f'general/{str(date_of_day)}.csv'
        # filename = f'csvs/{str(date_of_day)}.csv'
        if not os.path.isfile(filename):
            df.to_csv(filename, index=False)
        else:
            df.to_csv(filename, mode='a', header=False, index=False)


# print(matches)
