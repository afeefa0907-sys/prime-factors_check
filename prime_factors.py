print("Hello and WELCOME :::")
def prime_check():
    while True :
        num=input("Enter the number you want to check is prime or not >>> ")
        if num.lower().strip()=='stop':
            break
        else:    
             try:             
                num=int(num)
                if num==1:
                    print("This is number is neither prime nor commposite>>")
                elif num<=0:
                    print("Negative numbers are not considered prime >>")
                else:
                    factors=list()
                    for k in range(2,num): 
                        if num%k==0 :
                            factors.append(k)
                    if len(factors)==0:
                        print("This number is prime:>>>")
                    else:  
                        print("This number is not primme") 
             except ValueError:
                 invalid()           
def factor_list():
    while True :
            num=input("Enter the number whose list of factors you want  >>> ")
            if num.lower().strip()=='stop':
                break
            else: 
                try:             
                    num=int(num)
                    factor_list=list()
                    for k in range(1,num+1):
                        if num%k==0:
                            factor_list.append(k)
                    print(f"List of factors of {num} are {factor_list}")            
                except ValueError:
                    invalid()
def invalid():
    print(":::Please enter a valid integer value :::")
print("Tyype 'stop' anytime  to close the program>>>")
question={
    1:'Check if a number is prime or not >>',
    2:'Find the list of factors of a number>>',
    3:'STOP'
}
print(question)
while True:
   ask=input("Enter the number of the question you want to ask >>> ")
   try :
        ask=int(ask)
        if ask==1:
            prime_check()
        elif ask==2:
            factor_list()
        elif ask==3:
            print("Goodbye!!!")
            break 
        else:
            print("<<< Please enter a valid nummber between 1,2 and 3 >>>")       
   except ValueError:
       invalid()