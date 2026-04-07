
# ── 1. __repr__ and __str__ ───────────────────────────────────────────────
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """For developers — unambiguous, ideally eval()-able."""
        return f"Point({self.x!r}, {self.y!r})"

    def __str__(self):
        """For users — readable and pretty."""
        return f"({self.x}, {self.y})"


p = Point(3, 4)

print(str(p))    # (3, 4)       ← __str__
print(repr(p))   # Point(3, 4)  ← __repr__
print(p)         # (3, 4)       ← print() calls __str__

# Inside a list, __repr__ is used
points = [Point(1, 2), Point(3, 4)]
print(points)   # [Point(1, 2), Point(3, 4)]

# ── 2. __repr__ only (fallback) ───────────────────────────────────────────
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"


v = Vector(1, 2, 3)
print(v)        # Vector(1, 2, 3) — __repr__ used as fallback
print(repr(v))  # Vector(1, 2, 3)

# ── 3. Arithmetic dunder methods ──────────────────────────────────────────
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        """Called on: v1 + v2"""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Called on: v1 - v2"""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Called on: v * 3"""
        return Vector2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Called on: v1 == v2"""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """Called on: len(v) — magnitude as int"""
        return int((self.x**2 + self.y**2) ** 0.5)


v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

print(v1 + v2)    # Vector2D(4, 6)
print(v2 - v1)    # Vector2D(2, 2)
print(v1 * 3)     # Vector2D(3, 6)
print(v1 == v2)   # False
print(len(v2))    # 5

# ── 4. __bool__, __len__ for truthiness ───────────────────────────────────
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __bool__(self):
        """Called on: if wallet, bool(wallet)"""
        return self.amount > 0

    def __repr__(self):
        return f"Wallet({self.amount})"


w1 = Wallet(50)
w2 = Wallet(0)

if w1:
    print(f"{w1} has money!")   # Wallet(50) has money!
if not w2:
    print(f"{w2} is empty!")    # Wallet(0) is empty!