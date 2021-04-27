def bracket_check(text):
    stack = []
    for ch in text:
        if ch == '(':
            stack.append('(')
        elif ch == ')':
            if not stack or stack[-1] != '(':
                print('NO')
                return
            stack.pop()
    if not stack:
        print('YES')
    else:
        print('NO')
