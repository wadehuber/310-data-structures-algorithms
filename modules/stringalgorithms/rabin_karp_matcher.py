"""
Rabin-Karp Rolling Hash Pattern Matcher
Features:
- Tunable parameters (d = base, q = prime modulus)
- Prints hash values for every window
- Counts spurious collisions (hash match but string mismatch)
"""


class RabinKarpMatcher:
    """Rabin-Karp algorithm with rolling hash and collision detection"""

    def __init__(self, pattern, d=256, q=101):
        """
        d: alphabet size (default 256 for ASCII)
        q: prime number for modulus (default 101)
        """
        self.pattern = pattern
        self.d = d
        self.q = q
        self.pattern_hash = None
        self.spurious_collisions = 0

    def compute_hash(self, string):
        """Compute hash value for a string"""
        hash_value = 0
        for char in string:
            hash_value = (hash_value * self.d + ord(char)) % self.q
        return hash_value

    def roll_hash(self, old_hash, old_char, new_char, d_pow):
        """Update hash when rolling the window by one character"""
        new_hash = (old_hash - ord(old_char) * d_pow) % self.q
        new_hash = (new_hash * self.d + ord(new_char)) % self.q
        new_hash = (new_hash + self.q) % self.q
        return new_hash

    def search(self, text, verbose=True):
        """
        Search for pattern in text using rolling hash.
        Returns list of starting positions where pattern is found.
        """
        n = len(text)
        m = len(self.pattern)
        matches = []
        self.spurious_collisions = 0

        if verbose:
            print(f"\n{'=' * 80}")
            print("RABIN-KARP ROLLING HASH MATCHER")
            print(f"{'=' * 80}")
            print(f"Text:     '{text}'")
            print(f"Pattern:  '{self.pattern}'")
            print(f"Alphabet size (d): {self.d}")
            print(f"Prime modulus (q): {self.q}")
            print(f"{'=' * 80}\n")

        if m > n:
            if verbose:
                print("Pattern longer than text. No matches found.\n")
            return matches

        # Precompute d^(m-1) mod q
        d_pow = 1
        for i in range(m - 1):
            d_pow = (d_pow * self.d) % self.q

        # Compute hash for pattern and first window
        self.pattern_hash = self.compute_hash(self.pattern)
        window_hash = self.compute_hash(text[0:m])

        if verbose:
            print(f"Pattern hash: {self.pattern_hash}")
            print(f"{'Window':<15} {'Hash':<8} {'Match?':<10} {'Verified?':<12}")
            print("-" * 50)

        # Slide the window
        for i in range(n - m + 1):
            window = text[i:i + m]
            window_hash = self.compute_hash(window)

            hash_match = window_hash == self.pattern_hash
            string_match = window == self.pattern

            if verbose:
                match_str = "YES" if hash_match else "NO"
                verified_str = "YES" if string_match else "NO"
                print(f"{window:<15} {window_hash:<8} {match_str:<10} {verified_str:<12}", end="")

            # Hash collision - verify with actual string comparison
            if hash_match:
                if string_match:
                    matches.append(i)
                    if verbose:
                        print(" ← MATCH FOUND")
                else:
                    self.spurious_collisions += 1
                    if verbose:
                        print(" ← SPURIOUS COLLISION (hash match, string mismatch)")
            else:
                if verbose:
                    print()

            # Update hash for next window
            if i < n - m:
                old_char = text[i]
                new_char = text[i + m]
                window_hash = self.roll_hash(window_hash, old_char, new_char, d_pow)

        if verbose:
            print("-" * 50)
            print("\nRESULTS:")
            print(f"  Matches found: {len(matches)} at position(s) {matches}")
            print(f"  Spurious collisions: {self.spurious_collisions}")
            print(f"{'=' * 80}\n")

        return matches


def main():
    """Test Rabin-Karp matcher with examples"""
    print("\n" + "=" * 80)
    print("RABIN-KARP ROLLING HASH MATCHER - TEST")
    print("=" * 80)

    # Test 1: Basic ASCII text
    text1 = "ABCCDDEFFGGHII"
    pattern1 = "DD"
    rk1 = RabinKarpMatcher(pattern1, d=256, q=101)
    rk1.search(text1, verbose=True)

    # Test 2: Numeric text with smaller parameters (demonstrates spurious collision)
    text2 = "3141592653589793"
    pattern2 = "26"
    rk2 = RabinKarpMatcher(pattern2, d=10, q=13)
    rk2.search(text2, verbose=True)

    # Test 3: Multiple matches
    text3 = "AABAABAABAAB"
    pattern3 = "AAB"
    rk3 = RabinKarpMatcher(pattern3, d=256, q=101)
    rk3.search(text3, verbose=True)


if __name__ == "__main__":
    main()
