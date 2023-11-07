from readString import _readString

def simplifyQuadratic(StdFunction):
    try:
        a, b, c = _readString(StdFunction)
    except ValueError as e: 
        return 'ERROR: No x^2 term'

    while a.is_integer() != True or b.is_integer() != True or c.is_integer() != True:
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