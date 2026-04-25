public class StringOperations {

    // Calculate string length manually
    public static int stringLength(String str) {
        int length = 0;
        for (char c : str.toCharArray()) {
            length++;
        }
        return length;
    }

    // Find first occurrence of a character in a string
    public static int findChar(String str, char ch) {
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == ch) {
                return i;
            }
        }
        return -1; // not found
    }

    // Reverse a string
    public static String reverseString(String str) {
        char[] chars = str.toCharArray();
        int n = chars.length;
        for (int i = 0; i < n / 2; i++) {
            char temp = chars[i];
            chars[i] = chars[n - 1 - i];
            chars[n - 1 - i] = temp;
        }
        return new String(chars);
    }

    // Convert string to uppercase
    public static String toUppercase(String str) {
        return str.toUpperCase();
    }

    // Check if two strings are equal
    public static boolean stringsEqual(String str1, String str2) {
        return str1.equals(str2);
    }

    // Simple pattern matching - find substring
    public static int findSubstring(String text, String pattern) {
        int textLen = text.length();
        int patternLen = pattern.length();

        for (int i = 0; i <= textLen - patternLen; i++) {
            boolean match = true;
            for (int j = 0; j < patternLen; j++) {
                if (text.charAt(i + j) != pattern.charAt(j)) {
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
    public static int countChar(String str, char ch) {
        int count = 0;
        for (char c : str.toCharArray()) {
            if (c == ch) {
                count++;
            }
        }
        return count;
    }

    // Check if string is palindrome
    public static boolean isPalindrome(String str) {
        String cleaned = str.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        return cleaned.equals(reverseString(cleaned));
    }

    public static void main(String[] args) {
        System.out.println("=== String Operations in Java ===\n");

        // Test string length
        String str1 = "Hello, World!";
        System.out.println("String: '" + str1 + "'");
        System.out.println("Length: " + stringLength(str1) + "\n");

        // Test find character
        System.out.println("Find 'W' at index: " + findChar(str1, 'W'));
        System.out.println("Find 'Z' at index: " + findChar(str1, 'Z') + "\n");

        // Test string equality
        String str2 = "Hello, World!";
        String str3 = "Goodbye";
        System.out.println("'" + str1 + "' == '" + str2 + "': " + stringsEqual(str1, str2));
        System.out.println("'" + str1 + "' == '" + str3 + "': " + stringsEqual(str1, str3) + "\n");

        // Test substring finding
        System.out.println("Find 'World' in '" + str1 + "': index " + findSubstring(str1, "World") + "\n");

        // Test reverse
        String str4 = "REVERSE";
        System.out.println("Original: '" + str4 + "'");
        System.out.println("Reversed: '" + reverseString(str4) + "'\n");

        // Test uppercase
        String str5 = "lowercase";
        System.out.println("Original: '" + str5 + "'");
        System.out.println("Uppercase: '" + toUppercase(str5) + "'\n");

        // Test character count
        System.out.println("Count of 'l' in '" + str1 + "': " + countChar(str1, 'l') + "\n");

        // Test palindrome
        String pal1 = "A man, a plan, a canal: Panama";
        String pal2 = "Hello";
        System.out.println("Is '" + pal1 + "' palindrome: " + isPalindrome(pal1));
        System.out.println("Is '" + pal2 + "' palindrome: " + isPalindrome(pal2));
    }
}
