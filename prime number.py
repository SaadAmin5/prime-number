# prime number

def prime_number(number):

    is_prime = True 

    for i in range(2, number):

        if number % i == 0:
            is_prime = False


    if is_prime==True:
        print('It\'s a prime number.')
    else:
        print('It\'s not a prime number.')
        

num=int(input('Please input a number to determine whether it is a prime number or not: '))
prime_number(number=num)