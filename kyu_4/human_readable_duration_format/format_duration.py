#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/


def format_duration(seconds: int) -> str:
    """
    A function which formats a duration, given as a
    number of seconds, in a human-friendly way.

    The resulting expression is made of components like 4 seconds,
    1 year, etc. In general, a positive integer and one of the
    valid units of time, separated by a space. The unit of time
    is used in plural if the integer is greater than 1.

    The components are separated by a comma and a space (", ").
    Except the last component, which is separated by " and ", just
    like it would be written in English.

    A more significant units of time will occur before than a least
    significant one. Therefore, 1 second and 1 year is not correct,
    but 1 year and 1 second is.

    Different components have different unit of times. So there is
    not repeated units like in 5 seconds and 1 second.

    A component will not appear at all if its value happens to be zero.
    Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

    A unit of time must be used "as much as possible". It means that the
    function should not return 61 seconds, but 1 minute and 1 second instead.
    Formally, the duration specified by of a component must not be greater than
    any valid more significant unit of time.
    :param seconds:
    :return:
    """

    if seconds == 0:
        return 'now'

    result = ''

    years = calc_years(seconds)
    days = calc_days(seconds)
    hours = calc_hours(seconds)
    minutes = calc_minutes(seconds)
    seconds = calc_seconds(seconds)

    if years > 0:
        result += '{}'.format(get_string(years, 'year'))

    if days > 0:
        if result != '':
            result += ', {}'.format(get_string(days, 'day'))
        else:
            result += '{}'.format(get_string(days, 'day'))

    if hours > 0:
        if result != '':
            result += ', {}'.format(get_string(hours, 'hour'))
        else:
            result += '{}'.format(get_string(hours, 'hour'))

    if minutes > 0:
        if result != '':
            if seconds == 0:
                result += ' and {}'.format(get_string(minutes, 'minute'))
            else:
                result += ', {}'.format(get_string(minutes, 'minute'))
        else:
            result += '{}'.format(get_string(minutes, 'minute'))

    if seconds > 0:
        if result != '':
            result += ' and {}'.format(get_string(seconds, 'second'))
        else:
            result += '{}'.format(get_string(seconds, 'second'))

    return result


def get_string(number: int, string: str) -> str:
    """
    Concatenate string result
    :param number:
    :param string:
    :return:
    """

    if number > 0:
        if number == 1:
            return '{} {}'.format(number, string)
        else:
            return '{} {}s'.format(number, string)


def calc_seconds(seconds: int) -> int:
    """
    Calculate seconds
    :param seconds:
    :return:
    """

    if seconds < 60:
        return seconds

    return seconds % 60


def calc_minutes(seconds: int) -> int:
    """
    calculate minutes
    :param seconds:
    :return:
    """
    minutes = seconds // 60
    if minutes < 60:
        return minutes
    else:
        return minutes % 60


def calc_hours(seconds: int) -> int:
    """
    Calculate hours
    :param seconds:
    :return:
    """
    hours = seconds // (60 * 60)
    if hours < 24:
        return hours
    else:
        return hours % 24


def calc_days(seconds: int) -> int:
    """
    Calculate days
    :param seconds:
    :return:
    """
    days = seconds // (60 * 60 * 24)
    if days < 365:
        return days
    else:
        return days % 365


def calc_years(seconds: int) -> int:
    """
    Calculate years
    :param seconds:
    :return:
    """

    return seconds // (60 * 60 * 24 * 365)
