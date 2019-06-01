from logic import TruthTable


p1 = raw_input('Enter proposition 1: ')
p2 = raw_input('Enter proposition 2: ')
myTable = TruthTable(['p', 'q'], [p1, p2])
flag = 0
for i in myTable.table:
    if i[1][1] != i[1][0]:
        flag = 1

if flag:
    print ("The propositions are not equivalent")
else:
    print ("The propositions are equivalent")
