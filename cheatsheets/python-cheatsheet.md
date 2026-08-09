# Python Cheatsheet

## Variables and Data Types

```python
name = "Alice"        # string
age = 18              # integer
height = 1.65         # float
is_student = True     # boolean

print(type(name))     # <class 'str'>
```

## Math Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `5 + 3 = 8` |
| `-` | Subtraction | `5 - 3 = 2` |
| `*` | Multiplication | `5 * 3 = 15` |
| `/` | Division | `5 / 2 = 2.5` |
| `//` | Floor division | `5 // 2 = 2` |
| `%` | Modulo | `5 % 2 = 1` |
| `**` | Power | `2 ** 3 = 8` |

## Lists

```python
fruits = ["apple", "banana", "cherry"]
fruits[0]            # "apple"
fruits[-1]           # "cherry"
fruits.append("date")
fruits.remove("banana")
len(fruits)          # 3
```

## Dictionaries

```python
student = {
    "name": "Alice",
    "age": 18,
    "major": "Data Science"
}

student["name"]      # "Alice"
student["gpa"] = 3.8
"name" in student    # True
```

## Conditions

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
```

## Loops

```python
for fruit in fruits:
    print(fruit)

n = 0
while n < 5:
    print(n)
    n += 1
```

## Functions

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

## String Formatting

```python
name = "Alice"
age = 18
print(f"{name} is {age} years old.")
```

## List Comprehensions (Optional)

```python
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]
```

## Common Built-in Functions

| Function | Description |
|---|---|
| `print()` | Display output |
| `len()` | Length of a list or string |
| `sum()` | Sum of numbers |
| `min()` / `max()` | Smallest / largest value |
| `round()` | Round a number |
| `sorted()` | Sort a list |
| `type()` | Get the data type |
| `int()` / `float()` / `str()` | Convert types |
