from mrjob.job import MRJob
import mrjob
import pdb
import math

class MRAverage(MRJob):

    def mapper(self, _, line):
        # Each line is CSV
        # Skip header and emit month and count
        temp=[0.0,0.0]
        l = [s.strip('"') for s in line.split(',')]
        if l[0] != '':
            month = int(l[0])
            temp[0]=int(l[2])
            temp[1]=1
            # strip off quotes
            yield month, temp

    def combiner(self, month, temp):
        i=0;
        totaltemp1=[0.0,0.0]
        for i in temp:
            totaltemp1[0]+=i[0]
            totaltemp1[1]+=1
        yield month, totaltemp1

    def reducer(self, month, temp):
        i=0.0;
        totaltemp2=0.0
        totalcount2=0
        for i in temp:
            totaltemp2+=i[0]
            totalcount2+=i[1]
        yield month, totaltemp2/float(totalcount2)

if __name__ == '__main__':
    MRAverage.run()
