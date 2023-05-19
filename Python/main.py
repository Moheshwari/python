print("Hello, World!")

# Method..
def my_method():
    a = 34
    b = 40
    if a>b :
        print ("a is greater than b")
    else :
        print ("b is greater than a")

my_method()


# Method for getting value from user
def user_input():
    a = int ( input ("Enter value of a =")) # @typcasting..
    b = int (input ("Enter value of b ="))  # @typecasting..
    if a>b :
        print ("a is greater than b")
    else :
        print ("b is greater than a")

user_input()


# Method for checking ...@Pallindrome...while loop
def check_pallindrome():
    a = str ( input ("Enter a string ")) # @typcasting..

    i =0 
    check =len (a) # length of a
    while i < len(a)//2: # integer divison....
        if a [i] != a[check-1-i]:
            print ("not a pallindrome")
            return
        i+= 1
    print ("it's a pallindrome")
        

check_pallindrome()
