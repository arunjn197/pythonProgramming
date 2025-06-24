words = ["cat", "window", "defenestrate"]

for w in words:
    print(w, len(w))

#####################################

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

for i in range(5):
    print(i)

##################################
numList1 = list(range(5,10))

print(numList1)

##################################
numList1 = list(range(0, 10, 3))

print(numList1)

##################################
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')