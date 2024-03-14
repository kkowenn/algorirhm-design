'''

316. Remove Duplicate Letters
Medium

Topics
Companies

Hint
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order
 among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count of each character in the string
        char_count = {char: 0 for char in s}
        for char in s:
            char_count[char] += 1

        result = []  # Stack to build the result string
        in_result = {char: False for char in s}  # Track if a char is in the result

        for char in s:
            # Decrease the count for the current character
            char_count[char] -= 1

            # If char is already in result, skip it
            if in_result[char]:
                continue

            # If the current character is smaller than the last character in result
            # and the last character appears later in the string, we can pop it and add the current character
            while result and char < result[-1] and char_count[result[-1]] > 0:
                in_result[result.pop()] = False

            result.append(char)
            in_result[char] = True

        return ''.join(result)

# Testing the fixed solution
solution_instance = Solution()
result1 = solution_instance.removeDuplicateLetters("bcabc")
result2 = solution_instance.removeDuplicateLetters("cbacdcbc")
print(result1, result2)
