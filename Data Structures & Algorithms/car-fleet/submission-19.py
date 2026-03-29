class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        diff = []
        time = []
        
        for p in position:
            diff.append(target - p)
        print(f'diff: {diff}')
        for i, d in enumerate(diff):
            time.append(d / speed[i])
        mapping = {}
        for i, p in enumerate(position):
            mapping[p] = time[i]
        sorted_positions = sorted(position)
        sorted_positions_time = []
        for p in sorted_positions:
            sorted_positions_time.append(mapping[p])
        print(f'sorted_positions: {sorted_positions}')
        print(f'sorted_positions_time: {sorted_positions_time}')
        tmp_result = len(set(time))
        print(f'time: {time}')
        print(f'set(time): {set(time)}')
        print(f'tmp_result: {tmp_result}')
        stack = []
        counter = 0
        for t in sorted_positions_time:
            if len(stack) == 0:
                stack.append(t)
                print(f'stack: {stack}')
            else:
                last_t = stack[-1]
                print(f't: {t}')
                print(f'last_t: {last_t}')
                while t >= last_t and len(stack) > 0:
                    stack.pop()
                    counter += 1
                    if len(stack) == 0:
                        break
                    last_t = stack[-1]
                    print(f'counter: {counter}')
                    print(f'stack: {stack}')
                    print(f'last_t: {last_t}')
                    print(f'**********')
                stack.append(t)
                print(f'stack: {stack}')
                print(f'---------')
        print(f'stack: {stack}')
        print(f'counter: {counter}')
        return len(stack)

# target=12
# position=[10,8,0,5,3]
# speed=[2,4,1,1,3]
# diff = [2, 4, 12, 7, 9]
# time = [1.0, 1.0, 12.0, 7.0, 3.0]
# speed=[2,4,1,1,3]
# iteration_0 = [10,8,0,5,3]
# iteration_1 = [12,12,1,6,6] # first fleet: 10, 8
# iteration_2 = [12,12,2,7,7]
# iteration_3 = [12,12,3,8,8] # second fleet: 3 !!! not correct !!!
# iteration_4 = [12,12,4,9,9]
# iteration_5 = [12,12,5,10,10]
# iteration_6 = [12,12,6,11,11]
# iteration_7 = [12,12,7,12,12] # second fleet 5, 3
# iteration_8 = [12,12,8,12,12]
# iteration_9 = [12,12,9,12,12]
# iteration_10 = [12,12,10,12,12]
# iteration_11 = [12,12,11,12,12]
# iteration_12 = [12,12,12,12,12] # third fleet: 0



