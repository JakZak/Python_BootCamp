def countdown (n):
    if n == 0:
        print ('odpalenie')
    n = n -1
    countdown(n)

countdown(3)