from logic import TruthTable


temp_list = []
flag = 1
i = 0
while flag:
    i = i + 1
    p1 = raw_input('Enter a proposition: ')
    p2 = raw_input('Would you like to enter more (Y/N):')
    temp_list.append(p1)
    if p2 == 'N':
        flag = 0

myTable = TruthTable(temp_list)
print myTable.table
for i in myTable.table:
    temp = 0
    for j in range(len(temp_list)):
        if i[1][j] == 1:
            temp = temp + 1
    if(temp == len(temp_list)):
        flag = 1


if flag:
    print ("Your description is consistent.")
else:
    print ("Your description is not consistent.")
