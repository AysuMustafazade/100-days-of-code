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

Where variables can be accessed.

### Types:
- Local
- Global

### LEGB Rule:
1. Local  
2. Enclosing  
3. Global  
4. Built-in  

💡 Scope controls variable visibility

---

## 12. Tracebacks

Error messages showing:
- where error happened
- what type of error

💡 Read from bottom → top

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