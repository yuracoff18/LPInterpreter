"""

    Yura Hernandez H
    02/03/2025
    Matematicas discretas

"""
from parteA import val, string_to_list, values
from sys import stdin


def prove_val(LP):
    answers = []
    for p in [0,1]:
        for q in [0,1]:
            for r in [0,1]:
                for s in [0,1]:
                    for t in [0,1]:
                        values["p"] = p
                        values["q"] = q
                        values["r"] = r
                        values["s"] = s
                        values["t"] = t
                        
                        answers.append(val(LP, 0, len(LP)-1))
    ans = None
    if answers.count(1) > 0 and answers.count(0) == 0:
        ans = 1
    elif answers.count(1) == 0 and answers.count(0) > 0:
        ans = 0
    else:
        ans = -1
    return ans
    
    
def main():
    for i in range(int(stdin.readline().strip())):
        LP = string_to_list(stdin.readline().strip())
        print(prove_val(LP))
            

if __name__ == "__main__":
    main()