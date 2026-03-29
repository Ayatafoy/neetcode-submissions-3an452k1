class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if len(strs) == 0:
            return ""
        len_list = []
        total_len = 0
        for str_i in strs:
            len_counter = len(str_i)
            total_len += len_counter
            len_list.append(str(len_counter))
        metadata = "|".join(len_list)
        metadata = f"{metadata}&{total_len}"
        strs_joined = "".join(strs)
        result = f"{strs_joined}{metadata}"
        return result

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == "":
            return []
        total_count = int(s.split("&")[-1])
        total_count_len = len(str(total_count)) + 1
        s_without_total_len = s[0:-total_count_len]
        input_str = s[0:total_count]
        len_list_str = s_without_total_len[total_count:]
        len_list = len_list_str.split("|")
        current = 0
        result = []
        for length_str in len_list:
            length = int(length_str)
            partial_str = input_str[current:current+length]
            result.append(partial_str)
            current += length
        return result
