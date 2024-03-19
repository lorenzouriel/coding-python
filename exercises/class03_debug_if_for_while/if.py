# If is a fundamental conditional structure in Python that evaluates whether a condition is True and, if so, executes a block of code. 
# If the initial condition is not true, you can use elif (else if) to check additional conditions, and else to execute a block of code when none of the previous conditions are true.

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')