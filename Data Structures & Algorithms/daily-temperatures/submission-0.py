class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for pair in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(pair)
                continue
            
            while len(stack) != 0 and pair[1] > stack[-1][1]:
                top = stack.pop()
                result[top[0]] = pair[0] - top[0]

            stack.append(pair)

        return result