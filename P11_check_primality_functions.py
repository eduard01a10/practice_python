def primality(num):
    
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False
    

if __name__ == "__main__":
    print("In this program we are going to check if your number is a prime number")
    num = int(input("Enter a number: "))

    
    result = primality(num)

    if result == True:
        print("Your number is prime")
    elif result == False:
        print("Your number is not prime")