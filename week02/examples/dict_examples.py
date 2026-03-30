# dict_examples.py — Dictionary Operations & Use Cases

# ──────────────────────────────────────────────────────────────
person = {"name": "Alice", "age": 25, "city": "Baku"}

print(person["name"])           
print(person.get("email", "N/A")) 

# Add / Update / Delete ───────────────────────────────────────────────
person["email"] = "alice@example.com"   # add
person["age"] = 26                       # update
person.update({"city": "London", "job": "Developer"})

del person["email"]
removed = person.pop("job", None)   

print(person)

# Iterating ───────────────────────────────────────────────────────────
scores = {"Alice": 92, "Bob": 78, "Charlie": 85}

for name, score in scores.items():
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"{name}: {score} ({grade})")

# Dictionary Comprehensions ───────────────────────────────────────────
# Squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # {1:1, 2:4, 3:9, 4:16, 5:25}

# Filter — only passing scores
passing = {name: score for name, score in scores.items() if score >= 80}
print(passing)

# Invert key-value
inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}
print(inverted)   # {1: "a", 2: "b"}

# Nested Dict — Student Grades ────────────────────────────────────────
students = {
    "Alice": {"math": 95, "english": 88, "science": 91},
    "Bob":   {"math": 72, "english": 85, "science": 79},
}

for student, grades in students.items():
    avg = sum(grades.values()) / len(grades)
    print(f"{student}: average = {avg:.1f}")