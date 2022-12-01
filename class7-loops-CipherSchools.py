### Control Flow
## 2. Looping statements
# (i) While loops

a = 1
while a < 10:
    print(a)
    a += 1

# (ii) For loops

name = "jatin"
print(name.__iter__)

for c in name:
    print(c)
    print(type(c))

for i in range(5):
    print(i)

for i in range(5):
    print(i)
    if i==3:
        break

a=1
print(a)
del a  # Deletes "a" from memory
print(a) # Gives an error

for i in range(5):
    print(i)
    if i == 3:
        break
else: # The loop will run till 3 and will not run else
    print("something")
# for an else block to run a "for" loop should end sucessfully