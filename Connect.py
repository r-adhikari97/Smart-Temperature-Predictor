import serial.tools.list_ports as A


class Connection:

    def Connection_A(self):
        CON = "Disconnected"
        while True:
            portData = A.comports()
            for  i in portData:
                val = str(i)
                if "Arduino" in val:
                    SP = val.split('  ')
                    CON = (SP[0])
                    return(CON[0:4])
            return 1






#Driver test code

'''
while True:
    obj = Connection()
    value = obj.Connection_A()
    if value== 1:
        print('Disconnected')
    else:
        print(value)
        print("Connected")

'''





























































  
