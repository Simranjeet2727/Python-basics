#syntific calculator


import math
def add():
    a,b=map(int,input("enter two numbers: ").split())
    d=a+b
    
    print(d)
    
def sub():
    a,b=map(int,input("enter two numbers: ").split())  
    d=a-b
    
    print(d)
    
def mult():
    a,b=map(int,input("enter two numbers: ").split())  
    d=a*b
    
    print(d)
    
def div():
    a,b=map(int,input("enter two numbers: ").split())  
    d=a/b
    
    print(d)
    
def floor():
    a,b=map(int,input("enter two numbers: ").split())  
    d=a//b
    
    print(d)
    
def modulus():
    a,b=map(int,input("enter two numbers: ").split())  
    d=a%b
 
    print(d)
    
def sin():
    a=int(input("enter a number: "))  
    d=math.sin(a)
 
    print(d)
    
def cos():
    a=int(input("enter a number: "))
    d=math.cos(a)
 
    print(d)
    
def tan():
    a=int(input("enter a number: "))  
    d=math.tan(a)
 
    print(d)
    
def isin():
    a=int(input("enter a number: ")) 
    d=math.asin(a)
 
    print(d)
    
def icos():
    a=int(input("enter a number: ")) 
    d=math.acos(a)
 
    print(d)
    
def itan():
    a=int(input("enter a number: "))
    d=math.atan(a)
 
    print(d) 
    
def expon():
    a=int(input("enter a number: "))
    b=int(input("enter a number: "))
    print(a**b)
    
def log():
    a=int(input("enter a number: "))   
    b=int(input("enter base: "))     
    print(math.log(a,b))
        

    
    
    
    
#to get value

print("1 to add,2 to sub,3 to mult,4 to div,5 to floor,6 to modulus,7 to sin,8 to cos,9 to tan,10 to isin,11 to icos,12 to itan")

c=int(input("enter any no.: "))   
if c==1:
    add()
elif c==2:
      sub()    
elif c==3:
      mult() 
elif c==4:
      div()       
elif c==5:
      floor() 
elif c==6:
      modulus() 
elif c==7:
      sin() 
elif c==8:
      cos() 
elif c==9:
      tan() 
elif c==10:
      isin()
elif c==11:
      icos()       
elif c==12:
      itan()       
elif c==13:
      expon()       
elif c==14:
      log()       
       
      
      
      
      
      
      