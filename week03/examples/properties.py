
# ── 1. The problem without properties ─────────────────────────────────────
class PersonBad:
    def __init__(self, age):
        self.age = age   # anyone can set age = -99

p = PersonBad(25)
p.age = -99   # nothing stops this 
print(p.age)  # -99


# ── 2. Pythonic @property ──────────────────────────────────────────────────
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age     # calls the setter immediately

    @property
    def age(self):
        """Getter — called on: person.age"""
        return self._age

    @age.setter
    def age(self, value):
        """Setter — called on: person.age = value"""
        if not isinstance(value, int):
            raise TypeError("Age must be an integer.")
        if not 0 <= value <= 150:
            raise ValueError(f"Invalid age: {value}")
        self._age = value

    @age.deleter
    def age(self):
        """Deleter — called on: del person.age"""
        print("Deleting age...")
        del self._age


p = Person("Alice", 25)
print(p.age)     # 25 — calls getter
p.age = 26       # calls setter — validates
try:
    p.age = -5   # raises ValueError
except ValueError as e:
    print(f"Error: {e}")

# ── 3. Read-only property ─────────────────────────────────────────────────
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        import math
        return round(math.pi * self.radius ** 2, 2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2   # update radius with diameter


c = Circle(5)
print(c.area)       # 78.54
print(c.diameter)   # 10

c.diameter = 20     # sets radius to 10
print(c.radius)     # 10.0

try:
    c.area = 100    # AttributeError — no setter defined
except AttributeError as e:
    print(f"Error: {e}")

# ── 4. Temperature with full property ─────────────────────────────────────
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius  

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    def __repr__(self):
        return f"Temperature({self._celsius}°C)"


t = Temperature(100)
print(t.fahrenheit)   # 212.0
print(t.kelvin)       # 373.15

t.fahrenheit = 32
print(t.celsius)      # 0.0