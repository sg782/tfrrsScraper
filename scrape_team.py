import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np

from data_card import DataCard
from scrape_athlete import get_single_athlete_data

import matplotlib.pyplot as plt



def get_roster_links(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    }


    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")

    # roster = soup.find('table', {'id': 'tablesaw-7595'})

    # somewhat hardcoding the location of the roster table, but isnt that what web scraping is anyway?
    roster_table = soup.select('table.tablesaw.table-striped.table-bordered.table-hover')[1]

    rows = roster_table.select('tr')

    links = []
    base_url = "https://www.tfrrs.org"

    for row in rows:
        athlete_link = row.select_one('a')

        if athlete_link is not None:
            extension = athlete_link['href']

            links.append(base_url + extension)

    return links



def get_team_results(team_link):
    athlete_data_list = []

    roster_links = get_roster_links(team_link)

    for link in roster_links:
        athlete_data = get_single_athlete_data(link)
        athlete_data_list.append(athlete_data)

    return athlete_data_list
