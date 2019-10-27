numbers =[0,1]

def fib(numbers):
    new = 0
    for i in range(50):
        new = numbers[-1] + numbers[-2]
        print(new)
        numbers.append(new)
print(0)
fib(numbers)