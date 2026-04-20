# ── 1. Multiple base classes ───────────────────────────────────────────────
class Flyable:
    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    def swim(self):
        return f"{self.name} is swimming!"

class Walkable:
    def walk(self):
        return f"{self.name} is walking!"

class Animal:
    def __init__(self, name):
        self.name = name

class Duck(Animal, Flyable, Swimmable, Walkable):
    def speak(self):
        return "Quack!"

class Penguin(Animal, Swimmable, Walkable):
    def speak(self):
        return "Squawk!"


donald = Duck("Donald")
print(donald.fly())    # Donald is flying!
print(donald.swim())   # Donald is swimming!
print(donald.speak())  # Quack!

tux = Penguin("Tux")
print(tux.swim())      # Tux is swimming!
print(tux.walk())      # Tux is walking!
# tux.fly()            # AttributeError — penguins can't fly!

# ── 2. MRO — Method Resolution Order ─────────────────────────────────────
class A:
    def hello(self):
        return "Hello from A"

class B(A):
    def hello(self):
        return "Hello from B"

class C(A):
    def hello(self):
        return "Hello from C"

class D(B, C):
    pass  


d = D()
print(d.hello())     # "Hello from B" — B comes first in MRO

# Inspect MRO
print(D.mro())
# [D, B, C, A, object]
# Python reads left to right: D → B → C → A → object

# ── 3. Diamond problem — solved by MRO ───────────────────────────────────

class Base:
    def method(self):
        return "Base"

class X(Base):
    def method(self):
        return f"X → {super().method()}"

class Y(Base):
    def method(self):
        return f"Y → {super().method()}"

class Z(X, Y):
    def method(self):
        return f"Z → {super().method()}"


z = Z()
print(z.method())   # Z → X → Y → Base
print(Z.mro())      # [Z, X, Y, Base, object]

# ── 4. Cooperative super() ────────────────────────────────────────────────
class LogMixin:
    def greet(self):
        print("[LOG] greeting called")
        return super().greet()

class FormalGreeter:
    def greet(self):
        return "Good day, sir."

class Person(LogMixin, FormalGreeter):
    def __init__(self, name):
        self.name = name


p = Person("Alice")
result = p.greet()
# [LOG] greeting called
print(result)   # Good day, sir.
print(Person.mro())  # [Person, LogMixin, FormalGreeter, object]