# 📘 Week 3 — Classes, Objects & OOP

> **Topics covered:** OOP Principles · Classes & Objects · Attributes · Properties · Magic Methods · Class/Static Methods


## 1. What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organises code around **objects** — bundles of data (attributes) and behaviour (methods) — rather than just functions and logic.

### The 4 Pillars of OOP

| Pillar | Meaning |
|--------|---------|
| **Encapsulation** | Bundling data and methods together; hiding internal details |
| **Abstraction** | Exposing only what's necessary; hiding complexity |
| **Inheritance** | A class can inherit attributes/methods from another class |
| **Polymorphism** | Different classes can share the same interface |

```python
# Procedural approach — just functions and data
name = "Alice"
age = 25
def greet(name):
    return f"Hello, {name}!"

# OOP approach — data and behaviour bundled together
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, I'm {self.name}!"
```

---

## 2. First-Class Everything

In Python, **everything is an object** — including functions, classes, and even types themselves.

```python
# Functions are objects
def add(a, b):
    return a + b

print(type(add))         # <class 'function'>
print(add.__name__)      # "add"

# You can pass functions as arguments
def apply(func, a, b):
    return func(a, b)

print(apply(add, 3, 5))  # 8

# Classes are objects too
class Dog:
    pass

print(type(Dog))         # <class 'type'>
print(type(Dog()))       # <class '__main__.Dog'>

# Even integers are objects
x = 42
print(type(x))           # <class 'int'>
print(x.bit_length())    # 6  ← calling a method on an int!
```

>  "First-class" means: can be assigned to variables, passed as arguments, returned from functions, stored in data structures.

---

## 3. Classes and Objects

A **class** is a blueprint. An **object** (or **instance**) is a concrete thing created from that blueprint.

```python

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def describe(self):
        return f"{self.year} {self.brand} {self.model}"


car1 = Car("Toyota", "Camry", 2022)
car2 = Car("BMW", "X5", 2023)


print(car1.describe())   # 2022 Toyota Camry
print(car2.describe())   # 2023 BMW X5


print(type(car1))                   # <class '__main__.Car'>
print(isinstance(car1, Car))        # True
print(car1 is car2)                 # False — different objects!
```

### Class vs Object vs Instance

| Term | Meaning |
|------|---------|
| **Class** | The template/blueprint (`Car`) |
| **Object** | Any instance of a class (`car1`, `car2`) |
| **Instance** | Same as object — a specific realisation of a class |

> "Object" and "instance" are interchangeable. Every object IS an instance; every instance IS an object.

---

## 4. Attributes — Public, Protected, Private

Python uses **naming conventions** (not true access modifiers like Java) to signal how attributes should be used.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # PUBLIC — anyone can access
        self._balance = balance     # PROTECTED — "please don't touch directly"
        self.__pin = "1234"         # PRIVATE — name-mangled by Python

account = BankAccount("Alice", 1000)

# Public — freely accessible
print(account.owner)        # "Alice" 

# Protected — accessible but discouraged outside class/subclass
print(account._balance)     # 1000  (works, but bad practice)

# Private — name-mangled, not directly accessible
# print(account.__pin)      #  AttributeError
print(account._BankAccount__pin)  # "1234"  (mangled name — exists, just hidden)
```

### Summary

| Convention | Syntax | Meaning |
|------------|--------|---------|
| Public | `self.name` | Anyone can read/write |
| Protected | `self._name` | Internal use (class + subclasses) |
| Private | `self.__name` | Internal only — name-mangled to `_ClassName__name` |

>  Python doesn't enforce access control — it's all convention and trust. The underscore is a signal to other developers: "I'm not part of the public API."

---

## 5. self

`self` is a reference to the **current instance** of the class. It's the first parameter of every instance method.

```python
class Dog:
    def __init__(self, name):
        self.name = name     # store name ON THIS SPECIFIC instance

    def bark(self):
        print(f"{self.name} says: Woof!")   # access this instance's name

rex = Dog("Rex")
buddy = Dog("Buddy")

rex.bark()    # Rex says: Woof!
buddy.bark()  # Buddy says: Woof!

# Python translates this:
rex.bark()
# into this behind the scenes:
Dog.bark(rex)   # self = rex
```

>  `self` is just a convention — you could name it anything, but **never do that**. Always use `self`.

---

## 6. Methods

A **method** is a function defined inside a class. There are three types:

```python
class MyClass:

    class_var = 0   # class attribute

    def instance_method(self):
        """Has access to the instance (self) and class."""
        return f"Instance method, self = {self}"

    @classmethod
    def class_method(cls):
        """Has access to the class (cls), not the instance."""
        return f"Class method, cls = {cls}"

    @staticmethod
    def static_method():
        """No access to instance or class — just a regular function inside a class."""
        return "Static method"
```

---

## 7. \_\_init\_\_ Method

`__init__` is the **constructor** — it runs automatically when a new object is created.

```python
class Person:
    def __init__(self, name, age):
        print(f"Creating Person: {name}") 
        self.name = name
        self.age = age

p = Person("Alice", 25)
# Output: Creating Person: Alice

# __init__ can have default values
class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

c1 = Circle()       # radius = 1.0 (default)
c2 = Circle(5.0)    # radius = 5.0

print(c1.area())   # 3.14...
print(c2.area())   # 78.53...
```

> `__init__` is NOT where the object is created — that's `__new__`. `__init__` just initialises it. You almost never need to override `__new__`.

---


## 8. Properties — Pythonic Getters & Setters

In Python, **properties** are the Pythonic way to add controlled access to attributes — without changing the public API.

### Without property (bad — Java style)

```python
class Person:
    def __init__(self, age):
        self._age = age

    def get_age(self):     # getter
        return self._age

    def set_age(self, age):   # setter
        self._age = age

p = Person(25)
p.set_age(26)         
print(p.get_age())
```

### With @property (Pythonic )

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        """Getter — called when you read person.age"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter — called when you write person.age = value"""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if value < 0 or value > 150:
            raise ValueError(f"Invalid age: {value}")
        self._age = value

    @age.deleter
    def age(self):
        """Deleter — called when you write del person.age"""
        del self._age

p = Person(25)
print(p.age)      # calls getter → 25
p.age = 26        # calls setter 
del p.age         # calls deleter
```

### Attribute vs Property

| | Attribute | Property |
|--|-----------|----------|
| Definition | `self.name = value` | `@property` decorator |
| Access | Direct | Via getter method |
| Validation | None | Can add validation in setter |
| Read-only | No | Yes — define getter, no setter |

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius   

    @property
    def area(self):             
        import math
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

c = Circle(5)
print(c.area)       # 78.53... — computed on the fly
print(c.diameter)   # 10
c.diameter = 20     # sets radius to 10
print(c.radius)     # 10
```

---

## 9. \_\_str\_\_ and \_\_repr\_\_

These **dunder (magic) methods** control how objects are represented as strings.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Official representation — for developers.
        Goal: unambiguous. Ideally: eval(repr(obj)) == obj"""
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self):
        """Human-readable representation — for end users.
        Goal: readable and pretty."""
        return f"({self.x}, {self.y})"


p = Point(3, 4)

print(str(p))    # (3, 4)       ← __str__
print(repr(p))   # Point(3, 4)  ← __repr__
print(p)         # (3, 4)       ← print() uses __str__

# In a list, repr() is used
points = [Point(1, 2), Point(3, 4)]
print(points)   # [Point(1, 2), Point(3, 4)]
```

### \_\_str\_\_ vs \_\_repr\_\_

| | `__str__` | `__repr__` |
|--|-----------|------------|
| Purpose | Human-readable | Developer/debugging |
| Called by | `str()`, `print()` | `repr()`, interactive console, inside containers |
| Goal | Readable | Unambiguous |
| Fallback | Falls back to `__repr__` if not defined | No fallback |

---

## 10. Class Attributes vs Instance Attributes

```python
class Dog:
    # CLASS ATTRIBUTE — shared by ALL instances
    species = "Canis familiaris"
    count = 0

    def __init__(self, name, breed):
        # INSTANCE ATTRIBUTES — unique to each instance
        self.name = name
        self.breed = breed
        Dog.count += 1   # update class attribute via class name

    def __repr__(self):
        return f"Dog({self.name!r}, {self.breed!r})"


d1 = Dog("Rex", "German Shepherd")
d2 = Dog("Buddy", "Labrador")

# Class attribute — same for all
print(Dog.species)    # "Canis familiaris"
print(d1.species)     # "Canis familiaris" — accessed with instance
print(d2.species)     # "Canis familiaris"

# Instance attributes — unique
print(d1.name)   # "Rex"
print(d2.name)   # "Buddy"

# Class attribute shared
print(Dog.count)   # 2


d1.species = "Modified"   # creates instance attribute, doesn't change class attr
print(d1.species)         # "Modified"   ← instance attribute
print(Dog.species)        # "Canis familiaris" ← class attribute unchanged
print(d2.species)         # "Canis familiaris" ← unaffected
```

---

## 11. Class Methods and Static Methods

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date({self.year}, {self.month}, {self.day})"

    # INSTANCE METHOD — has access to self
    def is_leap_year(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    # CLASS METHOD — has access to cls, not self
    # Common use: alternative constructors
    @classmethod
    def from_string(cls, date_string):
        """Create a Date from a 'YYYY-MM-DD' string."""
        year, month, day = map(int, date_string.split("-"))
        return cls(year, month, day)   # cls() creates a new instance

    @classmethod
    def today(cls):
        """Create a Date for today."""
        import datetime
        d = datetime.date.today()
        return cls(d.year, d.month, d.day)

    # STATIC METHOD — no access to instance or class
    @staticmethod
    def is_valid_month(month):
        """Check if month is valid — doesn't need class or instance."""
        return 1 <= month <= 12

    @staticmethod
    def days_in_month(month, year):
        import calendar
        return calendar.monthrange(year, month)[1]


# Usage
d1 = Date(2024, 3, 15)
d2 = Date.from_string("2024-06-21")    # classmethod as alternative constructor
d3 = Date.today()                       # classmethod

print(d1.is_leap_year())               # True
print(Date.is_valid_month(13))         # False — staticmethod
print(Date.days_in_month(2, 2024))     # 29 — leap year Feb
```

### When to use which?

| Method type | Decorator | First param | Use when... |
|-------------|-----------|-------------|-------------|
| Instance method | (none) | `self` | Needs instance data |
| Class method | `@classmethod` | `cls` | Alternative constructors, factory methods |
| Static method | `@staticmethod` | (none) | Utility functions related to class, but no instance/class needed |

---

## 12. Dynamic Attributes

Python lets you add attributes to an instance **after** it's been created.

```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.__dict__)   # {"name": "Alice"}

# Add attribute dynamically
p.age = 25
p.city = "Baku"
print(p.__dict__)   # {"name": "Alice", "age": 25, "city": "Baku"}

# Add to the class itself — affects all instances
Person.species = "Homo sapiens"
print(p.species)   # "Homo sapiens"

# Using setattr / getattr
setattr(p, "email", "alice@example.com")
print(getattr(p, "email"))           # "alice@example.com"
print(getattr(p, "phone", "N/A"))   # "N/A" — default if not found

# hasattr / delattr
print(hasattr(p, "age"))   # True
delattr(p, "age")
print(hasattr(p, "age"))   # False
```

---

## 13. \_\_dict\_\_, getattr, and Attribute Lookup

### \_\_dict\_\_

```python
class Car:
    wheels = 4   # class attribute

    def __init__(self, brand):
        self.brand = brand   # instance attribute

c = Car("Toyota")

# Instance __dict__ — only instance attributes
print(c.__dict__)      # {"brand": "Toyota"}

# Class __dict__ — class attributes, methods, etc.
print(Car.__dict__)
# {"wheels": 4, "__init__": <function>, ...}

# wheels is in CLASS __dict__, not instance __dict__
print("wheels" in c.__dict__)     # False
print("wheels" in Car.__dict__)   # True
print(c.wheels)                   # 4
```

### Attribute Lookup Order (MRO)

When you access `obj.attr`, Python looks in this order:

```
1. obj.__dict__           (instance attributes)
2. type(obj).__dict__     (class attributes, methods)
3. Parent classes         (via MRO — Method Resolution Order)
4. AttributeError         (if not found anywhere)
```

```python
class Animal:
    sound = "..."

class Dog(Animal):
    sound = "Woof"

d = Dog()
d.sound = "WOOF!"   # instance attribute

# Lookup: instance → Dog class → Animal class
print(d.sound)        # "WOOF!"  ← instance wins
del d.sound
print(d.sound)        # "Woof"   ← Dog class
```

### getattr, setattr, hasattr, delattr

```python
class Robot:
    def __init__(self, name):
        self.name = name
        self.power = 100

r = Robot("R2D2")

# getattr — get attribute by name string
print(getattr(r, "name"))           # "R2D2"
print(getattr(r, "speed", 0))       # 0 — default if missing, no error

# setattr — set attribute by name string
setattr(r, "speed", 50)
print(r.speed)   # 50

# hasattr — check if attribute exists
print(hasattr(r, "power"))   # True
print(hasattr(r, "fly"))     # False

# delattr — delete attribute
delattr(r, "speed")
print(hasattr(r, "speed"))   # False


attrs = ["name", "power"]
for attr in attrs:
    print(f"{attr}: {getattr(r, attr, 'N/A')}")
```