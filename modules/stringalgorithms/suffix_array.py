"""
Suffix Array with LCP (Longest Common Prefix) Array
Features:
- Build suffix array by sorting (suffix, starting_index) tuples
- Compute LCP array between consecutive sorted suffixes
- Detailed logging of construction process
"""


class SuffixArray:
    """Build suffix array and compute LCP array"""

    def __init__(self, text):
        self.text = text + "$"  # Add sentinel character
        self.n = len(self.text)
        self.suffix_array = None
        self.lcp_array = None

    def build_suffix_array(self, verbose=True):
        """
        Build suffix array by sorting (suffix, index) tuples.
        Returns list of starting indices in sorted order.
        """
        if verbose:
            print(f"\n{'=' * 80}")
            print(f"SUFFIX ARRAY CONSTRUCTION")
            print(f"{'=' * 80}")
            print(f"Text: '{self.text}'")
            print(f"{'=' * 80}\n")

        # Create list of (suffix, starting_index) tuples
        suffixes = []
        for i in range(self.n):
            suffix = self.text[i:]
            suffixes.append((suffix, i))

        if verbose:
            print("All suffixes (before sorting):")
            for i, (suffix, idx) in enumerate(suffixes):
                print(f"  {i:2d}: SA[{idx:2d}] = '{suffix}'")
            print()

        # Sort by suffix (lexicographic order)
        suffixes.sort(key=lambda x: x[0])

        # Extract just the indices
        self.suffix_array = [idx for _, idx in suffixes]

        if verbose:
            print("Suffix array (after sorting):")
            for rank, idx in enumerate(self.suffix_array):
                suffix = self.text[idx:]
                print(f"  SA[{rank:2d}] = {idx:2d} → '{suffix}'")
            print()

        return self.suffix_array

    def compute_lcp_array(self, verbose=True):
        """
        Compute LCP (Longest Common Prefix) array.
        LCP[i] = length of longest common prefix between
        suffixes at suffix_array[i] and suffix_array[i+1]
        """
        if self.suffix_array is None:
            self.build_suffix_array(verbose=False)

        n = len(self.suffix_array)
        lcp = [0] * (n - 1)

        if verbose:
            print(f"{'=' * 80}")
            print(f"LONGEST COMMON PREFIX (LCP) ARRAY COMPUTATION")
            print(f"{'=' * 80}\n")

        for i in range(n - 1):
            idx1 = self.suffix_array[i]
            idx2 = self.suffix_array[i + 1]
            suffix1 = self.text[idx1:]
            suffix2 = self.text[idx2:]

            # Compute LCP length
            lcp_length = 0
            for j in range(min(len(suffix1), len(suffix2))):
                if suffix1[j] == suffix2[j]:
                    lcp_length += 1
                else:
                    break

            lcp[i] = lcp_length

            if verbose:
                print(f"LCP[{i}] = {lcp_length}")
                print(f"  Suffix 1 (SA[{i}]={idx1}):   '{suffix1[:10]}{'...' if len(suffix1) > 10 else ''}'")
                print(f"  Suffix 2 (SA[{i+1}]={idx2}): '{suffix2[:10]}{'...' if len(suffix2) > 10 else ''}'")
                if lcp_length > 0:
                    common = suffix1[:lcp_length]
                    print(f"  Common prefix: '{common}'")
                print()

        self.lcp_array = lcp

        if verbose:
            print(f"{'=' * 80}")
            print(f"LCP Array: {lcp}")
            print(f"{'=' * 80}\n")

        return lcp

    def print_summary(self):
        """Print a nice table of suffix array with LCP values"""
        if self.suffix_array is None:
            self.build_suffix_array(verbose=False)
        if self.lcp_array is None:
            self.compute_lcp_array(verbose=False)

        print(f"\n{'=' * 80}")
        print("SUFFIX ARRAY SUMMARY")
        print(f"{'=' * 80}")
        print(f"{'Rank':<6} {'Index':<8} {'LCP':<6} {'Suffix':<40}")
        print("-" * 80)

        for rank in range(len(self.suffix_array)):
            idx = self.suffix_array[rank]
            suffix = self.text[idx:]
            lcp_val = self.lcp_array[rank] if rank < len(self.lcp_array) else "-"
            print(f"{rank:<6} {idx:<8} {lcp_val:<6} '{suffix[:35]}{'...' if len(suffix) > 35 else ''}'")

        print(f"{'=' * 80}\n")


def main():
    """Test suffix array with examples"""
    print("\n" + "=" * 80)
    print("SUFFIX ARRAY WITH LCP ARRAY - TEST")
    print("=" * 80)

    # Test 1: "banana"
    print("\n[Test 1] Text: 'banana'")
    text1 = "banana"
    sa1 = SuffixArray(text1)
    sa1.build_suffix_array(verbose=True)
    sa1.compute_lcp_array(verbose=True)
    sa1.print_summary()

    # Test 2: "mississippi"
    print("\n[Test 2] Text: 'mississippi'")
    text2 = "mississippi"
    sa2 = SuffixArray(text2)
    sa2.build_suffix_array(verbose=False)
    sa2.compute_lcp_array(verbose=False)
    sa2.print_summary()

    # Test 3: "abracadabra"
    print("\n[Test 3] Text: 'abracadabra'")
    text3 = "abracadabra"
    sa3 = SuffixArray(text3)
    sa3.build_suffix_array(verbose=False)
    sa3.compute_lcp_array(verbose=False)
    sa3.print_summary()


if __name__ == "__main__":
    main()
