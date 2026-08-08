# numbers = set()
#
# numbers.add(10)
# numbers.add(20)
# numbers.add(30)
#
# numbers.add(20)
#
# print(numbers)


s = {1, 2, 33, 4, 5}
s.remove(3)
s.discard(10)
print(s)

my_set = {10, 20, 30, 40}
print(my_set)

numbers = {10, 20, 30}
numbers.add(40)
print(numbers)


numbers = {10,20}
numbers.update((30,40, 50))
print(numbers)


numbers = {10, 20, 30}
numbers.add(20)
print(numbers)


numbers = {10,20,30,40}
numbers.remove(20)
print(numbers)

fruits = {"apple", "banana", "cherry"}

if "banana" in fruits:
    print("Found")
else:
    print("Not found")

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

total = set1.intersection(set2)
print(total)

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}