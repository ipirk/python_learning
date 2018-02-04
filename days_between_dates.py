'''
Created on 03/10/2017

@author: it
'''
# it does not occur at all.
def biggest(a,b,c):
    if a>b:
        biggest=a
    else:
        biggest=b
    if c>biggest:
        biggest=c
    return biggest

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days=0
    #print(dayinyear(year1, month1, day1))
    #print(dayinyear(year2, month2, day2))
    if year1==year2:
        return (dayinyear(year2, month2, day2)-dayinyear(year1, month1, day1))
    else:
        days+=(dayinyear(year1, 12, 31)-dayinyear(year1, month1, day1))
        days+=dayinyear(year2, month2, day2)
        while year2-year1>1:
            year1+=1
            if isleapyear(year1):
                days+=366
            else:
                days+=365
    return(days)

        

def dayinyear(year, month, day):
    if isleapyear(year):
        daysOfMonths = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthcount=0
    days=0
    while monthcount<month-1:
        #print daysOfMonths[monthcount]
        days+=daysOfMonths[monthcount]
        monthcount+=1
        #print "days=", days
    days+=day
    return(days)

def isleapyear(year):
    if not year%4==0:
        return(0)
    elif not year%100==0:
        return(1)
    elif not year%400==0:
        return(0)
    else:
        return 1



def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed", "result=", result)
        else:
            print ("Test case passed!")

test()  
print (daysBetweenDates(2012, 1, 1, 2012, 1, 2))
