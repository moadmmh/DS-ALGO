#implementing queue

class queue :
    def __init__ (self):
      self.queue =[]
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue (self):
        self.queue.pop(0)
    def isEmpty (self):
        return self.queue==[]
    def getLength (self):
        return len(self.queue)
    def printing (self):
        for elem in self.queue :
            print(elem,end=" ")
        print("\n")

object1=queue()
object1.enqueue(5)
object1.enqueue(58)
object1.enqueue(9)
object1.enqueue(12)
print("elements are")
object1.printing()
print(object1.getLength())
print(object1.isEmpty())
object1.dequeue()
print("new length after dequeue")
print(object1.getLength())
