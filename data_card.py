import datetime


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
    
    def format_time(self):
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        #
        # 1. remove commas
        # 2. if meet was multiple days, only choose first day listed
        # 3. convert to python datetime object
        #

        date_one = self.date[:6].split() #single digit days are given a double space, lets us use this simple indexing

        month = months.index(date_one[0]) + 1
        day = int(date_one[1])
        year = int(self.date[-4:])


        try:
            self.date = datetime.datetime(year, month, day)
        except:
            print("Error converting Date: ", self.date)
            self.date = datetime.datetime(1971,1,1)




        # what if a meet has multiple years in it (happened over new years?)


    def format_result(self):
        decimal_accuracy = 4

        #general formatting

        #
        # 1. remove 'm'
        # 2. replace 'NH', 'DNS', 'DNF' ,'FOUL', 'FS', 'DQ', 'NM', 'NP', 'NT', with 0
        # 3. convert all times into a decimal form of minutes 
        #    - I have not seen how hours are represented, so we will just treat that as an edge case that we havent supported untilwe run across it :P
        #


        # should add in try catch but ion wanna
        self.result = self.result.replace("m","")

        if(self.result in ['NH', 'DNS', 'DNF' ,'FOUL', 'FS', 'DQ', 'NM', 'NP', 'NT']): # is this list exhaustive?
            self.result = '0'

        if(":" in self.result):

            minutes, seconds = self.result.split(":")

            minutes = float(minutes)
            seconds = float(seconds)

            time = minutes + seconds / 60.          
            rounded_time = round(time,decimal_accuracy)

            self.result = rounded_time


        try:
            self.result = float(self.result)
        except:
            # print for debuggin
            print("Athlete with bad data: ", self.athlete)
            print("\t" , self.event, self.result)

    def format(self):
        self.format_result()
        self.format_time()

        
