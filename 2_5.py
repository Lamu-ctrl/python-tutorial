arr1 = [i for i in range(1, 21, 2)]
arr2 = [i for i in range(2, 21, 2)]

for index in range(len(arr1)):
    print(arr1[index], '<--->', arr2[index])


for o, e in zip(arr1, arr2):
    print(o, e, sep=' <---> ')

# eles
arr1 = [i for i in range(10)]
arr2 = [i for i in range(5, 15)]

for t in zip(arr1, arr2):
    print(t[0], t[1])
print('*' * 10)

for i, j in zip(arr1, arr2):
    print(i, j)
print('*' * 10)
