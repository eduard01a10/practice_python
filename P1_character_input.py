import datetime as dt

def run():
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    now = dt.datetime.now()
    one_hundred = (now.year - age) + 100
    print(f"Hi {name} you are {age} years old and in the year {one_hundred} you will be 100 years old")

if __name__ == "__main__":
    run()
