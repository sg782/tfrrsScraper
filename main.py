from scrape_athlete import get_single_athlete_data

data = get_single_athlete_data("https://www.tfrrs.org/athletes/7453592/SE_Missouri/Shea_Degraaf")
data = list(reversed(data))


event_history = {}

for data_card in data:
    event = data_card['event']

    if event not in event_history:
        event_history[event] = [data_card['result']]
    else:
        event_history[event].append(data_card['result'])


for ev in event_history:
    print(ev ,  " " , event_history[ev])

# print(event_history['PV'])

# plot_pv_data(event_history['PV'])
