def parenthesis(n):
    stack = []
    matching = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for character in n:
        if character in "({[":
            stack.append(character)

        elif character in ")}]":
            if not stack:
                return "Not Balanced"

            if stack[-1] != matching[character]:
                return "Not Balanced"

            stack.pop()

    return "Balanced" if not stack else "Not Balanced"


print(parenthesis("((a+b))"))       
print(parenthesis("{[(a+b)]}"))     
print(parenthesis("([)]"))          
print(parenthesis("{[a+b]"))        