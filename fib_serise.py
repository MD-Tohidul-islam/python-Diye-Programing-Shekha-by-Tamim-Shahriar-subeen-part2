def find_fib(n):
    if n<=2:
        return 1
    fib_x,fib_next = 1,1
    i = 3
    while i<=n:
        i+=1
        fib_x, fib_next = fib_next,(fib_x+fib_next)
    return fib_next
for x in range(1,11):
    print(find_fib(x))
print()
def list_fib(n):
    v = [0,1]
    if n<= 2:
        return v[:n]
    a = 0
    b = 1
    for i in range(n-2):
        c = a+b
        a, b = b,c
        v.append(c)
    return v
print(list_fib(10))
def l_fib(n):
    fib = []
    n1,n2 = 0,1
    count = 0
    if n<=0:
        print('please enter postive number ')
    elif n ==1:
        fib.append(n1)
    else:

        while count<n:
            nth = n1+n2
            fib.append(n1)
            n1 = n2
            n2 = nth
            #fib.append(n1)
            count+=1
    return fib
print(l_fib(10))