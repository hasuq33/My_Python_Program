# coding: utf-8

from datetime import datetime,date


def main(usrDate,usrWeekday,usrMonth):

    print(f"The Date is {usrDate} and WeekDay is  {usrWeekday}") 
     
    StartYear = date.today().year # Getting the current Year 
    EndYear = StartYear +50 # Ending Year is From current Year to Next 50 Years 
    monthDict = {
        "January":1,
        "February":2,
        "March":3,
        "April":4,
        "May":5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12
    }
    
    month = monthDict.get(usrMonth)

    # Printing dates with same same weekday
    for year in range(StartYear,EndYear+1):
            x= datetime(year,month,usrDate)
            y= x.strftime("%A") # Finding WeekDay 
            if y == usrWeekday: 
                expectedDate = datetime(year,month,usrDate).strftime("%Y-%m-%d")
                print(f"{expectedDate} WeekDay: {y}")
    

if __name__ == '__main__':
    usrDate = int(input("Enter the date: "))
    usrWeekday = input("Enter the weekday: ").capitalize()
    usrMonth = input("Enter the month: ").capitalize()
    main(usrDate,usrWeekday,usrMonth)