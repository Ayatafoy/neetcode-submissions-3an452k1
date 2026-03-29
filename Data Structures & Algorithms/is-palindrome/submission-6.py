class Solution:
    def filter_non_alphanumeric_loop(self, text):
        filtered_chars = []
        for char in text:
            if char.isalnum():
                filtered_chars.append(char)
        return "".join(filtered_chars)

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = self.filter_non_alphanumeric_loop(s)
        left_pointer = 0
        right_pointer = len(s) - 1
        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                # print(s[left_pointer])
                # print(s[right_pointer])
                return False
            left_pointer += 1
            right_pointer -= 1
        return True