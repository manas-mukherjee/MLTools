#Item: Avoid ELSE block after For and While loop
for i in range(3):
    print(i)
else:
    print("for loop ended")

try:
    x = 5
finally:
    print("Always run")

for i in []:
    print('will not work')
else:
    print("else block")

#usefulness of else block after loop
a = 4
b = 9

for i in range(2, min(a,b)+1):
    if a%i==0 and b%i==0:
        print("not coprime")
        break
else:
    print("prime")