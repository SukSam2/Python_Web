inLine = input("Enter integer: ")
if inLine.isdigit() :
    num = int(inLine)
    nSquare = num * num
    print("{}의 제곱은 {}입니다.".format(num, nSquare))
else:
    print("정수를 입력하세요!")

