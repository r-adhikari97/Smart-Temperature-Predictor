########################################################################################################################

#Modules , Libraries etc

import Stats
import R_W_Script
import Connect
import continuous_threading
import time



########################################################################################################################

#GUI

from tkinter import*
from tkinter.ttk import *
import tkinter as tk


########################################################################################################################


#Connect Obj ---> GUI

Conn = Connect.Connection()


val = 0
def read_S():
    global Indicator
    global LF
    OP = Conn.Connection_A()
    #while True:
    if OP != 1:
        val = 1
        Indicator.grid_forget()
        Indicator = Label(LF,text = f'Connected : {OP} Arduino UNO', font = ("Arial",10))
        Indicator.grid(row = 0 , column = 0, padx = 20, pady = 20)
    else:
        val = 0
        Indicator.grid_forget()
        Indicator = Label(LF,text = "Disconnected ", font = ("Arial",10))
        Indicator.grid(row = 0, column = 0, padx = 20, pady = 20)
    return val

     
t1 = continuous_threading.PeriodicThread(0.5,read_S)



########################################################################################################################


# SUBMIT ----> Program & GUI

def Submit():
    global Result
    global value
    
    value = int(E1.get())

    #Regression ----> Program
    ob = Stats.Regression()
    VAL = ob.L_Reg_X(Record[0], Record[1], value)

    #Result ----> GUI
    Result.grid_forget()
    Result = Label(LF3, text = VAL, font =("ARIAL",12))
    Result.grid(row = 0, column = 0, padx = 30, pady = 42)

    

############################################################################################################################



# CONTINUE -----> Continues the Timer GUI

def Continue():
    A = Read.Continue(value)


##############################################################################################################################

    

# SUBMIT 2 ---------> SAMPLING and RECORDING data

def Submit_2():

    global Record
    global Read
    
    #Current ----> GUI
    global value_2
    value_2 = int(E2.get())
    #print(value_2)
    
    #Read and Write obj ----> Program
    Read = R_W_Script.Arduino_Py()
    Record = Read.RW_Data(value_2)



##################################################################################################################################



#GUI Window

W = tk.Tk()
W.title("Temperature Sensor")
W.geometry('600x475')

#Main Label Frame -----> MAIN
LF0 = LabelFrame(W, text = "Master Window", border= 2)
LF0.grid(row = 0, column = 0, pady = 10, padx = 10)



# # # # # # # #  I N D I C A T O R  # # # # # # # # # # # # # # # # # # # # #


#Label Frame ---> Indicator
LF = LabelFrame(LF0, text = " Arduino UNO ", border = 2, labelanchor = NW)
LF.grid(row = 0, column = 0, padx = 10, pady = 20)


#Label ----> Indicator
Indicator = Label(LF,text = "NONE", font = ("Arial",10))
Indicator.grid(row = 0 , column = 0, padx = 10, pady = 10)




# # # # # # # #    I N T E R F A C E   # # # # # # # # # # # # # # # # # # # # #


#Label Frame ----> Interface
LF2 = LabelFrame(LF0, text = "Interface", border = 2, width= 100)
LF2.grid(row = 50 , column = 0, padx = 20, pady = 10)


#Label ----> Interface
Interface = Label(LF2, text = 'Enter Time Stamp: ', width = 25)
Interface.grid(row = 0, column = 0, padx = 5, pady = 20)


#Entry ---> Interface
E1 = Entry(LF2, width = 25)
E1.grid(row = 0, column = 50, padx = 5, pady = 10,columnspan = 100)

#Button ---> Interface
B1 = Button(LF2, width = 20, text = "Submit", command = Submit)
B1.grid(row = 1, column = 0, padx = 10, pady = 10, columnspan = 200)





# # # # # # # #    R E S U L T   # # # # # # # # # # # # #  # #  # # # # # #



#Label Frame ------> Result
LF3 = LabelFrame(LF0, text = 'Forecast', border = 2)
LF3.grid(row = 50, column = 50, padx = 10, pady = 10)

#Label -----> Result
Result = Label(LF3, text = 'NONE C', font =("ARIAL",12))
Result.grid(row = 0, column = 0, padx = 30, pady = 42)



# # # # # # # #    C U R R E N T  # # # # # # # # # # # # #  # #  # # # # # #


#Label Frame ------> Current
LF4 = LabelFrame(LF0, text = 'Current', border = 2)
LF4.grid(row = 0, column = 50, padx = 10, pady = 10)

#Label -----> Current
Current = Label(LF4, text = "Sampling", font =("ARIAL",12))
Current.grid(row = 0, column = 0, padx = 10, pady = 10)

#Entry -----> Current
E2 = Entry(LF4, width = 20)
E2.grid(row = 1, column = 0, padx = 10, pady = 10)

#Button -----> Current
B2 = Button(LF4, text = 'Submit',width = 10, command = Submit_2)
B2.grid(row = 2, column = 0, padx = 10, pady = 10)



# # # # # # # #    L I V E  # # # # # # # # # # # # #  # #  # # # # # #


#Label Frame ------> Live
LF5 = LabelFrame(LF0, text = 'LIVE DATA', border = 2)
LF5.grid(row = 100, column = 0, padx = 10, pady = 10, columnspan = 400)

#Label -----> Live
#Live = Label(LF5, text = 'Accuracy % is : ABC ', font =("ARIAL",12), width=30)
#Live.grid(row = 0, column = 0 , padx = 30, pady = 30)

#Button ------> Continue
B3 = Button(LF5, text = 'CONTINUE TIMER',width = 30,command = Continue)
B3.grid(row = 0, column = 0 , padx = 30, pady = 30)



#Processess
t1.start()


W.mainloop()
