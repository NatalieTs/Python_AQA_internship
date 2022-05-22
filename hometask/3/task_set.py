# Write a Python program to check if two given sets have no elements in common.

x = {1, 2, 3, 4}
y = {4, 5, 6, 7}
z = {8}

print("Original set elements:")
print(x)
print(y)
print(z)

print("\nConfirm two given sets have no element(s) in common:")
if x.isdisjoint(z):
    print(x, ' and ', z)
if y.isdisjoint(z):
    print(y, ' and ', z)
if x.isdisjoint(y):
    print(x, ' and ', y)


# Write a Python program to remove the intersection of a 2nd set from the 1st set.

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print('Removed intersection of 2nd set from the 1st set: ', sn1 - sn2)
print("Original sets:")
print(sn1)
print(sn2)


