from sys import stdin

op = {
    "&": lambda x, y: x and y, 
    "|": lambda x, y: x or y,  
}

values = {}

class Node:
    def __init__(self, LP, op: int, start: int, end: int):
        self.center = LP[op]
        self.left = LP[start: op]
        self.right = LP[op + 1: end]
    
    def true_value(self):
        return op[self.center](self.left, self.right)
        
        
# Conversion de string a string sin espacios
def no_space_str(string):
    converted = ""
    for i in string:
        if i != " ":
            converted += i
    return converted


#Verificasion de la expresion
def valid_LP(LP):
    pila = []
    ans = None
    for i in range(len(LP)):
        char = LP[i]
        if char == "(" or char == ")" or char in op:
            pila.append(char)
            if len(pila) >= 3:
                if pila[-1] == ")" and pila[-2] in op and pila[-3] == "(":
                    pila.pop()
                    pila.pop()
                    pila.pop()
    if len(pila) == 0:
        ans = True
    else:
        ans = False
    
    return ans
        

 
# Valoracion de la expresion    
def val(LP, start, end):
    
    ans = None
    negation = False
    
    if LP[start] == "!":
        if LP[start + 1] == "(":
            ans = not val(LP, start + 1, end)
        else:
            ans = not values[LP[start+1]]
            
        negation = True
    
    if not negation:
        brk = 0
        md = -1
        for i in range(end):
            if LP[i] == "(":
                brk += 1
            elif LP[i] == ")":
                brk -= 1
        
            if LP[i] in op and brk == 1:
                md = i
                
                x = Node(LP, md , start + 1, end)
                if x.left.isalpha():
                    x.left = values[x.left]
                else:
                    x.left = val(x.left, 0, len(x.left) - 1)
                    
                    
                if x.right.isalpha():
                    x.right = values[x.right]
                else:
                    x.right = val(x.right, 0, len(x.right) - 1)
                    
                ans = x.true_value()
    
    return int(ans)
    


def main():
    for i in range(int(stdin.readline().strip())):
        truevalue = stdin.readline().split()
        values[truevalue[0]] = int(truevalue[1])
    
    for i in range(int(stdin.readline().strip())):
        LP = no_space_str(stdin.readline().strip())
        if valid_LP(LP):
            print(val(LP, 0, len(LP)-1))
        else:
            print("Exprecion no valida")
            

if __name__ == "__main__":
    main()