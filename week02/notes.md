# 📘 Week 2 — More Data Structures, Exceptions & TDD

> **Topics covered:** Sets · Dictionaries · Exceptions · Test-Driven Development

---

## 📌 Table of Contents

1. [Sets](#1-sets)
2. [Dictionaries](#2-dictionaries)
3. [Exceptions](#3-exceptions)
4. [Test-Driven Development (TDD)](#4-test-driven-development-tdd)

---

## 1. Sets

A **set** is an unordered collection of **unique** elements. No duplicates allowed.

```python
# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()
# From a list removes duplicates automatically
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = set(names)
print(unique_names)   # {"Alice", "Bob", "Charlie"}
```

> ⚠️ Sets are **unordered** — you cannot access elements by index (`my_set[0]` raises `TypeError`).

### Common Set Methods

```python
s = {1, 2, 3}

s.add(4)          # add a single element → {1, 2, 3, 4}
s.remove(2)       # remove element — raises KeyError if not found
s.discard(99)     # remove element — NO error if not found ✅
s.pop()           # remove and return a random element
s.clear()         # remove all elements

print(3 in s)     # True — membership check O(1) — very fast!
print(len(s))     # number of elements
```

### Set Operations — the real power of sets

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union — all elements from both sets
print(a | b)          # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))     # same

# Intersection — only elements in BOTH sets
print(a & b)                  # {4, 5}
print(a.intersection(b))      # same

# Difference — elements in a but NOT in b
print(a - b)              # {1, 2, 3}
print(a.difference(b))    # same

# Symmetric difference — elements in one but NOT both
print(a ^ b)                        # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))    # same

# Subset / Superset
small = {1, 2}
print(small.issubset(a))    # True — all of small is in a
print(a.issuperset(small))  # True — a contains all of small
print(a.isdisjoint(b))      # False — they share elements
```

### When to Use Sets?

| Use a Set when...                              |
|------------------------------------------------|
| You need to remove duplicates from a list      |
| You need fast membership checks (`in`)         |
| You need to compare two collections (union, intersection, etc.) |
| Order doesn't matter and you don't need indexing |

```python
# Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = set(list1) & set(list2)
print(common)   # {3, 4, 5}

# Remove duplicates from a list
data = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(data))
print(unique)   # [1, 2, 3, 4]
```

---

## 2. Dictionaries

A **dictionary** is an unordered collection of **key-value pairs**. Keys must be unique and immutable.

```python
# Creating dictionaries
person = {"name": "Alice", "age": 25, "city": "Baku"}
empty = {}
empty = dict()

# From pairs
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)   # {"a": 1, "b": 2}
```

### Accessing Values

```python
person = {"name": "Alice", "age": 25}

# Direct access — raises KeyError if key doesn't exist
print(person["name"])    # "Alice"

# .get() — returns None (or default) if key doesn't exist ✅
print(person.get("age"))         # 25
print(person.get("email"))       # None
print(person.get("email", "N/A"))  # "N/A" — custom default
```

### Modifying Dictionaries

```python
person = {"name": "Alice", "age": 25}

# Add / update
person["email"] = "alice@example.com"  # add new key
person["age"] = 26                      # update existing key

# Update multiple keys at once
person.update({"age": 27, "city": "Baku"})

# Remove
del person["email"]              # raises KeyError if not found
popped = person.pop("age")       # removes & returns value
popped = person.pop("x", None)   # safe pop — no error if missing

person.clear()   # remove all items
```

### Iterating Over Dictionaries

```python
person = {"name": "Alice", "age": 25, "city": "Baku"}

# Keys only (default)
for key in person:
    print(key)

# Values only
for value in person.values():
    print(value)

# Keys and values together ✅ most common
for key, value in person.items():
    print(f"{key}: {value}")

# Check membership (checks keys)
print("name" in person)    # True
print("Alice" in person)   # False — "Alice" is a value, not a key
```

### Useful Dictionary Methods

```python
d = {"a": 1, "b": 2, "c": 3}

print(d.keys())     # dict_keys(["a", "b", "c"])
print(d.values())   # dict_values([1, 2, 3])
print(d.items())    # dict_items([("a",1), ("b",2), ("c",3)])

# setdefault — returns value if key exists, otherwise sets default
d.setdefault("d", 0)    # adds "d": 0 if "d" doesn't exist
print(d)                # {"a": 1, "b": 2, "c": 3, "d": 0}

# Merge dicts (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2     # {"a": 1, "b": 2}
```

### Dictionary Comprehensions

```python
# Basic
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}

# Count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {word: words.count(word) for word in set(words)}
# {"apple": 3, "banana": 2, "cherry": 1}
```

### Nested Dictionaries

```python
students = {
    "Alice": {"grade": "A", "score": 95},
    "Bob":   {"grade": "B", "score": 82},
}

print(students["Alice"]["score"])   # 95

# Iterate nested
for name, info in students.items():
    print(f"{name}: {info['grade']} ({info['score']})")
```

### Sets vs Dictionaries vs Lists — Quick Comparison

| Feature        | List    | Set       | Dictionary      |
|----------------|---------|-----------|-----------------|
| Ordered        | ✅      | ❌        | ✅ (Python 3.7+)|
| Indexed        | ✅      | ❌        | ✅ (by key)     |
| Duplicates     | ✅      | ❌        | ❌ (keys)       |
| Mutable        | ✅      | ✅        | ✅              |
| Use case       | sequence| unique items | key-value store |

---

## 3. Exceptions

An **exception** is a runtime error that interrupts the normal flow of a program.
Python lets you **catch** exceptions, handle them gracefully, and even **raise** your own.

### try / except

```python
# Without exception handling — program crashes
print(10 / 0)   # ZeroDivisionError: division by zero

# With exception handling — program continues
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Output: Cannot divide by zero!
```

### Catching Multiple Exceptions

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except TypeError:
        print("Error: Invalid types for division!")

safe_divide(10, 0)      # ZeroDivisionError
safe_divide(10, "a")    # TypeError

# Catch multiple in one line
try:
    pass
except (TypeError, ValueError) as e:
    print(f"Error: {e}")

# Catch all exceptions (use sparingly)
try:
    risky_operation()
except Exception as e:
    print(f"Something went wrong: {e}")
```

### else and finally

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error!")
else:
    # Runs ONLY if no exception occurred
    print(f"Result: {result}")   # Result: 5.0
finally:
    # ALWAYS runs — with or without exception
    # Use for cleanup: close files, DB connections, etc.
    print("Done.")
```

**Summary:**

| Block     | When it runs                          |
|-----------|---------------------------------------|
| `try`     | Always (until an exception)           |
| `except`  | Only when the matched exception occurs|
| `else`    | Only when NO exception occurs         |
| `finally` | Always — exception or not             |

### Raising Exceptions

```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)   # Age cannot be negative!
```

### Creating Custom Exceptions

```python
# Define a custom exception by inheriting from Exception
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}. Balance is only {self.balance}."
            )
        self.balance -= amount
        return self.balance

account = BankAccount(100)

try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)
# Cannot withdraw 150. Balance is only 100.
```

### Common Built-in Exceptions

| Exception           | Cause                                    |
|---------------------|------------------------------------------|
| `ValueError`        | Right type, wrong value (`int("abc")`)   |
| `TypeError`         | Wrong type (`"a" + 1`)                   |
| `KeyError`          | Dict key doesn't exist                   |
| `IndexError`        | List index out of range                  |
| `AttributeError`    | Object doesn't have the attribute        |
| `FileNotFoundError` | File doesn't exist                       |
| `ZeroDivisionError` | Division by zero                         |
| `NameError`         | Variable not defined                     |
| `ImportError`       | Module can't be imported                 |
| `StopIteration`     | Iterator exhausted                       |

---

## 4. Test-Driven Development (TDD)

**TDD** is a development approach where you write **tests before writing the code**.

### The TDD Cycle — Red → Green → Refactor

```
1. RED    — Write a test that FAILS (the feature doesn't exist yet)
2. GREEN  — Write the minimum code to make the test PASS
3. REFACTOR — Clean up the code while keeping tests passing
Repeat.
```

### Why TDD?

- Catches bugs **before** they reach production
- Forces you to think about **what** the code should do before **how**
- Acts as living documentation
- Makes refactoring safe — tests tell you if you broke something

### Python's `unittest` Module

```python
import unittest

# The function we want to test
def add(a, b):
    return a + b

# Test class must inherit from unittest.TestCase
class TestAdd(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)

if __name__ == "__main__":
    unittest.main()
```

Run: `python test_add.py`

### Common Assertion Methods

```python
self.assertEqual(a, b)        # a == b
self.assertNotEqual(a, b)     # a != b
self.assertTrue(x)            # x is True
self.assertFalse(x)           # x is False
self.assertIsNone(x)          # x is None
self.assertIsNotNone(x)       # x is not None
self.assertIn(item, container)       # item in container
self.assertNotIn(item, container)    # item not in container
self.assertRaises(ExcType, func, *args)  # func raises ExcType
```

### TDD Example — Step by Step

**Step 1: Write the test FIRST (it will fail — that's expected)**

```python
# test_calculator.py
import unittest
from calculator import Calculator   # doesn't exist yet!

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """setUp runs before EACH test method."""
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
```

**Step 2: Write the minimum code to make tests pass**

```python
# calculator.py
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
```

**Step 3: Run tests — all should pass ✅**

```bash
python -m unittest test_calculator.py -v
# test_add ... ok
# test_divide ... ok
# test_divide_by_zero ... ok
# test_multiply ... ok
# test_subtract ... ok
# Ran 5 tests in 0.001s — OK
```

### Test Structure — AAA Pattern

```python
def test_something(self):
    # ARRANGE — set up inputs and state
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]

    # ACT — call the function being tested
    result = max(numbers)

    # ASSERT — verify the result
    self.assertEqual(result, 9)
```

### setUp and tearDown

```python
class TestBankAccount(unittest.TestCase):

    def setUp(self):
        """Runs before EACH test — create fresh state."""
        self.account = BankAccount(balance=1000)

    def tearDown(self):
        """Runs after EACH test — cleanup."""
        pass  # useful for closing files, DB connections, etc.

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800)

    def test_overdraft(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(9999)
```

### Testing Exceptions

```python
# Method 1: assertRaises as context manager (preferred)
def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        divide(10, 0)

# Method 2: assertRaises as function call
def test_divide_by_zero(self):
    self.assertRaises(ZeroDivisionError, divide, 10, 0)
```

### Running Tests

```bash
# Run a specific test file
python -m unittest test_calculator.py

# Run with verbose output (shows each test name)
python -m unittest test_calculator.py -v

# Run all tests in the current directory
python -m unittest discover

# Run a specific test class
python -m unittest test_calculator.TestCalculator

# Run a specific test method
python -m unittest test_calculator.TestCalculator.test_add
```

### TDD vs Writing Tests After

| | TDD (tests first) | Tests after |
|---|---|---|
| Design | Forces better API design | Code may be hard to test |
| Coverage | High by default | Easy to forget edge cases |
| Confidence | High — tests verify every feature | Lower — tests may miss things |
| Speed | Slower initially | Faster initially, slower later |