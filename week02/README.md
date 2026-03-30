# Week 2 — More Data Structures, Exceptions & TDD

> 📅 **Challenge:** #100DaysOfCode  
> 🐍 **Language:** Python 
> 🗓️ **Week:** 2

---

## 📚 Topics Covered

### 🗂️ More Data Structures
- Sets: creation, methods, set operations (union, intersection, difference)
- When to use sets vs lists
- Dictionaries: creation, access, modification, iteration
- Dictionary comprehensions
- Nested dictionaries
- Sets vs Dictionaries vs Lists — comparison

### ⚠️ Exceptions
- try / except — catching exceptions
- Catching multiple exceptions
- `else` and `finally` blocks
- Raising exceptions with `raise`
- Creating custom exceptions
- Common built-in exceptions

### 🧪 Test-Driven Development (TDD)
- The Red → Green → Refactor cycle
- Python's `unittest` module
- Common assertion methods
- setUp and tearDown
- Testing exceptions with `assertRaises`
- Running tests from command line
- AAA pattern (Arrange, Act, Assert)

---

## 📁 Files

| File | Description |
|------|-------------|
| `notes.md` | Detailed notes with explanations |
| `examples/` | Mini projects and code examples |
| `README.md` | This file |

### Examples folder structure

```
examples/
├── sets_examples.py          # Set operations and use cases
├── dict_examples.py          # Dictionary operations and use cases
├── exceptions_examples.py    # Exception handling patterns
├── bank_account.py           # BankAccount class with custom exceptions
├── test_bank_account.py      # TDD — tests for BankAccount
├── calculator.py             # Calculator class
└── test_calculator.py        # TDD — tests for Calculator
```

---

## 💡 Key Takeaways

- `set()` not `{}` for empty sets — `{}` creates an empty **dict**
- Use `.get()` instead of `[]` when a key might not exist — avoids `KeyError`
- `finally` always runs — perfect for cleanup (closing files, DB connections)
- In TDD, **write the test first** — let it fail, then write code to make it pass
- `setUp()` runs before **each** test — keeps tests independent of each other
- Sets have O(1) membership check — much faster than lists for `in` operator

