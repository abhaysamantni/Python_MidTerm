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
import matplotlib.pyplot as plt
f1=open('datefile.txt','r')
f2=open('maxTempfile.txt','r')
f3=open('minTempfile.txt', 'r')
f4=open('avgTempfile.txt','r')
data2d=[[]]
#x_coords=[]
#y_coords=[]
data2d = [[0 for i in range(366)] for i in range(4)]
#x_coords = [0 for i in range(366)]
#y_coords = [0 for i in range(366)]
#print(data2d)
date=f1.readline().rstrip('\n')
maxt=f2.readline().rstrip('\n')
mint=f3.readline().rstrip('\n')
avgt=f3.readline().rstrip('\n')
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
#Find the hottest day of the year
max_index=(data2d[1][0:366]).index(max(data2d[1][0:366]))
print("Hottest day in the year was", (data2d[0][0:366])[max_index])
#Find the coldest day of the year
#print(data2d[2][0:366])
#coldesttemp=list(map(int, (data2d[2][0:366])))[0]
#print("Coldest day temp", coldesttemp)
min_index=(data2d[2][0:366]).index(min(data2d[2][0:366]))
print("Coldest day in the year was",(data2d[0][0:366])[min_index])


plt.yticks([0, 10, 20, 30, 40, 50],['0', '20', '40', '60', '80', '100'])
plt.plot(data2d[3][0:366])
plt.show()
f1.close()
f2.close()
f3.close()
f4.close()