class AthleteData:
    def __init__(self,athlete):
        self.athlete = athlete
        self.results = []

    def add_data_card(self, data_card):
        # just a big list of all results
        self.results.append(data_card)

    def get_data_cards_by_event(self):
        if(len(self.results) ==0):
            return []
        

        event_history = {}
        
        for data_card in self.results:
            event = data_card.event

            if event not in event_history:
                event_history[event] = [data_card]
            else:
                event_history[event].append(data_card)

        return event_history
    
    

