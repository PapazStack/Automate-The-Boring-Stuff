def collatz(number):

    print(number, end=' ')

    if number % 2 == 0:
        number = number // 2
        # print(number, end=' ')
        return(number)
    
    elif number % 2 == 1:
        number = 3 * number + 1
        # print(number, end=' ')
        return(number)
        
        

print('Please give me a number')

while True:
    try:
        number = collatz(int(input('>')))

        while True:
            if number != 1:
                number = collatz(number)
            elif number == 1:
                print(number)
                break
    except ValueError: 
        print('Must give an integer')
    else:
        break