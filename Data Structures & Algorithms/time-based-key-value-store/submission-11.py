class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key][timestamp] = value
        else:
            self.hashmap[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        print(f'Get {timestamp}')
        print(f'hashmap {self.hashmap}')
        if not key in self.hashmap:
            return ""
        if key in self.hashmap and timestamp in self.hashmap[key]: 
            return self.hashmap[key][timestamp]
        numbers = list(self.hashmap[key].keys())
        print(f'numbers: {numbers}')
        if timestamp < numbers[0]:
            return ""
        left_idx = 0
        right_idx = len(numbers) - 1
        left_value = numbers[left_idx]
        right_value = numbers[right_idx]
        while left_idx < right_idx:
            print(f'left_idx: {left_idx}')
            print(f'right_idx: {right_idx}')
            mid_idx = (left_idx + right_idx) // 2
            mid_value = numbers[mid_idx]
            print(f'mid_idx: {mid_idx}')
            print(f'mid_value: {mid_value}')
            if mid_idx == left_idx:
                if right_value < timestamp:
                    left_idx = right_idx
                break
            if mid_value < timestamp:
                print(f'mid_value < timestamp')
                left_idx = mid_idx
                left_value = numbers[left_idx]
            else:
                print(f'mid_value >= timestamp')
                right_idx = mid_idx
                right_value = numbers[right_idx]
        print(f'left_idx: {left_idx}')
        print(f'right_idx: {left_idx}')
        timestamp = numbers[left_idx]
        print(f'timestamp: {timestamp}\n')
        print('---------')
        return self.hashmap[key][timestamp]
        
