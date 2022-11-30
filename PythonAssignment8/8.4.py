# This is problem to convert all the negative coordinates to a positive coordinates;
# The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
# We can add or delete any number from the coordinates ; however graph should not be changed;
# Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
# Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]

list_x=[]
list_y=[]
n=int(input("Enter the number of coordinates"))
for x in range(0,n):
    list_x.append(int(input("Enter the x value:")))
    list_y.append(int(input("Enter the y values:")))
list_p=[]
mini=min(min(list_x),min(list_y))
if mini < 0:
    to_add = 0-(mini)
    for x in range(0,n):
        list_x[x]=int(list_x[x])+to_add
        list_y[x]=int(list_y[x])+to_add
    for x in range(0, n):
        print("(", list_x[x], ",", list_y[x], ")")
else:
    print("All the coordinates are positive")



