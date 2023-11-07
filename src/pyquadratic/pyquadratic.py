import math
import re


def realSolution(string: str) -> []: 
    nums= _readString(string)
    a=nums[0]
    b=nums[1]
    c=nums[2]
    answers=[]
    if b*b-4*a*c < 0:
        raise ValueError("Error: No Real Solution, Try Again")
    answers.append((b*(-1)+math.sqrt(b*b-4*a*c))/2*a)
    answers.append((b*(-1)-math.sqrt(b*b-4*a*c))/2*a)

    for a in range(len(answers)):
        if answers[a]==int(answers[a]):
            answers[a]=int(answers[a])
    return answers

def toFactoredForm(stdForm: str) -> str:
    coefs = _readString(stdForm)
    a = coefs[0]
    if a == 0:
        return stdForm
    solutions = realSolution(stdForm)
    if a == 1:
        a = ""
    sign0 = "+" if solutions[0] < 0 else "-"
    sign1 = "+" if solutions[1] < 0 else "-"
    solutions[0] = abs(solutions[0])
    solutions[1] = abs(solutions[1])
    if int(solutions[0]) == solutions[0]:
        r1 = int(solutions[0])
    else:
        r1 = solutions[0]
    
    if int(solutions[1]) == solutions[1]:
        r2 = int(solutions[1])
    else:
        r2 = solutions[1]

    factored_form = str(a) + "(x" + str(sign0) + str(r1) + ")(x" + str(sign1) + str(r2) + ")"
    return factored_form 

def toVertexForm(stdForm: str) -> str:
   
    #find values of a,b,c
    a=_readString(stdForm)[0]
    b=_readString(stdForm)[1]
    c=_readString(stdForm)[2]


    # Convert to vertex form
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)

    a_str = '' if a == 1 else '-' if a == -1 else str(a)

    h = int(h) if int(h)==h else float(h)

    h_str = '' if h == 0 else str(abs(h))
    h_sign = '+' if h < 0 else '-'
    h_term = f"(x{h_sign}{h_str})" if h_str else "x"

    k = int(k) if int(k)==k else float(k)

    k_str = '' if k == 0 else f"+{k}" if k > 0 else f"-{-k}"

    vertex_form = f"{a_str}{h_term}^2{k_str}"

    return vertex_form

def simplifyQuadratic(stdForm: str) -> str:
    try:
        a, b, c = _readString(stdForm)
    except ValueError as e: 
        raise ValueError('Error: Invalid Input, Try Again') 

    while a != int(a) or b != int(b) or c != int(c):
        a *= 10
        b *= 10
        c *= 10

    a = int(a)
    b = int(b)
    c = int(c)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def gcd_iteration(a, b, c):
        return gcd(gcd(a, b), c)

    result = gcd_iteration(a, b, c)

    if result > 0:
        result = result
    elif result < 0:
        result = -result

    a_result = a/result
    b_result = b/result
    c_result = c/result

    a_result = int(a_result)
    b_result = int(b_result)
    c_result = int(c_result)

    if a_result == 1:
        a_result = None
    elif a_result < 1:
        b_result = -b_result
        c_result = -c_result
        if a_result == -1:
            a_result = None
        else:
            a_result = -a_result

    if b_result == 0.0 and c_result == 0.0:
        return f"{result}x^2"
    elif b_result > 0:
        if b_result != 1:
            if c_result > 0:
                if a_result != None:
                    return f"{a_result}x^2+{b_result}x+{c_result}"
                else:
                    return f"x^2+{b_result}x+{c_result}"
            elif c_result < 0:
                if a_result != None:
                    return f"{a_result}x^2+{b_result}x{c_result}"
                else:
                    return f"x^2+{b_result}x{c_result}"
            else:
                if a_result != None:
                    return f"{a_result}x^2+{b_result}x"
                else:
                    return f"x^2+{b_result}x"
        else:
            if c_result > 0:
                if a_result != None:
                    return f"{a_result}x^2+x+{c_result}"
                else:
                    return f"x^2+x+{c_result}"
            elif c_result < 0:
                if a_result != None:
                    return f"{a_result}x^2+x{c_result}"
                else:
                    return f"x^2+x{c_result}"
            else:
                if a_result != None:
                    return f"{a_result}x^2+x"
                else:
                    return f"x^2+x"
    elif b_result < 0:
        if b_result != -1:
            if c_result > 0:
                if a_result != None:
                    return f"{a_result}x^2{b_result}x+{c_result}"
                else:
                    return f"x^2{b_result}x+{c_result}"
            elif c_result < 0:
                if a_result != None:
                    return f"{a_result}x^2{b_result}x{c_result}"
                else:
                    return f"x^2{b_result}x{c_result}"
            else:
                if a_result != None:
                    return f"{a_result}x^2{b_result}x"
                else:
                    return f"x^2{b_result}x"
        else:
            if c_result > 0:
                if a_result != None:
                    return f"{a_result}x^2-x+{c_result}"
                else:
                    return f"x^2-x+{c_result}"
            elif c_result < 0:
                if a_result != None:
                    return f"{a_result}x^2-x{c_result}"
                else:
                    return f"x^2-x{c_result}"
            else:
                if a_result != None:
                    return f"{a_result}x^2-x"
                else:
                    return f"x^2-x"
    else:
        if c_result > 0:
            if a_result != None:
                return f"{a_result}x^2+{c_result}"
            else:
                return f"x^2+{c_result}"
        elif c_result < 0:
            if a_result != None:
                return f"{a_result}x^2{c_result}"
            else:
                return f"x^2{c_result}"
        else:
            if a_result != None:
                return f"{a_result}x^2"
            else:
                return f"x^2"

def _readString(string: str):

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

    #check  if x is included in string
    if re.search("x",fixed_string) == None:
        raise ValueError("Error: Invalid Input, Try Again")
    
    #check if term a is negative
    if fixed_string[0]=='-':
        info[3]='-'
        #correct string
        temp=""
        for m in range(1,len(fixed_string)):
            temp+=fixed_string[m]
        fixed_string=temp

    #check for only one exponential
    if len(re.findall("\^",fixed_string))>1:
        raise ValueError("Error: Invalid Input, Try Again")

    #check there are no more than 3 terms
    if len(re.findall("x",fixed_string))>2 or len(re.findall("\+|-",fixed_string))>2:
        raise ValueError("Error: Invalid Input, Try Again")
    
    #check if expression is quadratic
    if re.search("\^2",fixed_string) == None or (fixed_string[re.search("\^2",fixed_string).start()+1].isnumeric() and 
                                                 re.search("\^2",fixed_string).start()+3==len(fixed_string)):
        raise ValueError("Error: Invalid Input, Try Again")

    #check there are well defined terms
    for split in re.split("\+|-",fixed_string):
        if len(split)<1:
            raise ValueError("Error: Invalid Input, Try Again")

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
    found_decimal0=False
    decimal_pos0=0

    #iterate backwards to find full coefficient
    for i in range(c0i-1,-1,-1): 
        if skip0==True:
            break
        if fixed_string[i].isnumeric()==False:
            if fixed_string[i]=='.' and found_decimal0==False:
                found_decimal0=True
                decimal_pos0=counter_0s_0
                continue
            raise ValueError("Error: Invalid Input, Try Again")
        info[0] += int(fixed_string[i])*10**counter_0s_0
        counter_0s_0+=1

    if info[0]==0:
        raise ValueError("Error: Invalid Input, Try Again")

    info[0]=info[0]/(10**decimal_pos0)

    ###########################################################################################
    #find coefficient b
    ###########################################################################################  
    
    #splits string in 2 after first "x" has been found
    split_string = re.split("x", fixed_string, 1) 

    #check there is only one exponential term
    if len(re.findall("\^",split_string[1]))>1:
        raise ValueError("Error: Invalid Input, Try Again")
    
    
    c1=re.search("x",split_string[1])
    skip1=False

    if c1: #there is a b term
        c1i=c1.start()
    else: #there is no b term
        info[1]=0
        c1i=9 #dummy value, won't be used anyways
        skip1=True
        info[5]=info[4] #assign negative sign to c term if b term doesn't exist to account for minus sign in string (if minus sign exists)
        info[4]='+' #if no b term, sign should be positive so that b term shows as 0 rather than -0
            
    #no explicit coefficient for x term means coefficient==1
    if c1i==3:
        info[1]=1
        skip1=True

    counter_0s_1=0
    decimal_pos1=0
    found_decimal1=False

    #iterate backards to find full coe
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

    passed_digits=0
    decimal_pos2=0
    found_decimal2=False
    if skip2==False:
        c2=""
        #iterate through final string of the array, which only contains numbers not followed by x (c term)
        for l in c2split[len(c2split)-1]:
            if l.isnumeric()==False:
                if l=='.' and found_decimal2==False:
                    found_decimal2=True
                    decimal_pos2=passed_digits
                    continue
                raise ValueError("Error: Invalid Input, Try Again")
            c2+=l
            passed_digits+=1

        info[2]=int(c2)

        if found_decimal2==True:
            info[2]=info[2]/(10**(len(c2)-decimal_pos2))

    #assign signs to integers
    a=""
    b=""
    c=""
    coefs=[a,b,c]

    #formatting return values
    for r in range(3,6):
        if info[r]=='-':
            coefs[r-3]+='-'
    for r2 in range(3):
        if r2==3:
            break
        coefs[r2]+=str(info[r2])
        coefs[r2]=float(coefs[r2])
    for r3 in range(3):
        if int(coefs[r3])==coefs[r3]:
            coefs[r3]=round((coefs[r3]))

    return coefs
