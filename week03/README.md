# Week 3 — Classes, Objects & OOP

> 📅 **Challenge:** #100DaysOfCode  
> 🐍 **Language:** Python 
> 🗓️ **Week:** 3

---

## 📚 Topics Covered

### 🧱 Classes & Objects 
- What is OOP and its 4 pillars
- "First-class everything" in Python
- Classes vs Objects vs Instances
- Public, protected (`_`) and private (`__`) attributes
- `self` — what it is and how it works
- Instance methods
- `__init__` constructor
- Data Abstraction, Encapsulation & Information Hiding
- Properties (`@property`) — Pythonic getters & setters
- Attribute vs Property
- Dynamic attributes
- `__dict__` of a class and instance
- Attribute lookup order
- `getattr`, `setattr`, `hasattr`, `delattr`
- `__str__` and `__repr__` — string representations
- Difference between `__str__` and `__repr__`
- Class attributes vs instance attributes
- Class methods (`@classmethod`) — alternative constructors
- Static methods (`@staticmethod`) — utility functions
- Binding attributes to objects and classes

---

## 📁 Files

| File | Description |
|------|-------------|
| `notes.md` | Detailed notes with explanations |
| `examples/` | Code examples |
| `README.md` | This file |


## 💡 Key Takeaways

- A **class** is a blueprint; an **object** is a concrete instance of it
- `self` is just the first argument of instance methods — Python passes it automatically
- Use `_name` for protected, `__name` for private (name-mangling, not true private)
- `@property` is the Pythonic alternative to `get_age()` / `set_age()` methods
- `__repr__` is for developers (unambiguous), `__str__` is for users (readable)
- **Class attributes** are shared by all instances; **instance attributes** are unique
- `@classmethod` receives `cls` — perfect for alternative constructors
- `@staticmethod` receives nothing — utility functions that belong to the class conceptually
- Python looks up attributes: instance → class → parent classes → `AttributeError`

