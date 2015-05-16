"""
    Implementation of the Longest Common Sequence algorithm

    Longest Common Subsequence Overview:
    ------------------------------------

    The longest common subsequence (LCS) problem is the problem of finding the
    longest subsequence common to all sequences in a set of sequences
    (often just two sequences)

    Fonte: http://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""


def _lcs_matrix(word1, word2):
    """
    Create the LCS matrix

    |   |   | A | G | C | A | T |
    |---|---|---|---|---|---|---|
    |   | 0 | 0 | 0 | 0 | 0 | 0 |
    | G | 0 | 0 | 1 | 1 | 1 | 1 |
    | A | 0 | 1 | 1 | 1 | 2 | 2 |
    | C | 0 | 1 | 1 | 2 | 2 | 2 |
    """

    # Initialize the matrix with zeros
    matrix = [[ 0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

    for i, a in enumerate(word1):
        for j, b in enumerate(word2):
            if a == b:
                matrix[i+1][j+1] = matrix[i][j] + 1
            else:
                matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])
    return matrix


def _discover_sequence(lcs_matrix, word1, word2):
    """Discover the sequence making the traceback"""

    i = len(word1) - 1
    j = len(word2) - 1
    seq = ""

    while i >= 0 and j >= 0:
        if word1[i] == word2[j]:
            seq = seq + word1[i]
            i -= 1
            j -= 1
        elif lcs_matrix[i][j+1] >= lcs_matrix[i+1][j]:
            i -= 1
        else:
            j -= 1

    # The sequence is discovered backwards
    return seq[::-1]


def lcs(word1, word2):
    """Longest Common Subsequence of two words"""

    matrix = _lcs_matrix(word1, word2)
    return _discover_sequence(matrix, word1, word2)
