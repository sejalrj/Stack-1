class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #If the warmer temp for some day can not be received on immediete next day, you put it on stack and move ahead. once you receive greater temp, you start looking for stack elements if they can consider this greater element as a warmer temperature for them as well. if yes, subtract the index of them and pop the element from stack. if not, push it to the stack.

        stack = deque()
        stack.append((temperatures[0], 0))
        res = [0]*len(temperatures)

        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp = stack.pop()
                res[temp[1]] = i - temp[1]
            
            stack.append((temperatures[i], i))

        return res
