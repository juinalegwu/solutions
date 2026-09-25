for number in range(1, 21):
    print(number)

cubes = [number ** 3 for number in range(1, 11)]
print(cubes)

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(numbers[:3])
print(numbers[-3:])

original = ["cake", "doughnut", "meatpie"]
copy = original[:]
copy.append("samosa")
print("Original:", original)
print("copy:", copy)
