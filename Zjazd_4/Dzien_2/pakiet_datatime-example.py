import datetime

now = datetime.datetime.today()


print(now)


birthday = datetime.datetime(1993, 2, 27 )
print(birthday.weekday())

minelo_dni = datetime.datetime.today() - birthday
print(minelo_dni.days)