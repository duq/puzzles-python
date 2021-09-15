def isValid(s: str) -> bool:
    parenthesisPairs = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    stack = []

    for char in s:
        if (char in parenthesisPairs.values()):
            stack.append(char)
        elif char in parenthesisPairs.keys():
            if stack == [] or parenthesisPairs[char] != stack.pop():
                return False
        else:
            continue
    return stack == []

print(isValid("s()[]{}xx(())xss"))
