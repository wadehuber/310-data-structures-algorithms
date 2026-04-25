#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Calculate string length manually
int string_length(const char *str) {
    int length = 0;
    while (str[length] != '\0') {
        length++;
    }
    return length;
}

// Find first occurrence of a character in a string
int find_char(const char *str, char ch) {
    int i = 0;
    while (str[i] != '\0') {
        if (str[i] == ch) {
            return i;
        }
        i++;
    }
    return -1; // not found
}

// Reverse a string in-place
void reverse_string(char *str) {
    int n = string_length(str);
    for (int i = 0; i < n / 2; i++) {
        char temp = str[i];
        str[i] = str[n - 1 - i];
        str[n - 1 - i] = temp;
    }
}

// Convert string to uppercase
void to_uppercase(char *str) {
    int i = 0;
    while (str[i] != '\0') {
        str[i] = toupper((unsigned char)str[i]);
        i++;
    }
}

// Check if two strings are equal
int strings_equal(const char *str1, const char *str2) {
    int i = 0;
    while (str1[i] != '\0' || str2[i] != '\0') {
        if (str1[i] != str2[i]) {
            return 0;
        }
        i++;
    }
    return 1;
}

// Simple pattern matching - find substring
int find_substring(const char *text, const char *pattern) {
    int text_len = string_length(text);
    int pattern_len = string_length(pattern);

    for (int i = 0; i <= text_len - pattern_len; i++) {
        int match = 1;
        for (int j = 0; j < pattern_len; j++) {
            if (text[i + j] != pattern[j]) {
                match = 0;
                break;
            }
        }
        if (match) {
            return i;
        }
    }
    return -1;
}

int main() {
    printf("=== String Operations in C ===\n\n");

    // Test string length
    char str1[] = "Hello, World!";
    printf("String: '%s'\n", str1);
    printf("Length: %d\n\n", string_length(str1));

    // Test find character
    printf("Find 'W' at index: %d\n", find_char(str1, 'W'));
    printf("Find 'Z' at index: %d\n\n", find_char(str1, 'Z'));

    // Test string equality
    char str2[] = "Hello, World!";
    char str3[] = "Goodbye";
    printf("'%s' == '%s': %s\n", str1, str2, strings_equal(str1, str2) ? "true" : "false");
    printf("'%s' == '%s': %s\n\n", str1, str3, strings_equal(str1, str3) ? "true" : "false");

    // Test substring finding
    printf("Find 'World' in '%s': index %d\n\n", str1, find_substring(str1, "World"));

    // Test reverse
    char str4[] = "REVERSE";
    printf("Original: '%s'\n", str4);
    reverse_string(str4);
    printf("Reversed: '%s'\n\n", str4);

    // Test uppercase
    char str5[] = "lowercase";
    printf("Original: '%s'\n", str5);
    to_uppercase(str5);
    printf("Uppercase: '%s'\n", str5);

    return 0;
}
