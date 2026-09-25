class Dog:
    """A simple class representing a dog."""
    
    def __init__(self, name, breed):
        """Constructor: Initializes name and breed attributes."""
        self.name = name
        self.breed = breed
        
    def bark(self):
        """A simple method."""
        return f"{self.name} says Woof!"

my_dog = Dog("Rex", "German Shepherd")
print(my_dog.name)   
print(my_dog.bark()) 



def findMissingElements(nums):
    # min_num = min(nums)
    # max_num = max(nums)
    original_nums =[]
    i = min(nums)
    while i <= max(nums):
        original_nums.append(i)
        i += 1
    compared_nums = set(original_nums) ^ set(nums)
    return list(compared_nums)
nums = [1,4,2,5,9,3]
print(findMissingElements(nums))




point = (3, 4)
single = (42,) 
x, y = point        

# Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)



if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")




class Dog:
    
    species = "Canis lupus"

    def __init__(self, name: str, age: int):
        self.name = name        
        self.age = age

    def bark(self) -> str:
        return f"{self.name} says Woof!"

    def __str__(self) -> str:
        return f"Dog({self.name}, {self.age})"

    def __repr__(self) -> str:
        return f"Dog(name='{self.name}', age={self.age})"

class Puppy(Dog):
    def __init__(self, name: str):
        super().__init__(name, age=0)

    def bark(self) -> str:
        return f"{self.name} says Yip!"

dog = Dog("Rex", 5)
print(dog.bark())



import functools

def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        print("Before")

        result = func(*args, **kwargs)

        print("After")

        return result

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()