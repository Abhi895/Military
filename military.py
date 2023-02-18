
stringTimes = ["zero", 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'thirty', 'forty', 'fifty']

def getHour(initialTime, time):
    hundredHours = False

    militaryHour = ""

    if len(time) > 2:
        if time[-2:] == "00":
            hundredHours = True
        time = time[:-2]

    if "AM" in initialTime:
        if time != "12":
            militaryHour += stringTimes[int(time)]
        else:
            militaryHour = "zero"
    else:
        if time == "12":
            militaryHour = "twelve"
        else:
            print(time)
            militaryHour = stringTimes[int(time) + 12]
    
    if hundredHours:
        militaryHour += " hundred hours"
    
    return militaryHour
 


def convertToMilitary(timeToConvert):

    integerTime = timeToConvert[:-2]
    integerTime = integerTime.replace(":", "")
    militaryTime = ""

    if integerTime[-2:] != "00" and len(integerTime) > 2:
        minutes = integerTime[-2:]
        hours = integerTime.replace(minutes, "")
        if int(hours) < 10 and "AM" in timeToConvert:
            militaryTime = "zero "

        militaryHour = getHour(timeToConvert, integerTime)
        militaryTime += militaryHour + " "


        if minutes[0] == "1":
            militaryTime += stringTimes[int(minutes)]
        
        elif int(minutes) < 10:
            militaryTime += "zero "
            militaryTime += stringTimes[int(minutes[1])]
        else:
            index = int(minutes[0]) + 21
            if minutes[0] == "2":
                index = 20
            militaryTime += stringTimes[index] + " "
            if minutes[1] != 0:
                militaryTime += stringTimes[int(minutes[1])]

        print(militaryTime)

    else:
        hour = getHour(timeToConvert, integerTime)
        print(hour)




convertToMilitary("12:05PM")
