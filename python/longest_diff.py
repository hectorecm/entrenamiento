'''
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

Here's a starting point:

def longest_substring_with_k_distinct_characters(s, k):
  # Fill this in.

print longest_substring_with_k_distinct_characters('aabcdefff', 3)
# 5 (because 'defff' has length 5 with 3 characters)
'''

def longest_substring_with_k_distinct_characters(s, k):

    size = len(s)
    max_length = 1
    longest = s[0]

    for length in range(0, size):
        for start in range(size-length):
            end = start + length + 1
            substr = s[start:end]
            if len(set(substr)) == k and len(substr) > max_length:
                max_length = len(substr)
                longest = substr

    return longest

print (longest_substring_with_k_distinct_characters('hector', 6))
print (longest_substring_with_k_distinct_characters('aabcdefff', 3))
