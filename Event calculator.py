#my first python program
def sus():
    hour = int(input("Starting time (hours): "))
    mins = int(input("Starting time (minutes): "))
    dura = int(input("Event duration (minutes): "))

    if(hour<24):
        minutes = (dura + mins)%60
        hours = (hour + (dura+mins)//60)%24
        print('The Event Will end in : ', hours,':',minutes, sep='')
    else:
        print('The time you entered is not valid')
