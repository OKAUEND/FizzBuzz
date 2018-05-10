
Count = 1

while Count < 101:
    if Count % 3 == 0 and Count % 5 == 0 :
        print('FizzBuzz')
    
    elif Count % 5 == 0 :
        print('Buzz')
    
    elif Count % 3 == 0:
        print('Fizz')

    else:
        print(str(Count))

    Count += 1
