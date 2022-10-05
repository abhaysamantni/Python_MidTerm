# A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories burned, heart rate,
# sleeping patterns, and so on. One common physical activity that most of these devices track is the number of steps
# you take each day. You have been provided a file “steps.txt”, which contains the number of steps a person has taken
# each day for the year 2019. There are 365 lines in the file, and each line contains the number of steps taken during a day.
# The first line is the number of steps taken on January 1st, second line is the number of steps taken on January 2nd,
# and so forth. Write a program that reads the file, and performs the following tasks:

# 2.1 Display steps taken on 03/01 (March 01)
# 2.2 Display the average number of steps taken for each month.
# 2.3 User Matplotlib (or similar plotting library) functions to display the number of steps taken on Y-axis.
# X-axis are numbers from 1 to 366.

# note: The data is from a year that was not a leap year, so February has 28 days.

#Solution for 1
from datetime import date, datetime
day_of_the_year = date(2019, 3, 1).timetuple().tm_yday
print(day_of_the_year)
steps_file=open("steps.txt",'r')
count=0
while(count!=day_of_the_year):
    num_steps=steps_file.readline()
    count+=1
print(num_steps)
steps_file.close()

#Solution for 2
from datetime import date, datetime
steps_file=open("steps.txt",'r')
count=0
for i in range(1,12):
    if ((i == 1) or (i == 3) or (i == 5) or (i == 7) or (i == 8) or (i == 10) or (i ==12)):
        n = 31
    elif (i == 2):
        n = 28
    elif ((i == 4) or (i == 6) or (i ==9) or (i == 11)):
        n == 30
    count=0
    total=0
    while(count<n):
        num_steps=int(steps_file.readline())
        total+=num_steps
        count+=1
#    print("Sum for month", i, 'is', total)
    print("Average for month", i, 'is', total/n)
steps_file.close()