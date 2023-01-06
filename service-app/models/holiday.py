from datetime import datetime


class Holiday(object):
    def __init__(self, date, holiday_weight, day_weight):
        self.date = date
        self.holiday_weight = holiday_weight
        self.day_weight = day_weight

    def get_date(self):
        return datetime.strptime(self.date, '%Y-%m-%d').date()
