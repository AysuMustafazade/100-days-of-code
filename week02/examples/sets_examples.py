# sets_examples.py — Set Operations & Use Cases

# ──────────────────────────────────────────────────────────────
fruits = {"apple", "banana", "cherry", "apple"}  
print(fruits)          
print(type(fruits)) 

empty_set = set()      
print(type(empty_set)) 

# ── Add / Remove ────────────────────────────────────────────────────────
s = {1, 2, 3}
s.add(4)         
s.discard(99)     
s.remove(2)       
print(s)         

# ── Set Operations ──────────────────────────────────────────────────────
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("Union:               ", a | b)   # {1,2,3,4,5,6,7,8}
print("Intersection:        ", a & b)   # {4,5}
print("Difference (a-b):    ", a - b)   # {1,2,3}
print("Symmetric difference:", a ^ b)   # {1,2,3,6,7,8}

# ──  Remove duplicates ────────────────────────────────────────
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique = list(set(data))
print("Unique:", unique)

# ── Find common elements ─────────────────────────────────────
python_devs = {"Alice", "Bob", "Charlie", "Diana"}
js_devs     = {"Bob", "Diana", "Eve", "Frank"}

both   = python_devs & js_devs        
either = python_devs | js_devs          
only_python = python_devs - js_devs     

print("Know both:       ", both)
print("Know either:     ", either)
print("Only Python devs:", only_python)

# ── Unique Visitor Tracker ───────────────────────────────────────────────
class UniqueVisitorTracker:
    def __init__(self):
        self.visitors = set()

    def visit(self, user_id):
        self.visitors.add(user_id)
        print(f"User {user_id} visited. Total unique: {len(self.visitors)}")

    def has_visited(self, user_id):
        return user_id in self.visitors

    def total(self):
        return len(self.visitors)


tracker = UniqueVisitorTracker()
tracker.visit("user_001")
tracker.visit("user_002")
tracker.visit("user_001")   

print(f"Has user_001 visited? {tracker.has_visited('user_001')}")  # True
print(f"Has user_999 visited? {tracker.has_visited('user_999')}")  # False
print(f"Total unique visitors: {tracker.total()}")                 # 3