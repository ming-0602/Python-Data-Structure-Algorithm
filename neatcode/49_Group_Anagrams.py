from collections import defaultdict

#using hashmap which use import of defaultdict
def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    anagram_map = defaultdict(list)
    result = []

    for s in strs:
        sorted_s = tuple(sorted(s))
        anagram_map[sorted_s].append(s)

    for value in anagram_map.values():
        result.append(value)

    return result