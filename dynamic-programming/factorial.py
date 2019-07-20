from timeit import default_timer as timer

def fac_mem(n):
    table = [0] * (n+1)
    table[0] = 1
    return fac_recurrence(n, table)

def fac_recurrence(n, table):
    if table[n] != 0:
        return table[n]
    return n * fac_recurrence(n-1, table)

def fac_tab(n):
    myTable = [0] * (n+1)
    myTable[0] = 1

    for i in range(1, n + 1):
        myTable[i] = i * myTable[i-1]

    return myTable[n]

print "Factorial of 10 is", fac_mem(10)
print "Factorial of 10 is", fac_tab(10), "\n"

start = timer()
for i in range(1000):
    fac_mem(10)
end = timer()
print "Memoization took", (end - start) / 1000, "seconds on average."

start = timer()
for i in range(1000):
    fac_tab(10)
end = timer()
print "Tabulation took", (end - start) / 1000, "seconds on average."
