
def piramad():
    while 1:   
        print("피라미드의 높이를 입력하세요: ")
        height = int(input())
        if height < 1 :
            print("범위이탈 함수종료.")
            break
        for i in range(height):
            print(" " * (3*(height - i)-1), end="")
            for j in range(i+1):
                print(str(2 * j + 1).ljust(2), end=" ")
            for j in range(i, 0, -1):
                print(str(2 * j - 1).ljust(2), end=" ")
            print("\n")
piramad()