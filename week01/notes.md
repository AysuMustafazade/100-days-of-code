# 📘 Week 1 — Python Fundamentals

> **Topics covered:** if/else · loops · functions · imports & modules · lists · tuples

---

## 📌 Table of Contents

1. [Why Indentation Matters](#1-why-indentation-matters)
2. [if / if...else Statements](#2-if--ifelse-statements)
3. [Comments](#3-comments)
4. [Variables & Value Assignment](#4-variables--value-assignment)
5. [while and for Loops](#5-while-and-for-loops)
6. [break, continue, pass](#6-break-continue-pass)
7. [else on Loops](#7-else-on-loops)
8. [range()](#8-range)
9. [Functions](#9-functions)
10. [Return Statement & Default Return](#10-return-statement--default-return)
11. [Variable Scope](#11-variable-scope)
12. [Tracebacks](#12-tracebacks)
13. [Arithmetic Operators](#13-arithmetic-operators)
14. [Imports & Modules](#14-imports--modules)
15. [Lists](#15-lists)
16. [Tuples](#16-tuples)

---

## 1. Why Indentation Matters

Python does **not** use `{}` curly braces to define code blocks like C, Java, or JavaScript.
Instead, Python uses **indentation** (spaces/tabs) to group statements together.

> ✅ Standard: **4 spaces** per indentation level (PEP 8 style guide)
```python
# CORRECT ✅
if True:
    print("This is inside the if block")
    print("This too!")
print("This is outside")

# WRONG ❌ — IndentationError
if True:
print("No indentation!")
```

**Why it matters:**
- Misaligned code raises an `IndentationError` or — worse — runs with unexpected logic
- Mixing tabs and spaces causes a `TabError`
- Good indentation = readable, bug-free code

---

## 2. if / if...else Statements

Used to make **decisions** in code based on conditions.
```python
age = 20

# Simple if
if age >= 18:
    print("You are an adult.")

# if...else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if...elif...else (multiple conditions)
score = 75

if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")
```

**Comparison operators used in conditions:**

| Operator | Meaning           |
|----------|-------------------|
| `==`     | Equal to          |
| `!=`     | Not equal to      |
| `>`      | Greater than      |
| `<`      | Less than         |
| `>=`     | Greater or equal  |
| `<=`     | Less or equal     |

**Logical operators:**
```python
if age > 18 and age < 65:
    print("Working age")

if age < 5 or age > 80:
    print("Special care needed")

if not age == 0:
    print("Age is not zero")
```

---

## 3. Comments

Comments are lines Python **ignores**. They exist only for humans reading the code.
```python
# This is a single-line comment

x = 5  # Inline comment — explains what this line does

"""
This is a multi-line string often used as
a multi-line comment or docstring.
"""

def greet(name):
    """
    This is a docstring — it documents what the function does.
    It appears right after the function definition.
    """
    print(f"Hello, {name}!")
```

> 💡 Good comments explain **WHY**, not **WHAT**. The code already shows what — explain the reasoning.

---

## 4. Variables & Value Assignment

A **variable** is a name that stores a value in memory.
```python
# Basic assignment
name = "Rustam"
age = 22
gpa = 3.8
is_student = True

# Multiple assignment on one line
x, y, z = 1, 2, 3

# Assign same value to multiple variables
a = b = c = 0

# Reassignment — variables can change type!
x = 10
x = "now I'm a string"
x = [1, 2, 3]

# Augmented assignment operators
count = 0
count += 1   # count = count + 1  → 1
count -= 1   # count = count - 1  → 0
count *= 3   # count = count * 3  → 0
```

**Python naming rules:**
- Must start with a letter or `_`
- Can contain letters, digits, `_`
- Case-sensitive: `Name` ≠ `name`
- Use `snake_case` (not camelCase) by convention

---

## 5. while and for Loops

### `while` loop — runs **as long as** a condition is True
```python
count = 0
while count < 5:
    print(count)
    count += 1
# Prints: 0 1 2 3 4

# Infinite loop — be careful!
while True:
    user_input = input("Type 'quit' to stop: ")
    if user_input == "quit":
        break
```

### `for` loop — iterates over a **sequence**
```python
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a string
for char in "Python":
    print(char)

# Iterating over a range
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (step=2)
    print(i)
```

---

## 6. break, continue, pass

### `break` — **exits** the loop immediately
```python
for i in range(10):
    if i == 5:
        break       # stops at 5
    print(i)
# Prints: 0 1 2 3 4
```

### `continue` — **skips** current iteration, goes to next
```python
for i in range(10):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)
# Prints: 1 3 5 7 9
```

### `pass` — **does nothing** — a placeholder
```python
# Use when Python syntax requires a block but you have nothing to write yet
for i in range(5):
    pass  # TODO: add logic later

def my_function():
    pass  # placeholder — function body can't be empty

class MyClass:
    pass  # empty class definition
```

> 💡 `pass` is useful when you're building the structure of your code before filling in the logic.

---

## 7. else on Loops

In Python, loops can have an `else` block. It runs **only if the loop completed normally** (without hitting `break`).
```python
# else runs — no break was triggered
for i in range(5):
    print(i)
else:
    print("Loop finished normally!")

# else does NOT run — break was triggered
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will NOT print")
```

**Practical use — searching:**
```python
users = ["Alice", "Bob", "Charlie"]
target = "Bob"

for user in users:
    if user == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found.")
```

---

## 8. range()

`range()` generates a sequence of numbers — it does **not** create a list in memory (memory efficient).
```python
range(stop)               # 0 to stop-1
range(start, stop)        # start to stop-1
range(start, stop, step)  # with custom step

# Examples
list(range(5))          # [0, 1, 2, 3, 4]
list(range(1, 6))       # [1, 2, 3, 4, 5]
list(range(0, 10, 2))   # [0, 2, 4, 6, 8]
list(range(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Loop n times
for _ in range(3):
    print("Hello!")
# _ is used when you don't need the loop variable
```

---

## 9. Functions

A **function** is a reusable block of code that performs a specific task.
```python
# Defining a function
def greet():
    print("Hello, World!")

# Calling a function
greet()

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Rustam")

# Function with default parameter
def greet_user(name="stranger"):
    print(f"Hello, {name}!")

greet_user()          # Hello, stranger!
greet_user("Alice")   # Hello, Alice!

# Function with multiple parameters
def add(a, b):
    return a + b

result = add(3, 5)   # result = 8

# Function with return value
def square(n):
    return n * n

print(square(4))   # 16

# Function with multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi = min_max([3, 1, 9, 2])
print(lo, hi)  # 1 9
```

---

## 10. Return Statement & Default Return
```python
# With return — sends value back to caller
def add(a, b):
    return a + b

result = add(2, 3)  # result = 5

# Without return — function returns None
def say_hi():
    print("Hi!")

result = say_hi()   # prints "Hi!"
print(result)       # prints None  ← default return value!
```

> ⚠️ A function that has no `return` statement (or just `return` with no value) **always returns `None`**.
```python
def do_nothing():
    pass

print(do_nothing())   # None

# return also exits the function early
def check_positive(n):
    if n < 0:
        return "Negative"   # exits here
    return "Positive"
```

---

## 11. Variable Scope

**Scope** defines where a variable can be accessed.

### Local scope — inside a function
```python
def my_func():
    x = 10      # local variable
    print(x)    # works fine

my_func()
print(x)        # ❌ NameError — x doesn't exist outside
```

### Global scope — outside all functions
```python
x = 100         # global variable

def my_func():
    print(x)    # ✅ can READ global variable

my_func()       # prints 100
```

### Modifying a global variable from inside a function
```python
counter = 0

def increment():
    global counter      # declare intent to modify global
    counter += 1

increment()
print(counter)   # 1
```

> 💡 Using `global` too much is bad practice. Prefer returning values and reassigning.

### LEGB Rule — Python looks for variables in this order:
1. **L**ocal
2. **E**nclosing (nested functions)
3. **G**lobal
4. **B**uilt-in (`len`, `print`, etc.)

---

## 12. Tracebacks

A **traceback** is Python's error report — it shows what went wrong and where.
```
Traceback (most recent call last):
  File "script.py", line 6, in <module>
    result = divide(10, 0)
  File "script.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```

**How to read it:**
- Read from **bottom to top** — the last line is the actual error
- The error type: `ZeroDivisionError`
- The message: `division by zero`
- The file and line number: `script.py, line 2`

**Common errors:**

| Error | Cause |
|-------|-------|
| `SyntaxError` | Invalid Python syntax |
| `NameError` | Variable not defined |
| `TypeError` | Wrong type operation (`"a" + 1`) |
| `IndexError` | List index out of range |
| `ZeroDivisionError` | Division by zero |
| `IndentationError` | Wrong indentation |

---

## 13. Arithmetic Operators
```python
a = 10
b = 3

print(a + b)   # 13   — Addition
print(a - b)   # 7    — Subtraction
print(a * b)   # 30   — Multiplication
print(a / b)   # 3.33 — Division (always float)
print(a // b)  # 3    — Floor division (integer result)
print(a % b)   # 1    — Modulo (remainder)
print(a ** b)  # 1000 — Exponentiation (10³)
```

**Useful tricks:**
```python
# Check if number is even/odd
n = 7
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Integer vs float division
print(7 / 2)    # 3.5
print(7 // 2)   # 3
```

---

## 14. Imports & Modules

A **module** is a `.py` file containing Python code (functions, variables, classes).
**Importing** lets you use code from other files/modules.

### Importing built-in modules
```python
import math
print(math.sqrt(16))     # 4.0
print(math.pi)           # 3.14159...

import random
print(random.randint(1, 10))  # random number 1-10

import os
print(os.getcwd())       # current working directory
```

### Different import styles
```python
# Import entire module
import math
math.sqrt(9)

# Import specific function
from math import sqrt, pi
sqrt(9)         # no need for "math." prefix

# Import with alias
import numpy as np
np.array([1, 2, 3])

# Import everything (avoid in large projects)
from math import *
sqrt(9)
```

### Creating your own module
```python
# mymodule.py
def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

PI = 3.14159
```
```python
# main.py
import mymodule

print(mymodule.add(2, 3))       # 5
print(mymodule.greet("Alice"))  # Hello, Alice!
```

### `dir()` — list all attributes of a module
```python
import math
print(dir(math))
# ['__doc__', '__name__', 'acos', 'asin', 'ceil', 'cos', 'floor', 'log', 'pi', 'sqrt', ...]
```

### `__name__ == "__main__"` — prevent code from running on import
```python
# mymodule.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("Testing add function:")
    print(add(2, 3))
```

### Command line arguments
```python
# script.py
import sys

print(sys.argv)         # list of arguments
print(sys.argv[0])      # script name
print(sys.argv[1])      # first argument

# Run: python script.py hello world
# sys.argv = ['script.py', 'hello', 'world']
```

---

## 15. Lists

A **list** is an ordered, mutable (changeable) collection that can hold any types.
```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# Accessing elements (0-indexed)
print(fruits[0])    # "apple"
print(fruits[-1])   # "cherry" (last element)
print(fruits[1:3])  # ["banana", "cherry"] (slice)

# Modifying elements
fruits[0] = "mango"
print(fruits)   # ["mango", "banana", "cherry"]
```

### Common list methods
```python
fruits = ["apple", "banana"]

fruits.append("cherry")           # add to end
fruits.insert(1, "mango")         # insert at index
fruits.extend(["grape", "kiwi"])  # add multiple items

fruits.remove("banana")      # remove by value
popped = fruits.pop()        # remove & return last item
popped = fruits.pop(0)       # remove & return item at index

fruits.sort()                # sort ascending
fruits.sort(reverse=True)    # sort descending
fruits.reverse()             # reverse in place

print(len(fruits))           # number of items
print("apple" in fruits)     # True/False
print(fruits.index("apple")) # index of item
print(fruits.count("apple")) # count occurrences

fruits.clear()               # remove all items
copy = fruits.copy()         # shallow copy
```

### Lists as Stack (LIFO)
```python
stack = []
stack.append("a")   # push
stack.append("b")
stack.append("c")
top = stack.pop()   # pop → "c"
```

### Lists as Queue (FIFO)
```python
from collections import deque

queue = deque(["a", "b", "c"])
queue.append("d")       # enqueue
first = queue.popleft() # dequeue → "a"
```

### List Comprehensions
```python
# Traditional way
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension — same result, one line
squares = [x ** 2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Nested
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
```

### Strings vs Lists

| Feature | String | List |
|---------|--------|------|
| Ordered | ✅ | ✅ |
| Indexing | ✅ | ✅ |
| Slicing | ✅ | ✅ |
| Iterable | ✅ | ✅ |
| Mutable | ❌ | ✅ |
| Holds types | chars only | any type |

### `del` statement
```python
fruits = ["apple", "banana", "cherry"]

del fruits[1]   # remove item at index
print(fruits)   # ["apple", "cherry"]

del fruits      # delete entire variable
```

---

## 16. Tuples

A **tuple** is an ordered, **immutable** (unchangeable) collection.
```python
# Creating tuples
coordinates = (10, 20)
rgb = (255, 128, 0)
single = (42,)      # ⚠️ single item needs trailing comma!
empty = ()

# Accessing (same as lists)
print(coordinates[0])   # 10
print(coordinates[-1])  # 20
print(rgb[0:2])         # (255, 128)

# Tuples are IMMUTABLE — this raises TypeError:
# coordinates[0] = 99   ❌
```

### Tuple Packing & Unpacking
```python
# Packing
point = 3, 7           # same as (3, 7)

# Unpacking
x, y = point
print(x)   # 3
print(y)   # 7

# Extended unpacking
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

# Swap variables
a, b = 10, 20
a, b = b, a
print(a, b)   # 20 10
```

### When to use Tuple vs List?

| Use **Tuple** when... | Use **List** when... |
|-----------------------|----------------------|
| Data should not change | Data changes over time |
| Returning multiple values from a function | Building a collection dynamically |
| Dictionary keys (tuples are hashable) | You need `.append()`, `.remove()` etc. |
| Slightly faster than lists | Order/content may vary |

### Sequences

Strings, lists, and tuples are all **sequences** — they share common operations:
```python
# All sequences support:
len(s)      # length
s[0]        # indexing
s[1:3]      # slicing
s + s       # concatenation
s * 2       # repetition
"h" in s    # membership
for c in s: # iteration
```