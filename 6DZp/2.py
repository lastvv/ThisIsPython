import random

def get_list(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]

#def shuffle_list(lst):
    #return random.shuffle(lst)
shuffle_list=lambda shuffle: random

n = 10
lft = -20
rght = 50

mylist = get_list(n, lft, rght)
print(mylist)
shuffle_list(mylist)
print(mylist)