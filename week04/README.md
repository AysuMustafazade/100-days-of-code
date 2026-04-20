# Week 4 — Inheritance, Abstract Classes & Interfaces

> 📅 **Challenge:** #100DaysOfCode  
> 🐍 **Language:** Python 
> 🗓️ **Week:** 4

---

## 📚 Topics Covered

### 🧬 Inheritance
- Superclass / base class / parent class
- Subclass / derived class / child class
- The default base class — `object`
- Single inheritance — how to inherit a class
- What subclasses inherit (public, protected — not private)
- When instances can have new attributes
- Overriding methods and attributes
- `super()` — calling the parent class
- `isinstance()`, `issubclass()`, `type()` — type checking
- Listing attributes and methods with `dir()`, `vars()`, `__dict__`

### 🏛️ Abstract Classes & Interfaces
- `ABC` and `@abstractmethod` — defining abstract classes
- Abstract properties
- Interfaces and duck typing
- `Protocol` (Python 3.8+)
- Method overriding in depth
- Multiple inheritance and MRO (Method Resolution Order)
- Subclassing standard base classes (`list`, `dict`, iterators)
- Mixins — composing behaviour across unrelated classes

---

## 📁 Files

| File | Description |
|------|-------------|
| `notes.md` | Detailed notes with explanations and code snippets |
| `examples/` | Code examples per topic |
| `README.md` | This file |

### Examples folder structure

```
examples/
├── inheritance_basics.py     # Single inheritance, super(), overriding
├── multiple_inheritance.py   # Multiple bases, MRO, diamond problem
├── type_checking.py          # isinstance, issubclass, type
├── abstract_classes.py       # ABC, @abstractmethod, abstract properties
├── duck_typing.py            # Duck typing, Protocol
├── subclass_builtins.py      # Custom list, dict, iterator
├── mixins.py                 # Mixin composition
└── projects/
    └── animal_system.py      # Full project — Animal hierarchy with ABC
```

---

## 💡 Key Takeaways

- **Inheritance** models "is-a" relationships — use it when the subclass truly IS a type of the parent
- `super()` follows MRO — always prefer it over hardcoding the parent class name
- `isinstance()` respects inheritance; `type()` is strict — prefer `isinstance()`
- **Abstract classes** enforce a contract — subclasses MUST implement `@abstractmethod` methods
- **Duck typing**: Python doesn't care about class hierarchy — only whether the object has the right methods
- **Mixins** add behaviour without being standalone classes — name them `XxxMixin` or adjectives like `Flyable`
- MRO (Method Resolution Order) determines which method is called in multiple inheritance — use `ClassName.mro()` to inspect it

---
