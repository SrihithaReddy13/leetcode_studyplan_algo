class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=''
        ans = 0
        for i in s:
            if i in window:
                dup = window.index(i)
                window = window[dup+1:]+i
            else:
                window+=i
            ans = max(ans, len(window))
        return ans
