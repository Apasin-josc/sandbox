words = ['salsa']

for word in words:
    count = [0] * 26

    for c in word:
        count[ord(c) - ord('a')] += 1

    key = tuple(count)


print(count)
"""
english character lower case salsa hashed
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0]
"""