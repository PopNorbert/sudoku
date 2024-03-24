def check(x):
    groups = []
    for i in range(9):
        a = []
        for j in range(9):
            a.append(x[(i,j)])
        groups.append(a)
    for j in range(9):
        a = []
        for i in range(9):
            a.append(x[(i,j)])
        groups.append(a)
    for i in range(3):
        for j in range(3):
            a = []
            for m in range(i*3,i*3+3):
                for n in range(j*3, j*3+3):
                    a.append(x[(m,n)])
            groups.append(a)
    for group in groups:
        if len(group) != len(set(group)):
            return False
    return True