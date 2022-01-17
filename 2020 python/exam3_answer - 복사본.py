## 3장부터 모든 문제는 함수로 작성되어야 합니다.

def problem3_25(students):
    for st in students:
        if 'A' <= st[0] <= 'M':
            print(st)
    return 

def problem3_27(n):
    # 프로그램을 작성한다.
    return

def problem3_32(n):
    # 프로그램을 작성한다.
    return




if __name__ == '__main__':
    problem3_25(['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin'])

    # 키보드에서 입력하는 대신에 인자로 보낸다. 
    problem3_27(5)

    # 키보드에서 입력하는 대신에 인자로 보낸다. 
    problem3_29(49)

    # 키보드에서 입력하는 대신에 인자로 보낸다. 
    problem3_32(1234)

    #이하도 위와 같은 방법으로 함수로 작성해야 한다. 
    # problem3_34
    print('문제 3.34 = ', pay(10, 35)) # 값이 반환되어야 한다.
    print('문제 3.34 = ', pay(10, 55))

    # problem3_38
    print('문제 3.38 = ', abbreviation('Tuesday')) # 값이 반환되어야 한다.

    # problem3_43
    print('문제 3.43 = ', hit(0, 0, 3, 3, 0)) # 값이 반환되어야 한다.
    print('문제 3.43 = ', hit(0, 0, 3, 4, 0))

    

    




