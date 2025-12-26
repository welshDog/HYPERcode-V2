# 📖 HyperCode Syntax Reference

Complete reference for all HyperCode operations.

---

## 📜 Basics

### **Comments**

```hypercode
# Single-line comment
let x = 5;  # Inline comment

/* Multi-line
   comment
   spanning lines */
```

### **Semicolons**

Every statement ends with `;` (semicolon)

```hypercode
print "hello";    ✅ Correct
print "hello"     ❌ Wrong (missing ;)
```

---

## 💰 Output (Printing)

### **print**

Output text or values to console.

```hypercode
print "Hello, World!";
print 42;
print 3.14;

let name = "Alex";
print name;
print "Name: ";
print name;
```

**Output:**
```
Hello, World!
42
3.14
Alex
Name: 
Alex
```

---

## 🖱 Variables

### **let (Create Variable)**

Declare and initialize a variable.

```hypercode
let x = 10;              # Number
let message = "hello";   # String
let pi = 3.14;           # Decimal
let count = 0;           # Start with zero
```

### **Using Variables**

```hypercode
let age = 25;
print age;               # Output: 25

let new_age = age + 1;
print new_age;           # Output: 26
```

### **Variable Naming Rules**

```✅ VALID:                  ❌ INVALID:
x                          123x (starts with number)
my_variable                 my-variable (uses dash)
VARIABLE                    variable! (has special char)
var123                      let (reserved keyword)
```

---

## 🗣 Data Types

### **Numbers**

```hypercode
let integer = 42;         # Whole number
let decimal = 3.14;       # With decimal point
let negative = -10;       # Negative numbers
```

### **Strings**

Text enclosed in quotes:

```hypercode
let name = "Alex";
let message = "Hello, World!";
let empty = "";
```

**String Operations:**

```hypercode
let first = "Hello";
let second = "World";
let combined = first + second;  # Concatenation
print combined;                 # Output: HelloWorld
```

### **Type Conversion**

```hypercode
let num = 42;
let text = "42";

# Numbers and strings are different
let sum1 = 10 + 5;       # 15 (math)
let sum2 = "10" + "5";   # "105" (concatenation)
```

---

## 📍 Arithmetic

### **Basic Operations**

```hypercode
let a = 10;
let b = 3;

let add = a + b;         # Addition: 13
let subtract = a - b;    # Subtraction: 7
let multiply = a * b;    # Multiplication: 30
let divide = a / b;      # Division: 3.333...
let modulo = a % b;      # Remainder: 1
```

### **Order of Operations**

```hypercode
let result = 2 + 3 * 4;  # 14 (multiply first, then add)
let correct = (2 + 3) * 4;  # 20 (parentheses first)
```

### **Operators**

```
+   Addition
-   Subtraction
*   Multiplication
/   Division
%   Modulo (remainder)
```

---

## 🔍 Comparisons

Compare values and get true/false results.

```hypercode
let x = 10;
let y = 5;

if x > y print "greater";      # true
if x < y print "less";         # false
if x == y print "equal";       # false
if x != y print "not equal";   # true
if x >= y print ">==";         # true
if x <= y print "<=";          # false
```

### **Comparison Operators**

```
>      Greater than
<      Less than
==     Equal to
!=     Not equal to
>=     Greater than or equal
<=     Less than or equal
```

---

## 🔄 Conditionals (if)

### **Single Statement**

```hypercode
let age = 20;

if age >= 18 print "Adult";
if age < 18 print "Minor";
```

### **Multiple Statements**

```hypercode
let score = 85;

if score >= 90 {
  print "A";
  print "Excellent!";
}

if score >= 80 {
  print "B";
}
```

### **Nested Conditionals**

```hypercode
let age = 25;
let license = true;

if age >= 18 {
  if license == true {
    print "Can drive";
  }
}
```

---

## 🔁 Loops (Coming Soon)

Repeat code multiple times.

```hypercode
loop(5) {
  print "Hello!";
}

# Output:
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!
```

---

## 📄 Functions (Coming Soon)

Reusable blocks of code.

```hypercode
function greet(name) {
  print "Hello, ";
  print name;
}

greet("Alex");
greet("Jordan");
```

---

## 📋 Arrays (Coming Soon)

Collections of values.

```hypercode
let numbers = [1, 2, 3, 4, 5];
let first = numbers[0];     # 1
let second = numbers[1];    # 2

let mixed = ["Alex", 25, true];
print mixed[0];              # Alex
```

---

## 🐤 Objects (Coming Soon)

Key-value pairs.

```hypercode
let person = {
  name: "Alex",
  age: 25,
  city: "Portland"
};

print person.name;  # Alex
print person.age;   # 25
```

---

## 🧰 AI Integration (Coming Q1 2026)

```hypercode
ai:prompt("Analyze this code", model="claude");
ai:generate("Write a hello world", language="hypercode");
```

---

## 🌬 Quantum (Coming Q2 2026)

```hypercode
quantum:init(3);              # 3 qubits
quantum:hadamard([0, 1]);     # Apply operation
quantum:measure() -> result;  # Get result
```

---

## 🪦 DNA Computing (Coming Q3 2026)

```hypercode
dna:encode("ATCG", pattern="strand");
dna:simulate();
dna:synthesize() -> oligos;
```

---

## 🚰 Error Messages

HyperCode errors are designed to help:

```
❌ Syntax Error: Expected semicolon at line 2
   Tip: Check your brackets, quotes, and semicolons

❌ Name Error: Variable 'x' is not defined
   Tip: Use 'let x = value;' to create a variable

❌ Type Error: Cannot add string and number
   Tip: Make sure both values are the same type
```

---

## 🚫 Reserved Keywords

These words are special and can't be variable names:

```
let        print      if         function   loop
return     true       false      and        or
not        elif       else       class      quantum
ai         dna        for        while
```

---

## 📒 Examples

### **Hello World**
```hypercode
print "Hello, World!";
```

### **Variables and Math**
```hypercode
let x = 10;
let y = 5;
let sum = x + y;
print sum;
```

### **Conditionals**
```hypercode
let age = 20;

if age >= 18 print "Adult";
if age < 18 print "Minor";
```

### **Combining Operations**
```hypercode
let name = "Alex";
let score = 95;

print name;
print score;

if score >= 90 print "Excellent!";
if score < 90 print "Good job!";
```

---

## 🌟 Tips & Tricks

1. **Use print for debugging**
   ```hypercode
   let x = 10;
   print "x is: ";
   print x;
   ```

2. **Name variables clearly**
   ```hypercode
   let student_age = 20;  # Good
   let a = 20;            # Not clear
   ```

3. **Add comments for complex logic**
   ```hypercode
   # Check if person can vote
   if age >= 18 print "Eligible";
   ```

4. **Test with REPL**
   ```bash
   python hypercode_repl.py
   >>> let x = 5;
   >>> if x > 3 print "yes";
   yes
   ```

---

**Next:** Check [GETTING_STARTED.md](./GETTING_STARTED.md) for tutorials!
