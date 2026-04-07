
# ── 1. Class attributes ────────────────────────────────────────────────────
class Dog:
    species = "Canis familiaris"   # shared by ALL instances
    count = 0

    def __init__(self, name, breed):
        self.name = name    # unique per instance
        self.breed = breed
        Dog.count += 1      # update shared counter

    def __repr__(self):
        return f"Dog({self.name!r})"


d1 = Dog("Rex", "German Shepherd")
d2 = Dog("Buddy", "Labrador")
d3 = Dog("Max", "Poodle")

print(Dog.count)    
print(d1.species)    
print(d2.species)    

# assigning with instance creates instance attr
d1.species = "Modified"
print(d1.species)    # "Modified"  — instance attr 
print(d2.species)    #  class attr unchanged

# ── 2. @classmethod — alternative constructors ────────────────────────────
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self):
        return f"Date({self.year}, {self.month:02d}, {self.day:02d})"

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

    @classmethod
    def from_string(cls, date_str):
        """Alternative constructor from 'YYYY-MM-DD' string."""
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)

    @classmethod
    def today(cls):
        """Alternative constructor for today's date."""
        import datetime
        d = datetime.date.today()
        return cls(d.year, d.month, d.day)

    @staticmethod
    def is_valid(year, month, day):
        """Utility — validates a date. Doesn't need class or instance."""
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        return True

    @staticmethod
    def is_leap_year(year):
        """Utility — check leap year."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


d1 = Date(2024, 6, 15)
d2 = Date.from_string("2024-12-25")   # classmethod
d3 = Date.today()                      # classmethod

print(repr(d1))   # Date(2024, 06, 15)
print(str(d2))    # 2024-12-25
print(d3)         # today

print(Date.is_valid(2024, 13, 1))    # False — staticmethod
print(Date.is_leap_year(2024))       # True

# ── 3. Student with class counter ─────────────────────────────────────────
class Student:
    _total = 0      # class attribute — tracks count

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student._total += 1
        self._id = Student._total

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not 0 <= value <= 100:
            raise ValueError(f"Grade must be 0-100, got {value}")
        self._grade = value

    @classmethod
    def total_students(cls):
        return cls._total

    @staticmethod
    def passing_grade(grade):
        return grade >= 50

    def __repr__(self):
        return f"Student(id={self._id}, name={self.name!r}, grade={self._grade})"


s1 = Student("Alice", 92)
s2 = Student("Bob", 45)
s3 = Student("Charlie", 78)

print(Student.total_students())       # 3
print(Student.passing_grade(45))      # False
print(Student.passing_grade(78))      # True

for s in [s1, s2, s3]:
    status = "PASS" if Student.passing_grade(s.grade) else "FAIL"
    print(f"{s.name}: {s.grade} — {status}")