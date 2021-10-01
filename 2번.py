class Date:
    def __init__(self,year,month, day):
        self.year = year
        self.month = month
        self.day = day
    def __gt__(self, rhs): # > greater than 왼쪽이 오른쪽보다 크다
        return (self.year, self.month, self.day) > (rhs.year, rhs.month, rhs.day)
    def __lt__(self, rhs): # < less than 오른쪽이 왼쪽보다 크다
        return (self.year, self.month, self.day) < (rhs.year, rhs.month, rhs.day)
    def __str__(self):
        return "{0}/{1}/{2}".format(self.year,self.month,self.day)


def findMinMax(lst):
    min = [0,0,0]
    max = [0,0,0]
    maxTmp = Date(0,0,0)
    minTmp = Date(3000,12,31)
    for i in range(len(lst)):
        if lst[i].__gt__(maxTmp) == True:
            maxTmp = lst[i]
        if lst[i].__lt__(minTmp) == True:
            minTmp = lst[i]
    min = minTmp
    max = maxTmp
    return min,max

def main():
    inFile = open("E:\MyCodes\input.txt","r")
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()] #split() 공백시 스페이스 기준으로 나눈다
        lst.append(Date(date[0],date[1],date[2]))
    for i in range(len(lst)):
        print(lst[i])
    min, max = findMinMax(lst)
    print()
    print("earlist date:",min)
    print("latest data: ",max)
    inFile.close()
    
main()