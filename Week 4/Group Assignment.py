class linkedList :
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class queue :
    def __init__(self):
        self.count=0
        self.head = None
        self.tail = None

    def isEmpty (self):
        if self.head == None :
            print("The queue is empty")
        else:
            print("The queue is not empty")


    def enqueue(self, x):
        newNode = linkedList(x)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.count+=1
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.count += 1

    def dequeue (self):
        self.head=self.head.next
        self.count -= 1

    def displayTheHead(self):
        print(self.head.data)

    def displayTheEnd (self):
        print(self.tail.data)

    def counter (self):
        print(self.count)
    def returnCounter (self):
        return self.count

    def printQueue(self):
        tmp=self.head
        listlink=[]
        while tmp.next!=None:
            listlink.append(tmp.data)
            #print(tmp.data,end=" ")
            tmp=tmp.next
        listlink.append(tmp.data)
        print(listlink)

x=queue()
while True:
    print("Queue")
    print("----------------")
    print("1.Add Elements to the queue")
    print("2.Remove Elements from the queue")
    print("3.Count Element in Queue")
    print("4.Show List of Elements in the Queue")
    print("5.Check if queue is empty")
    print("6.Check and display the last item in the Queue")
    print("7. Check and display the first item in the Queue")
    print("8. Exit")
    print("What do you want to do now ?")

    n=int(input())
    if n>0 and n<9 :
       if n==1 :
           ans='a'
           while ans is not int:
                try:
                    ans = int(input('What element do you want to add : '))
                    break
                except ValueError:
                    print('Please enter a valid number: ')
           x.enqueue(ans)
           while True:
               print("Do you want to add another element ? Y/N")
               ans=input()
               if ans == 'y' or ans == 'Y':
                   a='a'
                   while a is not int:
                       try:
                           a = int(input('What element do you want to add : '))
                           break
                       except ValueError:
                           print('Please enter a valid number: ')
                   x.enqueue(a)
               elif ans == 'n' or ans == 'N':
                 break
               else:
                print("Invalid input, try again.. ")

       elif n == 2:
           ans = 'a'
           while ans is not 'n' or 'N' or 'y' or 'Y':
               try:
                   ans = input('Do you want to delete an element ? Y/N  ')
                   break
               except ValueError:
                   print('Please enter a valid choice: ')

           if ans == 'y' or ans=='Y' :
              a=x.returnCounter()
              if a==0 :
                 print('The queue is empty!')
              elif a>0:
                 x.dequeue()
                 print(" You have deleted one element!")
           elif ans == 'n' or ans == 'N':
                break

       elif n == 3:
            print("The number of element in the queue is :")
            x.counter()

       elif n == 4:
           a=x.returnCounter()
           if a >0:
                print("The list of the element in the queue is :")
                x.printQueue()
           else:
               print("The lis is empty!")

       elif n == 5:
            x.isEmpty()

       elif n == 6:
           a = x.returnCounter()
           if a > 0:
                print("The the last element in the queue is : ")
                x.displayTheEnd()
           else:
             print("The lis is empty!")


       elif n==7:
            a = x.returnCounter()
            if a > 0:
                 print("The the first element in the queue is :")
                 x.displayTheHead()
            else:
                print("The lis is empty!")


       elif n == 8:
            print("Thanks for being here")
            break

    else:
        print("Wrong choice ")
        print("What do you want to do now ?")


