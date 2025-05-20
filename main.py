from scrape_athlete import get_single_athlete_data
from utils import plot_event_data
from scrape_team import get_team_results

link = "https://www.tfrrs.org/athletes/7453592"
data = get_single_athlete_data(link)

# print(data.get_data_cards_by_event())
# # data = list(reversed(data))


# event_history = {}

# for data_card in data:
#     event = data_card['event']

#     if event not in event_history:
#         event_history[event] = [data_card['result']]
#     else:
#         event_history[event].append(data_card['result'])

# for ev in event_history:
#     print(ev,event_history[ev])

# # for ev in event_history:
# #     plot_event_data(ev,event_history[ev])


# team_link = "https://www.tfrrs.org/teams/MO_college_m_SE_Missouri.html"
# data = get_team_results(team_link)

# print(data)
