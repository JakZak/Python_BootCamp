zbior = {1,2,3,4}

zbior.add (1)

print(1 in zbior)

print(20 in zbior)

zbior.add('k')

for i in zbior:
    print(i)

print(zbior)

a ={1,2,3}
b ={3,4,5}

print(a|b) #suma
print (a - b) # różnica
print (a&b) # część wspólna - iloczyn
print (a^b) #różnica symetryczna

print (dir(a))
print (a.union(b))#suma
print(a.difference(b))# różnica
print(a.intersection(b))# część wspólna - iloczyn
print(a.symmetric_difference(b))#różnica symetryczna

