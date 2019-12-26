class Solution:
    def isValid(self, st):
        symbols_map = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in st:
            if len(stack) > 0:
                if symbols_map.get(c,'') == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack) == 0

if __name__ == '__main__':
    # Test Program
    s = "()(){(())"
    # should return False
    print(Solution().isValid(s))

    s = ""
    # should return True
    print(Solution().isValid(s))

    s = "([{}])()"
    # should return True
    print(Solution().isValid(s))