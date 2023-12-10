from datetime import datetime, timedelta


def convert_str_to_time(str_time_list: list, current_day: datetime) -> list:
    busy_time = []
    for str_time in str_time_list:
        str_start = str_time.get('start').split(':')
        str_stop = str_time.get('stop').split(':')
        start = current_day.replace(hour=int(str_start[0]), minute=int(str_start[1]))
        stop = current_day.replace(hour=int(str_stop[0]), minute=int(str_stop[1]))
        busy_time.append([start, stop])
    return busy_time


def convert_time_to_str(time_list: list) -> list:
    free_time = []
    for time in time_list:
        time_period = {'start': time[0].strftime("%H:%M"), 'stop': time[1].strftime("%H:%M")}
        free_time.append(time_period)
    return free_time


def get_free_time(busy_time: list, current_day: datetime, day_start: list, day_end: list) -> list:
    current_time = current_day.replace(hour=day_start[0], minute=day_start[1], second=00)
    day_end = current_day.replace(hour=day_end[0], minute=day_end[1], second=00)
    free_time = []

    while current_time < day_end:
        time_crossing = False
        free_time_start = current_time
        current_time = current_time + timedelta(minutes=30)
        for i, b in enumerate(busy_time):
            if b[0] < current_time <= b[1] or (free_time_start < b[0] and current_time >= b[1]):
                time_crossing = True
                current_time = b[1]
                break

        if not time_crossing:
            free_time.append([free_time_start, current_time])

    return free_time


busy = [
{'start' : '10:30',
'stop' : '10:50'
},
{'start' : '18:40',
'stop' : '18:50'
},
{'start' : '14:40',
'stop' : '15:50'
},
{'start' : '16:40',
'stop' : '17:20'
},
{'start' : '20:05',
'stop' : '20:20'
},
]

current_day = datetime.now()
busy_time_list = convert_str_to_time(busy, current_day)
free_time_list = get_free_time(busy_time_list, current_day, [9, 0], [21, 0])
free_time = convert_time_to_str(free_time_list)
print(free_time)
