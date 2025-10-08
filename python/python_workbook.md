# Python Introduction


This guide provides an introduction to **Python** commands.  
Each command is shown with a **description** and **example usage**.

---

## **1. Introduction to Python Basics**

### `print()` – Displaying Output
Prints the specified message to the screen.
```python
print("Hello World!")
```
Always put text inside quotation marks (`" "` or `' '`) — otherwise, Python thinks it’s a variable name, not text.

Example output:
```
Hello World!
```

---

### `Variables` – Storing Information
A variable is a name used to store data so you can reuse it later.

Think of it as a labeled box where you keep a value.
```python
name = "Bob"
age = 27
print(name)
print(age)
```
Variable names cannot have spaces and must start with a letter or underscore.

Example output:
```
Bob
27
```
---

### `Data Types` – Numbers, Text and Booleans
Python can store different types of data:
- `str` – String: text, written in quotes
- `int` – Integer: whole numbers
- `float` – Float: decimal numbers
- `bool` – Boolean: `True` or `False`

```python
name = "Bob"      # string
age = 27          # integer
height = 1.75     # float
is_student = True # boolean
```

---

### `input()` – Getting User Input
You can ask the user for input using the `input()` function.

Everything entered by the user is read as text (a string).

```python
name = input("Enter your name: ")
print("Hello,", name, "!")
```
Example output:
```
Enter your name: Bob
Hello, Bob !
```

---

### Simple Arithmetic
| Operation          | Symbol | Example  | Result |
| ------------------ | ------ | -------- | ------ |
| Addition           | `+`    | `2 + 2`  | 4      |
| Subtraction        | `-`    | `4 - 1`  | 3      |
| Multiplication     | `*`    | `5 * 2`  | 10     |
| Division           | `/`    | `8 / 2`  | 4.0    |
| Floor division     | `//`   | `8 // 3` | 2      |
| Modulo (remainder) | `%`    | `7 % 3`  | 1      |
| Power              | `**`   | `2 ** 3` | 8      |

```python
a = 10
b = 3
print("Sum:", a + b)
print("Remainder:", a % b)
```
Example output:
```
Sum: 13
Remainder: 1
```

---

## **2. Collections in Python**

Collections let you store multiple values in a single variable.

The four main built-in types in Python are:
| Type           | Ordered             | Changeable | Allows Duplicates     | Syntax         |
| -------------- | ------------------- | ---------- | --------------------- | -------------- |
| **List**       | ✅ Yes               | ✅ Yes      | ✅ Yes                 | `[ ]`          |
| **Tuple**      | ✅ Yes               | ❌ No       | ✅ Yes                 | `( )`          |
| **Set**        | ❌ No                | ✅ Yes      | ❌ No                  | `{ }`          |
| **Dictionary** | ✅ Yes (Python 3.7+) | ✅ Yes      | ❌ Keys must be unique | `{key: value}` |

---

### **Lists**
A list stores multiple items in a specific order and can be changed.

```python
fruits = ["apple", "banana", "cherry"]
```
**Accessing elements:**
```python
print(fruits[0])   # first item
print(fruits[2])   # third item
print(fruits[-1])  # last item
```
Example output:
```
apple
cherry
cherry
```
**Modifying a list:**
```python
fruits.append("orange")  # add
fruits[1] = "kiwi"       # change
fruits.remove("apple")   # remove
print(fruits)
```
Example output:
```
['kiwi', 'cherry', 'orange']
```
**Common List functions:**
| Function      | Description        | Example          | Result    |
| ------------- | ------------------ | ---------------- | --------- |
| `len(list)`   | Number of items    | `len(fruits)`    | 3         |
| `sum(list)`   | Sum of all numbers | `sum([2, 4, 6])` | 12        |
| `max(list)`   | Largest value      | `max([3, 7, 1])` | 7         |
| `min(list)`   | Smallest value     | `min([3, 7, 1])` | 1         |
| `list.sort()` | Sorts in order     | `[3,1,2].sort()` | `[1,2,3]` |

---

### **Tuples**

A tuple is like a list, but it cannot be changed (it’s immutable).

```python
colors = ("red", "green", "blue")
print(colors[0])
```
If you try to modify it:
```python
colors[0] = "yellow"
```
You’ll get an error, because tuples can’t be changed.

Use tuples when your data shouldn’t change (like days of the week).

---

### **Sets**

A set is an unordered collection of unique items.
```python
numbers = {1, 2, 3, 3, 4}
print(numbers)
```
Example output:
```
{1, 2, 3, 4}
```
Notice: duplicates are removed automatically.

You can also perform set operations:
```python
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))       # combine sets
print(a.intersection(b)) # common elements
```
Example output:
```
{1, 2, 3, 4}
```

---

### **Dictionaries**

A dictionary stores data in key–value pairs.

```python
person = {"name": "Alice", "age": 25, "city": "Prague"}
print(person["name"])  # access value by key
```

**Add or modify values:**

```python
person["age"] = 26
person["job"] = "Engineer"
print(person)
```

---

## **3. Conditional Statements (if/elif/else)**

Conditional statements let your program make decisions - they control what happens based on certain conditions.

---

### `if` Statement
The `if` statement runs a block of code only if the condition is true.
```python
x = 10
if x > 5:
    print("x is greater than 5")
```
Indentation (spaces before the line) is very important in Python.
Use 4 spaces (or press Tab once) to indent code inside an if block.

Example output:
```
x is greater than 5
```

---

### `if ... else` Statement
The `else` block runs if the condition is not true.
```python
number = 0
if number > 0:
    print("Positive number")
else:
    print("Negative number or zero")
```

Example output:
```
Negative number or zero
```

---

### `if ... elif ... else` Statement
When you have multiple conditions, use elif (“else if”).
```python
temperature = 25

if temperature > 30:
    print("It's hot outside.")
elif temperature > 20:
    print("It's warm outside.")
else:
    print("It's cold outside.")
```

Example output:
```
It's warm outside.
```

---

### Comparison and Logical Operators

| Operator | Meaning                  | Example  | Result |
| -------- | ------------------------ | -------- | ------ |
| `==`     | Equal to                 | `5 == 5` | `True` |
| `!=`     | Not equal to             | `5 != 3` | `True` |
| `>`      | Greater than             | `8 > 6`  | `True` |
| `<`      | Less than                | `3 < 5`  | `True` |
| `>=`     | Greater than or equal to | `6 >= 6` | `True` |
| `<=`     | Less than or equal to    | `4 <= 5` | `True` |

**Logical operators** let you combine conditions:
- `and` – both conditions must be True
- `or` – at least one condition must be True
- `not` – reverses the condition

```python
age = 18
if age >= 18 and age < 65:
    print("You are an adult.")
```

Example output:
```
You are an adult.
```

---

## **4. Loops**
Loops let you repeat code multiple times without writing it again and again.

They are useful when you need to perform a task many times or go through a collection of data.

### `while` Loop
A `while` loop repeats as long as its condition is **True**.

```python
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
```
Example output:
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```
Be careful with while loops - if the condition never becomes `False`, you’ll create an infinite loop.

---

**Summing Numbers with a `while` Loop**

```python
total = 0
number = 1

while number <= 5:
    total += number
    number += 1

print("Total:", total)
```
Inside the loop, count += 1 means: add 1 to count

Example output:
```
Total: 15
```

---

**Example** – Simple Guessing Game

```python
secret = 7
guess = int(input("Guess a number between 1 and 10: "))

while guess != secret:
    print("Wrong! Try again.")
    guess = int(input("Guess again: "))

print("You got it!")
```

---

### `range()` Function
`range()` is a built-in Python function that generates a sequence of numbers.

You can use it in a `for` loop to control how many times the loop runs.

Basic forms of `range()`:

| Form                       | Meaning                                              | Example           | Generated Numbers |
| -------------------------- | ---------------------------------------------------- | ----------------- | ----------------- |
| `range(stop)`              | Counts from 0 up to (but not including) `stop`       | `range(5)`        | 0, 1, 2, 3, 4     |
| `range(start, stop)`       | Counts from `start` up to (but not including) `stop` | `range(2, 6)`     | 2, 3, 4, 5        |
| `range(start, stop, step)` | Counts by `step`                                     | `range(1, 10, 2)` | 1, 3, 5, 7, 9     |

---

### `for` – Loop
A `for` loop is used to iterate over a sequence - like a list, string, or range of numbers.
```python
for i in range(5):
    print("Iteration:", i)
```
Example output:
```
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
```

---

**Example** – Printing Even Numbers

```python
for number in range(2, 11, 2):
    print(number)
```
Example output:
```
2
4
6
8
10
```

---

**Looping Through a String**

```python
word = "Python"
for letter in word:
    print(letter)
```
Example output:
```
P
y
t
h
o
n
```

---

**Looping Through a List**

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)
```
Example output:
```
I like apple
I like banana
I like cherry
```

---

## **5. Practice Exercises**



---


