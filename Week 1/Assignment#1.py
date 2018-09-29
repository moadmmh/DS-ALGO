
#Declaring the list name and its element
Fruits=["Apple","Orange","Durian","Mangos","Watermelon","Leomn","Jackfruit","Mangosteens"]

#Printing the elemnt and its index
for pos,name in enumerate(Fruits):
    print(pos,end=" ")
    print(name)

#adding 4 Fruits that starts with 'P'
Fruits.extend(["Pineapple","Papaya","Peach","Pitaya"])

#Removing elements starting with letter 'A'
for pos,elem in enumerate(Fruits) :
    if(elem.startswith('A')):
        del Fruits[pos]

print("\n")
print("printing the new list elements ")        
#print the new list
for pos,name in enumerate(Fruits):
    print(pos,end=" ")
    print(name)
    
#printing the new list size
print("The new size is :",len(Fruits))

#Declaring the new list Fruitri        
FruiTri =[]

#adding Fruits to FruiTri 3 times
for i in range(3):
    FruiTri.extend(Fruits)

print("\n")

#Sort the items in reversed way
FruiTri.sort(reverse=True)

CntWatermelon=0
CntL=0
CntO=0

for idx,elem in enumerate(FruiTri) :
    if(elem=="Watermelon"):
        CntWatermelon+=1
        print("The word watermelon exists in index ",idx)
    if(elem[0]=='L'): #We can use elem.startswith('L')
        CntL+=1
        print("A fruit that starts with Letter 'L' is:",elem," in index: ",idx)
    if(elem.endswith('O')): #We can use elem[-1]=='O'
        CntO+=1
        print("A fruit that ends with Letter 'o' is:",elem," in index: ",idx)

#Checking if thelements existed or not 
if(CntWatermelon==0):
    print("The word Watermelon is not in the FruiTri")
if(CntL==0):
    print("There is no element that starts with the letter 'L' in the FruiTri")
if(CntO==0):
    print("There is no elemnet that ends with the letter 'O' in the FruiTri")


print("Thanks for being here !")
