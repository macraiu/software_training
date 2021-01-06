# A Python program to demonstrate use 
# of packing 
  
# This function uses packing to sum 
# unknown number of arguments 
def mySum(*args): 
    sum = 0
    for i in range(0, len(args)): 
        sum = sum + args[i] 
    return sum 
  
# Driver code 
a = [10,4,6,39]
b = [100,45,22,56]
c = a + b
print(c)
print(mySum(1, 2, 3, 4, 5)) 
print(mySum(10, 20)) 
print(mySum(*c))
print(mySum(*a, *b))

# A Python program to demonstrate packing of 
# dictionary items using ** 
def fun(**kwargs): 
  
    # kwargs is a dict 
    print(type(kwargs)) 
  
    # Printing dictionary items 
    for key in kwargs: 
        print("%s = %s" % (key, kwargs[key])) 
  
# Driver code 
fun(name="geeks", ID="101", language="Python") 

