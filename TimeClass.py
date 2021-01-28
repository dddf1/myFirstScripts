import datetime


class Time:
    def __init__(self):
        self.time = datetime.datetime.now()

    def GetTime(self):
        return self.time

    def GetTimeWithoutDate(self):
        return self.time.strftime("%X")

    def GetTimeWithoutDateOrSeconds(self):
        return self.time.strftime("%H" + ":" + "%M")

    def GetYear(self):
        return self.time.strftime("%Y")

    def GetMonthAndDay(self):
        return self.time.strftime("%B" + ", " + "%A")

