import gc
class Node:
    def __init__(self, item, next = None):
        self.item = item
        self.next = next
class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0
    def isEmpty(self):
        if self.top:
            return False
        return True
    def size(self):
        return self.count            
    def clear(self):
        self.__init__()
        gc.collect()
    def push(self, item):
        newnode = Node(item, self.top)
        self.top = newnode
        self.count += 1
    def pop(self):
        if self.isEmpty():
            return None
        self.count -= 1
        item = self.top.item
        self.top = self.top.next
        return item
    def peek(self):
        if self.isEmpty():
            return None
        return self.top.item
    def print(self):
        if self.size() != 0:
            n = self.top
            while n is not None:
                if n.next is None:
                    print(n.item)
                else:
                    print(n.item,end=" ")
                n = n.next


def main():
    stack = LinkedStack()
    print("Enter a command: pop, push, peek, size, empty, p(rint), q(uit)")
    while True:
        print("> ", end = "")
        line = input().split()
        command = line[0]
        if command == "push":
            item = line[1]
            stack.push(item)
        elif command == "pop":
            print(stack.pop())
        elif command == "peek":
            print(stack.peek())
        elif command == "empty":
            print(stack.isEmpty())
        elif command == "size":
            print(stack.size())
        elif command == "p":
            stack.print()
        elif command == "c":
            stack.clear()
        elif command == "q":
            break
main()