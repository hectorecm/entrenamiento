'''

Hi, here's your problem today. This problem was recently asked by Twitter:

A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"

'''

class Solution:
    def longestPalindrome(self, s):

        size = len(s)

        # stores the longest substring starting index and its length
        index = 0
        max_length = 1

        # flags[i][j] represents if a substring from i to j is palindrome
        flags = [[False] * size for _ in range(size)]

        # all substring of length 1 are palindrome
        for i in range(size):
            flags[i][i] = True

        # length = size of substring range (searching palindromes of size 2, 3, etc...)
        for length in range(1, size):
            for start in range(size-length):
                end = start + length
                if s[start] == s[end] and (length == 1 or flags[start+1][end-1]):
                    flags[start][end] = True
                    if length > max_length:
                        max_length = length
                        index = start
        return s[index : index + max_length + 1]

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("aaaabbaa"))
    print(s.longestPalindrome("yataysometemosareasoyosnorrron"))
    print(s.longestPalindrome("abayataysometemosyatayaba"))


