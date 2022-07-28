def add_time(start, duration, week=None):
    weeks = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
             'Friday', 'Saturday', 'Sunday']
    days = 0

    temp_time, hour_clock = start.split()

    init_time = temp_time.split(":")
    a_time = duration.split(":")

    if hour_clock == 'PM' and int(init_time[0]) < 12:
        init_min = ((int(init_time[0]) + 12) * 60) + int(init_time[1])
    else:
        init_min = (int(init_time[0]) * 60) + int(init_time[1])

    a_min = (int(a_time[0]) * 60) + int(a_time[1])

    total_min = init_min + a_min

    hh = total_min // 60
    mm = total_min % 60

    if hh >= 24:
        days = hh // 24
        hh = hh % 24

    if 12 < hh < 24:
        hh = hh - 12
        hour_clock = 'PM'
    elif hh == 12:
        hour_clock = 'PM'
    elif 0 < hh < 12:
        hour_clock = 'AM'
    elif hh == 0:
        hh = 12
        hour_clock = 'AM'

    new_time = f'{hh}:{mm:02} {hour_clock}'

    if week != None:
        coming_day = (weeks.index(week.capitalize()) + days) % 7
        new_time += f", {weeks[coming_day]}"

    comments = ""

    if days > 1:
        comments = " ({} days later)".format(days)
    elif days == 1:
        comments = " (next day)"

    new_time += comments

    return new_time