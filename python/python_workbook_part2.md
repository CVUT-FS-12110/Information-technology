# Python Workbook Part 2: Functions, Files, and OOP

This notebook provides an overview of key Python programming concepts - including functions, file handling, and object-oriented programming.

🐍 You’ll learn how to:

- Write and use **functions** to avoid repeating code

- Work with **strings, files, and errors** more effectively

- Use modules and **Object-Oriented Programming** (OOP) to structure larger programs

---

## **1. Functions**

Functions are **blocks of reusable code** that perform a specific task.

They help make your programs easier to read, test, and maintain.

---

### Defining and Calling a Function

You define a function using a keyword `def`, followed by the function name and parentheses `()`.

```python
def greet():
    print("Hello, Python learner!")
```
To run the function, call it by name:

```python
greet()
```

Example output:
```
Hello, Python learner!
```
---

### Functions with Parameters

Functions can take **parameters** - values you pass in when calling the function.

```python
def greet_user(name):
    print("Hello,", name + "!")

greet_user("Bob")
```
Here, `"Bob"` is an argument passed into the function parameter `name`.

Example output:
```
Hello, Bob!
```
---

### Functions That Return a Value

Functions can **return a result** instead of printing directly.

```python
def add(a):
    return a + 1

result = add(3)
print("Sum:", result)
```
The `return` statement sends a value back to the place where the function was called.

Example output:
```
Sum: 4
```
---

### Default Parameters

You can set a **default value** for a parameter - used when no argument is provided.

```python
def greet(name="friend"):
    print("Hello,", name + "!")

greet()
greet("John")
```
Example output:
```
Hello, friend!
Hello, John!
```
---

### Multiple Parameters

Functions can take multiple inputs - separate them with commas.

```python
def multiply(x, y):
    return x * y

print(multiply(4, 5))
```
Example output:
```
20
```
---

### Local and Global Variables

Variables created **inside a function** exist only there - they’re *local*.

```python
x = 10

def show_number():
    x = 5
    print("Inside function:", x)

show_number()
print("Outside function:", x)
```
Example output:
```
Inside function: 5
Outside function: 10
```
---

### Summary - Functions in Python

| Concept           | Description                 | Example                       |
| ----------------- | --------------------------- | ----------------------------- |
| Define a function | Create reusable code block  | `def greet():`                |
| Call a function   | Run the code inside it      | `greet()`                     |
| Parameter         | Value passed into function  | `def add(a, b):`              |
| Return value      | Send result back            | `return a + b`                |
| Default value     | Optional parameter value    | `def greet(name="friend"):`   |
| Local variable    | Exists only inside function | `x` inside `def` block        |
| Global variable   | Accessible everywhere       | Declared outside any function |

---

## **String Indexing and Slicing**

Strings are sequences of characters used to store and manipulate text.

You can create a string using single `(' ')` or double `(" ")` quotes:

```python
text = "Hello, Python!"
```
---

### Local and Global Variables

You can access parts of a string using **indexes**.

Python counts from 0 (first character) onward.

```python
word = "Python"
print(word[0])   # First letter
print(word[2:5]) # Slice from index 2 to 4
print(word[-1])  # Last letter
```
`word[start:end]` includes `start` but excludes `end`.

Example output:
```
P
tho
n
```
---

### Combining and Repeating Strings

You can join strings using `+` and repeat them using `*`.

```python
greeting = "Hello"
name = "Alice"

print(greeting + " " + name)
print("Hi! " * 3)
```

Example output:
```
Hello Alice
Hi! Hi! Hi!
```
---

### String Formatting (f-strings)

You can combine text and variables using f-strings (formatted strings).

```python
name = "Bob"
age = 27
print(f"My name is {name} and I am {age} years old.")
```

f-strings make your code cleaner than using `+` for concatenation.

Example output:
```
My name is Bob and I am 27 years old.
```
---

### Useful String Methods

String methods help you easily manipulate text.

| Method           | Description                           | Example                     | Output          |
| ---------------- | ------------------------------------- | --------------------------- | --------------- |
| `.upper()`       | Converts to uppercase                 | `"hello".upper()`           | `HELLO`         |
| `.lower()`       | Converts to lowercase                 | `"Hello".lower()`           | `hello`         |
| `.title()`       | Capitalizes first letter of each word | `"python guide".title()`    | `Python Guide`  |
| `.strip()`       | Removes extra spaces                  | `"  hi  ".strip()`          | `hi`            |
| `.replace(a, b)` | Replaces part of string               | `"hello".replace("h", "j")` | `jello`         |
| `.split()`       | Splits into list by spaces            | `"a b c".split()`           | `['a','b','c']` |
| `.join()`        | Joins list into string                | `" ".join(['a','b','c'])`   | `a b c`         |
| `.count(x)`      | Counts occurrences                    | `"banana".count("a")`       | `3`             |

---

### Summary - Strings in Python

| Concept          | Description      | Example                              | Output      |
| ---------------- | ---------------- | ------------------------------------ | ----------- |
| Create string    | Use quotes       | `"Hello"`                            | Hello       |
| Access character | Use index        | `"Python"[0]`                        | P           |
| Slice            | Get substring    | `"Python"[1:4]`                      | yth         |
| Combine          | Join text        | `"Hi " + "there"`                    | Hi there    |
| Repeat           | Multiply string  | `"Hi! " * 3`                         | Hi! Hi! Hi! |
| Length           | Count characters | `len("Python")`                      | 6           |
| f-string         | Embed variables  | `f"Hi {name}"`                       | Hi Alice    |
| Common methods   | Modify strings   | `.upper()`, `.replace()`, `.split()` | —           |


---

## 4. Working with Files

Python allows you to read from and write to files - so your programs can **save data, process documents**, or **store user information** permanently.

---

### Opening a File

You open a file using the built-in `open()` function:

```python
file = open("example.txt", "r")  # "r" = read mode
content = file.read()
print(content)
file.close()
```

Always close the file after using it - this frees system resources.

---

### Using `with open()` - Automatic Closing

The preferred way to open files is with a `with` statement - it automatically closes the file when you’re done.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

This is **safer** and **cleaner** - no need to call `close()` manually.

---

### Writing to a File

Use **write mode** (`"w"`) to create or overwrite a file.

```python
with open("output.txt", "w") as file:
    file.write("This is my first file!\n")
    file.write("Python is awesome!")
```

If the file already exists, this **overwrites** it.
If it doesn’t, Python **creates a new one**.

---

### Appending to a File

Use **append mode** (`"a"`) to add new lines **without deleting existing content**.

```python
with open("output.txt", "a") as file:
    file.write("\nAdding another line.")
```

---

### Reading Files Line by Line

Sometimes, you want to read one line at a time - especially for large files.

```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes \n
```

---

## 4. Error Handling

Sometimes, things go wrong when your program runs - maybe a file doesn’t exist, a user types text instead of a number, or you divide by zero.

Instead of crashing, Python lets you **handle errors** using `try` and `except`.

---

### Basic `try` / `except` Block

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except:
    print("Something went wrong!")
```

The `try` block is where you *attempt* risky code.

If an error occurs, the `except` block runs instead of stopping the program.

Example output:
```
Something went wrong!
```

---

### Catching Specific Error Types

You can specify which type of error you expect - this makes debugging easier.

```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You can’t divide by zero!")
except ValueError:
    print("Please enter a valid number.")
```
Example output:
```
# User enters 0:
You can’t divide by zero!

# User enters "abc":
Please enter a valid number.
```

---

### `else` and `finally` Clauses

- `else` runs if no error happens.
- `finally` runs always — even if there was an error (useful for cleanup).

```python
try:
    num = int(input("Enter a positive number: "))
except ValueError:
    print("That’s not a number!")
else:
    print("Thank you, you entered:", num)
finally:
    print("Program finished.")
```
Example output:
```
Enter a positive number: 5
Thank you, you entered: 5
Program finished.
```

---

### Raising Your Own Errors

You can use `raise` to generate a custom error when certain conditions aren’t met.

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    else:
        print("Age is valid.")

check_age(25)
check_age(-2)
```
Example output:
```
Age is valid.
ValueError: Age cannot be negative!
```

---

### Summary - Error Handling in Python

| Keyword   | Purpose                        | Example                         | Runs When       |
| --------- | ------------------------------ | ------------------------------- | --------------- |
| `try`     | Code that might cause an error | `try:`                          | Always          |
| `except`  | Handles the error              | `except ZeroDivisionError:`     | If error occurs |
| `else`    | Runs if no error occurs        | `else:`                         | No errors       |
| `finally` | Always runs (cleanup)          | `finally:`                      | Always          |
| `raise`   | Creates a custom error         | `raise ValueError("Bad input")` | When triggered  |

---

## 5. Object-Oriented Programming (OOP)

OOP helps you organize your code around objects - things that have properties (data) and behaviors (functions).
For example, a `Car` can have a color (property) and a `drive()` function (behavior).

OOP is one of the most important concepts in programming!

---

### What Is a Class and an Object?

- **Class** – a blueprint for creating objects
- **Object** – an instance of a class

Think of a class like a *recipe*, and an object like the *cake* you bake from that recipe.

---

### Defining a Simple Class

You can use `raise` to generate a custom error when certain conditions aren’t met.

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} is driving!")

# Create an object
my_car = Car("Toyota", "red")
my_car.drive()
```
`__init__()` is called automatically when a new object is created.

`self` refers to the current object.

Example output:
```
The red Toyota is driving!
```

---

### Attributes and Methods

| Term          | Meaning                     | Example                         |
| ------------- | --------------------------- | ------------------------------- |
| **Attribute** | A variable inside an object | `self.color`                    |
| **Method**    | A function inside a class   | `def drive(self):`              |
| **Object**    | An instance of a class      | `my_car = Car("Toyota", "red")` |

---

### Example: Dog Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

dog1.bark()
dog2.bark()
```

Example output:
```
Buddy says woof!
Lucy says woof!
```

---

### Adding and Modifying Attributes

You can change object properties after creation:

```python
dog1.age = 4
print(dog1.age)
```

Example output:
```
4
```

You can also add new attributes dynamically:

```python
dog1.breed = "Golden Retriever"
print(dog1.breed)
```

Example output:
```
Golden Retriever
```

---
