'''
5 5 5 5 5
5 4 4 4 5
5 4 3 4 5
5 4 4 4 5
5 5 5 5 5
'''

'''
6 6 6 6 6 6
6 5 5 5 5 6
6 5 4 4 5 6
6 5 4 4 5 6
6 5 5 5 5 6
6 6 6 6 6 6
'''
'''
7 7 7 7 7 7 7 
7 6 6 6 6 6 7
7 6 5 5 5 6 7
7 6 5 4 5 6 7
7 6 5 5 5 6 7
7 6 6 6 6 6 7
7 7 7 7 7 7 7
'''
b = 5
for i in range(b):
    for j in range(b):
        print(i+1,end=" ")
    print()
print()
for i in range(b):
    for j in range(b):
        print(j+1,end=" ")
    print()
print()
for i in range(b):
    for j in range(b):
        print(max(i+1,j+1),end=" ")
    print()
print()
for i in range(b):
    for j in range(b):
        print(b-i,end=" ")
    print()
print()
for i in range(b):
    for j in range(b):
        print(b-j,end=" ")
    print()
print()
for i in range(b):
    for j in range(b):
        print(max(b-i,b-j),end=" ")
    print()
print()
a = 5
for i in range(a):
    for j in range(a):
        print(max(i+1,  j+1, a-i, a-j),end=" ")
    print()