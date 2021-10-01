def googoodan():
    while True:
        print("구구단의 단을 입력하세요 : ",end=" ")
        dan = int(input())
        if(dan <= 1) :
            print("정해진 범위를 넘은 숫자를 입력받았습니다. 구구단 종료.")
            break
        elif(dan >= 2 & dan <= 9):
            for i in range(1,10):
                for j in range(2,dan+1):
                    print(j,"*",i,"=",str(i*j).rjust(2),end="\t")
                print()
    return 0
googoodan();


# for i in range(1,10):
#     for j in range(2,5):
#         print(j,"*",i,"=",str(i*j).rjust(2),end="\t")
#     print()    

        
