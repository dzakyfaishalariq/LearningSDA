# learning loop and recursif data in python

# fibonaci by for loop
def fibonaciByForLoop(n_range: int)->int:
    pref2 = 0
    pref1 = 1
    for fib in range(n_range):
        num_fibo = pref1 + pref2
        print("value to-> " + str(num_fibo))
        pref2 = pref1
        pref1 = num_fibo

# fibonaci by recursif
count = 2
def fibonaciByRecursif(pref1: int, pref2: int)->int:
    global count
    if count <= 12:
        num_fibonaci = pref1 + pref2
        print(f"value to -> {num_fibonaci}")
        pref2 = pref1
        pref1 = num_fibonaci
        count += 1
        fibonaciByRecursif(pref1, pref2)
    else:
        return

# menggunkan F(n) = F(n-1) + F(n-2)
def F(n: int)->int:
    if n <= 1:
        return n
    else:
        return F(n-1) + F(n-2)
