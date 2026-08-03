class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        characters_map  =  {")":"(","}":"{","]":"["}
        for i in s:
            if i in characters_map:
                if (stack and stack[-1] ==  characters_map[i]):
                    stack.pop()
                    continue
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
