class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key][timestamp] = value
        else:
            self.hashmap[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hashmap:
            return ""
        if key in self.hashmap and timestamp in self.hashmap[key]: 
            return self.hashmap[key][timestamp]
        numbers = list(self.hashmap[key].keys())
        if timestamp < numbers[0]:
            return ""
        left_idx = 0
        right_idx = len(numbers) - 1
        left_value = numbers[left_idx]
        right_value = numbers[right_idx]
        while left_idx < right_idx:
            mid_idx = (left_idx + right_idx) // 2
            mid_value = numbers[mid_idx]
            if mid_idx == left_idx:
                if right_value < timestamp:
                    left_idx = right_idx
                break
            if mid_value < timestamp:
                left_idx = mid_idx
                left_value = numbers[left_idx]
            else:
                right_idx = mid_idx
                right_value = numbers[right_idx]
        timestamp = numbers[left_idx]
        return self.hashmap[key][timestamp]
        
