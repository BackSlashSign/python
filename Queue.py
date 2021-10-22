MAX_SIZE = 3
class Queue:
    def __init__(self):
        self.items = [None] * MAX_SIZE
        self.front = 0
        self.rear = 0
        self.count = 0
        self.maxSize = int(MAX_SIZE)

    def isEmpty(self):
        return self.count == 0
    def isFull(self):
        if self.count == self.maxSize:
            return True
        else :
            return False
    def clear(self):
        self.items.clear()
    def enqueue(self,elem):      #맨뒤에다 집어넣음
        if self.isFull() is not True:    
            for i in range(self.items.__len__()):
                if self.items[i] == None:
                    self.items[i] = elem
                    self.count += 1
                    # print("count:",self.count)
                    return self.items
        elif self.isFull() is True:
            lst = [None] * self.count
            self.resize()
            self.items.extend(lst)
            return self.enqueue(elem)
    def dequeue(self):      #맨앞에서 빼고 출력
        print(self.items.pop(0))        
    def resize(self):
        self.maxSize = self.maxSize * 2
        # print("maxSize:",self.maxSize)
        # print("count:",self.count)
        return 0
    def peek(self):         #맨앞 요소 확인
        return print(self.items[0])
    def size(self):
        count = 0
        for i in range(self.items.__len__()):
            if self.items[i] is not None:
                count = count + 1
        return print("size:",str(count).rjust(2))
    def print(self):
        lst = []
        for i in range(self.items.__len__()):
            if self.items[i] is not None:
                lst.append(self.items[i])
        return print(lst)
    def quit(self):
        exit()

def main():
    circlequeue = Queue()
    print("Enter a command: e(nqueue), d(equeue), peek, s(ize), p(rint), or q(uit)")
    while True :
        userInput = input()
        inputLst = userInput.split()
        if inputLst[0] == 'e':
            circlequeue.enqueue(inputLst[1])
        elif inputLst[0] == 'd':
            circlequeue.dequeue()
        elif inputLst[0] == 'peek':
            circlequeue.peek()
        elif inputLst[0] == 's':
            circlequeue.size()
        elif inputLst[0] == 'p':
            circlequeue.print()
        elif inputLst[0] == 'q':
            circlequeue.quit()
        elif inputLst[0] == 'size':
            circlequeue.size()
        else :
            print("잘못된 입력")
            break
    return

main()