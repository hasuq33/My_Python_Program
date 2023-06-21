# coding: utf-8

from datetime import datetime 

def main(usrDate,usrWeekDay):
    date_obj = datetime.strptime(usrDate,"%Y-%m-%d")

    month = date_obj.month
    day = date_obj.day
    StartYear = date_obj.year
    EndYear = StartYear + 50

    # Printing weekdays with same month 
    for year in range(StartYear, EndYear+1):
        x = datetime(year,month,day)
        y = x.strftime("%A")
        if y == usrWeekDay:
            expectedDate = datetime(year,month,day).strftime("%Y-%m-%d")
            print(f"{expectedDate} WeekDay:{usrWeekDay}")

if __name__ == '__main__':
    usrDate = input("Enter the date in the format of 'yyyy-mm-dd'.")
    usrWeekDay = input("Enter The Week Day.").capitalize()
    main(usrDate,usrWeekDay)