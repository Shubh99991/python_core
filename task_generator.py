# basic
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)
print()

#list genrator
def square_numbers(nums):
    for n in nums:
        yield n * n

for i in square_numbers([1, 2, 3, 4]):
    print(i)
print()

#fibbonaci genrator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(6):
    print(num)
