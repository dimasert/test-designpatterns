import datetime
import time
x = 0

while x <10:
    try:
        time.sleep(1)
        print(x, sep=" - ", end=' Missipi \n ')
        x += 1
    except:
        print("Something went wrong")
        break
    else:
        print("Nothing went wrong")   

x = datetime.datetime.now()
print(x)