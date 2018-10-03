class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def AddElement (self,elem):
        newnode=Node(elem)
        newnode.next=self.head
        self.head=newnode
        
    def DeleteElementOnFront (self):
        tmp=self.head
        if tmp!=None:
            self.head=tmp.next
        else :
            print("The Linked List is empty we can't find a Head")

    def DeleteElementOnTail (self):
        tmp=self.head 
        prev=None
        while tmp.next:
            prev=tmp
            tmp=tmp.next
        prev.next=None
            
    def GetLength(self):
        tmp=self.head
        cnt=0
        while tmp!=None:
            tmp=tmp.next
            cnt+=1
        return cnt

    def isEmpty(self):
        if self.head==None :
            print("The list is Empty !")
        else :
            print("There are some elements on the list")
        
    def count (self):
        tmp=self.head
        sum=0
        while tmp!=None:
            sum+=tmp.data
            tmp=tmp.next
        return sum
    
    def getHead(self):
        tmp=self.head
        return tmp.data

    def getTail(self):
        tmp = self.head
        while tmp.next:
            tmp = tmp.next
        return tmp.data

    def delete(self, data):
        tmp = self.head
        prev = None
        found = False
        while tmp and not found:
            if data == tmp.data:
                found = True
            else:
                prev = tmp
                tmp = tmp.next
        if found:
            if prev == None:
                self.head = self.head.next
            else:
                prev.next = tmp.next

    def SortElements (self,newList=[]):

            anotherList = []
            tmp =self.head
            x=self.head
            while tmp!=None :
                anotherList.append(tmp.data)
                tmp=tmp.next
            anotherList=sorted(anotherList,reverse =False)
            
            for i in anotherList :
                    if x!=None :
                        x.data=i
                        x=x.next
            
    def PrintList(self):
        tmp=self.head
        while tmp.next!=None:
            print(tmp.data,end=" ")
            tmp=tmp.next
        print(tmp.data)

    def SearchItem (self,item):
        tmp=self.head
        while tmp!=None :
            if tmp.data==item:
                print("The item was found")
                return 
            tmp=tmp.next
        print("Item is not in the list !")

    def appending (self,item):
        newnode=Node(item)
        if self.head==None:
            self.head=newnode
        else :
            while self.head!=None :
                self.head=self.head.next
            self.head=newnode
            
        
print("Linked List")
while True:
    print("----------------")
    print("1.Create the list")
    print("2.Add Elements at the beginnig of the list")
    print("3.Get the Head Value")
    print("4.Remove the Head Value")
    print("5.Get the Tail Value")
    print("6.Remove the Tail Value")
    print("7.Sort the Elements in the Linked list")
    print("8.Print the elements in the Linked List")
    print("9.GEt the sum of the Linked List elements")
    print("10.Check if the List is Empty !")
    print("11.The Length of The list")
    print("12.Search for a specific Item in the Linked List")
    print("13.To append elements to the list")
    print("14.Exit")

    a=int(input())

    if a==1:
        list=SinglyLinkedList()
        print("We created a new list for you :)")

    elif a==2:
        char='y'
        while char=='y' or char=='Y' :
            print("Enter number to add to list:")
            z=int(input())
            list.AddElement(z)
            print("Enter more(y/n):")
            char=input()
        charr ='y'
        print("Do you want To delete any specific Element (In case YOU Entered a wrong value)")
        charr =input()
        while charr=='y' or charr=='Y':
            print("Enter the Number's Value :")
            b=int(input())
            list.delete(b)
            print("Another one maybe ?")
            charr=input()
        print("Adding Elements Operation is Done !")
        
    elif a== 3:
        print("The Head's Value is :",list.getHead())

    elif a== 4:
        list.DeleteElementOnFront()
        print("The Head value was removed")

    elif a==5:
        print("The  Tail value is :",list.getTail())

    elif a==6 :
        list.DeleteElementOnTail()
        print("The tail Value was removed")

    elif a==7 :
        list.SortElements()
        print("Your Linked List elements have been sorted")

    elif a==8 :
        print("Here are your Linked List Elements")
        list.PrintList()

    elif  a==9 :
        print("The sum of your Linked List Elements is : ",list.count())

    elif a==10 :
        list.isEmpty()

    elif a==11 :
        print("The size of Linked List is :",list.GetLength())

    elif a==12 :
        print("Enter the Item Value")
        r=int(input())
        list.SearchItem(r)

    elif a==13 :
        print("Enter number")
        f=int(input())
        list.appending(f)
        print("Done !")
        
    elif a==14 :
        print("Thanks for being here")
        break

    else :
        print("Enter only numbers from 1-14 accordingly !!")

    print("-------------------")
    print("\n")
