class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i, next_t in enumerate(temperatures):
            print(f'i: {i}')
            print(f'next_t: {next_t}')
            if len(stack) == 0:
                stack.append(i)
                print(f'stack: {stack}')
            else:
                last_t = stack[-1]
                print(f'last_t: {last_t}')
                if next_t >= temperatures[last_t]:
                    while temperatures[last_t] < next_t:
                        result[last_t] = i - last_t
                        print(f'result: {result}')
                        stack.pop()
                        if len(stack) == 0:
                            break
                        last_t = stack[-1]
                        print(f'last_t: {last_t}')
                        print(f'stack: {stack}')
                        print('***************')
                stack.append(i)
                print(f'stack: {stack}')
            print(f'stack: {stack}')
            print('-----------------')
        return result
                    
            
       

        