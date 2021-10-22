import gc
class Node:
    def __init__(self,it,nt=None):
        self.item = it
        self.next = nt
class UnsortedLinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.count = 0
    def isEmpty(self):
        if self.head:
            return False
        return True
    def clear(self):
        self.__init__()
        gc.collect()
    def insertFirst(self, data):
        if self.isEmpty():
            newnode = Node(data)
            self.head = newnode         #self.head => Node
            self.last = newnode
            self.count += 1
        else:
            newnode = Node(data,self.head)
            self.head = newnode
            self.count += 1
    def insertLast(self, data):
        if self.isEmpty():
            self.insertFirst(data)
        else:
            self.count += 1
            newlastnode = Node(data)
            self.last.next = newlastnode
            self.last = newlastnode
    def remove(self, data):
        if self.size():
            print("List is empty")
            return
        elif self.size() != 0:
            n = self.head
            if n.item == data:
                result = data
                self.head = n.next
                self.count -= 1
                return result
            while n is not None:
                if n.next is None:
                    return
                elif n.next.item == data:
                    result = data
                    n.next = n.next.next
                    self.count -= 1
                    return result
                n = n.next
            gc.collect()
            return 
        elif self.size():
            print("List is empty")
            return
    def find(self, data):
        if self.size():
            print("List is empty")
            return
        elif self.size() != 0:
            n = self.head
            while n is not None:
                if n.item == data:
                    print(data," found")
                    break
                n = n.next
            return 
    def size(self):
        return self.count
    def print(self):
        if self.size() != 0:
            n = self.head
            while n is not None:
                if n.next is None:
                    print(n.item)
                else:
                    print(n.item,end=" ")
                n = n.next

def main():
    lst = UnsortedLinkedList()
    print("Enter a command: inf(insertFirst), inl(insertLast), e(mpty), c(lear),")
    print("r(emove), f(ind), p(rint): ")
    while True:
        print("> ", end = "")
        line = input().split()
        command = line[0]
        if command == "inf":
            lst.insertFirst(line[1])
        elif command == "inl":
            lst.insertLast(line[1])
        elif command == "e": print(lst.isEmpty())
        elif command == "c": lst.clear()
        elif command == "p": lst.print()
        elif command == "s": print(lst.size())
        elif command == "r":
            elem = line[1]
            try:
                if lst.remove(elem):
                    print(elem, " removed")
                else:
                    if lst.count == 0:
                        print("List is empty") 
                    else:
                        print("No such element")
            except Exception as e:
                print(e)
        elif command == "f":
            elem = line[1]
            try:
                if lst.find(elem):
                    print(elem," found")
                else:
                    if lst.count == 0:
                        print("List is empty") 
                    else:
                        print("No such element")
            except Exception as e:
                print(e)
        elif command == "q" : break

main()