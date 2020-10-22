def run():
    print("""This program will tell you if the string you enter is either a palindrome or not""")
    word = input("Please enter a string: ").replace(" ", "")
    reverse = word[::-1]

    if word == reverse:
        print("is palindrome")
    else:
        print("is not a palindrome")

if __name__ == "__main__":
    run()