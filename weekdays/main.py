from dateutil import rrule


def get_business_days(alpha, omega, weekoff=None, holidays=None):
    """return a list of business days between (inclusive) the
    from and to limits.
    @type alpha: datetime.datetime
    @type omega: datetime.datetime
    @param weekoff: a list of non working days in a normal week
    @type weekend: list of rrule.weekdays. Ex: [rrule.SA, rrule.SU]
    @param holidays: a list of special non working days
    @type holidays: list of datetime.datetime.
        ex: [datetime.datetime(2013, 11, 11)]
    """
    # create an rrule.rruleset instance
    dates = rrule.rruleset()

    # this set is INCLUSIVE of alpha and omega
    dates.rrule(rrule.rrule(
        rrule.DAILY, dtstart=alpha, until=omega)
    )

    if weekoff:
        # here's where we exclude the weekend dates
        dates.exrule(rrule.rrule(
            rrule.DAILY, byweekday=weekoff, dtstart=alpha)
        )

    if holidays:
        result = [day for day in dates if day not in holidays]
    else:
        result = list(dates)

    return result
