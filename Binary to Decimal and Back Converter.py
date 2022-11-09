def main():
    choice = input('Enter 1 to convert decimal to binary or 2 to convert binary to decimal: ')
    if choice == '1': #convert decimal to binary
        decimal = int(input('Enter a decimal number: '))
        binary = ''
        while decimal >= 1:
            binary += str(decimal % 2)
            decimal = decimal // 2
        print(binary[::-1])
    elif choice == '2': #convert binary to decimal
        binary = input('Enter a binary number: ')
        decimal = 0

        n = list(range(len(binary)))[::-1]

        for i in range(len(binary)):
            decimal += int(binary[i]) * 2 ** int(n[i])
        print(decimal)
    else:
        print('Invalid input')
        main()
    
if __name__ == '__main__':
    main()