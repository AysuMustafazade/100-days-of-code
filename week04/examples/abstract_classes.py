from abc import ABC, abstractmethod
import math

# ── 1. Basic abstract class ────────────────────────────────────────────────
class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    # Concrete method — shared, no override needed
    def describe(self):
        return (f"{self.__class__.__name__}: "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f}")


# Cannot instantiate abstract class
try:
    s = Shape()
except TypeError as e:
    print(f"Error: {e}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimeter(self):
        return self.a + self.b + self.c


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    print(shape.describe())

# ── 2. Abstract property ──────────────────────────────────────────────────
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def sound(self):
        """Subclasses must define what sound they make."""
        pass

    @property
    @abstractmethod
    def legs(self) -> int:
        pass

    def describe(self):
        return f"{self.name} has {self.legs} legs and says '{self.sound}'"


class Dog(Animal):
    @property
    def sound(self):
        return "Woof"

    @property
    def legs(self):
        return 4


class Bird(Animal):
    @property
    def sound(self):
        return "Tweet"

    @property
    def legs(self):
        return 2


for animal in [Dog("Rex"), Bird("Tweety")]:
    print(animal.describe())

# ── 3. Abstract class as interface ────────────────────────────────────────
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Resizable(ABC):
    @abstractmethod
    def resize(self, factor: float):
        pass

class Saveable(ABC):
    @abstractmethod
    def save(self, path: str):
        pass


class Canvas(Drawable, Resizable, Saveable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return f"Drawing {self.width}x{self.height} canvas"

    def resize(self, factor):
        self.width = int(self.width * factor)
        self.height = int(self.height * factor)

    def save(self, path):
        return f"Saving canvas to {path}"


c = Canvas(800, 600)
print(c.draw())        # Drawing 800x600 canvas
c.resize(0.5)
print(c.draw())        # Drawing 400x300 canvas
print(c.save("output.png"))