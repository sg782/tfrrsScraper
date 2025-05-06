import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

url = "https://www.tfrrs.org/athletes/8318488/SE_Missouri/Sullivan_Gleason.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
}


heights  = []

results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")

meet_results_div = soup.find("div", { "id": "meet-results" })

if meet_results_div:
    rows = meet_results_div.select("table tr td a")

    for row in rows:
        txt = row.text.strip()
        if(txt == "NH"):
            heights.append(0)
        else:
            heights.append(float(txt[:4]))

else:
    print("No div with id 'meet-results' found.")


def get_rolling_avg_n(data, n):
    out = []

    for i in range(len(data)):
        running_n = min(i,n)

        out.append(np.mean(data[i-running_n:i]))

    return out

# print(heights.reverse)

heights = list(reversed(heights))

running_average = get_rolling_avg_n(heights,2)


plt.plot(np.arange(len(heights)), running_average )
plt.show()


