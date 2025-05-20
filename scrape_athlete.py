import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np

from data_card import DataCard
from athlete_data import AthleteData

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

    athlete_data_obj = AthleteData(athlete_name)

    meet_results_div = soup.find("div", { "id": "meet-results" })

    data = []

    if meet_results_div:

        # some results are metric, some are imperial, either way, both are supported, just not always in the same column.
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


                # sometimes
                result_a = result.a.text.strip()

                # if it is in imperial units
                if("'" in result_a):
                    try:
                        # if there is another result
                        result_a = result.find_all("span")[1].text.strip()
                    except:
                        print("Issue found", result_a)

                dc = DataCard(athlete_name, event, result_a, meet, date)
                dc.format()

                athlete_data_obj.add_data_card(dc)

                # data.append(dc.to_dict())

    else:
        print("No div with id 'meet-results' found.")

    return athlete_data_obj




