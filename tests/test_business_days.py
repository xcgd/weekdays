import datetime
from dateutil import rrule
from weekdays import get_business_days


def test_simple_week():
    start = datetime.datetime(2013, 11, 1)
    end = datetime.datetime(2013, 11, 3)
    nonworkingdays = [rrule.SA, rrule.SU]

    res = get_business_days(start, end, nonworkingdays)
    print "Res: %s" % res
    assert res == [datetime.datetime(2013, 11, 1, 0, 0)]


def test_naive_full_month():
    start = datetime.datetime(2013, 11, 1)
    end = datetime.datetime(2013, 11, 30)
    nonworkingdays = [rrule.SA, rrule.SU]

    res = get_business_days(start, end, nonworkingdays)
    print "Res: %s" % res
    assert res == [
        datetime.datetime(2013, 11, 1, 0, 0),
        datetime.datetime(2013, 11, 4, 0, 0),
        datetime.datetime(2013, 11, 5, 0, 0),
        datetime.datetime(2013, 11, 6, 0, 0),
        datetime.datetime(2013, 11, 7, 0, 0),
        datetime.datetime(2013, 11, 8, 0, 0),
        datetime.datetime(2013, 11, 11, 0, 0),
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


def test_full_month():
    start = datetime.datetime(2013, 11, 1)
    end = datetime.datetime(2013, 11, 30)
    nonworkingdays = [rrule.SA, rrule.SU]
    holidays = [
        datetime.datetime(2013, 11, 1),
        datetime.datetime(2013, 11, 11),
    ]

    res = get_business_days(start, end, nonworkingdays, holidays=holidays)
    print "Res: %s" % res
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
