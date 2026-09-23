student = {
    "name": "Alice",
    "age": 20,
    "courses": ["math", "Physics"]
}
print(student["name"])
print(student["age"])


student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}


student["gpa"] = 3.9

student["age"] = 21

print(student)


score = 85
if score >= 90:
    print("Excellent")
if score <= 70:
    print("Good")
else:
    print("Needs Improvement")


total = 0
for number in range(1, 51):
    total = total + number
print(total)


number = 1 
while number <= 15:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1

names = ["favy", "dorina" "preshy", "jaycee"]
lengths = [len(name) for name in names]
print(lengths)


def multiply(a, b):
    return a * b
result = multiply(4, 5)
print(result)


name = "Alice"
greeting = f"Hello, {name}!"
calc = f"2 + 2 = {2 + 2}"
print(greeting)
