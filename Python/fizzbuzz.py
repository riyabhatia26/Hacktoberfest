# FizzBuzz is a good one to know for interviews! The rules are:
# https://en.wikipedia.org/wiki/Fizz_buzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
