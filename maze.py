class Stack:
    def __init__(self):
        self.top = []
        # self.InputUpdate()
    def isEmpty(self):
        bool_ = True
        if len(self.top) == 0:
            bool_ = True
            return bool_
        else :
            bool_ = False
            return bool_
    def size(self):
        return print(str(len(self.top))),self.InputUpdate()
    def clear(self):
        self.top = []
        return self.InputUpdate()
    def push(self,item):
        self.top.append(item)
        # return self.InputUpdate()    
    def pop(self):
        if self.isEmpty is not True:
            elem = self.top.pop()
            print("pop:",elem)
            return elem
        else :
            print("err")
            return 0    
    def peek(self) :
        return print(self.top[int(len(self.top)-1)]),self.InputUpdate()
    def __str__(self):
        return str(self.top),self.InputUpdate()
    def print(self):
        templst = []
        j=0
        for i in range(len(self.top)-1,-1,-1):
            templst.append(self.top[i])
        return print(templst), self.InputUpdate()
    def quit(self):
        return 0

    def InputUpdate(self):
        yourInput = input()
        return self.InputSplit(yourInput)

    def InputSplit(self,yourinput):          #초기화 : ArrayList클래스 사용
        inputdata = []
        inputdata = yourinput.split(" ")
        return self.StrFilter(inputdata)
    
    def StrFilter(self,inputdata):    #pop, push, peek, size, empty, p(rint), m(atch), q(uit)
        if inputdata:

            return 0
        else:
            print("형식에 맞지 않게 입력되었습니다. 다시 입력하세요")
            return self.InputUpdate(self)
        return 0

class Maze:
    def __init__(self):
        self.mazemap = []
        self.mapsizeX = 0
        self.mapsizeY = 0
        print("mazemap",self.mazemap)

class Location:
    def __init__(self):
        self.lst = []

def getLocation(x,y):
    pos = Location()
    pos.lst.append(x)
    pos.lst.append(y)
    print("pos.lst:",pos.lst)
    return pos.lst

def isValid(maze,x,y):
    print("mazemap\n",maze.mazemap)
    print("x:",x," y:",y)
    if x < 0 or y < 0 or x >= maze.mapsizeX or y >= maze.mapsizeY : 
        return 0, print("X, 실패")
    else :        
        if maze.mazemap[y][x] == '0':
            return 1
        elif maze.mazemap[y][x] == 'E':
            print("O, 성공")
            return 1
        

def DFS(maze,startpos):
    x = int() 
    y = int()
    here = Location()
    stack = Stack()
    stack.push(getLocation(startpos[0],startpos[1]))        #시작위치 pos 리턴->값 두개인 리스트
    print("({0}, {1}) 에서 출발 ==> ".format(startpos[0],startpos[1]))

    while stack.isEmpty() == 0:
        here.lst = []
        print("here.lst1:",here.lst)
        here.lst.append(stack.pop())
        print("here.lst2:",here.lst)
        here.lst = here.lst[0]
        print("here.lst3:",here.lst)
        print("here.lst[0]:",here.lst[0])
        print("here.lst[1]:",here.lst[1])
        x = int(here.lst[0])
        y = int(here.lst[1])
        print("x:", x," y:", y)
        print("maze.mazemap[y][x]:",maze.mazemap[y][x])
        if maze.mazemap[y][x] == 'E' : return print("O, 성공")
        else:
            maze.mazemap[y][x] = '2'
            if isValid(maze,x-1,y) == 1 : 
                stack.push(getLocation(x-1,y))
            elif isValid(maze,x+1,y) == 1 : 
                stack.push(getLocation(x+1,y))
            elif isValid(maze,x,y-1) == 1 : 
                stack.push(getLocation(x,y-1))
            elif isValid(maze,x,y+1) == 1 : 
                stack.push(getLocation(x,y+1))
    return print("X, 실패")

def mazefind(maze):
    startposfile = open("mazeinput.txt","r",encoding="utf8")
    lines = startposfile.readlines()
    print("lines:",lines)               #['1 7\n', '7 6\n', '8 5\n', '10 5\n'...]
    print("lines length :",len(lines))  #16
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        # print(lines[i])
    for j in range(len(lines)):
        templst = lines[j].split()
        print()
        print("templst:",templst)
        for k in range(len(templst)) :
            templst[k] = int(templst[k])-1
        DFS(maze,templst)
        # print(lines[j])
    print(lines)
        # DFS(maze,lines[j])
    

def getmaze(file):
    maze = Maze()
    mazeSize = file.readline().split(" ")
    
    for i in range(len(mazeSize)):
        mazeSize[i] = mazeSize[i].strip()

    maze.mapsizeX = int(mazeSize[0])
    maze.mapsizeY = int(mazeSize[1])

    print(maze.mapsizeX,maze.mapsizeY)      #[0-11],[1-19]

    lines = file.readlines()    
    for line in lines:                  #maze = [[1111],[1111],[1111],[1111],[1111]]...
        lst = []
        for char in line:
            if char == '\n'or char == '':
                break
            lst.append(char)
        maze.mazemap.append(lst)
    for i in range(len(maze.mazemap)):
        for j in range(len(maze.mazemap[i])):
            print(maze.mazemap[i][j],end="")
        print()
    mazefind(maze)
    return maze

def main():
    file = open("maze.txt","r",encoding="utf8")
    getmaze(file)
    file.close()


main()