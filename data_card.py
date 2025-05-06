class DataCard:
    def __init__(self, athlete, event, result, meet, date):
        self.athlete = athlete
        self.event = event
        self.result = result
        self.meet = meet
        self.date = date

    def print_data():
        print("data")

    def to_dict(self):
        keys = ['athlete', 'event', 'result', 'meet', 'date']
        values = [self.athlete, self.event, self.result, self.meet, self.date]

        out = dict(zip(keys,values))

        return out

        