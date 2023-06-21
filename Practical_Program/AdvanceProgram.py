# Take three input from the user 
# Start Date,End Date and week Day

from datetime import datetime,timedelta

 

def main():

    StartDate = input("Enter the start date as a format of 'yy-mm-dd'")
    EndDate = input("Enter the end date as a format of 'yy-mm-dd'")
    WeekDay = input("Enter the week day do you want to count: ")


    StartDate = datetime.strptime(StartDate, '%Y-%m-%d')
    EndDate = datetime.strptime(EndDate, '%Y-%m-%d')

    delta = timedelta(days=1) #timedelta module is used for manupalating timedate intevals

    totalDays = 0

    while StartDate<=EndDate:
        # if StartDate.weekday() == RandDay:
        #     totalDays+= 1
        ans = datetime.date(StartDate)
        z = ans.strftime("%A")
        # print(z)
        if z == WeekDay:

            print(WeekDay,StartDate )
        
        StartDate += delta



    print(f"{totalDays} {WeekDay}s are coming between {StartDate} and {EndDate}.")  

if __name__ == '__main__':
    main()

