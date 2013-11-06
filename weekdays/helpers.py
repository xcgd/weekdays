import datetime
from weekdays import get_business_days
import calendar


class BusinessCalendar(calendar.Calendar):

    def __init__(self, weekstartday, weekoff, holidays):

        self.weekstartday = weekstartday
        self.weekoff = weekoff
        self.holidays = holidays

        super(BusinessCalendar, self).__init__(weekstartday)

    def get_month_business_days(self, year, month):
        """given a year and a month returns the business days for this month
        respecting the rules that were give during calendar initialisation.
        """
        start = datetime.datetime(year, month, 1, 0, 0)
        # get last day of the desired month
        lastdaynum = calendar.monthrange(year, month)[1]
        end = datetime.datetime(year, month, lastdaynum, 0, 0)

        return get_business_days(start, end, self.weekoff, self.holidays)
