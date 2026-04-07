
# ── 1. First-class everything ──────────────────────────────────────────────
def greet(name):
    return f"Hello, {name}!"

# Functions are objects
print(type(greet))           # <class 'function'>
print(greet.__name__)        # "greet"

# Can be passed as argument
def apply(func, value):
    return func(value)

print(apply(greet, "Alice")) # "Hello, Alice!"

# Classes are objects too
class Dog:
    pass

print(type(Dog))    # <class 'type'>
print(type(Dog()))  # <class '__main__.Dog'>

# ── 2. Class and Object ────────────────────────────────────────────────────
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        return f"{self.year} {self.brand} {self.model}"

    def age(self):
        return 2025 - self.year

# Creating instances
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("BMW", "X5", 2023)

print(car1.describe())          # 2020 Toyota Camry
print(car2.describe())          # 2023 BMW X5
print(car1 is car2)             # False — different objects
print(isinstance(car1, Car))    # True

# ── 3. self — what it really is ───────────────────────────────────────────
class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0


c = Counter(10)
c.increment()
c.increment()

# Python translates c.increment() into Counter.increment(c)
Counter.increment(c)   # same thing
print(c.value)         # 13

# ── 4. __init__ with defaults ─────────────────────────────────────────────
class Circle:
    PI = 3.14159265358979

    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    def area(self):
        return Circle.PI * self.radius ** 2

    def perimeter(self):
        return 2 * Circle.PI * self.radius


c1 = Circle()           # defaults: radius=1.0, color="red"
c2 = Circle(5.0)        # radius=5.0, color="red"
c3 = Circle(3.0, "blue")

print(f"c1 area: {c1.area():.2f}")         # 3.14
print(f"c2 perimeter: {c2.perimeter():.2f}") # 31.42
print(f"c3 color: {c3.color}")             # blue