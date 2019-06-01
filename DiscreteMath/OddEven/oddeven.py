arr = []
max = 0

while max < 10:
    num = int(input('enter an int: '))
    if num & 1:
        arr.append(num)
    max = max + 1

if len(arr) == 0:
    print('No odd numbers were entered')
else:
    oddArr = sorted(arr)
    print(oddArr[-1])
