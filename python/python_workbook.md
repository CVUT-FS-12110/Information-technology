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

### Simple Assignment Operators

| Operator | Example   | Same as      | Description                            |
| -------- | --------- | ------------ | -------------------------------------- |
| `=`      | `x = 5`   | `x = 5`      | Assigns value 5 to variable `x`        |
| `+=`     | `x += 3`  | `x = x + 3`  | Adds and assigns the result            |
| `-=`     | `x -= 2`  | `x = x - 2`  | Subtracts and assigns the result       |
| `*=`     | `x *= 4`  | `x = x * 4`  | Multiplies and assigns the result      |
| `/=`     | `x /= 2`  | `x = x / 2`  | Divides and assigns the result (float) |
| `%=`     | `x %= 3`  | `x = x % 3`  | Modulus (remainder) and assign         |
| `//=`    | `x //= 2` | `x = x // 2` | Floor division and assign (integer)    |
| `**=`    | `x **= 2` | `x = x ** 2` | Exponentiation and assign              |
| `&=`     | `x &= 3`  | `x = x & 3`  | Bitwise AND and assign                 |
| `\|=`    | `x \|= 2` | `x = x \| 2` | Bitwise OR and assign                  |
| `^=`     | `x ^= 2`  | `x = x ^ 2`  | Bitwise XOR and assign                 |
| `>>=`    | `x >>= 1` | `x = x >> 1` | Bitwise right shift and assign         |
| `<<=`    | `x <<= 1` | `x = x << 1` | Bitwise left shift and assign          |

```python
count = 0
count += 1
print("Result:", count)
```
Example output:
```
Result: 1
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
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # first item
print(fruits[2])   # third item
print(fruits[-1])  # last item
```

Note: Comments starts with a `#`, and Python will ignore them.

Example output:
```
apple
cherry
cherry
```
**Modifying a list:**
```python
fruits = ["apple", "banana", "cherry"]

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
print(a.union(b))        # combine sets
print(a.intersection(b)) # common elements
```
Example output:
```
{1, 2, 3, 4, 5}
{3}
```

---

### **Dictionaries**

A dictionary stores data in key–value pairs.

```python
person = {"name": "Bob", "age": 27, "city": "Prague"}
print(person["name"])  # access value by key
```
Example output:
```
Bob
```

**Add or modify values:**

```python
person["age"] = 26
person["job"] = "Engineer"
print(person)
```
Example output:
```
{'name': 'Bob', 'age': 26, 'city': 'Prague', 'job': 'Engineer'}
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

---

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

**Summing Numbers with a `while` Loop:**

```python
total = 0
number = 1

while number <= 5:
    total += number
    number += 1

print("Total:", total)
```

Example output:
```
Total: 15
```

**Try it for yourself** – Simple Guessing Game:

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

**Basic forms of `range()`:**

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

**Looping Through a String:**

You can loop through each character in a string - the loop variable will take one character at a time.
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

**Looping Through a List:**

You can also loop through each element in a list - great for processing items one by one.
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)
```
Each time the loop runs, the variable fruit stores one list element.

Example output:
```
I like apple
I like banana
I like cherry
```

**Try it for yourself** – Printing Even Numbers:

```python
for number in range(2, 11, 2):
    print(number)
```
Here we used `range()` function to control how counting works.

---

## **5. Practice Exercises**

**A.** Write a program that checks whether a number is even or odd

---

**B.** Ask the user to input their age
- If age < 13 → print “Child”
- If 13–19 → print “Teenager”
- Otherwise → print “Adult”

---

**C.** Ask the user to enter a number
- If it’s positive → print “Positive”
- If it’s zero → print “Zero”
- If it’s negative → print “Negative”

---

**D.** Create a simple grading system
```python
score = int(input("Enter your score: "))
# If score >= 90: print "A"
# If 80–89: print "B"
# If 70–79: print "C"
# If 60–69: print "D"
# Otherwise: print "F"
```

---

**E.** Count from 1 to 10 using a `while` loop

---

**F.** Print all even numbers from 1 to 20 using a `for` loop

---

**G.** Calculate the factorial of a number using a `while` loop

Hint: Multiply numbers from 1 up to `n` to get the factorial.

Example: 5! = 1 × 2 × 3 × 4 × 5 = 120
```python
n = int(input("Enter the number from which the factorial will be calculated: "))
```

---

**H.** Multiplication table - ask for a number and print its table up to 10

Example for 3:
```python
3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
```

---

**I.** Draw a triangle using `*` symbols

Task: Print a growing triangle pattern using stars.
```python
*
**
***
****
*****
```

---

**J.** Even or Odd (Using a Loop + Condition)

Task: Write a program that prints whether each number between 1 and 10 is even or odd.

Hint: Use `for number in range(1, 11)` and the modulus operator `%`.

---

**K.** Sum of Positive Numbers (While Loop + Condition)

Task: Ask the user to enter numbers until they type 0.
Then print the sum of all positive numbers they entered.

Hint: Use a `while` loop with `input()` and convert to `int`.

---

**L.** Favorite Fruits (List + Loop + Condition)

Task: Create a list of your favorite fruits.
Ask the user to input a fruit name and tell them whether it’s in your list.

---

**M.** Word Counter (String + Loop + Dictionary)

Task: Count how many times each word appears in a short sentence.

Hint: Split the sentence into words with `.split()` and use a dictionary to count.

---

**N.** Multiplication Table (Nested Loop)

Task: Print a multiplication table (1–10) neatly formatted.

Output should look like this:
```
1	2	3	4	5	6	7	8	9	10
2	4	6	8	10	12	14	16	18	20
...
10	20	30	40	50	60	70	80	90	100
```

---
