
def isValid(s):
    # using a stack/list DS
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if stack and bracket_map.get(char) == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return not stack


if __name__ == "__main__":
    s = "{}))"
    print(isValid(s))