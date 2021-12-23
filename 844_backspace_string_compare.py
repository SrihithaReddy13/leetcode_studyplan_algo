class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = ""
        for i in s:
            if i == "#" and stack!="":
                stack = stack[:-1]
            elif i!="#":
                stack+=i
        s=stack
        stack = ""
        for i in t:
            if i == "#" and stack!="":
                stack = stack[:-1]
            elif i!="#":
                stack+=i
        t=stack
        if t==s:
            return True
        return False
