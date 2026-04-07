

# ── 1. Access levels ───────────────────────────────────────────────────────
class Employee:
    company = "TechCorp"   # class attribute — public

    def __init__(self, name, salary, ssn):
        self.name = name        # PUBLIC — intended for anyone
        self._salary = salary   # PROTECTED — internal use
        self.__ssn = ssn        # PRIVATE — name-mangled

    def get_info(self):
        # Inside the class, all levels are accessible
        return f"{self.name} | {self._salary} | {self.__ssn}"

emp = Employee("Alice", 75000, "123-45-6789")

print(emp.name)         #  "Alice"
print(emp._salary)      #  works but bad practice — 75000
#print(emp.__ssn)        #  AttributeError
print(emp._Employee__ssn)  #  mangled name — "123-45-6789"
print(emp.get_info())      #  access with method

# ── 2. __dict__ ────────────────────────────────────────────────────────────
class Point:
    dimensions = 2   # class attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)

print("Instance __dict__:", p.__dict__)
# {"x": 3, "y": 4}

print("Class __dict__ keys:", list(Point.__dict__.keys()))
# ["dimensions", "__init__", "__dict__", "__weakref__", "__doc__"]

print("x" in p.__dict__)          # True  — instance attr
print("dimensions" in p.__dict__) # False — class attr
print(p.dimensions)               # 2 

# ── 3. Attribute lookup order ──────────────────────────────────────────────
class Animal:
    sound = "..."

class Dog(Animal):
    sound = "Woof"   

d = Dog()
d.sound = "WOOF!"   

print(d.sound)      
del d.sound
print(d.sound)      
del Dog.sound
print(d.sound)      

# ── 4. getattr / setattr / hasattr / delattr ──────────────────────────────
class Robot:
    def __init__(self, name):
        self.name = name
        self.power = 100

r = Robot("R2D2")

# getattr — safe access with default
attr_name = "speed"
print(getattr(r, attr_name, 0))   

# setattr — dynamic attribute setting
setattr(r, "speed", 75)
print(r.speed)   # 75

# hasattr
print(hasattr(r, "speed"))   # True
print(hasattr(r, "fly"))     # False

# delattr
delattr(r, "speed")
print(hasattr(r, "speed"))   # False


config = {"color": "red", "weight": 50, "version": "2.0"}
for key, value in config.items():
    setattr(r, key, value)

print(r.color)    # "red"
print(r.weight)   # 50