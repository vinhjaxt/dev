def collatz(number):
    if (number % 2 ) == 0:
        return number // 2
    else:
        return number * 3 + 1
if __name__ == "__main__":
    print('Nhap so bat ky lon hon 1 vao:')
    try:
        number = int(input())
        while True:
            if (number != 1):
                number = collatz(number)
                print(number)
            else:
                break
    except:
        print('Ban phai nhap so lon hon 1')
    