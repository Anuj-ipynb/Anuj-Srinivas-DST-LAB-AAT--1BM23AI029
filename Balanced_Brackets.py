

import math
import os
import random
import re
import sys

def isBalanced(s):
    map = {')': '(', '}': '{', ']': '['}
    stack = []
    for c in s:
        if c in map.values(): 
            stack.append(char)
        elif c in map:  
            if stack and stack[-1] == map[c]:
                stack.pop() 
            else:
                return "NO"  
        else:
            return "NO"  
    return "YES" if not stack else "NO"
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
