
def convetTime(seconds):
    if seconds >0 and seconds <= 59:
        print('0:0:' + str(seconds))
    elif seconds >59 and seconds < 3599:
        print('0:' + str({seconds//60}) +':' + str({seconds%60}))
    else:
        hours = seconds // (60*60)
        mins = (seconds % (60*60)) // 60
        seconds = seconds % 60
        print(str(hours) + ':' + str(mins) + ':' + str(seconds))

seconds = int(input('enter the seconds:'))
convetTime(seconds)