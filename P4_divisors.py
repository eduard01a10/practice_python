def run():
    user_number = int(input("Please enter a number from 1 to 100: "))
    new_list = []
    x = range(1, 101)
    for i in x:
        if user_number % i == 0:
            new_list.append(i)
    print(f"This list represents all the numbers divisible by your number {new_list}")


if __name__ == "__main__":
    run()