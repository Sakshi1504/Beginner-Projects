from datetime import datetime
from playsound import playsound

itime=input("Enter time at which you want the alarm to play: HH:MM:SS (am/pm) \n")
print(itime)
alarmhour=itime[0:2]
alarmmin=itime[3:5]
alarmsec=itime[6:8]
alarmper=itime[9:]
print(alarmhour)
print(alarmmin)
print(alarmsec)
print(alarmper)

curtime = datetime.now()
curhr = curtime.strftime("%H")
curmin = curtime.strftime("%M")
cursec = curtime.strftime("%S")
curp = curtime.strftime("%p")


if alarmper.casefold()==curp.casefold():
    print("Period Matched")

if True:
    print("In")



#playsound('Alarm.mp3')

while True:
    curtime = datetime.now()
    curhr = curtime.strftime("%H")
    curmin = curtime.strftime("%M")
    cursec = curtime.strftime("%S")
    curp = curtime.strftime("%p")
    print(curtime)

    if curp.casefold() == alarmper.casefold():
        if curhr == alarmhour:
            if curmin == alarmmin:
                if cursec == alarmsec:
                    print("Wake up Time!!!")
                    playsound('Alarm.mp3')
                    break
