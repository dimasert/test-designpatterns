import datetime

x = 1

while x <10:
    try:
        print(x)
        x += 1
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")   

x = datetime.datetime.now()
print(x)