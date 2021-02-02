# 01.01.1900 mon

firstDay = 1
firstMonth  = 1
firstYear = 1900

firstSundayDay = 7

startDay = 1
startMonth = 1
startYear = 1901

endDay = 31
endMonth = 12
endYear = 2001

currentDay = 7

currentMonth = 1
currentMonthDayCount = 31
currentYear = 1900

sundayCount = 0

month30 = [4,6,9,11]
month31 = [1,3,5,7,8,10,12]

def setCurrentMonthDayCount():
    global currentMonthDayCount
    global currentMonth
    global currentYear

    # case 30 day month
    if(month30.count(currentMonth) == 1):
        currentMonthDayCount = 30
        return
    # case 31 day month
    if(month31.count(currentMonth) == 1):
        currentMonthDayCount = 31
        return

    # case feb
    isLeapYear = False
    if((currentYear % 4 ) == 0):
        isLeapYear = True
    if((currentYear % 100) == 0):
        isLeapYear = False
    if((currentYear % 400) == 0):
        isLeapYear = True
        
    if(isLeapYear):
        currentMonthDayCount = 29
        return
    currentMonthDayCount = 28


def nextMonth():
    global currentDay
    global currentMonth
    global currentYear
    global currentMonthDayCount

    currentDay -= currentMonthDayCount
    if(currentDay == 0):
        currentDay = 1
    currentMonth += 1
    if(currentMonth == 13):
        currentMonth = 1
        currentYear+=1
    
    setCurrentMonthDayCount()

isStartDate = False
isNotEndDate = True

while isNotEndDate:
    
    if(currentDay == 1 and isStartDate):
        sundayCount += 1
    
    currentDay +=7

    if(currentDay > currentMonthDayCount):
         nextMonth()

    if(currentYear >= endYear ):
        isNotEndDate = False
    if(currentYear >= startYear):
        isStartDate = True


print(sundayCount)