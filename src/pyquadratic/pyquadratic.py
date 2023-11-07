import math
import re

def realSolution(string: str): 
    nums= _readString(string)
    a=nums[0]
    b=nums[1]
    c=nums[2]
    answers=[]
    if b*b-4*a*c < 0:
        raise ValueError("Error: No Real Solution, Try Again")
    answers.append((b*(-1)+math.sqrt(b*b-4*a*c))/2*a)
    answers.append((b*(-1)-math.sqrt(b*b-4*a*c))/2*a)
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
    factored_form = str(a) + "(x" + str(sign0) + str(solutions[0]) + ")(x" + str(sign1) + str(solutions[1]) + ")"
    return factored_form 

def toVertexForm(stdForm: str) -> str:
    # Remove whitespace and tokenize the input
    tokens = re.findall(r'([-+]?[^-+]+)', stdForm.replace(" ", ""))
    a = b = c = 0

    # check if quadratic
    x2_present = any('x^2' in token for token in tokens)
    if not x2_present:
        raise ValueError("Error: Invalid Input, Try Again")

    # Regular expressions to match coefficients
    square_term = r'([-+]?\d*\.?\d*)x\^2'
    linear_term = r'([-+]?\d*\.?\d*)x(?!\^)'
    constant_term = r'([-+]?\d*\.?\d*)$'

    # Extract coefficients
    for token in tokens:
        if 'x^2' in token:
            if token.strip() in ['-x^2', '+x^2', 'x^2']:
                a = 1 if token.strip() in ['+x^2', 'x^2'] else -1
            else:
                a = float(re.search(square_term, token).group(1))
        elif 'x' in token:
            if token.strip() in ['-x', '+x', 'x']:
                b = 1 if token.strip() in ['+x', 'x'] else -1
            else:
                b = float(re.search(linear_term, token).group(1))
        else:
            match = re.search(constant_term, token)
            if match:
                c = float(match.group(1))

    # if a = 0 invalid quadratic
    if a == 0:
        raise ValueError("Error: No Real Solution, Try Again")

    # Convert to vertex form
    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)

    a_str = '' if a == 1 else '-' if a == -1 else str(a)

    h = round(h, 2) if h % 1 else float(h)
    h_str = '' if h == 0 else str(abs(h))
    h_sign = '+' if h < 0 else '-'
    h_term = f"(x {h_sign} {h_str})" if h_str else "x"

    k = round(k, 2) if k % 1 else int(k)
    k_str = '' if k == 0 else f" + {k}" if k > 0 else f" - {-k}"

    vertex_form = f"{a_str}{h_term}^2{k_str}"

    return vertex_form

def simplifyQuadratic(stdForm: str) -> str:
    pass

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

    #iterate backwards to find full coefficient
    for i in range(c0i-1,-1,-1): 
        if skip0==True:
            break
        if fixed_string[i].isnumeric()==False:
            raise ValueError("Error: Invalid Input, Try Again")
        info[0] += int(fixed_string[i])*10**counter_0s_0
        counter_0s_0+=1

    if info[0]==0:
        raise ValueError("Error: Invalid Input, Try Again")

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
            
    #no explicit coefficient for x term means coefficient==1
    if c1i==3:
        info[1]=1
        skip1=True

    counter_0s_1=0

    #iterate backards to find full coe
    for k in range(c1i-1,-1,-1): 
        if skip1==True:
            break
        if split_string[1][k].isnumeric()==False:
            #this would be an error, i think this part of the code can never be reached, need to double check
            if split_string[1][k]=='+' or split_string[1][k]=='-':
                break

            info[1]="ERROR"
            break
        info[1] += int(split_string[1][k])*10**counter_0s_1
        counter_0s_1+=1

    
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


    if skip2==False:
        c2=""
        #iterate through final string of the array, which only contains numbers not followed by x (c term)
        for l in c2split[len(c2split)-1]:
            if l.isnumeric()==False:
                raise ValueError("Error: Invalid Input, Try Again")
            c2+=l

        info[2]=int(c2)

    #assign signs to integers
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