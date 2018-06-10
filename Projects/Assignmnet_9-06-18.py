





Num_list = [5,7,9,10,11,12,73,1,5,-7]


Max_value = Num_list[0]
Min_value = Num_list[0]

'''

###### Max and Min using Funtions


for i in range(0, len(Num_list),1):

    Max_value = max(Max_value, Num_list[i])
    Max_value = min(Max_value, Num_list[i])

print("Max value is :",Max_value)
print("Min value is :",Min_value)


'''
'''

for i in range(0, len(Num_list),1):
    if Max_value < Num_list[i]:
        Max_value = Num_list[i]

print("Max value is :",Max_value)

for i in range(0, len(Num_list),1):
    if Min_value > Num_list[i]:
        Min_value = Num_list[i]
print("Min value is :",Min_value)

'''
'''
for j in range(0,9):
    for i in range(0,9):
        if Num_list[i] > Num_list[i+1]:
            Swap = Num_list[i]
            Num_list[i] = Num_list[i+1]
            Num_list[i+1] = Swap
print ("The Min Value is :", Num_list[0])
print ("The Max Value is :",Num_list[9])
print ("The Sorted List is : ", Num_list)

'''

'''

A = 10
B = 10

if A > B :
    print("A is Big :", A)
elif A < B :
    print ("B is big :", B)
else:
    print (A," = ",B)


'''

