class Set:
    def __init__(self):
        self.items = []

    def __eq__(self, setB):
        if self.items == setB: 
            # print("A equal B: True")
            return True
        else: 
            # print("A equal B: False")
            return False

    def size(self):
        return self.items

    def print(self):
        return self.items

    def contains(self, item):
        for i in range(len(self.items)):        #self.items의 모든 항목에 대해
            if self.items[i] == item:           #item이 self.items[i]와 같으면
                return True                     #집합 내에 있으므로 return True
        return False                            #없음. return False
                                #self.items > item : item은 self.items의 부분 집합
    def insert(self, elem):
        if elem not in self.items :
            self.items.append(elem)
    
    def delete(self, elem):
        if elem in self.items :
            self.items.remove(elem)
            
    def union(self, setB):                  #C = self U B
        setC = Set()                        #결과 집합
        setC.items = list(self.items)       #self의 리스트를 setC에 복사
        for elem in setB.items :            #외부루프: setB의 모든 항목에 대해
            if elem not in self.items :     #내부루프: self에 없으면
                setC.items.append(elem)     #중복이 아니므로 추가함
        return setC.items                         #C = A + B

    def intersect(self, setB):              #C = self ^ B
        setC = Set()
        for elem in setB.items:             #외부루프 : setB의 모든 항목에 대해
            if elem in self.items:          #내부루프 : self에 있으면
                setC.items.append(elem)     #양쪽에 모두 있음 -> 추가함
        return setC.items                     #C = A ^ B 교집합

    def difference(self, setB):             #C = self - B
        setC = Set()
        for elem in self.items:             #외부루프 : self의 모든 항목에 대해
            if elem not in setB.items:      #내부루프 : setB에 없으면
                setC.items.append(elem)     #추가함
        return setC.items                     #C = A - B
    
    def isSubset(self, setB):
        for i in self.items:
            setB.contains(i)
            if setB.contains(i) == True and self.items.__len__() <= setB.items.__len__():
                return True
            else :
                return False   

    def isProperSubset(self, setB):
        if self.isSubset == True and self.__eq__(setB) == False:
            return True
        else : return False

def test(setA, setB):
    print("SetA: ", setA.items)
    print("SetB: ", setB.items)
    if setA == setB:
        print("A equal B: True")
    else:
        print("A equal B: False")
    print("A subset B: ", setA.isSubset(setB))
    print("A proper subset B: ", setA.isProperSubset(setB))
    print("A union B: ",setA.union(setB))
    print("A inTersect B: ", setA.intersect(setB))
    print("A defference B: ", setA.difference(setB))
    print()
def main():
    setA = Set()
    setA.insert(2)
    setA.insert(3)
    setA.insert(4)

    setB = Set()
    setB.insert(2)
    setB.insert(3)
    setB.insert(4)

    setC = Set()
    setC.insert(2)
    setC.insert(3)
    setC.insert(4)
    setC.delete(4)

    test(setA, setB)
    test(setA, setC)
    test(setC, setA)

main()