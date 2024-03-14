'''
409. Longest Palindrome
Easy

Topics
Companies
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.



Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    # this function not work properly
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = 0
        for k, v in collections.Counter(s).iteritems():
            odds += v & 1
        return len(s) - odds + int(odds > 0)

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = sum(map(lambda x: x & 1, collections.Counter(s).values()))
        return len(s) - odd + int(odd > 0)

class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = [0] * 128  # Assuming ASCII characters
        odds = 0
        for char in s:
            char_counts[ord(char)] += 1

        for count in char_counts:
            odds += count % 2

        return len(s) - odds + int(odds > 0)

class Solution3(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = {}
        odds = 0
        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
            if char_counts[char] % 2 == 0:
                odds -= 1
            else:
                odds += 1
        return len(s) - odds + int(odds > 0)

solution_instance = Solution()
result1 = solution_instance.longestPalindrome2("abccccdd")
result2 = solution_instance.longestPalindrome2("a")
print(result1, result2)

solution_instance = Solution2()
result1 = solution_instance.longestPalindrome("abccccdd")
result2 = solution_instance.longestPalindrome("a")
print(result1, result2)

solution_instance = Solution3()
result1 = solution_instance.longestPalindrome("abccccdd")
result2 = solution_instance.longestPalindrome("a")
print(result1, result2)
