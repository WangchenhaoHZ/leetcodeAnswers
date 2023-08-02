class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == "(") or (c == "[") or (c == "{"):
                stack.append(c)
            elif stack:
                if (c == ")") and (stack[-1] == "("):
                    stack.pop()
                elif (c == "]") and (stack[-1] == "["):
                    stack.pop()
                elif (c == "}") and (stack[-1] == "{"):
                    stack.pop()
                else:
                    return False
            else:
                return False
        if stack:
            return False
        else:
            return True

print(
    Solution().isValid(
        "(])"
    )
)