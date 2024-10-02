numbers = [1,2,3,4,5,1,2,3,4,1,2,3]
# counter = []
# for i in range(max(numbers)):
#     counter.append(0)
# for number in numbers:
#     counter[number-1] += 1
# print(counter)

counter = {}
for number in numbers:
    if number not in counter:
        counter[number] = 1
    else:
        counter[number] += 1
print(counter)