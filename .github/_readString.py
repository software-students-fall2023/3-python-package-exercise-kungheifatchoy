def readString(string):
    import re

    info=[0,0,0,'+','+','+']

    #make all x's lowercase, delete spaces
    fixed_string=""
    for j in string:
        if j==' ':
            continue
        if j=='X':
            fixed_string+='x'
            continue
        fixed_string+=j

    #_________________________________________
    #Initial Checks

    #check  if x is included in string
    if re.search("x",fixed_string) == None:
        return "ERROR: No variable"
    
    #check if term a is negative
    if fixed_string[0]=='-':
        info[3]='-'
        #correct string
        temp=""
        for m in range(1,len(fixed_string)):
            temp+=fixed_string[m]
        fixed_string=temp

    #check there are no more than 3 terms
    if len(re.findall("x",fixed_string))>2 or len(re.findall("\+|-",fixed_string))>2:
        return "ERROR: incorrect format of quadratic @ 34"
    
    #check if expression is quadratic
    if re.search("\^2",fixed_string) == None or (fixed_string[re.search("\^2",fixed_string).start()+1].isnumeric() and 
                                                 re.search("\^2",fixed_string).start()+3==len(fixed_string)):
        return "ERROR: No x^2 term" 

    #check there are well defined terms
    for split in re.split("\+|-",fixed_string):
        if len(split)<1:
            return "ERROR: incorrect format of quadratic @ 44"
              
    #_________________________________________

    ###########################################################################################
    #find operators
    ###########################################################################################

    ops=re.findall("\+|-",fixed_string)
    if ops:
        info[4]=ops[0]
        if len(ops)>1:
            info[5]=ops[1]

   
    ###########################################################################################
    #find coefficient a
    ###########################################################################################
    

    c0i=re.search("x\^2",fixed_string).start()


    skip0=False

    #no explicit coefficient for x^2 term means coefficient must equal 1
    if c0i==0:
        info[0]=1
        skip0=True

    counter_0s_0=0

    #iterate backwards to find full coefficient
    found_decimal0=False
    decimal_pos0=0
    for i in range(c0i-1,-1,-1): 
        if skip0==True:
            break
        if fixed_string[i].isnumeric()==False:
            if fixed_string[i]=='.' and found_decimal0==False:
                found_decimal0=True
                decimal_pos0=counter_0s_0
                continue

            return "ERROR: incorrect format of quadratic @ 81"
        info[0] += int(fixed_string[i])*10**counter_0s_0
        counter_0s_0+=1

    if info[0]==0:
        return "ERROR: not quadratic"
    
    if decimal_pos0>0:
        info[0]=info[0]/(10**decimal_pos0)

    ###########################################################################################
    #find coefficient b
    ###########################################################################################  
    
    #splits string in 2 after first "x" has been found
    split_string = re.split("x", fixed_string, 1) 

    #check there is only one exponential term
    if len(re.findall("\^",split_string[1]))>1:
        return "ERROR: incorrect format of quadratic @ 97"
    
    
    c1=re.search("x",split_string[1])
    skip1=False

    if c1: #there is a b term
        c1i=c1.start()
    else: #there is no b term
        info[1]=0
        c1i=9 #dummy value, won't be used anyways
        skip1=True
        

    
    #no explicit coefficient for x term means coefficient==1
    if c1i==3:
        info[1]=1
        skip1=True

    counter_0s_1=0
    decimal_pos1=0

    #iterate backards to find full coefficient
    found_decimal1=False
    for k in range(c1i-1,-1,-1): 
        if skip1==True:
            break
        if split_string[1][k].isnumeric()==False:
            if split_string[1][k]=='.' and found_decimal1==False:
                found_decimal1=True
                decimal_pos1=counter_0s_1
                continue
            #this would be an error, i think this part of the code can never be reached, need to double check
            if split_string[1][k]=='+' or split_string[1][k]=='-':
                break

            info[1]="ERROR"
            break
        info[1] += int(split_string[1][k])*10**counter_0s_1
        counter_0s_1+=1

    if decimal_pos1>0:
        info[1]=info[1]/(10**decimal_pos1)

    
    ###########################################################################################
    #find coefficient c
    ########################################################################################### 

    #array of entered string split by + or -
    c2split=re.split("\+|-",fixed_string)
    c_found=False
    skip2=False

    #check if there is no c term
    for s in c2split:
        if re.search("x",s) == None:
            c_found=True
    if c_found == False:
        info[2]=0
        skip2=True

    found_decimal2=False
    decimal_pos2=0
    digits_passed=0

    if skip2==False:
        c2=""
        #iterate through final string of the array, which only contains numbers not followed by x (c term)
        for l in c2split[len(c2split)-1]:
            if l.isnumeric()==False:
                if l=='.' and found_decimal2==False:
                    found_decimal2=True
                    decimal_pos2=digits_passed
                    continue
                return "ERROR: incorrect format of quadratic @ 158"
            c2+=l
            digits_passed +=1

        info[2]=int(c2)

        if decimal_pos2>0:
            info[2]=info[2]/(10**(len(c2)-decimal_pos2))



    #assign signs to coefficients
    #_______________________________
    a=""
    b=""
    c=""
    coefs=[a,b,c]

    for r in range(3,6):
        if info[r]=='-':
            coefs[r-3]+='-'
    for r2 in range(3):
        if r2==3:
            break

        coefs[r2]+=str(info[r2])
        coefs[r2]=float(coefs[r2])

    return coefs

