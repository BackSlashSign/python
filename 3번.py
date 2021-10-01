# 1, 3, 5, 7, 8, 10, 12월이면 31일 
# 4, 6, 9, 11월이면 30일, 2월은 윤년이면 29일 평년이면 28일
class Date:
    def __init__(self,year,month,day,increNum):
        self.year = year
        self.month = month
        self.day = day
        self.increNum = increNum

    

    def __str__(self):
        return "{0}/{1}/{2}/{3}".format(self.year, self.month, self.day, self.increNum)

    def lastDayOfTheMonth(self):
        if self.month == 2:
            if self.year % 4 == 0:  #윤년 2월이 29일
                if self.day == 29:
                    return 29
            elif self.day == 28:
                return 28
        elif self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 \
            or self.month == 10 or self.month == 12:
            return 31
        elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11 :
            return 30
        else:
            return 30
        

    def increment(self): 
        for i in range(self.increNum):
            if self.day == self.lastDayOfTheMonth(): 
                self.day = 1                #마지막 날이면 1일로 초기화
                if self.month == 12:        #12월이면 1월로 초기화하고 1년추가
                    self.month = 1 
                    self.year += 1 
                else:                       #12월이 아닐때 월을 1더함
                    self.month += 1 
            else:                           #마지막날이 아니면 1일만 추가
                self.day += 1 
            
        return "{0}/{1}/{2}".format(self.year,self.month,self.day)

def main():
    inFile = open("E:\MyCodes\input2.txt","r")
    lst = []
    afterIncre = []
    j=0
    while True:
        line = inFile.readline()
        if line == "":
            break
        date = [int(i) for i in line.split()] #split() 공백시 스페이스 기준으로 나눈다
        lst.append(Date(date[0],date[1],date[2],date[3]))
        print("{0}/{1}/{2}".format(date[0],date[1],date[2]).ljust(15),end="")
        print("{0}일 후  ==>".format(date[3]).rjust(15),end="   ")
        print(format(Date(date[0],date[1],date[2],date[3]).increment()))
    print(list(map(str,lst)))
    inFile.close()

main()