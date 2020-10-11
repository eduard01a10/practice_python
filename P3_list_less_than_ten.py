def run():
    user_number = int(input("Write a number: "))
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    new = []
    for i in a:
        if i < user_number:
            new.append(i)
    print(new)

if __name__ == "__main__":
    run()