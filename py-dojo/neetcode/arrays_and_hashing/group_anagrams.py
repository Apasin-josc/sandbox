from typing import List
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    words_map = {}
    for word in strs:
        key = ''.join(sorted(word))
        if key in words_map:
            words_map[key].append(word)
        else:
            words_map[key] = [word]
    return list(words_map.values())


print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))

"""
T: O(n.k.log(k))
S: O(n.k)
"""

def groupAnagramsHashTable(strs: List[str]) -> List[List[str]]:
    words_map = {}

    """ O (n)"""
    for word in strs:
        count = [0] * 26
        """ O (k)"""
        for c in word:
            count[ord(c) - ord('a')] += 1     #for knowing where to put the 1
        key = tuple(count)                    #tuples are inmutable in python (they can be keys)

        if key in words_map:
            words_map[key].append(word)
        else:
            words_map[key] = [word]
    
    return list(words_map.values())

"""
T: O(n.k)
S: O(n.k)
"""


print(groupAnagramsHashTable(["act","pots","tops","cat","stop","hat"]))