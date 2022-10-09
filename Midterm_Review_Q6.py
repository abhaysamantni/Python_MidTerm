

#This is the driver code that uses the hardwareSet class that you are writing.
import hardwareSet
#Create object ds1 of class DroneSet with capacity of 250
ds1=hardwareSet.DroneSet(250,100)
#print initial capacity units of ds1
print("Total capacity of units:", ds1.get_capacity())

#print number of available units of ds1
print("Number of available units:", ds1.get_availability())

#set new payload for ds1
ds1.set_payload(200)

#print new payload of ds1
print("New payload:", ds1.get_payload())
#checkin 180 units
#hwSet1.check_in(180)
#print number of units available after checkin
#print("Number of units available after checking in 180 units:", hwSet1.get_availability())







