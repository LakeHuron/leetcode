class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        length = 0; start = 0; i = 0; j = 0
        while j < len(s):
            if s.find(s[j], i, j) != -1:
                if (j-i > length):
                    length = j - i; start = i
                i = s.find(s[j], i, j) + 1
            j += 1
        return max(length, j - i)
