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
```
```python
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
def add(a, b):
    return a + b
```
```python
result = add(3, 5)
print("Sum:", result)
```
The `return` statement sends a value back to the place where the function was called.

Example output:
```
Sum: 8
```
---
---


