#Remove Brackets

def removeBrackets(Exp):
    s = list(Exp)
    n = len(Exp)

    ans = [1] * (n + 1)
    lasta = [0] * (n + 1)
    nxta = [0] * (n + 1)

    l = -1

    # Start Iterating from starting index
    for i in range(n):
        lasta[i] = l
        if s[i] in ['*', '+', '-', '/', '^', '%', '@', '?', ';', '~', '#', '$', '&']:
            l = s[i]

    # Start Iterating from last index
    l = -1

    for i in range(n - 1, -1, -1):
        nxta[i] = l
        if s[i] in ['*', '+', '-', '/', '^', '%', '@', '?', ';', '~', '#', '$', '&']:
            l = s[i]

    st = []
    sign = [-1] * 256
    mp = [0] * 256
    operand = ['*', '+', '-', '/', '^', '%', '@', '?', ';', '~', '#', '$', '&']

    for p in range(n):
        for x in operand:
            mp[ord(x)] = 0
            if x == s[p]:
                sign[ord(x)] = p
        if s[p] == '(':
            st.append(p)

        elif s[p] == ')':
            i = st.pop()
            j = p

            nxt = nxta[j]
            last = lasta[i]

            if i > 0 and (s[i - 1] == '%' or s[i-1] == '@' or s[i-1] == '?' or s[i-1] == ';' or s[i-1] == '»' or s[i-1] == '¿' or s[i-1] == '¸' or s[i-1] == '®' or s[i-1] == '¯') and s[i] == '(':
                continue


            # Iterate in operator array
            for x in operand:
                if sign[ord(x)] >= i:
                    mp[ord(x)] = 1
            ok = 0

            if i > 0 and j + 1 < n and s[i - 1] == '(' and s[j + 1] == ')':
                ok = 1
            if mp[ord('+')] == 0 and mp[ord('*')] == 0 and mp[ord('-')] == 0 and mp[ord('/')] == 0 and mp[ord('^')] == 0 and mp[ord('%')] == 0 and mp[ord('@')] == 0 and mp[ord('?')] == 0 and mp[ord(';')] == 0 and mp[ord('~')] == 0 and mp[ord('#')] == 0 and mp[ord('$')] == 0 and mp[ord('&')] == 0:
                ok = 1

            if last == -1 and nxt == -1:
                ok = 1
            if last == '/' or (last == '-' and (mp[ord('+')] == 1 or mp[ord('-')] == 1)):
                pass
            else:
                if (last == -1 or last == '+' or last == '-') and (nxt == -1 or nxt == '+' or nxt == '-'):
                    ok = 1

            # If the pair is reduntant
            if ok == 1:
                ans[i] = 0
                ans[j] = 0

    # Final string
    res = ""
    for i in range(n):
        if ans[i] > 0:
            res += s[i]
    return res
