# Carson Kramer
# Extra Credit MP 2
# 12/6/18
# Period 9

list1 = []
count = 0
for n in range(int(input("Enter the number of dice to roll: "))):
    list1.append(1)
#print(list1)

for a in range(6):
    for n in range(len(list1)):
        if (n + 1) % (a + 1) == 0 and list1[n] != 0 and a != 0:
            list1[n] = list1[n] + 1
    #if a != 0:
        #print(list1)
        
for b in range(len(list1)):
    if list1[b] == 1:
        count = count + 1
        
if count == 1:
    print("There is " + str(count) + " one in the final list.")
else:
    print("There are " + str(count) + " ones in the final list.")
