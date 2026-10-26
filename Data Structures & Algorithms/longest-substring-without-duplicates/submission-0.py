class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        left = 0

        length = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[r])
            length = max(length, r - left + 1)
        
        return length
