import datetime


def time_range(time_start: tuple, time_end: tuple) -> None:
    ts = datetime.datetime(1, 1, 1, time_start[0], time_start[1], time_start[0])
    te = datetime.datetime(1, 1, 1, time_end[0], time_end[1], time_end[0])
    res = ts + datetime.timedelta(hours=te.hour, minutes=te.minute, seconds=te.second)
    print(res)


time_range(time_start=(23, 57, 59), time_end=(0, 0, 3))