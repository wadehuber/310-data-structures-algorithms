# String Operations - Basic Examples

Simple, foundational string algorithm implementations across four programming languages. These examples demonstrate core string manipulation techniques from the CLRS textbook foundation level.

## Files

- **`string_operations.c`** - C implementation with manual memory handling
- **`StringOperations.java`** - Java implementation with object-oriented design
- **`string_operations.py`** - Python implementation with clean, readable syntax
- **`string_operations.cpp`** - C++ implementation using standard library containers

## Operations Covered

All implementations include the following string operations:

### Basic Operations

- **String Length** - Manual character counting (not using built-in length functions)
- **Character Search** - Find first occurrence of a character
- **String Equality** - Compare two strings character-by-character
- **String Reversal** - Reverse a string in-place or via new string
- **Case Conversion** - Convert string to uppercase

### Pattern Matching

- **Naive Substring Search** - Simple pattern matching with nested loops
- **Character Counting** - Count occurrences of a character

### Advanced Operations

- **Palindrome Detection** - Check if string is palindrome (ignoring punctuation)
- **Longest Common Substring** - Find longest substring common to two strings

## Usage

Each file includes a `main()` function with test cases demonstrating all operations:

```bash
# C
gcc -o string_operations string_operations.c
./string_operations

# Java
javac StringOperations.java
java StringOperations

# Python
python string_operations.py

# C++
g++ -o string_operations string_operations.cpp
./string_operations
```
