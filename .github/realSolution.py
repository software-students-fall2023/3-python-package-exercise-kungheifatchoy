from _readString import *
import math
def realSolution(string):
    
    nums=readString(string)
    a=nums[0]
    b=nums[1]
    c=nums[2]

    answers=['none','none']

    for i in answers:
        if i.isnumeric()==False:
            return readString(string)
    
    if b*b-4*a*c<0:
        print("No real solutions")

    answers[0]=(b*(-1)+math.sqrt(b*b-4*a*c))/2*a
    answers[1]=(b*(-1)-math.sqrt(b*b-4*a*c))/2*a
    
    return answers
