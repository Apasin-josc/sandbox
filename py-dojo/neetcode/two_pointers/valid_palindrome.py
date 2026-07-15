def isPalindrome(s: str) -> bool:
    L, R = 0, len(s) - 1
    while L <= R:
        if not s[L].isalnum():
            L += 1
            continue
        
        if not s[R].isalnum():
            R -= 1
            continue
        
        if s[L].lower() != s[R].lower():
            return False
        
        L += 1
        R -= 1
    return True

print(isPalindrome("Was it a car or a cat I saw?"))