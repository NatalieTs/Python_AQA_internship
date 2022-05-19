# Write a Python program calculate the product, multiplying all the numbers of a given tuple.
# Original Tuple:

nums = (4, 3, 2, 2, -1, 18)

result = 1
for i in nums:
    result *= i

#Product - multiplying all the numbers of the said tuple: -864
assert result == -864

# Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:
nums = (('333', '33'), ('1416', '55'))

result = []
for i in nums:
    t = []
    for y in i:
        t.append(int(y))
    result.append(tuple(t))

assert result == ((333, 33), (1416, 55))

# Write a Python program to convert a given tuple of positive integers into an integer.
# Original tuple:
original = (1, 2, 3)
res = ''
for i in original:
    res += str(i)
result = int(res)
assert result == 123

original = (10, 20, 40, 5, 70)

result = int(''.join(str(i) for i in original))

assert result == 102040570