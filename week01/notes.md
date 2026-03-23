# 📘 Week 1 — Python Fundamentals

This week focuses on the core building blocks of Python programming.

---

## 📌 Topics Covered

- Control Flow (if/else)
- Loops (for, while)
- Functions
- Imports & Modules
- Lists & Tuples
- Basic Operators
- Error Understanding (Tracebacks)

---

## 1. Why Indentation Matters

Python uses **indentation** instead of `{}` to define code blocks.

- Standard: **4 spaces**
- Incorrect indentation → `IndentationError`
- Mixing tabs & spaces → `TabError`

💡 Clean indentation = readable and predictable code

---

## 2. if / else Statements

Used to control decision-making in programs.

### Key Operators:
- `==` equal  
- `!=` not equal  
- `>` `<` `>=` `<=`

### Logical Operators:
- `and`
- `or`
- `not`

💡 Code flows based on conditions

---

## 3. Comments

Comments are ignored by Python and used for explanation.

- `#` → single-line comment  
- `""" """` → multi-line / docstring  

💡 Good comments explain **WHY**, not WHAT

---

## 4. Variables & Assignment

Variables store data.

### Rules:
- Use `snake_case`
- Case-sensitive
- Can change type dynamically

💡 Python is dynamically typed

---

## 5. Loops (for & while)

### while
- Runs while condition is True

### for
- Iterates over sequences (list, string, range)

💡 Use loops to automate repetition

---

## 6. break, continue, pass

- `break` → stops loop completely  
- `continue` → skips current iteration  
- `pass` → placeholder (does nothing)

💡 Useful for controlling loop behavior

---

## 7. else in Loops

`else` runs only if loop **does NOT break**

💡 Often used in search logic

---

## 8. range()

Generates number sequences.

- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`

💡 Memory efficient (not a full list)

---

## 9. Functions

Reusable blocks of code.

### Concepts:
- parameters
- return values
- default arguments

💡 Functions help organize and reuse logic

---

## 10. Return Statement

- `return` sends value back
- No return → returns `None` by default

💡 Every function returns something

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

- `+` addition  
- `-` subtraction  
- `*` multiplication  
- `/` division  
- `//` floor division  
- `%` modulo  
- `**` exponent  

💡 Used for calculations and logic

---

## 14. Imports & Modules

Modules = reusable Python files.

### Types:
- built-in (math, random)
- custom modules

### Special:
- `__name__ == "__main__"`

💡 Helps organize and reuse code

---

## 15. Lists

- Ordered
- Mutable
- Can store multiple types

### Key Features:
- indexing
- slicing
- methods (append, remove, sort)

💡 Most commonly used data structure

---

## 16. Tuples

- Ordered
- Immutable

### Use Cases:
- fixed data
- multiple return values

💡 Safer and slightly faster than lists

---

## 🔚 Summary

This week builds the **foundation of Python**:
- understanding how code flows
- writing reusable functions
- working with basic data structures

Consistency matters more than complexity.

---