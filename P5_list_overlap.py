def run():

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11, 7]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []

    for i in b:
        if a in b:
            c.append(i)
        print(i)


if __name__ == "__main__":
    run()