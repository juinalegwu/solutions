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
