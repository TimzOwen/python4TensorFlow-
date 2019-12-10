print("Hello world Machine Learning")

def HelloWorldXY(x,y)
    if(x<10):
        print("x was <10")
     elif(x<20):
        print("x was >=10 but < 20")
    else:
        print("Hello world x > 20")
    return x + y 
for i in range(8,25,5): #i=8, 13, 18,23 (start stop stop)
    print("--- now running with i: {}".format(i))
    r = HelloWorldXY(i, i)
    print("result from hello world: {} ".format(i, r))
    
    ##doing exponential functions 
    print(3**2)
    #9
    
    #modulo operator which returns the remainder of division 
    print(9%2)
    #1
    
    #Integer division which rounds off result to the next integer
    print(7%2)
    #3
    
