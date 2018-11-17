import numpy

def add_matrices(a, b):
    if ((len(a) != len(b))or (len(a[0]) != len(b[0]))):
        raise ValueError ("Różny kształt")
    c = []
    for i in range(len(a)):
        new_c = []
        for j in range(len(a[i])):
            new_c.append (a[i][j] + b[i][j])
        c.append(new_c)
    return c

def sub_matrices (a, b):
    if ((len(a) != len(b))or (len(a[0]) != len(b[0]))):
        raise ValueError ("Różny kształt")
    c = []
    for i in range(len(a)):
        new_c = []
        for j in range(len(a[i])):
            new_c.append (a[i][j] - b[i][j])
        c.append(new_c)
    print(c)

#albo zrobic matryce za pomoca numpy jest zainportowany

a = [
    [1,2,3],
     [4,5,6]
     ]
b = [
    [4,5,6],
     [1,2,3]
     ]






