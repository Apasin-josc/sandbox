def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_map = {}
    for c in s:
        s_map[c] = s_map.get(c, 0) + 1

    t_map = {}
    for c in t:
        t_map[c] = t_map.get(c, 0) + 1
    
    return s_map == t_map

"""
T: O(n)
S: O(1) max 26 claves(alfabeto fijo a-z) -- O(n)
"""

print(isAnagram("racecar", "carrace"))
print(isAnagram("jar", "ram"))

"""------------------------------------------------"""


def isAnagramChallenge(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_map = {}
    for c in s:
        char_map[c] = char_map.get(c, 0) + 1

    for c in t:
        char_map[c] = char_map.get(c, 0) - 1
    
    for key, value in char_map.items():
        if value != 0:
            return False
    
    return True

print(isAnagramChallenge("racecar", "carrace"))
print(isAnagramChallenge("jar", "ram"))