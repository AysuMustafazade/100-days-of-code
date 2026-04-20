# ── 1. Duck Typing ────────────────────────────────────────────────────────
class Dog:
    def speak(self): return "Woof!"
    def move(self):  return "runs"

class Cat:
    def speak(self): return "Meow!"
    def move(self):  return "slinks"

class Robot:
    def speak(self): return "Beep boop."
    def move(self):  return "rolls"

class Rock:
    pass   # no speak(), no move()

def make_it_speak(thing):
    """Works with ANY object that has speak() — no shared base needed."""
    if hasattr(thing, "speak"):
        print(thing.speak())
    else:
        print(f"{type(thing).__name__} cannot speak!")

for obj in [Dog(), Cat(), Robot(), Rock()]:
    make_it_speak(obj)


# ── 2. Protocol — formal duck typing (Python 3.8+) ────────────────────────
from typing import Protocol, runtime_checkable

@runtime_checkable
class Speakable(Protocol):
    def speak(self) -> str: ...

@runtime_checkable
class Movable(Protocol):
    def move(self) -> str: ...

def describe(thing: Speakable) -> str:
    return f"It says: {thing.speak()}"

print(describe(Dog()))    # It says: Woof!
print(describe(Robot()))  # It says: Beep boop.

print(isinstance(Dog(), Speakable))   # True
print(isinstance(Rock(), Speakable))  # False


# ── 3. Mixins ─────────────────────────────────────────────────────────────
import json

class ReprMixin:
    """Auto __repr__ from instance __dict__."""
    def __repr__(self):
        attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items()
                          if not k.startswith("_"))
        return f"{self.__class__.__name__}({attrs})"

class SerializeMixin:
    """Adds to_dict() and to_json() to any class."""
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()
                if not k.startswith("_")}

    def to_json(self):
        return json.dumps(self.to_dict(), indent=2)

    @classmethod
    def from_dict(cls, data: dict):
        obj = cls.__new__(cls)
        for k, v in data.items():
            setattr(obj, k, v)
        return obj

class ValidateMixin:
    """Adds validate() — subclass defines _validators dict."""
    def validate(self):
        errors = []
        for attr, validator in getattr(self, "_validators", {}).items():
            value = getattr(self, attr, None)
            if not validator(value):
                errors.append(f"Invalid {attr!r}: {value!r}")
        return errors

    def is_valid(self):
        return len(self.validate()) == 0

class CompareMixin:
    """Adds comparison based on a _compare_key property."""
    def __eq__(self, other):
        return self._compare_key == other._compare_key

    def __lt__(self, other):
        return self._compare_key < other._compare_key

    def __le__(self, other):
        return self._compare_key <= other._compare_key


# ── 4. Applying mixins ────────────────────────────────────────────────────
class Person(ReprMixin, SerializeMixin, ValidateMixin, CompareMixin):
    _validators = {
        "age":  lambda v: isinstance(v, int) and 0 <= v <= 150,
        "name": lambda v: isinstance(v, str) and len(v) > 0,
    }

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    @property
    def _compare_key(self):
        return self.age


class Product(ReprMixin, SerializeMixin, CompareMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def _compare_key(self):
        return self.price


# Person
alice = Person("Alice", 25, "Baku")
bob   = Person("Bob", 30, "London")
bad   = Person("", -5, "?")

print(repr(alice))           # Person(name='Alice', age=25, city='Baku')
print(alice.to_json())
print(alice.validate())      # [] — all good
print(bad.validate())        # ["Invalid 'age': -5", "Invalid 'name': ''"]
print(alice < bob)           # True (25 < 30)

# Deserialize
data = {"name": "Charlie", "age": 22, "city": "Paris"}
charlie = Person.from_dict(data)
print(repr(charlie))

# Product
p1 = Product("Phone", 499)
p2 = Product("Laptop", 999)
products = [p2, p1]
products.sort()              
print([repr(p) for p in products])
# [Product(name='Phone', price=499), Product(name='Laptop', price=999)]