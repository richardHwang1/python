old_list = [1,2,3,1,2,3]
value = 2
new_list = []

print(old_list)

while old_list:
    temp = old_list.pop()
    if temp == value:
        continue
    else:
        new_list.insert(0,temp)

print(new_list)