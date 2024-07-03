#exception: it is a logical loop hole that occurs in a code and it can be handled yusing try and except block. 
#in the code inside the try block , if there are more than one exception then thge except block corresponding to the frst exception will get executed. 
#and once the control comes from try block to except block , the control will not go back to try block again.  
#this is called exception masking. 
a = int(input("enter "))
b = int(input("enter "))
try: 
    print(a/b)
    h = [1,2,3,4,5]
    print(h[55])
    
except ZeroDivisionError:
    print("cannot do")
except IndexError:
    print("cannot find")
    
finally:
    print("thanks")
    
c = a*a
print(c)


