def dna_match_topdown(DNA1, DNA2):
    memo = {}

    def helper(i, j):
        # Base case: If either of the strings is empty, return 0
        if i == 0 or j == 0:
            return 0

        # Check if the result is already computed and stored in the memo
        if (i, j) in memo:
            return memo[(i, j)]

        # If the last characters of both strings match, increment the result by 1
        if DNA1[i - 1] == DNA2[j - 1]:
            result = 1 + helper(i - 1, j - 1)
        else:
            result = max(helper(i - 1, j), helper(i, j - 1))

        memo[(i, j)] = result
        return result

    return helper(len(DNA1), len(DNA2))

def dna_match_bottomup(DNA1, DNA2):
    m = len(DNA1)
    n = len(DNA2)

    # Create a table to store the computed results
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Populate the table from bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if DNA1[i - 1] == DNA2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    return table[m][n]




