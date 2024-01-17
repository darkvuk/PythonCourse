import datetime


# Danasnji datum
d = datetime.datetime.today()
print(d)


# Dobijanje pojedinacnih informacija iz datuma
print(d.date())
print(d.time())
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)


# Rucno uneseni datum
d = datetime.datetime(2024,1,17)
print(d)

d = datetime.datetime(2024,1,17,13,18,23)
print(d)

print(d.date())
print(d.time())


# dodavanje odredjenog broja dana / sati / sedmica na trenutni datum
d = d + datetime.timedelta(days=90)
d = d + datetime.timedelta(weeks=30)
d = d + datetime.timedelta(seconds=4)
print(d)