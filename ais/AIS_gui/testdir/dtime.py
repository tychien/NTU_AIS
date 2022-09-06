from datetime import datetime
timestart   = '2021-08-30 21:23:35'
timeend     = '2021-09-30 22:24:20'

time1       = '2021-10-30 20:23:23'
time1_d     = datetime.strptime(time1,'%Y-%m-%d %H:%M:%S')
timestart_d = datetime.strptime(timestart,'%Y-%m-%d %H:%M:%S')
timeend_d   = datetime.strptime(timeend,'%Y-%m-%d %H:%M:%S')

if timestart_d < time1_d < timeend_d:
    print("nice")
else:
    print("shit")


print(time1_d.day)

