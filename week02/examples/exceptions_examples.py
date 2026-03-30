# exceptions_examples.py — Exception Handling Patterns

# ── try / except ──────────────────────────────────────────────────
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ── Multiple except blocks ─────────────────────────────────────────────
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid integer.")
    except TypeError:
        print(f"Cannot convert type {type(value).__name__}.")
    return None

print(safe_convert("42"))     # 42
print(safe_convert("hello"))  # ValueError
print(safe_convert(None))     # TypeError

# ── else and finally ────────────────────────────────────────────────────
def read_number(prompt):
    try:
        value = float(input(prompt))
    except ValueError:
        print("Not a valid number!")
        return None
    else:
        print(f"Got: {value}")  # only if no exception
        return value
    finally:
        print("Input attempt complete.")  # always runs

# ──  Raising Exceptions ─────────────────────────────────────────────────
def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age seems unrealistic.")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    set_age("twenty")
except TypeError as e:
    print(f"TypeError: {e}")


# ── Safe File Reader ────────────────────────────────────────────────────
def read_file_safe(filepath):
    try:
        with open(filepath, "r") as f:
            content = f.read()
            print(f"File read successfully: {len(content)} chars.")
            return content
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    except PermissionError:
        print(f"Permission denied: {filepath}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

read_file_safe("nonexistent.txt")    # FileNotFoundError
