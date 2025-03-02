"""

    Yura Hernandez H
    02/03/2025
    Matematicas discretas

"""
from sys import stdin


op = {
    "&": lambda x, y: x and y, 
    "|": lambda x, y: x or y,  
}

values = {}

def string_to_list(string):
    converted = []
    for i in string:
        if i != " ":
            converted.append(i)
    return converted
            
            
def val(LP, start, end):
    ans = None
        
    if start == end:
         ans = values[LP[start]]
            
    elif LP[start] == "!":
         ans = not val(LP, start + 1, end)
            
    elif LP[start] == "(" and LP[end] == ")":     
        br = 0
        i = start + 1
        lop = -1    
        while i < end and lop == -1:     
            if LP[i] == "(":
                br += 1
            elif LP[i] == ")":
                br -= 1
            
            if LP[i] in op and br == 0:
                lop = i
            i += 1
            
        ans = op[LP[lop]](val(LP, start + 1, lop - 1), val(LP, lop + 1, end - 1))
    return ans


def main():
    for i in range(int(stdin.readline().strip())):
        truevalue = stdin.readline().split()
        values[truevalue[0]] = int(truevalue[1])
    
    for i in range(int(stdin.readline().strip())):
        LP = string_to_list(stdin.readline().strip())
        print(val(LP, 0,len(LP)-1))
            
    

if __name__ == "__main__":
    main()