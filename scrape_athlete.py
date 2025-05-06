import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np

from data_card import DataCard

import matplotlib.pyplot as plt

def get_single_athlete_data(url):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    }


    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")

    # get ahtlete name
    athlete_info = soup.select_one('h3.panel-title.large-title').text.strip()
    athlete_name = athlete_info.split("\n")[0]

    meet_results_div = soup.find("div", { "id": "meet-results" })

    data = []

    if meet_results_div:
        rows = meet_results_div.select("table")

        for row in rows:
            
            # split into header and footer
            header = row.find('thead')
            body = header.find_next_siblings("tr")

            
            meet = header.select_one("a").text.strip()
            date = header.select_one("span").text.strip()

            for event_data in body:

                tds = list(event_data.find_all("td"))

                event = tds[0].text.strip()

                result = tds[1]
                result_metric = result.a.text.strip()

                dc = DataCard(athlete_name, event, result_metric, meet, date)
                dc.format()

                data.append(dc.to_dict())

    else:
        print("No div with id 'meet-results' found.")

    return data




