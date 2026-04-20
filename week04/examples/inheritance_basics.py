# ── 1. Basic inheritance ───────────────────────────────────────────────────
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r})"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # parent handles name + age
        self.breed = breed            # Dog-only attribute

    def speak(self):                  # override Animal.speak
        return f"{self.name} says: Woof!"

    def fetch(self):                  # new method, not in Animal
        return f"{self.name} fetches the ball!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"


dog = Dog("Rex", 3, "Labrador")
cat = Cat("Whiskers", 5)

print(dog.speak())      # Rex says: Woof!
print(dog.describe())   # Rex is 3 years old.  ← inherited
print(dog.fetch())      # Rex fetches the ball!
print(repr(dog))        # Dog('Rex')            ← inherited __repr__
print(cat.speak())      # Whiskers says: Meow!

# ── 2. What is inherited ──────────────────────────────────────────────────
class Parent:
    class_attr = "shared"

    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"   # name-mangled

    def public_method(self):
        return "public_method"

    def _protected_method(self):
        return "_protected_method"

    def __private_method(self):
        return "__private_method"


class Child(Parent):
    def show(self):
        print(self.public)           
        print(self._protected)       
        print(self.class_attr)       
        print(self.public_method())  
        # self.__private            #  AttributeError
        # self.__private_method()   #  AttributeError


c = Child()
c.show()

# ── 3. New attributes on instances ────────────────────────────────────────
dog = Dog("Rex", 3, "Lab")
dog.tricks = ["sit", "shake", "roll over"]   # added after creation 
print(dog.tricks)

# ── 4. super() in a chain ────────────────────────────────────────────────
class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def info(self):
        return f"{self.year} {self.make}"


class Car(Vehicle):
    def __init__(self, make, year, doors):
        super().__init__(make, year)
        self.doors = doors

    def info(self):
        base = super().info()        # reuse parent output
        return f"{base} ({self.doors}-door)"


class ElectricCar(Car):
    def __init__(self, make, year, doors, range_km):
        super().__init__(make, year, doors)
        self.range_km = range_km

    def info(self):
        base = super().info()
        return f"{base} — Electric, {self.range_km}km range"


ec = ElectricCar("Tesla", 2024, 4, 600)
print(ec.info())
# 2024 Tesla (4-door) — Electric, 600km range

# ── 5. Overriding with extension ──────────────────────────────────────────
class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")


class TimestampLogger(Logger):
    def log(self, msg):
        import datetime
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        super().log(f"{ts} | {msg}")  


tl = TimestampLogger()
tl.log("Server started")   # [LOG] 14:32:01 | Server started