from typing import List

def encode(strs: List[str]) -> str:
    if strs == []:
        return '👁️‍🗨️'
    
    encoded_string = '😛'.join(strs)
    return encoded_string


def decode(s: str) -> List[str]:
    if s == '👁️‍🗨️':
        return []

    decoded_string = s.split('😛')    
    return decoded_string
    
    

#string_to_decode = (encode(["Hello World", "Leetcode"]))
#print(decode(string_to_decode))


"""
T: O(n)
S: O(n) - the functions are creating a string/list new from the size of the input
"""


def encode_strong(strs: List[str]) -> str:
    if strs == []:
        return 'no len 👁️‍🗨️'
    result = ""
    for s in strs:
        result += str(len(s)) + "#" + s
    return result


def decode_strong(s: str) -> List[str]:
    if s == 'no len 👁️‍🗨️':
        return []
    
    res = []
    i = 0
    while i < len(s):
        j = i
        # 1. avanza j hasta el '#'
        while s[j] != '#':
            j += 1
        # 2. length = int(s[i:j])
        length = int(s[i:j]) 
        # 3. word = s[j+1 : j+1+length]
        word = s[j+1 : j+1+length]
        # 4. res.append(word)
        res.append(word)
        # 5. i = j + 1 + length
        i = j + 1 + length
    return res


string_to_decode_strong = (encode_strong(["Hello World", "Leetcode"]))
print(decode_strong(string_to_decode_strong))