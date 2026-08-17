s1 = {10, 16, 27, 35}
s2 = {7, 27, 35, 48, 62}
a = s1 | s2
print("UNION: ", a)
b = s1 & s2
print("INTERSECTION: ", b)
c = s1 ^ s2
print("SYMMETRIC DIFFERENCE: ", c)
d = s1 - s2
print("DIFFERENCE: ", d)
e = s2.issubset(s1)
f = s1.issuperset(s2)
print("SUBSET: ", e)
print("SUPERSET: ", f)
m = list(s1)
n = list(s2)
print(m)
print(n)

nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print("Removing Duplicates: ", unique_nums)
num1 = [10, 20, 30, 40]
num2 = [30, 40, 50, 60]
common_elements = set(num1) & set(num2)
print("Common Elements: ", common_elements)