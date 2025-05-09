from scrape_athlete import get_single_athlete_data
from utils import plot_event_data

link = "https://www.tfrrs.org/athletes/8318488/SE_Missouri/Sullivan_Gleason.html"
data = get_single_athlete_data(link)
data = list(reversed(data))


event_history = {}

for data_card in data:
    event = data_card['event']

    if event not in event_history:
        event_history[event] = [data_card['result']]
    else:
        event_history[event].append(data_card['result'])

for ev in event_history:
    print(ev,event_history[ev])

for ev in event_history:
    plot_event_data(ev,event_history[ev])


