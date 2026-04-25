"""
KMP (Knuth-Morris-Pratt) Pattern Matcher
Detailed step-by-step logging showing:
- Current position i, state q
- Prefix function lookups
- Mismatch occurrences
- Pattern-text alignment
"""


class KMPMatcher:
    """KMP algorithm with detailed step-by-step logging"""

    def __init__(self, pattern):
        self.pattern = pattern
        self.prefix = self.build_prefix_function(pattern)

    def build_prefix_function(self, pattern):
        """
        Build the prefix function (failure function).
        prefix[i] = length of longest proper prefix of pattern[0:i+1]
        that is also a suffix
        """
        m = len(pattern)
        prefix = [0] * m
        k = 0

        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = prefix[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            prefix[q] = k

        return prefix

    def search(self, text, verbose=True):
        """
        Search for pattern in text with detailed logging.
        Returns list of starting positions where pattern is found.
        """
        n = len(text)
        m = len(pattern := self.pattern)
        matches = []

        if verbose:
            print(f"\n{'=' * 80}")
            print(f"KMP PATTERN MATCHER")
            print(f"{'=' * 80}")
            print(f"Text:    '{text}'")
            print(f"Pattern: '{pattern}'")
            print(f"Prefix function: {self.prefix}")
            print(f"{'=' * 80}\n")

        q = 0  # number of characters matched
        step = 0

        for i in range(n):
            if verbose:
                step += 1
                print(f"Step {step}: i={i}, q={q}, text[{i}]='{text[i]}'")
                print(f"  Text:     {text}")
                print(f"  {'': <{i}}Pattern: {pattern}")

            # Mismatch handling
            while q > 0 and pattern[q] != text[i]:
                if verbose:
                    skipped = self.prefix[q - 1]
                    print(f"  → MISMATCH: pattern[{q}]='{pattern[q]}' != text[{i}]='{text[i]}'")
                    print(f"  → Using prefix function: q goes from {q} to {self.prefix[q - 1]}")

                q = self.prefix[q - 1]

            # Match handling
            if pattern[q] == text[i]:
                q += 1
                if verbose:
                    print(f"  → MATCH: pattern[{q-1}]='{pattern[q-1]}' == text[{i}]='{text[i]}', q→{q}")

            # Pattern found
            if q == m:
                matches.append(i - m + 1)
                if verbose:
                    print(f"  *** PATTERN FOUND at position {i - m + 1} ***")

                q = self.prefix[q - 1]
                if verbose:
                    print(f"  → Continuing search, q→{q}\n")
            else:
                if verbose:
                    print()

        if verbose:
            print(f"{'=' * 80}")
            print(f"SEARCH COMPLETE: Found {len(matches)} match(es) at position(s) {matches}")
            print(f"{'=' * 80}\n")

        return matches


def main():
    """Test KMP matcher with examples"""
    print("\n" + "=" * 80)
    print("KMP PATTERN MATCHER - TEST")
    print("=" * 80)

    # Test 1
    text1 = "ABABDABACDABABCABAB"
    pattern1 = "ABABCABAB"
    kmp1 = KMPMatcher(pattern1)
    kmp1.search(text1, verbose=True)

    # Test 2
    text2 = "AABAACAADAABAABA"
    pattern2 = "AABA"
    kmp2 = KMPMatcher(pattern2)
    kmp2.search(text2, verbose=True)

    # Test 3 - no match
    text3 = "ABCDEFG"
    pattern3 = "XYZ"
    kmp3 = KMPMatcher(pattern3)
    kmp3.search(text3, verbose=True)


if __name__ == "__main__":
    main()
