import serial
import csv
import Connect
import continuous_threading
import time
import sys
sys.setrecursionlimit(5000)

# # # # # Conencting Arduino to Python # # # # #


# Connect Object

obj = Connect.Connection()
CONNECT = obj.Connection_A()
if CONNECT != 1:
    serial_data = serial.Serial(CONNECT, baudrate = 9600, timeout =2)
else:
    print("Connection Issue")



#serial_data = serial.Serial(Conn(), baudrate = 9600, timeout =2)

    
class Arduino_Py:

    def RW_Data(self,a):

        #serial_data = serial.Serial(CONNECT, baudrate = 9600, timeout =2)

        #Connecting Pytthon data to file
        textfile = open('data.csv', 'w')

        #Collection and Append to csv file
        for i in range(a):
            and_data = serial_data.readline().decode('ascii')
            
            print(and_data)
            textfile.write(and_data)

        textfile.close()

        #Reading CSV file data
        time = []
        distance = []
        with open('data.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row:
                    continue
                else:
                    time.append(int(row[0]))
                    distance.append(float(row[1]))

        return (time, distance)



    def Continue(self, value):
        a = value+1

        while True:
            and_data = serial_data.readline().decode('ascii')
            DATA = str(and_data)
            time = int(DATA[0:4])

            if time < a:
                print(DATA)
            elif time >= value:
                print(" E N D ")
                break
#serial_data.close()


















        

        



