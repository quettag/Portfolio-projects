def caesar(x):
    lst = []
    space = ''
    for i in x:
        i = chr(ord(i)-1)
        lst.append(i)
    for i in lst:
        space += str(i) + "-"
        space = space[:-1]
    if '`' in space:
        output = space.replace("`","z")
        return output
    else:
        return space