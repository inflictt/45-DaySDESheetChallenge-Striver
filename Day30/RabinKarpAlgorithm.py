# Function to search for all occurrences of 'pat' in 'txt' using Rabin-Karp
def search(pat, txt):

    # Number of characters in the input alphabet (ASCII)
    d = 256

    # A prime number for modulo operations to reduce collisions
    q = 101

    # Length of the pattern
    m = len(pat)

    # Length of the text
    n = len(txt)

    # Hash value for pattern
    p = 0

    # Hash value for current window of text
    t = 0

    # High-order digit multiplier
    h = 1

    ans = []

    # Precompute h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * d) % q

    # Compute initial hash values for pattern and first window of text
    for i in range(m):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):

        # If hash values match, check characters one by one
        if p == t:
            match = True
            for j in range(m):
                if txt[i + j] != pat[j]:
                    match = False
                    break
            if match:
                ans.append(i)

        # Calculate hash value for the next window
        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q
            if t < 0:
                t += q

    return ans


if __name__ == "__main__":
    txt = "geeksforgeeks"
    pat = "geeks"
    res = search(pat, txt)

    for idx in res:
        print(idx, end=" ")
    print()