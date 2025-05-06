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
    
    

    def format(self):
        decimal_accuracy = 4

        #general formatting

        #
        # 1. remove 'm'
        # 2. replace 'NH', 'DNS', 'DNF', 'FOUL', with 0
        # 3. convert all times into a decimal form of minutes 
        #    - I have not seen how hours are represented, so we will just treat that as an edge case that we havent supported untilwe run across it :P
        #

        self.result = self.result.replace("m","")

        if(self.result in ['NH', 'DNS', 'DNF' ,'FOUL']): # is this list exhaustive?
            self.result = '0'

        if(":" in self.result):

            minutes, seconds = self.result.split(":")

            minutes = float(minutes)
            seconds = float(seconds)

            time = minutes + seconds / 60.

            
            rounded_time = round(time,decimal_accuracy)


            self.result = rounded_time
