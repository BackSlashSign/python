def fac(num):
    if num > 1:
        return num * fac(num-1)
    elif num == 1:
        return num

def main():
    # print("!num: ",fac(num))
    for i in range(20):
        print(i)
main()