



















def minAddToMakeValid(S):
    stack = []
    for i in S:
        if not stack:
            stack.append(i)
        else:
            if stack and ((stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']')):
                stack.pop()
            else:
                stack.append(i)

    return len(stack)




import sys
if __name__ == "__main__":
    # s = sys.stdin.readline().strip()
    s = ")([]]([(](])))([]()()]([][[)[()[)]([[(])][][[[([)]"
    # s = s.replace('[', '(').replace(']', ')')
    # s = "[])"

    print (minAddToMakeValid(s))

    # print (minAddToMakeValid(s)-len(s2)+minAddToMakeValid2(s)-len(s1))








