#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

// Calculate string length manually
int stringLength(const string& str) {
    int length = 0;
    for (char c : str) {
        length++;
    }
    return length;
}

// Find first occurrence of a character in a string
int findChar(const string& str, char ch) {
    for (size_t i = 0; i < str.length(); i++) {
        if (str[i] == ch) {
            return i;
        }
    }
    return -1; // not found
}

// Reverse a string
string reverseString(const string& str) {
    string reversed = str;
    reverse(reversed.begin(), reversed.end());
    return reversed;
}

// Convert string to uppercase
string toUppercase(const string& str) {
    string result = str;
    for (char& c : result) {
        c = toupper(static_cast<unsigned char>(c));
    }
    return result;
}

// Check if two strings are equal
bool stringsEqual(const string& str1, const string& str2) {
    return str1 == str2;
}

// Simple pattern matching - find substring using naive approach
int findSubstring(const string& text, const string& pattern) {
    int textLen = text.length();
    int patternLen = pattern.length();

    for (int i = 0; i <= textLen - patternLen; i++) {
        bool match = true;
        for (int j = 0; j < patternLen; j++) {
            if (text[i + j] != pattern[j]) {
                match = false;
                break;
            }
        }
        if (match) {
            return i;
        }
    }
    return -1;
}

// Count occurrences of a character
int countChar(const string& str, char ch) {
    int count = 0;
    for (char c : str) {
        if (c == ch) {
            count++;
        }
    }
    return count;
}

// Check if string is palindrome
bool isPalindrome(const string& str) {
    string cleaned;
    for (char c : str) {
        if (isalnum(static_cast<unsigned char>(c))) {
            cleaned += tolower(static_cast<unsigned char>(c));
        }
    }
    return cleaned == reverseString(cleaned);
}

// Longest common substring
string longestCommonSubstring(const string& s1, const string& s2) {
    if (s1.empty() || s2.empty()) {
        return "";
    }

    int maxLength = 0;
    size_t maxStart = 0;

    for (size_t i = 0; i < s1.length(); i++) {
        for (size_t j = 0; j < s2.length(); j++) {
            // Count matching characters
            int length = 0;
            while (i + length < s1.length() &&
                   j + length < s2.length() &&
                   s1[i + length] == s2[j + length]) {
                length++;
            }

            if (length > maxLength) {
                maxLength = length;
                maxStart = i;
            }
        }
    }

    return s1.substr(maxStart, maxLength);
}

int main() {
    cout << "=== String Operations in C++ ===\n" << endl;

    // Test string length
    string str1 = "Hello, World!";
    cout << "String: '" << str1 << "'" << endl;
    cout << "Length: " << stringLength(str1) << "\n" << endl;

    // Test find character
    cout << "Find 'W' at index: " << findChar(str1, 'W') << endl;
    cout << "Find 'Z' at index: " << findChar(str1, 'Z') << "\n" << endl;

    // Test string equality
    string str2 = "Hello, World!";
    string str3 = "Goodbye";
    cout << "'" << str1 << "' == '" << str2 << "': "
         << (stringsEqual(str1, str2) ? "true" : "false") << endl;
    cout << "'" << str1 << "' == '" << str3 << "': "
         << (stringsEqual(str1, str3) ? "true" : "false") << "\n" << endl;

    // Test substring finding
    cout << "Find 'World' in '" << str1 << "': index "
         << findSubstring(str1, "World") << "\n" << endl;

    // Test reverse
    string str4 = "REVERSE";
    cout << "Original: '" << str4 << "'" << endl;
    cout << "Reversed: '" << reverseString(str4) << "'\n" << endl;

    // Test uppercase
    string str5 = "lowercase";
    cout << "Original: '" << str5 << "'" << endl;
    cout << "Uppercase: '" << toUppercase(str5) << "'\n" << endl;

    // Test character count
    cout << "Count of 'l' in '" << str1 << "': " << countChar(str1, 'l') << "\n" << endl;

    // Test palindrome
    string pal1 = "A man, a plan, a canal: Panama";
    string pal2 = "Hello";
    cout << "Is '" << pal1 << "' palindrome: "
         << (isPalindrome(pal1) ? "true" : "false") << endl;
    cout << "Is '" << pal2 << "' palindrome: "
         << (isPalindrome(pal2) ? "true" : "false") << "\n" << endl;

    // Test longest common substring
    string s1 = "ABCDGH";
    string s2 = "AEDFHR";
    string lcs = longestCommonSubstring(s1, s2);
    cout << "Longest common substring of '" << s1 << "' and '" << s2
         << "': '" << lcs << "'" << endl;

    return 0;
}
