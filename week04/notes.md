# 📘 Week 4 — Inheritance, Abstract Classes & Interfaces

---

## 📌 Table of Contents

1. [What is Inheritance?](#1-what-is-inheritance)
2. [Superclass, Subclass & object](#2-superclass-subclass--object)
3. [How to Inherit a Class](#3-how-to-inherit-a-class)
4. [Overriding Methods & Attributes](#4-overriding-methods--attributes)
5. [super()](#5-super)
6. [Multiple Inheritance & MRO](#6-multiple-inheritance--mro)
7. [isinstance, issubclass, type](#7-isinstance-issubclass-type)
8. [Listing Attributes & Methods](#8-listing-attributes--methods)
9. [Abstract Classes](#9-abstract-classes)
10. [Interfaces & Duck Typing](#10-interfaces--duck-typing)
11. [Subclassing Standard Base Classes](#11-subclassing-standard-base-classes)
12. [Mixins](#12-mixins)

---

## 1. What is Inheritance?

**Inheritance** lets a class (subclass) acquire attributes and methods from another class (superclass) — promoting code reuse and a natural hierarchy.

```
Animal
├── Dog       (inherits from Animal)
├── Cat       (inherits from Animal)
└── Bird      (inherits from Animal)
    └── Parrot  (inherits from Bird)
```

**Why use it?**
- Avoid repeating code (DRY — Don't Repeat Yourself)
- Model real-world "is-a" relationships (`Dog` IS-A `Animal`)
- Extend or specialise existing behaviour without modifying it

---

## 2. Superclass, Subclass & object

| Term | Meaning | Also called |
|------|---------|-------------|
| **Superclass** | The class being inherited from | Base class, Parent class |
| **Subclass** | The class that inherits | Derived class, Child class |
| **`object`** | The default base class every Python class inherits from | Root of all classes |

```python
class Animal:       # superclass / parent class / base class
    pass

class Dog(Animal):  # subclass / child class / derived class
    pass

# Every class inherits from object — even if not stated explicitly
class MyClass:
    pass

print(MyClass.__bases__)     # (<class 'object'>,)
print(issubclass(Dog, object))   # True
print(issubclass(MyClass, object))  # True
```

---

## 3. How to Inherit a Class

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        raise NotImplementedError("Subclasses must implement speak()")

    def describe(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


# Single inheritance
class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call parent __init__
        self.breed = breed            # add Dog-specific attribute

    def speak(self):
        return f"{self.name} says: Woof!"

    def fetch(self):                  # Dog-specific method
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"


dog = Dog("Rex", 3, "Labrador")
cat = Cat("Whiskers", 5)

print(dog.speak())      # Rex says: Woof!
print(dog.describe())   # Rex is 3 years old. — inherited from Animal!
print(dog.fetch())      # Rex fetches the ball!
print(cat.speak())      # Whiskers says: Meow!
```

### What subclasses inherit:
- All **public** attributes and methods (`name`, `describe`)
- All **protected** attributes and methods (`_name`)
- NOT **private** attributes (`__name` — name-mangled)

```python
class Parent:
    pub = "public"
    _prot = "protected"
    __priv = "private"

class Child(Parent):
    def show(self):
        print(self.pub)      
        print(self._prot)    
        # print(self.__priv) #  AttributeError — name-mangled

c = Child()
c.show()
```

### New attributes on instances

An instance can get new attributes at any time:

```python
dog = Dog("Rex", 3, "Lab")
dog.tricks = ["sit", "shake"]   # added after creation — perfectly valid
print(dog.tricks)               # ["sit", "shake"]
```

---

## 4. Overriding Methods & Attributes

A subclass can **override** any inherited method or attribute by redefining it.

```python
class Shape:
    color = "white"   # class attribute

    def area(self):
        return 0

    def describe(self):
        return f"A {self.color} shape with area {self.area():.2f}"


class Circle(Shape):
    color = "red"     # overrides class attribute

    def __init__(self, radius):
        self.radius = radius

    def area(self):           # overrides method
        import math
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):           # overrides method
        return self.w * self.h


c = Circle(5)
r = Rectangle(4, 6)

print(c.describe())   # A red shape with area 78.54
print(r.describe())   # A white shape with area 24.00
```

---

## 5. super()

`super()` gives access to the **parent class** — without hardcoding the parent's name.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calls Animal.__init__
        self.breed = breed

    def speak(self):
        parent_result = super().speak()   # calls Animal.speak()
        return f"{self.name} says Woof! (parent said: {parent_result})"


class GoldenRetriever(Dog):
    def __init__(self, name):
        super().__init__(name, "Golden Retriever")  # calls Dog.__init__

    def speak(self):
        return f"{self.name} says: *happy woof*"


gr = GoldenRetriever("Buddy")
print(gr.name)    # "Buddy"   — from Animal
print(gr.breed)   # "Golden Retriever" — from Dog
print(gr.speak()) # Buddy says: *happy woof*
```

**Why use `super()` instead of `Parent.__init__(self, ...)`?**
- Works correctly with multiple inheritance (follows MRO)
- If you rename the parent class, you only change one place
- The Pythonic way

---

## 6. Multiple Inheritance & MRO

Python allows a class to inherit from **multiple** base classes.

```python
class Flyable:
    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming!"

class Animal:
    def __init__(self, name):
        self.name = name

class Duck(Animal, Flyable, Swimmable):
    def speak(self):
        return "Quack!"


donald = Duck("Donald")
print(donald.fly())    # Donald is flying!
print(donald.swim())   # Donald is swimming!
print(donald.speak())  # Quack!
```

### MRO — Method Resolution Order

When multiple classes define the same method, Python uses **MRO** (C3 linearisation) to decide which one to call.

```python
class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return "B"

class C(A):
    def hello(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.hello())        # "B" — B comes before C in MRO
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
print(D.mro())          # same, as a list
```

**MRO lookup order: D → B → C → A → object**

---

## 7. isinstance, issubclass, type

```python
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

rex = Dog()

# isinstance — checks if object is instance of a class (or its parents)
print(isinstance(rex, Dog))      # True
print(isinstance(rex, Animal))   # True — Dog IS-A Animal
print(isinstance(rex, Cat))      # False

# issubclass — checks class hierarchy
print(issubclass(Dog, Animal))   # True
print(issubclass(Dog, object))   # True — everything inherits from object
print(issubclass(Animal, Dog))   # False — not the other way around

# type — returns the EXACT type (no inheritance)
print(type(rex))           # <class '__main__.Dog'>
print(type(rex) is Dog)    # True
print(type(rex) is Animal) # False — type() is strict!

# isinstance vs type — key difference:
print(isinstance(rex, Animal))   # True  ← checks inheritance chain
print(type(rex) is Animal)       # False ← strict, no inheritance
```

> 💡 Prefer `isinstance()` over `type()` — it respects inheritance and is more Pythonic.

---

## 8. Listing Attributes & Methods

```python
class Animal:
    species = "Unknown"

    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def fetch(self):
        pass

d = Dog("Rex", "Lab")

# dir() — all attributes and methods (including inherited)
print(dir(d))
# ["__class__", "__init__", ..., "breed", "fetch", "name", "speak", "species"]

# vars() — same as __dict__ — only instance attributes
print(vars(d))        # {"name": "Rex", "breed": "Lab"}
print(d.__dict__)     # same

# __dict__ of the class
print(Dog.__dict__.keys())    # ["__init__", "fetch", ...]
print(Animal.__dict__.keys()) # ["species", "__init__", "speak", ...]

# Check specific attribute existence
print(hasattr(d, "fetch"))    # True
print(hasattr(d, "fly"))      # False
print(hasattr(d, "species"))  # True — inherited!
```

---

## 9. Abstract Classes

An **abstract class** defines an interface — it declares methods that **must** be implemented by subclasses. You can't instantiate an abstract class directly.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class — cannot be instantiated directly."""

    @abstractmethod
    def area(self):
        """Every shape MUST implement area()."""
        pass

    @abstractmethod
    def perimeter(self):
        """Every shape MUST implement perimeter()."""
        pass

    def describe(self):
        """Concrete method — shared by all subclasses."""
        return f"Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"


# ❌ Cannot instantiate abstract class
try:
    s = Shape()
except TypeError as e:
    print(e)  # Can't instantiate abstract class Shape with abstract methods area, perimeter

# ✅ Subclasses must implement all abstract methods
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.describe())
# Area: 78.54, Perimeter: 31.42
# Area: 24.00, Perimeter: 20.00
```

### Abstract with concrete methods

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass    # subclasses MUST implement this

    def breathe(self):
        return f"{self.name} breathes air."   # shared — no override needed

    @property
    @abstractmethod
    def legs(self):
        pass    # abstract property!


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

    @property
    def legs(self):
        return 4


d = Dog("Rex")
print(d.speak())    # Rex says Woof!
print(d.breathe())  # Rex breathes air.
print(d.legs)       # 4
```

---

## 10. Interfaces & Duck Typing

Python doesn't have a formal `interface` keyword like Java. Instead, it uses **duck typing**: *"If it walks like a duck and quacks like a duck, it's a duck."*

```python
# Duck typing — no shared base class needed!
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Robot:
    def speak(self):
        return "Beep boop."

def make_noise(thing):
    """Works with ANY object that has a speak() method."""
    print(thing.speak())

make_noise(Dog())    # Woof!
make_noise(Cat())    # Meow!
make_noise(Robot())  # Beep boop.
```

### Protocols (Python 3.8+) — formal duck typing

```python
from typing import Protocol

class Speakable(Protocol):
    def speak(self) -> str:
        ...   # just a signature, no implementation

class Duck:
    def speak(self) -> str:
        return "Quack!"

def make_it_speak(thing: Speakable) -> str:
    return thing.speak()

print(make_it_speak(Duck()))   # "Quack!"
# Duck doesn't inherit from Speakable — just needs the method!
```

### ABC as interface

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Resizable(ABC):
    @abstractmethod
    def resize(self, factor):
        pass

# Class implementing multiple "interfaces"
class Canvas(Drawable, Resizable):
    def __init__(self, size):
        self.size = size

    def draw(self):
        return f"Drawing canvas of size {self.size}"

    def resize(self, factor):
        self.size = int(self.size * factor)
        return self.size
```

---

## 11. Subclassing Standard Base Classes

You can extend Python's built-in types to create custom data structures.

```python
# Custom list that only accepts integers
class IntList(list):
    def append(self, item):
        if not isinstance(item, int):
            raise TypeError(f"Only integers allowed, got {type(item).__name__}")
        super().append(item)

    def extend(self, items):
        for item in items:
            self.append(item)   # reuses our validated append

    def sum(self):
        return sum(self)

    def average(self):
        return sum(self) / len(self) if self else 0


il = IntList([1, 2, 3])
il.append(4)
print(il)           # [1, 2, 3, 4]
print(il.sum())     # 10
print(il.average()) # 2.5

try:
    il.append("hello")   # TypeError
except TypeError as e:
    print(e)


# Custom dict with default value and logging
class LoggedDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._log = []

    def __setitem__(self, key, value):
        self._log.append(f"SET {key!r} = {value!r}")
        super().__setitem__(key, value)

    def __delitem__(self, key):
        self._log.append(f"DEL {key!r}")
        super().__delitem__(key)

    def history(self):
        return self._log.copy()


d = LoggedDict()
d["name"] = "Alice"
d["age"] = 25
del d["age"]
print(d.history())
# ["SET 'name' = 'Alice'", "SET 'age' = 25", "DEL 'age'"]


# Custom iterator
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for n in CountDown(5):
    print(n, end=" ")   # 5 4 3 2 1
```

---

## 12. Mixins

A **Mixin** is a class that provides methods to other classes through multiple inheritance — without being a standalone class itself. Mixins add behaviour without defining a full object.

```python
# Mixins — focused, single-purpose behaviour classes
class SerializeMixin:
    """Adds JSON serialization to any class."""
    import json as _json

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith("_")}

    def to_json(self):
        import json
        return json.dumps(self.to_dict(), indent=2)


class ReprMixin:
    """Adds automatic __repr__ to any class."""
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"


class ValidateMixin:
    """Adds validation support to any class."""
    def validate(self):
        errors = []
        for attr, validator in getattr(self, "_validators", {}).items():
            value = getattr(self, attr, None)
            if not validator(value):
                errors.append(f"Invalid value for {attr!r}: {value!r}")
        return errors


# Use mixins to compose behaviour
class Person(ReprMixin, SerializeMixin, ValidateMixin):
    _validators = {
        "age": lambda v: isinstance(v, int) and 0 <= v <= 150,
        "name": lambda v: isinstance(v, str) and len(v) > 0,
    }

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


class Product(ReprMixin, SerializeMixin):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


p = Person("Alice", 25, "Baku")
print(repr(p))           # Person(name='Alice', age=25, city='Baku')
print(p.to_json())       # {"name": "Alice", "age": 25, "city": "Baku"}
print(p.validate())      # [] — no errors

prod = Product("Laptop", 999.99, 50)
print(repr(prod))        # Product(name='Laptop', price=999.99, stock=50)
print(prod.to_json())    # JSON output
```

### Mixin naming convention

By convention, Mixin class names end in `Mixin` or start with a verb:
- `SerializeMixin`, `LoggableMixin`, `CacheMixin`
- `Flyable`, `Swimmable`, `Printable`

### Mixin rules:
- Should NOT have `__init__` (or only add to existing)
- Should NOT stand alone — always combined with a real class
- Should be focused on ONE behaviour
- Listed BEFORE the main class in inheritance: `class Child(Mixin1, Mixin2, MainBase)`