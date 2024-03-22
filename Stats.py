import numpy as np

class Regression:

    def L_Reg_X (self, x , y , val):
        N = 0  # Number of elements
        Sum_y = 0  # Summation of Y elemennts
        Sum_x = 0  # Summation of X elements
        SQ_x = 0  #  Square of X elemets
        SQ_y = 0  # Square of Y elements
        MUL = 0  # Multiplication and sum of X and Y elements


        # Length
    
        N = len(x)
    

        # Sum of y elements
    
        for i in y:
            SQ_y= SQ_y + i**2
            Sum_y = Sum_y + i
        

        # Sum of x elements
    
        for i in x:
            SQ_x = SQ_x + i**2
            Sum_x = Sum_x + i

        

        #Product of x and y
        
        for i in range(0,N):
            MUL = MUL + x[i]*y[i]
            NUMBER = round(MUL,3)


        # Generating eqn using 
    
        L1 = [[N, Sum_x], [Sum_x, SQ_x]]
        L2 = [Sum_y , NUMBER]

        print(L1,L2)

        

        # Solving Equations

        R = np.linalg.inv(L1).dot(L2)
        Y = R[0] + (R[1]*val)
        


        #Return value
        
        return (round(Y,3))

A = Regression()
L1 = [1,2,3,4,5,6,7]
L2 = [14.3, 14.2, 14.4, 14.1, 13.9, 14.1, 14.0]
print(A.L_Reg_X(L1, L2, 13))
