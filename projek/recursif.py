def fibonaciByForLoop(n_range: int)->int:
    pref2 = 0
    pref1 = 1
    for fib in range(n_range):
        num_fibo = pref1 + pref2
        print("value to-> " + str(num_fibo))
        pref2 = pref1
        pref1 = num_fibo