class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        res = []
        for word in strs:
            sorted_key_words = sorted(word)
            key_word = "".join(sorted_key_words)
            if key_word not in my_dict:
                my_dict[key_word] = [word]
            else:
                my_dict[key_word].append(word)

        for val in my_dict.values():
            res.append(val)

        return res