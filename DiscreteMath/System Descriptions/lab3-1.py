from logic import TruthTable


temp_list = []
temp_list2 = []
flag = 1
while flag:
  p1 = raw_input('Enter a proposition: ')
  p2 = raw_input('Would you like to enter more (Y/N):')
  temp_list.append(p1)
  if p2 == 'N':
    flag = 0

myTable = TruthTable(temp_list)

print("Your program uses propositional variables " + str(myTable.vars) + ":")
for i in myTable.vars:
  ptemp = raw_input("Enter meaning of " + str(i) + ":")
  temp_list2.append(ptemp)
for i in myTable.table:
  temp = 0
  for j in range(len(temp_list)):
    if i[1][j] == 1:
      temp = temp + 1
  if(temp == len(temp_list)):
    print("Your description is consistent when:")
    for j in range(len(temp_list2)):
      if(i[0][j]==0):
        print("It is not the case that "+str(temp_list2[j]))
      if(i[0][j]==1):
        print("It is the case that "+str(temp_list2[j]))
