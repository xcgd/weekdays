import calendar
import datetime
from dateutil import rrule
from weekdays import BusinessCalendar
import dateutil


def test_calendar_list_of_days():
    year = 2013
    month = 11
    weekstartday = calendar.MONDAY
    weekoff = [rrule.SA, rrule.SU]
    holidays = [
        datetime.datetime(2013, 11, 1),
        datetime.datetime(2013, 11, 11),
    ]
    c = BusinessCalendar(weekstartday, weekoff, holidays)
    res = c.get_month_business_days(year, month)
    assert res == [
        datetime.datetime(2013, 11, 4, 0, 0),
        datetime.datetime(2013, 11, 5, 0, 0),
        datetime.datetime(2013, 11, 6, 0, 0),
        datetime.datetime(2013, 11, 7, 0, 0),
        datetime.datetime(2013, 11, 8, 0, 0),
        datetime.datetime(2013, 11, 12, 0, 0),
        datetime.datetime(2013, 11, 13, 0, 0),
        datetime.datetime(2013, 11, 14, 0, 0),
        datetime.datetime(2013, 11, 15, 0, 0),
        datetime.datetime(2013, 11, 18, 0, 0),
        datetime.datetime(2013, 11, 19, 0, 0),
        datetime.datetime(2013, 11, 20, 0, 0),
        datetime.datetime(2013, 11, 21, 0, 0),
        datetime.datetime(2013, 11, 22, 0, 0),
        datetime.datetime(2013, 11, 25, 0, 0),
        datetime.datetime(2013, 11, 26, 0, 0),
        datetime.datetime(2013, 11, 27, 0, 0),
        datetime.datetime(2013, 11, 28, 0, 0),
        datetime.datetime(2013, 11, 29, 0, 0),
    ]


def test_calendar_list_of_days_rrule_args():
    year = 2013
    month = 11
    weekstartday = calendar.MONDAY
    weekoff = [rrule.SA, rrule.SU]
    holidays = [
        {'freq':dateutil.rrule.YEARLY, 'bymonthday':1, 'bymonth':11},
        {'freq':dateutil.rrule.YEARLY, 'bymonthday':11, 'bymonth':11},
    ]
    c = BusinessCalendar(weekstartday, weekoff, holidays)
    res = c.get_month_business_days(year, month)
    assert res == [
        datetime.datetime(2013, 11, 4, 0, 0),
        datetime.datetime(2013, 11, 5, 0, 0),
        datetime.datetime(2013, 11, 6, 0, 0),
        datetime.datetime(2013, 11, 7, 0, 0),
        datetime.datetime(2013, 11, 8, 0, 0),
        datetime.datetime(2013, 11, 12, 0, 0),
        datetime.datetime(2013, 11, 13, 0, 0),
        datetime.datetime(2013, 11, 14, 0, 0),
        datetime.datetime(2013, 11, 15, 0, 0),
        datetime.datetime(2013, 11, 18, 0, 0),
        datetime.datetime(2013, 11, 19, 0, 0),
        datetime.datetime(2013, 11, 20, 0, 0),
        datetime.datetime(2013, 11, 21, 0, 0),
        datetime.datetime(2013, 11, 22, 0, 0),
        datetime.datetime(2013, 11, 25, 0, 0),
        datetime.datetime(2013, 11, 26, 0, 0),
        datetime.datetime(2013, 11, 27, 0, 0),
        datetime.datetime(2013, 11, 28, 0, 0),
        datetime.datetime(2013, 11, 29, 0, 0),
    ]


def test_calendar_list_of_weeks():
    year = 2013
    month = 11
    weekstartday = calendar.MONDAY
    weekoff = [rrule.SA, rrule.SU]
    holidays = [
        datetime.datetime(2013, 11, 1),
        datetime.datetime(2013, 11, 11),
    ]
    c = BusinessCalendar(weekstartday, weekoff, holidays)
    res = c.get_weeks_business_days(year, month)

    assert res == [
        [],
        [
            datetime.datetime(2013, 11, 4, 0, 0),
            datetime.datetime(2013, 11, 5, 0, 0),
            datetime.datetime(2013, 11, 6, 0, 0),
            datetime.datetime(2013, 11, 7, 0, 0),
            datetime.datetime(2013, 11, 8, 0, 0),
        ],
        [
            datetime.datetime(2013, 11, 12, 0, 0),
            datetime.datetime(2013, 11, 13, 0, 0),
            datetime.datetime(2013, 11, 14, 0, 0),
            datetime.datetime(2013, 11, 15, 0, 0),
        ],
        [
            datetime.datetime(2013, 11, 18, 0, 0),
            datetime.datetime(2013, 11, 19, 0, 0),
            datetime.datetime(2013, 11, 20, 0, 0),
            datetime.datetime(2013, 11, 21, 0, 0),
            datetime.datetime(2013, 11, 22, 0, 0),
        ],
        [
            datetime.datetime(2013, 11, 25, 0, 0),
            datetime.datetime(2013, 11, 26, 0, 0),
            datetime.datetime(2013, 11, 27, 0, 0),
            datetime.datetime(2013, 11, 28, 0, 0),
            datetime.datetime(2013, 11, 29, 0, 0),
        ],
    ]


def test_calendar_list_of_weeks_rrule_args():
    year = 2013
    month = 11
    weekstartday = calendar.MONDAY
    weekoff = [rrule.SA, rrule.SU]
    holidays = [
        {'freq':dateutil.rrule.YEARLY, 'bymonthday':1, 'bymonth':11},
        {'freq':dateutil.rrule.YEARLY, 'bymonthday':11, 'bymonth':11},
    ]
    c = BusinessCalendar(weekstartday, weekoff, holidays)
    res = c.get_weeks_business_days(year, month)

    assert res == [
        [],
        [
            datetime.datetime(2013, 11, 4, 0, 0),
            datetime.datetime(2013, 11, 5, 0, 0),
            datetime.datetime(2013, 11, 6, 0, 0),
            datetime.datetime(2013, 11, 7, 0, 0),
            datetime.datetime(2013, 11, 8, 0, 0),
        ],
        [
            datetime.datetime(2013, 11, 12, 0, 0),
            datetime.datetime(2013, 11, 13, 0, 0),
            datetime.datetime(2013, 11, 14, 0, 0),
            datetime.datetime(2013, 11, 15, 0, 0),
        ],
        [
            datetime.datetime(2013, 11, 18, 0, 0),
            datetime.datetime(2013, 11, 19, 0, 0),
            datetime.datetime(2013, 11, 20, 0, 0),
            datetime.datetime(2013, 11, 21, 0, 0),
            datetime.datetime(2013, 11, 22, 0, 0),
        ],
        [
            datetime.datetime(2013, 11, 25, 0, 0),
            datetime.datetime(2013, 11, 26, 0, 0),
            datetime.datetime(2013, 11, 27, 0, 0),
            datetime.datetime(2013, 11, 28, 0, 0),
            datetime.datetime(2013, 11, 29, 0, 0),
        ],
    ]


def test_calendar_list_of_week_count():
    year = 2013
    month = 11
    weekstartday = calendar.MONDAY
    weekoff = [rrule.SA, rrule.SU]
    holidays = [
        datetime.datetime(2013, 11, 1),
        datetime.datetime(2013, 11, 11),
    ]
    c = BusinessCalendar(weekstartday, weekoff, holidays)
    res = c.get_weeks_daycount(year, month)
    assert res == [0, 5, 4, 5, 5]


def test_calendar_list_of_week_count_rrule_args():
    year = 2013
    month = 11
    weekstartday = calendar.MONDAY
    weekoff = [rrule.SA, rrule.SU]
    holidays = [
        {'freq':dateutil.rrule.YEARLY, 'bymonthday':1, 'bymonth':11},
        {'freq':dateutil.rrule.YEARLY, 'bymonthday':11, 'bymonth':11},
    ]
    c = BusinessCalendar(weekstartday, weekoff, holidays)
    res = c.get_weeks_daycount(year, month)
    assert res == [0, 5, 4, 5, 5]
