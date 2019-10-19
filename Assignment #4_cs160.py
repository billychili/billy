import time

def programmer():
    print("Programmer mode.")
    con = input("Would you like convert binary or decimal? ")
    if(con == "decimal"):
        num=input("Enter decimal to convert to binary number: ");   

        num=int(num);

        if(num == 0):
            print("digit 1: "+str(num))
            exit()
        elif(0<num<=255):
            for i in range(num):
                print("digit " +str(i+1)+": " + str(num%2));
                num = (num//2);
                if num == 0:
                    break
        else:
            print("you entered an invalid input")
            return
    elif(con == "binary"):
        num=input("Enter binary to convert to decimal number: ");   
        i = int(len(num))
        dec = 0
        x = 0

        for i in range (int(len(num)),0,-1):
        
            dec = dec + int(num[x])*(2**(i-1))
            x += 1
           
            
            if (i == 1):
                print (dec)
    else: 
        print("You typed an invalid input.") 
        return

def scientific(x,y):  
    print("Scientific mode.")
    x = int(input("Enter positive number: "))
    operator = str(input("Enter +, -, *, /, or **: "))
    y = int(input("Enter positive number: "))
    if (x >= 0 and y >= 0):
        if (operator == "+"):
            u = x + y
            print(u)
            return(u)
        elif(operator == "-"):
            u = x - y
            print (u)
            return(u)
        elif(operator == "*"):
            u = x * y
            print (u)
            return(u)
        
        elif(operator == "/"):
            u = x / y
            print (u)
            return(u)
        
        elif(operator == "**"):
            u = x**y
            print (u)
            return (u)
        else:
            print("You typed an invalid operator.")
            return
    else:
        print("You typed an invalid input.") 
        return   

    

def calculator():
    x = 0
    y = 0
    
    cho = str(input("Would you like to be put in scientific mode or programmer mode: "))
    while (True):
        
    
        if(cho == "s"):
            scientific(x,y)
            cho = input("Would you like to be put in scientific mode or programmer mode: ")
            
            
        elif(cho == "p"):
            programmer() 
            cho = input("Would you like to be put in scientific mode or programmer mode: ")

        elif(cho == "exit"):
            print("You exited the program")
            return
            
            
        else:
            print("you entered an invalid input")
            time.sleep(.5)
            cho = input("Would you like to be put in scientific mode or programmer mode: ")
            
            



calculator()
