def user_input():
    length = float( input ("Enter value of a =")) # @typcasting..
    bredth = float (input ("Enter value of b ="))  # @typecasting..
    
    if (length==bredth) :
        print ("Square")
    else :
        print ("Rectangular")

#user_input()

print("square" if (float( input ("Enter value of a =")) == float( input ("Enter value of b ="))) else "rectangle")