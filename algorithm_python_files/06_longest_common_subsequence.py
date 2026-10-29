"""Question 6: Longest Common Subsequence (LCS)."""


def lcs(first, second):
    m, n = len(first), len(second)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if first[i - 1] == second[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    result = []
    while i > 0 and j > 0:
        if first[i - 1] == second[j - 1]:
            result.append(first[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    result.reverse()
    return dp[m][n], "".join(result)


if __name__ == "__main__":
    first = "ABCBDAB"
    second = "BDCABA"
    length, sequence = lcs(first, second)
    print("String 1:", first)
    print("String 2:", second)
    print("LCS length:", length)
    print("LCS sequence:", sequence)
