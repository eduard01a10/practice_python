import random

def overlap(a, b):
    c = [i for i in a if i in b]
    return c
    
if __name__ == "__main__":
    a = random.sample(range(100), 5)
    b = random.sample(range(100), 8)
    
    print(overlap(a, b))