


with open('5-account.txt', 'r') as f:
    a = [x.rstrip() for x in f.readlines()]

for i in a:

    print(i.split(','))

print(a)