def user_input():
    a = int ( input ("Enter value of a =")) # @typcasting..
    b = int (input ("Enter value of b ="))  # @typecasting..
    c = int ( input ("Enter value of c =")) # @typcasting..
    if c < a > b :
        print ("a is the greatest number")
    elif a < b > c:
        print ("b is the greatest number")
    else :
        print ("c is the greatest number")

user_input() 