def print_abacus(value):
    #
    ### Add you code here 
    string=str(value)
    length=len(string)
    factor=10
    
    while factor>length:
        print("|00000*****   |")
        factor-=1
    
    while factor>0:
        number=int(string[length-factor])
        result="|"
        for x in range(0,10):
            i=10-x
            if i==number:
                if i>5: result+="   0"
                else: result+="   *"
            else:
                if i>5: result+="0"
                else: result+="*"
        result+="|"
        factor-=1  
            
        print(result) 
           
print_abacus(987654321)
