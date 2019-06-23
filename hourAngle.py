'''script for calculating angle between hands of the clock '''

def getAngle(hour): # hh:mm
    [p1,p2] = hour.split(":")
    p1 = int(p1)
    p2 = int(p2)
    if p1 > 12: # if 24-hours clock for example: 23:59 instead of 11:59
        p1 -=12

    degreePerMinute = 360 / 60
    degreePerHour = degreePerMinute * 5
    
    p1Angle = int(p1)*degreePerHour
    p2Angle = int(p2)*degreePerMinute

    return(p2Angle - p1Angle)


print(getAngle("15:30"))
print(getAngle("01:05"))
print(getAngle("15:05"))
    
    
