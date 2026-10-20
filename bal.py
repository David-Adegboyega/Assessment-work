def parenthesis(n):
    result = 0
    for i in n:
        if i == '(':
            result += 1
        elif i == ')':
            result -= 1
            if result < 0:
                return ("Not Balanced")
    
    return "Balanced" if result == 0 else "Not Balanced"


r = parenthesis("((a+b))")
print(r)