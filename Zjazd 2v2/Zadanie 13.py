lista = [9,8,7,6,5,4,3,2,1]

def Insert_sort(A):
    for i in range(1,len(A)):
        print(range(1, len(A)))
        print("FOR")
        print("i= ", i)
        klucz = A[i]
        print("Klucz = ", klucz)
        j = i - 1
        print("j = ", j)
        while j>=0 and A[j]>klucz:
            print ("A od J = ", A[j])
            print("Wchodzę do pętli WHILE")
            A[j + 1] = A[j]
            print("A[j+1] = ", A[j])
            j = j - 1
            print("j2 = ", j)
            print("WHILE PAPA")
        A[j + 1] = klucz
    print(A)
Insert_sort(lista)

#Prowadzący rozwiązanie

liczby = [5,2,1,4,3]

for i in range (len(liczby)):
    index_minimum = i
    print(liczby[i:])
    for j in range(i+1, len(liczby)):
        if liczby[j]<liczby[index_minimum]:
            index_minimum = j
    liczby[i], liczby[index_minimum]=liczby[index_minimum],liczby[i]
print(liczby)