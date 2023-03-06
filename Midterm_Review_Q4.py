# Use the files dateFile.txt, minTempFile.txt, maxTempFile.txt, and avgTempFile.txt to answer this question.
# These files contain temperature statistics (max, min, average) for each day of the year 2016.
# Note that 2016 was a leap year. You can open the files in a text editor to view the contents of the file.
#
# Write a Python program to do the following
#
# Read data from these files and store it in a Python 2D list. You must use the 2D list datatype to answer this question.
# Find the hottest day in the year. Hottest day is the day with the highest maximum temperature during the year.
# Print this value to the screen as shown below
# Find the coldest day in the year. Coldest day is the day with the lowest minimum temperature during the year.
# Print this value to the screen as shown below

#
# Hottest day in the year was 8/12/2016
# Coldest day in the year was 12/19/2016

f1=open('datefile.txt','r')
f2=open('maxTempfile.txt','r')
f3=open('minTempfile.txt', 'r')
f4=open('avgTempfile.txt','r')
data2d=[[]]
#x_coords=[]
#y_coords=[]
data2d = [[0 for i in range(366)] for i in range(4)]

date=f1.readline().rstrip('\n')
maxt=f2.readline().rstrip('\n')
mint=f3.readline().rstrip('\n')
avgt=f4.readline().rstrip('\n')
i=0
while(date!=''):
    data2d[0][i]=date
    data2d[1][i]=maxt
    data2d[2][i]=mint
    data2d[3][i]=avgt
    date=f1.readline().rstrip('\n')
    maxt=f2.readline().rstrip('\n')
    mint=f3.readline().rstrip('\n')
    avgt=f4.readline().rstrip('\n')
    i+=1
#Convert string list to integer list using map function before finding the hottest day of the year
temp_int_list=list(map(int, data2d[1][0:366]))
max_index=(temp_int_list).index(max(temp_int_list))
print("Hottest day in the year was", (data2d[0][0:366])[max_index])
#Convert string list to integer list before finding the coldest day of the year
temp_int_list=list(map(int, data2d[2][0:366]))
min_index=(temp_int_list).index(min(temp_int_list))
print("Coldest day in the year was",(data2d[0][0:366])[min_index])

f1.close()
f2.close()
f3.close()
f4.close()