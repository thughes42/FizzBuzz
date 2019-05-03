# FizzBuzz v3
# Siz FizzBuzzington ...the 3rd #
#                 _   
#         ##    _| |_     ##
#        ####- (╭ರ_•́) - ####

def FizzBuzz(number):
    for num in range(1,number):
        if num % 15 is 0:
            print('FizzBuzz')
        elif num % 3 is 0:
            print('Fizz')
        elif num % 5 is 0:
            print('Buzz')
        else:
            print(num)
