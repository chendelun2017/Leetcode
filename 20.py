class Solution(object):
    def isValid_1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        match = {'{':'}', '[':']', '(':')'}
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:     # 检查是否存在单个 右括号
                    return False

                top = stack.pop()
                
                if match[top] != i:
                    return False

        if len(stack) != 0:     # 检查是否存在单个 左括号
            return False
        return True

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match = {")": "(", "}": "{", "]": "["}
        
        for i in s:
            if i in match:
                top = stack.pop() if stack else '#'
                if match[i] != top:
                    return False
            else:
                stack.append(i)

        return not stack


s = Solution()
print(s.isValid(''))
print(s.isValid('()'))