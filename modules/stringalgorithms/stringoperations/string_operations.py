"""String Operations Examples - Based on CLRS String Algorithms"""

def string_length(s):
    """Calculate string length manually"""
    count = 0
    for _ in s:
        count += 1
    return count


def find_char(s, ch):
    """Find first occurrence of a character in a string"""
    for i, c in enumerate(s):
        if c == ch:
            return i
    return -1  # not found


def reverse_string(s):
    """Reverse a string"""
    return s[::-1]


def to_uppercase(s):
    """Convert string to uppercase"""
    return s.upper()


def strings_equal(s1, s2):
    """Check if two strings are equal"""
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def find_substring(text, pattern):
    """Simple pattern matching - find substring using naive approach"""
    text_len = len(text)
    pattern_len = len(pattern)

    for i in range(text_len - pattern_len + 1):
        match = True
        for j in range(pattern_len):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            return i
    return -1


def count_char(s, ch):
    """Count occurrences of a character"""
    count = 0
    for c in s:
        if c == ch:
            count += 1
    return count


def is_palindrome(s):
    """Check if string is palindrome (ignoring spaces and punctuation)"""
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def longest_common_substring(s1, s2):
    """Find longest common substring"""
    if not s1 or not s2:
        return ""

    max_length = 0
    max_start = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            # Count matching characters
            length = 0
            while (i + length < len(s1) and
                   j + length < len(s2) and
                   s1[i + length] == s2[j + length]):
                length += 1

            if length > max_length:
                max_length = length
                max_start = i

    return s1[max_start:max_start + max_length]


def main():
    print("=== String Operations in Python ===\n")

    # Test string length
    str1 = "Hello, World!"
    print(f"String: '{str1}'")
    print(f"Length: {string_length(str1)}\n")

    # Test find character
    print(f"Find 'W' at index: {find_char(str1, 'W')}")
    print(f"Find 'Z' at index: {find_char(str1, 'Z')}\n")

    # Test string equality
    str2 = "Hello, World!"
    str3 = "Goodbye"
    print(f"'{str1}' == '{str2}': {strings_equal(str1, str2)}")
    print(f"'{str1}' == '{str3}': {strings_equal(str1, str3)}\n")

    # Test substring finding
    print(f"Find 'World' in '{str1}': index {find_substring(str1, 'World')}\n")

    # Test reverse
    str4 = "REVERSE"
    print(f"Original: '{str4}'")
    print(f"Reversed: '{reverse_string(str4)}'\n")

    # Test uppercase
    str5 = "lowercase"
    print(f"Original: '{str5}'")
    print(f"Uppercase: '{to_uppercase(str5)}'\n")

    # Test character count
    print(f"Count of 'l' in '{str1}': {count_char(str1, 'l')}\n")

    # Test palindrome
    pal1 = "A man, a plan, a canal: Panama"
    pal2 = "Hello"
    print(f"Is '{pal1}' palindrome: {is_palindrome(pal1)}")
    print(f"Is '{pal2}' palindrome: {is_palindrome(pal2)}\n")

    # Test longest common substring
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    lcs = longest_common_substring(s1, s2)
    print(f"Longest common substring of '{s1}' and '{s2}': '{lcs}'")


if __name__ == "__main__":
    main()
