import datetime


current = datetime.datetime.today()
future = current + datetime.timedelta(days=365)
print(future)