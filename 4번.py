class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def __gt__(self, rhs): # < greater than 오른쪽이 읜쪽보다 크다
        return (self.year, self.month, self.day) < (rhs.year, rhs.month, rhs.day)
    def __lt__(self, rhs): # > less than  왼쪽이 오른쪽보다 크다
        return (self.year, self.month, self.day) > (rhs.year, rhs.month, rhs.day)
    def __eq__(self, rhs): # == 오른쪽 왼쪽이 같다
        return (self.year, self.month, self.day) == (rhs.year, rhs.month, rhs.day)
        
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
        
    def increment(self,other): 

        count = 0
        if self.__gt__(other) == True:

            while self.__eq__(other) != True:

                if self.day == self.lastDayOfTheMonth(): 
                    self.day = 1                #마지막 날이면 1일로 초기화
                    if self.month == 12:        #12월이면 1월로 초기화하고 1년추가
                        self.month = 1 
                        self.year += 1 
                    else:                       #12월이 아닐때 월을 1더함
                        self.month += 1 
                else:                           #마지막날이 아니면 1일만 추가
                    self.day += 1 
                count += 1

        else:
            while self.__eq__(other) != True:
    
                if self.day == self.lastDayOfTheMonth(): 
                    self.day = 1                #마지막 날이면 1일로 초기화
                    if self.month == 12:        #12월이면 1월로 초기화하고 1년추가
                        self.month = 1 
                        self.year += 1 
                    else:                       #12월이 아닐때 월을 1더함
                        self.month += 1 
                else:                           #마지막날이 아니면 1일만 추가
                    self.day += 1 
                count += 1
            return -count

        return count

def main():
    inFile = open("E:\MyCodes\input3.txt","r")
    # strng1 = "2020/10/10"
    # print("%10s"%strng1)
    lst = []
    while True:
        line = inFile.readline()
        if line == "":
            break
        date1 = [int(i) for i in line.split()] #split() 인자가 없을시 스페이스 기준으로 나눈다
        lst.append(Date(date1[0],date1[1],date1[2]))    # 0 2 4 짝수index
        lst.append(Date(date1[3],date1[4],date1[5]))    # 1 3 5 홀수index
        
        print("{0}/{1}/{2}".format(date1[0],date1[1],date1[2]).ljust(15),end="")
        print("{0}/{1}/{2}".format(date1[3],date1[4],date1[5]).ljust(15),end="")
        if (Date(date1[0],date1[1],date1[2])).__lt__(Date(date1[3],date1[4],date1[5])):
            print("==>      -{0} 일 경과".format((Date(date1[3],date1[4],date1[5])).increment(Date(date1[0],date1[1],date1[2]))))
        else :
            print("==>      {0} 일 경과".format((Date(date1[0],date1[1],date1[2])).increment(Date(date1[3],date1[4],date1[5]))))
        # print(format(Date(date1[0],date1[1],date1[2],date1[3]).increment()))
    inFile.close()

main()