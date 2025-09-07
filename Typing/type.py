from time import *

def mistake(par, user):
    err = 0
    for i in range(len(par)):
        try:
            if par[i] != user[i]:
                err = err + 1
        except:
            err = err + 1
    return err

def typing_speed(timeS, timeE, userI):
    time_delay = timeE - timeS
    time_R = round(time_delay, 2) 
    speed = len(userI) / time_R
    return round(speed*60)

while True:
    ck = input("Ready for Test?: yes / no: ") 
    if ck == "yes":
        text = "Hello my name is sahil jogi."

        print("***** TYPING TEST *****")
        print(text)
        print()
        print()
        timeA = time()
        testInput = input("Type here : ")
        timeB = time()

        print(f"Speed: {typing_speed(timeA, timeB, testInput)} w/sec")
        print(f"Error: {mistake(text, testInput)}")
    elif ck == "no":
        print("Thank You!")
        break
    else:
        print("wrong input")
