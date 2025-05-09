import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np

from data_card import DataCard

import matplotlib.pyplot as plt


def get_roster():

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    }

    url = "https://www.tfrrs.org/teams/MO_college_m_SE_Missouri.html"

    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")

    # roster = soup.find('table', {'id': 'tablesaw-7595'})

    # somewhat hardcoding the location of the roster table, but isnt that what web scraping is anyway?
    roster_table = soup.select('table.tablesaw.table-striped.table-bordered.table-hover')[1]

    rows = roster_table.select('tr')

    for row in rows:

        
        athlete_link = row.select_one('a')

        if athlete_link is not None:
            print(athlete_link['href'])

        print("\n\n\n")
    

get_roster()