class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_list = []
        hash_str = {}
        for string in strs:
            sorted_s = "".join(sorted(string))
            if sorted_s in hash_str:
                hash_str[sorted_s].append(string)
            else:
                hash_str[sorted_s] = [string]

        return list(hash_str.values())