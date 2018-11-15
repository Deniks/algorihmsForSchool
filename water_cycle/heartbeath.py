normalHeartbeath = list(range(101))[60:101] # the average heartbeath of a person
status = "Normal"
myHeartbeath = int(input("Your heartbeath - "))

while myHeartbeath:
    if myHeartbeath > normalHeartbeath[0] and myHeartbeath < normalHeartbeath[-1]:
        status = "Normal"
    if myHeartbeath < normalHeartbeath[0]:
        status = "Low heartbeath"
    if myHeartbeath < 20:
        status = "X_X"
    if myHeartbeath > normalHeartbeath[-1]:
        status = "You gotta be addicted to drugs"
    print(status)
    break
